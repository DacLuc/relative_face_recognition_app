# from fastapi_jwt_auth import AuthJWT
import uuid
import sys

sys.path.append("../../../relative_face_recognition_app/server")
from database.engine import engine

from models import *

from fastapi import FastAPI, HTTPException, Request
from sqlmodel import Field, Session, SQLModel, create_engine, select
from services.orm import *

app = FastAPI()


@app.get("/users")
async def read_user(username: str, password: str):
    results = select_users(username, password)
    print("results: ", results)
    # with Session(engine) as session:
    #     found_user = session.get(user.User, user_id)
    #     if not found_user:
    #         raise HTTPException(status_code=404, detail="User not found")
    #     return found_user

    if len(results):
        return {"status": 200, "message": "Login successfully", "data": results}
    else:
        return {"status": 400, "message": "Login failed!"}

@app.post("/user_info")
async def update_user_info(req: Request):
    data = await req.json()
    info = user_info.UserInfo(
        id_user=uuid.UUID("ee516811-03f5-4ad8-aeb9-db2bb2953caa").hex,
        full_name=data["full_name"],
        age=data["age"],
        gender=data["gender"],
        id_image=None,
        id_country=None,
        id_city=None,
        id_district=None,
        id_ward=None,
        is_finding_user=False,
        is_allowed=True,
        is_searched_user=False
    )
    with Session(engine) as session:
        session.add(info)
        session.commit()
    return {"status": 200, "message": "Successfully updated user info"}

@app.get("/user_info")
async def read_user_info(name: str, gender: str, age: str, country: str, city: str, district: str, ward: str, feature: str):
    print(name, gender, age, country, city, district, ward, feature)
    result = filter_users(name = name, gender = gender, age = 10)
    print("* ******* * result from filter_users: ", result)
    return {"status": 200, "message": "Successfully queried user info"}

@app.post("/users")
async def create_user(req: Request):
    data = await req.json()
    print("User from /users: ", data)
    new_user = user_credentials.UserCredentials(
        user_name=data["signup_username"],
        email=data["signup_email"],
        password=data["signup_password"],
    )
    with Session(engine) as session:
        session.add(new_user)
        session.commit()
    return {"status": 200, "message": "Successfully created a new user"}

@app.get("/auth/login")
def login(username, password):
    pass
    # if (username == username) & (self.user.password == password):
    #     access_token = AuthJWT.create_access_token(subject=str(
    #         self.user.id), expires_time=timedelta(minutes=ACCESS_TOKEN_EXPIRES_IN))
    #     refresh_token = AuthJWT.create_refresh_token(subject=str(
    #         self.user.id), expires_time=timedelta(minutes=REFRESH_TOKEN_EXPIRES_IN))
    #     return {'status': 200, 'access_token': access_token}
    # else:
    #     return {'status': 400, 'message': 'Username or password is not correct!'}


@app.post("/auth/register")
def register():
    pass
