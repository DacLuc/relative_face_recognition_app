from dotenv import load_dotenv
import requests
import os
from datetime import datetime, timedelta


class user_auth_controller:
    def __init__(self):
        load_dotenv()
        self.SECRET_KEY = os.getenv("SECRET_KEY")
        self.ACCESS_TOKEN_EXPIRES_IN = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")
        self.REFRESH_TOKEN_EXPIRES_IN = os.getenv("REFRESH_TOKEN_EXPIRES_MINUTES")

    # Register function
    def register(self, username: str, email: str, password: str):
        data = {
            "username": username,
            "email": email,
            "password": password,
        }
        URL = "http://localhost:8080/register"
        response = requests.post(url=URL, json=data)
        if response.status_code == 200:
            return True
        else:
            return False

    # Login function
    def log_in(self, username: str, password: str):
        data = {
            "username": username,
            "password": password,
        }
        URL = "http://localhost:8080/token"
        response = requests.post(url=URL, json=data)
        json_data = response.json()
        if response.status_code == 200:
            access_token = json_data["access_token"]
            self.save_token(access_token)
            return True
        else:
            return False

    # Update user info function
    def update_user_info(self, full_name, age, gender, country, city, district, ward):
        data = {
            "full_name": full_name,
            "age": age,
            "gender": gender,
            "id_country": country,
            "id_city": city,
            "id_district": district,
            "id_ward": ward,
        }
        URL = "http://localhost:8080/user_info"
        response = requests.post(url=URL, json=data, headers=self.get_auth_headers())
        if response.status_code == 200:
            return {"status": 200, "message": "Successfully updated user info."}
        else:
            return {"status": response.status_code, "message": response.text}

    # Find people function
    def find_people(
        self,
        user_info_name=None,
        user_info_gender=None,
        user_info_age=None,
        user_info_country=None,
        user_info_city=None,
        user_info_district=None,
        user_info_ward=None,
        user_info_feature=None,
        user_info_img=None,
    ):
        URL = "http://localhost:8080/user_info"
        params = {
            "name": user_info_name,
            "gender": user_info_gender,
            "age": user_info_age,
            "country": user_info_country,
            "city": user_info_city,
            "district": user_info_district,
            "ward": user_info_ward,
            "feature": user_info_feature,
        }
        response = requests.get(url=URL, params=params, headers=self.get_auth_headers())
        json_data = response.json()
        return json_data

    # Save jwt token function
    def save_token(self, token):
        # Lưu trữ token trong biến cục bộ
        global saved_token
        saved_token = token

    # Get auth headers function
    def get_auth_headers(self):
        # Lấy token đã lưu trước đó và trả về headers để gửi đi trong các yêu cầu
        access_token = self.get_saved_token()
        headers = {"Authorization": f"Bearer {access_token}"}
        return headers

    # Get jwt token function
    def get_saved_token(self):
        # Lấy token đã lưu trước đó từ biến cục bộ
        global saved_token
        return saved_token


# Biến toàn cục để lưu trữ token
saved_token = None
