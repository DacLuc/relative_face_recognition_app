from dotenv import load_dotenv
import requests
import os
import json
import uuid


class user_auth_controller:
    def __init__(self):
        load_dotenv()
        self.SECRET_KEY = os.getenv("SECRET_KEY")
        self.ACCESS_TOKEN_EXPIRES_IN = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")
        self.REFRESH_TOKEN_EXPIRES_IN = os.getenv("REFRESH_TOKEN_EXPIRES_MINUTES")

    # ------------------------
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

    # ------------------------
    # Login function
    def log_in(self, username: str, password: str):
        data = {
            "username": username,
            "password": password,
        }
        URL = "http://localhost:8080/token"
        response = requests.post(url=URL, json=data)
        print("response: ", response.status_code)
        try:
            json_data = response.json()
            # Xử lý dữ liệu JSON ở đây
            print("JSON response:", json_data)
        except json.decoder.JSONDecodeError:
            # Xử lý trường hợp response.text không phải là JSON hợp lệ
            print("Invalid JSON response:", response.text)
        if response.status_code == 200:
            access_token = json_data["access_token"]
            self.save_token(access_token)
            return True
        else:
            return False

    # -------------------------
    def get_user_id_from_auth_controller(self):
        response = requests.get(
            "http://localhost:8080/user_id",
            headers=self.get_auth_headers(),
        )
        print("response: ", response.status_code)
        print("response: ", response.text)

        if response.status_code == 200:
            return response.text.replace('"', "")
        else:
            # Handle error
            return None

    # Create user info function
    def create_user_info(
        self,
        id_user: uuid.UUID,
        full_name: str,
        age: int,
        gender: bool,
        id_image: uuid.UUID,
        id_country: uuid.UUID,
        id_city: uuid.UUID,
        id_district: uuid.UUID,
        id_ward: uuid.UUID,
        face_feature: str,
        is_allowed: bool,
    ):
        data = {
            "id_user": str(id_user),
            "full_name": full_name,
            "age": age,
            "gender": gender,
            "id_image": str(id_image),
            "id_country": str(id_country),
            "id_city": str(id_city),
            "id_district": str(id_district),
            "id_ward": str(id_ward),
            "face_feature": face_feature,
            "is_allowed": is_allowed,
        }
        print("data json: ", data)
        URL = "http://localhost:8080/create_user_info"
        response = requests.post(url=URL, json=data, headers=self.get_auth_headers())
        print("response: ", response.status_code)
        print("response: ", response.text)
        if response.status_code == 200:
            return True
        else:
            return False

    # -------------------------
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
