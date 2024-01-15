# from fastapi_jwt_auth import AuthJWT
import sys

sys.path.append("../../../relative_face_recognition_app/server")
from database.engine import engine


from models import *

from fastapi import FastAPI, HTTPException, Request
from fastapi import FastAPI, HTTPException, Request
from sqlmodel import Field, Session, SQLModel, create_engine, select
from services.orm import *
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


@app.post("/users")
async def create_user(req: Request):
    data = await req.json()
    print("User from /users: ", data)
    new_user = user.User(
        username=data["signup_username"],
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
