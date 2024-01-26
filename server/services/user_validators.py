from pydantic import BaseModel
import uuid


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
    full_name: str
    age: int
    gender: bool
    id_image: uuid.UUID
    id_country: uuid.UUID
    id_city: uuid.UUID
    id_district: uuid.UUID
    id_ward: uuid.UUID
    face_feature: str
    is_allowed: bool
