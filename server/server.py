import sys
sys.path.append("../../relative_face_recognition_app")
from database.engine import engine
from models import *
from typing import List, Optional

from fastapi import FastAPI, HTTPException
from sqlmodel import Field, Session, SQLModel, create_engine, select

app = FastAPI()

@app.get("/users/{user_id}", response_model=user.User)
def read_user(user_id: int):
    with Session(engine) as session:
        found_user = session.get(user.User, user_id)
        if not found_user:
            raise HTTPException(status_code=404, detail="User not found")
        return found_user
