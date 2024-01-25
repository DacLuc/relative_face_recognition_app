from models.user_credentials import UserCredentials
from models.user_info import UserInfo
from sqlmodel import Field, Session, SQLModel, create_engine, select, col
import sys

sys.path.append("../../../../relative_face_recognition_app/server")
from database.engine import engine


def select_users(username, password):
    with Session(engine) as session:
        statement = select(UserCredentials).where(
            UserCredentials.user_name == username, UserCredentials.password == password
        )
        results = session.exec(statement)
        return results.all()


def filter_users(
    name, gender, age, id_country=None, id_city=None, id_district=None, id_ward=None
):
    with Session(engine) as session:
        statement = select(UserInfo).where(
            col(UserInfo.full_name).contains(name),
            UserInfo.gender == (gender == "Nam"),
            UserInfo.age >= age,
            # UserInfo.id_country == id_country,
            # UserInfo.id_city == id_city,
            # UserInfo.id_district == id_district,
            # UserInfo.id_ward == id_ward
        )
        results = session.exec(statement)
        return results.all()
