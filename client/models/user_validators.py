from pydantic import BaseModel


class UserSignUp(BaseModel):
    username: str
    email: str
    password: str


class UserSignIn(BaseModel):
    username: str
    password: str
