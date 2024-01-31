import sys
import os

from models.image_info import ImageInfo
from models.user_credentials import UserCredentials
from models.user_info import UserInfo
from models.city import City
from models.district import District
from models.ward import Ward
from models.country import Country

sys.path.append("../../../face_recognition_app/server")
from database.engine import engine
from models import *
from fastapi import FastAPI, HTTPException, Depends, status, File, UploadFile
from fastapi.responses import FileResponse
from fastapi.security import OAuth2PasswordBearer
from services.orm import *
from jose import JWTError, jwt
from datetime import datetime, timedelta
from passlib.context import CryptContext
from sqlalchemy.orm import sessionmaker, Session
from dotenv import load_dotenv
from services.user_validators import (
    RegisterRequest,
    LoginRequest,
    UserInfoRequest,
)
import uuid

load_dotenv()

# Khởi tạo FastAPI
app = FastAPI()


# Endpoint để lấy id người dùng hiện tại
@app.get("/user_credentials_id", response_model=uuid.UUID)
async def get_user_credentials_id(
    current_user: UserCredentials = Depends(get_current_user),
):
    print("current_user: ", current_user)
    user_id = current_user.id
    return user_id


# Endpoint để nhap thong tin ca nhan cua nguoi dung
# Create user info function
@app.post("/create_user_info")
async def create_user_info(
    data: UserInfoRequest,
    db: Session = Depends(get_db),
    user_id: uuid.UUID = Depends(get_user_credentials_id),
):
    try:
        user_info = db.query(UserInfo).filter_by(id_user=user_id).first()
        if user_info:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="User info already exists for the specified user ID",
            )
        else:
            with db:
                data.id_user = user_id
                new_user_info = UserInfo(
                    id_user=data.id_user,
                    full_name=data.full_name,
                    age=data.age,
                    gender=data.gender,
                    id_image=data.id_image,
                    id_country=data.id_country,
                    id_city=data.id_city,
                    id_district=data.id_district,
                    id_ward=data.id_ward,
                    face_feature=data.face_feature,
                    is_allowed=data.is_allowed,
                )

                db.add(new_user_info)
                db.commit()
            db.close()
    except Exception as e:
        print(f"Error during user info creation: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error during user info creation",
        )


@app.get("/get_user_info/{user_id}")
async def get_user_info(
    user_id: uuid.UUID,
    db: Session = Depends(get_db),
    current_user: UserCredentials = Depends(get_current_user),
):
    try:
        if current_user.id != user_id:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Unauthorized access to user info",
            )
        user_info = db.query(UserInfo).filter_by(id_user=user_id).first()
        if user_info:
            return user_info.json()
        else:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User info not found for the specified user ID,",
            )

    except Exception as e:
        print(f"Error retrieving user info: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error retrieving user info",
        )


@app.delete("/delete_user_info/{user_id}")
async def delete_user_info(
    user_id: uuid.UUID,
    db: Session = Depends(get_db),
    current_user: UserCredentials = Depends(get_current_user),
):
    print("user_id: ", user_id)
    print("current_user: ", current_user)
    try:
        if current_user.id != user_id:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Unauthorized access to user info",
            )
        user_info = db.query(UserInfo).filter_by(id_user=user_id).first()
        if user_info:
            db.delete(user_info)
            db.commit()
            return {"status": 200, "message": "Successfully deleted user info"}
        else:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User info not found for the specified user ID,",
            )

    except Exception as e:
        print(f"Error retrieving user info: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error retrieving user info",
        )


@app.put("/update_user_info/{id_user}")
async def update_user_info(
    data: UserInfoRequest,
    db: Session = Depends(get_db),
    current_user: UserCredentials = Depends(get_current_user),
):
    print("user_id: ", data.id_user)
    print("current_user: ", current_user)
    try:
        if current_user.id != data.id_user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Unauthorized access to user info",
            )
        user_info = db.query(UserInfo).filter_by(id_user=data.id_user).first()
        if user_info is not None:
            with db:
                user_info.id_user = data.id_user
                user_info.full_name = data.full_name
                user_info.age = data.age
                user_info.gender = data.gender
                user_info.id_image = data.id_image
                user_info.id_country = data.id_country
                user_info.id_city = data.id_city
                user_info.id_district = data.id_district
                user_info.id_ward = data.id_ward
                user_info.face_feature = data.face_feature
                user_info.is_allowed = data.is_allowed
                db.commit()
                db.refresh(user_info)
            db.close()
        else:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User info not found for the specified user ID,",
            )

    except Exception as e:
        print(f"Error retrieving user info: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error retrieving user info",
        )


# ----------------------------------
# Endpoint de upload anh tren server
@app.post("/upload_image")
async def upload_image(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    id_credential_user: uuid.UUID = Depends(get_user_credentials_id),
):
    try:
        os.makedirs(UPLOAD_FOLDER, exist_ok=True)
        image_path = os.path.join(
            UPLOAD_FOLDER, f"{str(id_credential_user)}_{file.filename}"
        )

        with open(image_path, "wb") as image_file:
            image_file.write(file.file.read())

        with db:
            new_image_info = ImageInfo(
                id_user=id_credential_user,
                name_image=file.filename,
                image_path=image_path,
            )
            db.add(new_image_info)
            db.commit()
            db.refresh(new_image_info)

        return {"id_image": new_image_info.id}
    except Exception as e:
        print(f"Error during image upload: {e}")
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error during image upload",
        )
    finally:
        db.close()


