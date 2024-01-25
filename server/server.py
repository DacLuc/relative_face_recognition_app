import sys
import os

sys.path.append("../../../face_recognition_app/server")
from database.engine import engine
from models import *
from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer
from services.orm import *
from jose import JWTError, jwt
from datetime import datetime, timedelta
from passlib.context import CryptContext
from sqlalchemy.orm import sessionmaker, Session
from dotenv import load_dotenv
from services.user_validators import RegisterRequest, LoginRequest

load_dotenv()

# Khởi tạo FastAPI
app = FastAPI()
# Khởi tạo session để truy vấn CSDL
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Khởi tạo biến toàn cục để lưu id người dùng
global_id_user = None

# OAuth2 để xác thực người dùng
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


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
    return credentials


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


# Fuction de set global user id
def set_global_user_id(id_user):
    global global_id_user
    global_id_user = id_user


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


@app.get("/user_credentials")
async def read_user_info(current_user: UserCredentials = Depends(get_current_user)):
    # Sử dụng current_user để lấy thông tin người dùng từ CSDL và thực hiện các thao tác khác
    return {"user_info": current_user}


@app.post("/user_info")
async def update_user_info(data: user_info.UserInfo, db: Session = Depends(get_db)):
    with db:
        db.add(data)
        db.commit()
    return {"status": 200, "message": "Successfully updated user info"}


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
