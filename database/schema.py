from sqlmodel import SQLModel
import sys
sys.path.append("../../relative_face_recognition_app")
from models import *
from database.engine import engine

SQLModel.metadata.create_all(engine)