# ----------------------------------
# Endpoint de retrieve anh tu server
@app.get("/get_user_image/{user_id}")
async def get_user_image(user_id: uuid.UUID, db: Session = Depends(get_db)):
    try:
        # Fetch user image information from the database
        user_image_info = db.query(ImageInfo).filter_by(id_user=user_id).first()

        if user_image_info:
            # Return the image file using FileResponse
            return FileResponse(user_image_info.image_path, media_type="image/jpeg")
        else:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Image not found"
            )
    except Exception as e:
        print(f"Error retrieving user image: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error retrieving user image",
        )


@app.put("/update_user_image/{user_id}")
async def update_user_image(
    user_id: uuid.UUID,
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user: UserCredentials = Depends(get_current_user),
):
    print("user_id: ", user_id)
    print("current_user: ", current_user)
    try:
        if current_user.id != user_id:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Unauthorized access to user info",
            )
        user_image_info = db.query(ImageInfo).filter_by(id_user=user_id).first()
        if user_image_info:
            os.remove(user_image_info.image_path)
            image_path = os.path.join(UPLOAD_FOLDER, f"{str(user_id)}_{file.filename}")

            with open(image_path, "wb") as image_file:
                image_file.write(file.file.read())

            user_image_info.name_image = file.filename
            user_image_info.image_path = image_path
            db.commit()
            return {"id_image": user_image_info.id}
        else:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User image not found for the specified user ID,",
            )

    except Exception as e:
        print(f"Error retrieving user image: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error retrieving user image",
        )


@app.get("/get_country_info/{country_id}")
async def get_country_info(country_id: uuid.UUID, db: Session = Depends(get_db)):
    try:
        # Fetch user image information from the database
        country_info = db.query(Country).filter_by(id=country_id).first()

        if country_info:
            return country_info.json()
        else:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Country not found"
            )
    except Exception as e:
        print(f"Error retrieving country info: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error retrieving country info",
        )


# ----------------------------------
@app.get("/get_city_info/{city_id}")
async def get_city_info(city_id: uuid.UUID, db: Session = Depends(get_db)):
    try:
        # Fetch user image information from the database
        city_info = db.query(City).filter_by(id=city_id).first()

        if city_info:
            return city_info.json()
        else:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="City not found"
            )
    except Exception as e:
        print(f"Error retrieving city info: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error retrieving city info",
        )


# ----------------------------------
@app.get("/get_district_info/{district_id}")
async def get_district_info(district_id: uuid.UUID, db: Session = Depends(get_db)):
    try:
        # Fetch user image information from the database
        district_info = db.query(District).filter_by(id=district_id).first()

        if district_info:
            return district_info.json()
        else:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="District not found"
            )
    except Exception as e:
        print(f"Error retrieving district info: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error retrieving district info",
        )


@app.get("/get_ward_info/{ward_id}")
async def get_ward_info(ward_id: uuid.UUID, db: Session = Depends(get_db)):
    try:
        # Fetch user image information from the database
        ward_info = db.query(Ward).filter_by(id=ward_id).first()

        if ward_info:
            return ward_info.json()
        else:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Ward not found"
            )
    except Exception as e:
        print(f"Error retrieving ward info: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error retrieving ward info",
        )


# ----------------------------------
# Endpoint để xác thực và tạo token cho người dùng khi đăng nhập
@app.post("/token")
async def login_for_access_token(
    form_data: LoginRequest, db: Session = Depends(get_db)
):
    user = get_user(db, form_data)

    if not user or not user[0].password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    hashed_password = user[0].password

    if not verify_password(form_data.password, hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token_expires = timedelta(
        minutes=int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))
    )
    access_token = create_access_token(
        data={"sub": form_data.username}, expires_delta=access_token_expires
    )

    return {"access_token": access_token, "token_type": "bearer"}


# Endpoint để đăng ký người dùng va tạo token cho người dùng
@app.post("/register")
async def register_user(request_data: RegisterRequest, db: Session = Depends(get_db)):
    # Kiểm tra xem user_name có được cung cấp hay không
    user = UserCredentials(
        user_name=request_data.username,
        email=request_data.email,
        password=request_data.password,
    )
    if not user.user_name:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username is required for registration",
        )
    if not user.password:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Password is required for registration",
        )
    if not user.email:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email is required for registration",
        )

    # Tạo người dùng mới
    created_user = create_user(db, user)

    # Tạo token cho người dùng
    if created_user:
        # Check if the environment variable is set and not None
        access_token_expire_minutes = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")
        # Create access token
        if access_token_expire_minutes is not None:
            access_token_expires = timedelta(minutes=int(access_token_expire_minutes))
        else:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="ACCESS_TOKEN_EXPIRE_MINUTES environment variable not set",
            )

        access_token = create_access_token(
            data={"sub": created_user.user_name}, expires_delta=access_token_expires
        )
        return {"access_token": access_token, "token_type": "bearer"}
    else:
        # Handle errors during user creation
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error during user creation",
        )
    db.close()


@app.get("/user_info")
async def read_user_info(
    name: str,
    gender: str,
    age: str,
    country: str,
    city: str,
    district: str,
    ward: str,
    feature: str,
):
    # print(name, gender, age, country, city, district, ward, feature)
    result = filter_users(name=name, gender=gender, age=10)
    # print("* ******* * result from filter_users: ", result)
    return {"status": 200, "message": "Successfully queried user info"}
