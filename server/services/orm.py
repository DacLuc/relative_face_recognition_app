from sqlmodel import Field, Session, SQLModel, create_engine, select, col
import sys
import os

sys.path.append("../../../face_recognition_app/server")
from database.engine import engine
from server.models.user_credentials import User


def select_users(username, password):
    with Session(engine) as session:
        statement = select(User).where(
            User.username == username, User.password == password
        )
        results = session.exec(statement)
        return results.all()
