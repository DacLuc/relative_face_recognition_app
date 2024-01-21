from dotenv import load_dotenv
import requests
import os


class user_auth_controller:
    def __init__(self):
        load_dotenv()
        self.ACCESS_TOKEN_EXPIRES_IN = os.getenv("ACCESS_TOKEN_EXPIRES_IN")
        self.REFRESH_TOKEN_EXPIRES_IN = os.getenv("REFRESH_TOKEN_EXPIRES_IN")

    def log_in(self, username, password):
        URL = f"http://localhost:8080/users?username={username}&password={password}"
        data = requests.get(url=URL)
        json_data = data.json()
        print("json_data: ", json_data)
        if json_data["status"] == 200:
            return True
        else:
            return False

    def register(self, username, email, password):
        signup_username = username
        signup_email = email
        signup_password = password

        data = {
            "signup_username": signup_username,
            "signup_email": signup_email,
            "signup_password": signup_password,
        }
        URL = "http://localhost:8080/users/"
        req = requests.post(url=URL, json=data)
        # print(signup_username, signup_email, signup_password)
        if req.status_code == 200:
            return {"status": 200, "message": "Successfully added a new user."}
        else:
            return {"status": 400, "message": "Something went wrong."}

    def update_user_info(self, full_name, age, gender):
        data = {
            "full_name": full_name,
            "age": 16,
            "gender":  gender == "Nam",
        }
        URL = "http://localhost:8080/user_info/"
        req = requests.post(url=URL, json=data)
        # print(signup_username, signup_email, signup_password)
        if req.status_code == 200:
            return {"status": 200, "message": "Successfully updated user info."}
        else:
            return {"status": 400, "message": "Something went wrong."}

    def find_people(self, user_info_name = None, user_info_gender = None, user_info_age = None, user_info_country = None, user_info_city = None, user_info_district = None, user_info_ward = None, user_info_feature = None, user_info_img = None):
        # filter based on basic info
        URL = f"http://localhost:8080/user_info?name={user_info_name}&gender={user_info_gender}&age={user_info_age}&country={user_info_country}&city={user_info_city}&district={user_info_district}&ward={user_info_ward}&feature={user_info_feature}"
        data = requests.get(url=URL)
        json_data = data.json()
        print("---> json_data: ", json_data)

