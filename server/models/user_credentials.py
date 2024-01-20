from typing import Optional
from sqlmodel import Field, SQLModel
import uuid
from sqlalchemy import Column, DateTime, func
from datetime import datetime


# UserCredentials(id, user_name, email, password, created_at, updated_at, last_login, login_count)
# --> day la table de luu thong tin cua user khi dang ky (bang nay co 2 chuc nang chinh la: luu du lieu cua user dang ky va kiem tra xem user co tai khoan dang nhap hay khong)
# --> Muon biet duoc user nao dang nhap thi ta se dung cot last_login (neu last_login = None thi user do chua dang nhap, nguoc lai neu last_login != None thi user do da dang nhap)
# --> Muon biet duoc user nao dang nhap thi ta se dung cot login_count (neu login_count = 0 thi user do chua dang nhap, nguoc lai neu login_count != 0 thi user do da dang nhap)
class UserCredentials(SQLModel, table=True):
    # id_user: la id cua user account duoc tao khi dang ky
    id: Optional[uuid.UUID] = Field(
        default_factory=uuid.uuid4,
        primary_key=True,
        index=True,
        nullable=False,
        sa_column_kwargs=dict(server_default=func.gen_random_uuid()),
    )
    # user_name: la username cua user khi dang ky (check xem co ten user nay trong database chua, neu chua thi cho dang ky, nguoc lai thi bao loi va yeu cau user nhap lai username khac)
    user_name: str = Field(
        index=True,
        nullable=False,
        unique=True,
        max_length=50,
        min_length=3,
        regex="^[a-zA-Z0-9_]*$",
        description="Username must be between 3 and 50 characters long and can only contain letters, numbers and underscores.",
    )
    # emailL la email cua user khi dang ky (check xem co email nay trong database chua, neu chua thi cho dang ky, nguoc lai thi bao loi va yeu cau user nhap lai email khac)
    email: str = Field(
        index=True, nullable=False, unique=True, max_length=50, min_length=3
    )
    # password: la password cua user khi dang ky
    password: str = Field(
        index=True, nullable=False, max_length=50, min_length=3, regex="^[a-zA-Z0-9_]*$"
    )
    # created_at: la thoi diem ma user dang ky tai khoan thanh cong (luu ca ngay/thang/nam gio:phut:giay)
    created_at: Optional[datetime] = Column(
        DateTime, server_default=func.now(), nullable=False
    )
    # last_login: la thoi diem ma user dang nhap vao tai khoan (luu ca ngay/thang/nam gio:phut:giay)
    last_login: Optional[datetime] = Column(
        DateTime, server_default=func.now(), nullable=False
    )
    # login_count: la so lan ma user dang nhap vao tai khoan
    login_count: int = Field(default=0, nullable=False)
