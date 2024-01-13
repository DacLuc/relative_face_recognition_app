from sqlmodel import Field, Session, SQLModel, create_engine, select
import sys
sys.path.append("../../server")
from database.engine import engine
from models.user import User

def select_users(username, password):
    with Session(engine) as session:
        statement = select(User).where(User.username == username,
                                       User.password == password)
        results = session.exec(statement)
        return results.all()