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
