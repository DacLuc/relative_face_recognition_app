from pydantic import BaseModel
import uuid
from typing import Optional


class TokenRequest(BaseModel):
    username: str
    password: str


class RegisterRequest(BaseModel):
    username: str
    email: str
    password: str


class LoginRequest(BaseModel):
    username: str
    password: str


class UserInfoRequest(BaseModel):
    id_user: uuid.UUID
    full_name: Optional[str]
    age: Optional[int]
    gender: Optional[bool]
    id_image: uuid.UUID
    id_country: Optional[uuid.UUID]
    id_city: Optional[uuid.UUID]
    id_district: Optional[uuid.UUID]
    id_ward: Optional[uuid.UUID]
    face_feature: Optional[str]
    is_allowed: Optional[bool]
