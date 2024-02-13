from models.user_credentials import UserCredentials
from models.user_info import UserInfo
from models.image_info import ImageInfo
from models.request_image import RequestImage
from models.country import Country
from models.city import City
from models.district import District
from models.ward import Ward

from sqlmodel import Session, select, col, func
import sys
import os
import json
import numpy as np

sys.path.append("../../../../relative_face_recognition_app/server")
from database.engine import engine
from fastapi import HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer
from services.orm import *
from jose import JWTError, jwt
from datetime import datetime, timedelta
from passlib.context import CryptContext
from passlib.hash import bcrypt
from sqlalchemy.orm import sessionmaker, Session

from services.user_validators import (
    LoginRequest,
)

from pgvector.sqlalchemy import Vector
import uuid

from controllers.controllers_services import FaceRecognitionController

face_recognition_controller = FaceRecognitionController()


def select_users(username, password):
    with Session(engine) as session:
        statement = select(UserCredentials).where(
            UserCredentials.user_name == username, UserCredentials.password == password
        )
        results = session.exec(statement)
        return results.all()


def filter_users(
    name, gender, age, id_country=None, id_city=None, id_district=None, id_ward=None
):
    with Session(engine) as session:
        statement = select(UserInfo).where(
            col(UserInfo.full_name).contains(name),
            UserInfo.gender == (gender == "Nam"),
            UserInfo.age >= age,
            # UserInfo.id_country == id_country,
            # UserInfo.id_city == id_city,
            # UserInfo.id_district == id_district,
            # UserInfo.id_ward == id_ward
        )
        results = session.execute(statement)
        return results.all()


# Khởi tạo session để truy vấn CSDL
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Khởi tạo biến toàn cục để lưu id người dùng
global_id_user = None

# OAuth2 để xác thực người dùng
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Upload image folder
UPLOAD_FOLDER = "images/user_images/"
UPLOAD_FOLDER_REQUEST = "images/request_images/"


# Function để set global user id
def set_global_user_id(id_user):
    global global_user_id
    global_user_id = id_user


# get db session from orm.py
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Function để tạo token
def create_access_token(data: dict, expires_delta: timedelta):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode, os.getenv("SECRET_KEY"), algorithm=os.getenv("ALGORITHM")
    )
    return encoded_jwt


# Function để xác thực người dùng
def get_user(db: Session, form_data: LoginRequest):
    result_proxy = db.execute(
        select(UserCredentials).where(UserCredentials.user_name == form_data.username)
    )
    user = result_proxy.fetchone()
    return user


# Function để xác thực password
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


# Function để tạo người dùng
def create_user(db: Session, user: UserCredentials):
    try:
        # Check if the user_name is not provided or empty
        if user.user_name is None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Username is required for registration",
            )
        # Check if the email is not provided or empty
        if user.email is None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email is required for registration",
            )
        # Check if the password is not provided or empty
        if user.password is None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Password is required for registration",
            )
        # Hash mật khẩu trước khi lưu vào CSDL
        user.password = pwd_context.hash(user.password)

        # Tạo người dùng mới
        with db:
            # Add user to the database
            db.add(user)
            # Commit changes to the database
            db.commit()
            # Refresh the user object to get the id
            db.refresh(user)
            return user
    # Handle errors during user creation
    except Exception as e:
        print(f"Error during user creation: {e}")
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error during user creation",
        )
    finally:
        # Close the database session
        db.close()


# Function để lấy thông tin người dùng hiện tại
def get_current_user(
    db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)
):
    credentials = verify_token_and_get_credentials(token, db)
    return credentials[0]


# Function để xác thực token và lấy thông tin người dùng
def verify_token_and_get_credentials(token: str, db: Session):
    credentials = None
    try:
        payload = jwt.decode(
            token, os.getenv("SECRET_KEY"), algorithms=[os.getenv("ALGORITHM")]
        )
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials"
            )
        token_data = payload
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials"
        )

    if token_data:
        credentials = db.execute(
            select(UserCredentials).where(UserCredentials.user_name == username)
        ).first()

    if credentials is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials"
        )

    return credentials


def find_similar_users(request_image_id: uuid.UUID, db: Session = Depends(get_db)):
    print("request_image_id", request_image_id)
    # Lấy thông tin hình ảnh yêu cầu của người dùng
    request_image = db.query(RequestImage).filter_by(id=request_image_id).first()

    print("request_image", request_image)

    if not request_image:
        return []

    # Trích xuất embeddings của hình ảnh yêu cầu
    request_embeddings = np.array(request_image.embeddings)

    print("request_embeddings", request_embeddings)

    # request_embeddings = request_embeddings.reshape(1, -1)

    # print("request_embeddings", request_embeddings)

    # Tìm kiếm các hình ảnh gần giống trong cơ sở dữ liệu
    similar_images = []
    for image in db.query(ImageInfo):
        image_embeddings = np.array(image.embeddings)
        similarity = face_recognition_controller.compare_embeddings(
            request_embeddings, image_embeddings
        )
        if similarity > 0.7:
            similar_images.append(image)

    print("similar_images", similar_images)

    similar_users_infos = []

    # Lấy thông tin người dùng từ các hình ảnh gần giống
    for similar_image in similar_images:
        user_info = (
            db.query(UserInfo)
            .filter_by(id_image=similar_image.id, is_allowed=True)
            .first()
        )
        if user_info:
            similar_users_infos.append(user_info)
            print("similar_user_info", user_info)

    print("similar_users_infos", similar_users_infos)

    return similar_users_infos
