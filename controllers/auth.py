from dotenv import load_dotenv
from fastapi_jwt_auth import AuthJWT
from typing import List
import base64
import sys
sys.path.append("../../relative_face_recognition_app")
from models.user import User
import requests
from datetime import timedelta
import os

load_dotenv()

ACCESS_TOKEN_EXPIRES_IN = os.getenv("ACCESS_TOKEN_EXPIRES_IN")
REFRESH_TOKEN_EXPIRES_IN = os.getenv("REFRESH_TOKEN_EXPIRES_IN")

class UserAuth:
    def __init__(self, user):
        self.user = user

    def log_in(self, username, password):
        URL = "http://localhost:8080/users/1"
        data = requests.get(url=URL)
        json_data = data.json()
        username = json_data['username']
        password = json_data['password']
        if (self.user.username == username) & (self.user.password == password):
            access_token = AuthJWT.create_access_token(subject=str(self.user.id), expires_time=timedelta(minutes=ACCESS_TOKEN_EXPIRES_IN))
            refresh_token = AuthJWT.create_refresh_token(subject=str(self.user.id), expires_time=timedelta(minutes=REFRESH_TOKEN_EXPIRES_IN))
            return {'status': 200, 'access_token': access_token}
        else :
            return {'status': 400, 'message': 'Username or password is not correct!'}
        
    def register(self):
        pass
        