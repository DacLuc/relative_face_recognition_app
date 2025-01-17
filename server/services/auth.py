from dotenv import load_dotenv
import requests
import os
import json
import uuid
from typing import Optional

# Biến toàn cục để lưu trữ access_token
saved_token = None


# ---------------------------------
# User auth controller class
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
        try:
            json_data = response.json()
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
    # Get user id from auth controller function
    def get_user_credentials_id_from_auth_controller(self):
        response = requests.get(
            "http://localhost:8080/user_credentials_id",
            headers=self.get_auth_headers(),
        )

        if response.status_code == 200:
            return response.text.replace('"', "")
        else:
            # Handle error
            return None

    def get_user_credentials_name_from_auth_controller(self):
        response = requests.get(
            "http://localhost:8080/user_credentials_name",
            headers=self.get_auth_headers(),
        )

        if response.status_code == 200:
            return response.text.replace('"', "")
        else:
            # Handle error
            return None

    # -------------------------
    # Create user info function
    def create_user_info(
        self,
        id_user: uuid.UUID,
        full_name: Optional[str],
        age: Optional[int],
        gender: Optional[bool],
        id_image: Optional[uuid.UUID],
        id_country: Optional[uuid.UUID],
        id_city: Optional[uuid.UUID],
        id_district: Optional[uuid.UUID],
        id_ward: Optional[uuid.UUID],
        face_feature: Optional[str],
        is_allowed: Optional[bool],
    ):
        data = {
            "id_user": str(id_user),
            "full_name": full_name,
            "age": age,
            "gender": gender,
            "id_image": str(id_image),
            "id_country": str(id_country) if id_country else None,
            "id_city": str(id_city) if id_city else None,
            "id_district": str(id_district) if id_district else None,
            "id_ward": str(id_ward) if id_ward else None,
            "face_feature": face_feature,
            "is_allowed": is_allowed,
        }
        URL = "http://localhost:8080/create_user_info"
        response = requests.post(url=URL, json=data, headers=self.get_auth_headers())
        # response.status_code == 200: Success when creating user info
        if response.status_code == 200:
            return 0
        # response.status_code == 400: User info already exists -> Need to update user info
        elif response.status_code == 400:
            return 1
        # response.status_code == 500: Internal server error because of some reasons controller layers.
        else:
            return 2

    # -------------------------
    # Get user info function
    def get_user_info(self, id_user: uuid.UUID):
        URL = f"http://localhost:8080/get_user_info/{str(id_user)}"
        response = requests.get(url=URL, headers=self.get_auth_headers())
        # response.status_code == 200: Success when getting user info
        if response.status_code == 200:
            return response.json()  # Return user info json data type
        # response.status_code == 404: User info not found -> Need to create user info
        else:
            print("Error about User Info: ", response.status_code)
            print("Error about User Info Text: ", response.text)
            return None

    # -------------------------
    # Update user info function
    def update_user_info(
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
        URL = f"http://localhost:8080/update_user_info/{str(id_user)}"
        response = requests.put(url=URL, json=data, headers=self.get_auth_headers())
        # response.status_code == 200: Success when updating user info
        if response.status_code == 200:
            return True
        # response.status_code == 404: User info not found -> Need to create user info -> Then update user info
        else:
            print("Error about Update User Info: ", response.status_code)
            print("Error about Update User Info Text: ", response.text)
            return False

    # -------------------------
    # Upload image function
    def upload_image(self, name_image: str, image_path: str):
        try:
            with open(image_path, "rb") as image_file:
                files = {"file": (name_image, image_file, "image/jpeg")}

                URL = "http://localhost:8080/upload_image"
                response = requests.post(
                    url=URL,  # Send data as JSON in the request body
                    files=files,
                    headers=self.get_auth_headers(),
                )

                if response.status_code == 200:
                    json_data = response.json()
                    print("Upload Image: ", json_data)
                    print("Upload Image: ", json_data["id_image"])
                    return json_data["id_image"]
                elif response.status_code == 400:
                    return 400
                elif response.status_code == 500:
                    # Handle error
                    print("Error: ", response.status_code)
                    print("Error: ", response.text)
                    return None
        except Exception as e:
            # Handle other exception
            print(f"Error during image upload: {e}")
            return None

    # -------------------------
    # Update image function
    def update_image(self, id_user: uuid.UUID, name_image: str, image_path: str):
        try:
            with open(image_path, "rb") as image_file:
                files = {"file": (name_image, image_file, "image/jpeg")}

                URL = f"http://localhost:8080/update_user_image/{str(id_user)}"
                response = requests.put(
                    url=URL,  # Send data as JSON in the request body
                    files=files,
                    headers=self.get_auth_headers(),
                )
                # response.status_code == 200: Success when updating user image
                if response.status_code == 200:
                    json_data = response.json()
                    print("Updated Image: ", json_data)
                    print("Updated Image: ", json_data["id_image"])
                    return json_data["id_image"]
                # response.status_code == 404: User info image not found -> Need to create user info image -> Then update user info image
                elif response.status_code == 404:
                    return 404
                elif response.status_code == 400:
                    return 400
                else:
                    # Handle error
                    print("Error: ", response.status_code)
                    print("Error: ", response.text)
                    return None
        except Exception as e:
            # Handle other exception
            print(f"Error during image upload: {e}")
            return None

    # -------------------------
    # Delete image function
    def delete_image(self, user_id: uuid.UUID):
        URL = f"http://localhost:8080/delete_user_image/{str(user_id)}"
        response = requests.delete(url=URL, headers=self.get_auth_headers())
        # response.status_code == 200: Success when deleting user image
        if response.status_code == 200:
            return True
        else:
            # Handle error
            print("Error: ", response.status_code)
            print("Error: ", response.text)
            return False

    # -------------------------
    # Get image id function
    def get_image_id(self, user_id: uuid.UUID):
        URL = f"http://localhost:8080/get_user_image_by_id/{str(user_id)}"
        response = requests.get(url=URL, headers=self.get_auth_headers())
        # response.status_code == 200: Success when getting user image id
        if response.status_code == 200:
            print("Image ID: ", response.json())
            return response.json()
        # response.status_code == 404: User info image not found -> Need to create user info image
        else:
            print("Error about Image: ", response.status_code)
            print("Error about Image Text: ", response.text)
            return None

    # -------------------------
    def display_image(self, user_id: uuid.UUID):
        try:
            URL = f"http://localhost:8080/get_user_image/{str(user_id)}"
            response = requests.get(url=URL, headers=self.get_auth_headers())
            if response.status_code == 200:
                return response.content
            else:
                # Handle error
                print(f"Error fetching user image: {response.status_code}")
                return None
        except Exception as e:
            # Handle other exception
            print(f"Error during image display: {e}")
            return None

    # -------------------------
    def upload_request_image(self, name_image: str, image_path: str):
        try:
            with open(image_path, "rb") as image_file:
                files = {"file": (name_image, image_file, "image/jpeg")}

                URL = "http://localhost:8080/upload_request_image"
                response = requests.post(
                    url=URL,  # Send data as JSON in the request body
                    files=files,
                    headers=self.get_auth_headers(),
                )

                if response.status_code == 200:
                    json_data = response.json()
                    print("Upload Request Image: ", json_data)
                    print("Upload Request Image: ", json_data["id_request_image"])
                    return json_data["id_request_image"]
                elif response.status_code == 400:
                    return 400
                elif response.status_code == 500:
                    # Handle error
                    print("Error: ", response.status_code)
                    print("Error: ", response.text)
                    return None
        except Exception as e:
            # Handle other exception
            print(f"Error during request image upload: {e}")
            return None

    def update_request_image(
        self, id_user: uuid.UUID, name_image: str, image_path: str
    ):
        try:
            with open(image_path, "rb") as image_file:
                files = {"file": (name_image, image_file, "image/jpeg")}

                URL = f"http://localhost:8080/update_request_image/{str(id_user)}"
                response = requests.put(
                    url=URL,  # Send data as JSON in the request body
                    files=files,
                    headers=self.get_auth_headers(),
                )
                # response.status_code == 200: Success when updating user image
                if response.status_code == 200:
                    json_data = response.json()
                    print("Updated Request Image: ", json_data)
                    print("Updated Request Image: ", json_data["id_request_image"])
                    return json_data["id_request_image"]
                # response.status_code == 404: User info image not found -> Need to create user info image -> Then update user info image
                elif response.status_code == 404:
                    return 404
                elif response.status_code == 400:
                    return 400
                else:
                    # Handle error
                    print("Error: ", response.status_code)
                    print("Error: ", response.text)
                    return None
        except Exception as e:
            # Handle other exception
            print(f"Error during request image upload: {e}")
            return None

    def delete_request_image(self, user_id: uuid.UUID):
        URL = f"http://localhost:8080/delete_request_image/{str(user_id)}"
        response = requests.delete(url=URL, headers=self.get_auth_headers())
        # response.status_code == 200: Success when deleting user image
        if response.status_code == 200:
            return True
        else:
            # Handle error
            print("Error: ", response.status_code)
            print("Error: ", response.text)
            return False

    def get_request_image_id(self, user_id: uuid.UUID):
        URL = f"http://localhost:8080/get_request_image_by_id/{str(user_id)}"
        response = requests.get(url=URL, headers=self.get_auth_headers())
        # response.status_code == 200: Success when getting user image id
        if response.status_code == 200:
            print("Image ID: ", response.json())
            return response.json()
        # response.status_code == 404: User info image not found -> Need to create user info image
        else:
            print("Error about Image: ", response.status_code)
            print("Error about Image Text: ", response.text)
            return None

    def display_request_image(self, user_id: uuid.UUID):
        try:
            URL = f"http://localhost:8080/get_request_image/{str(user_id)}"
            response = requests.get(url=URL, headers=self.get_auth_headers())
            if response.status_code == 200:
                return response.content
            else:
                # Handle error
                print(f"Error fetching user image: {response.status_code}")
                return None
        except Exception as e:
            # Handle other exception
            print(f"Error during image display: {e}")
            return None

    # -------------------------
    # Get country function
    def get_country_name(self, id_country: uuid.UUID):
        # Check if id_country is None
        if id_country is None:
            return None
        # Check if id_country is not None
        else:
            URL = f"http://localhost:8080/get_country_info/{str(id_country)}"
            response = requests.get(url=URL, headers=self.get_auth_headers())
            # response.status_code == 200: Success when getting country info name
            if response.status_code == 200:
                json_data = response.json()
                return json_data
            # response.status_code == 404: Country info not found -> Need to create country info
            else:
                print("Error about Country: ", response.status_code)
                print("Error about Country Text: ", response.text)
                return None

    # -------------------------
    # Get city function
    def get_city_name(self, id_city: uuid.UUID):
        # Check if id_city is None
        if id_city is None:
            return None
        # Check if id_city is not None
        else:
            URL = f"http://localhost:8080/get_city_info/{str(id_city)}"
            response = requests.get(url=URL, headers=self.get_auth_headers())
            # response.status_code == 200: Success when getting city info name
            if response.status_code == 200:
                json_data = response.json()
                return json_data
            # response.status_code == 404: City info not found -> Need to create city info
            else:
                print("Error about City: ", response.status_code)
                print("Error about City Text: ", response.text)
                return None

    # -------------------------
    # Get district function
    def get_district_name(self, id_district: uuid.UUID):
        # Check if id_district is None
        if id_district is None:
            return None
        # Check if id_district is not None
        else:
            URL = f"http://localhost:8080/get_district_info/{str(id_district)}"
            response = requests.get(url=URL, headers=self.get_auth_headers())
            # response.status_code == 200: Success when getting district info name
            if response.status_code == 200:
                json_data = response.json()
                return json_data
            # response.status_code == 404: District info not found -> Need to create district info
            else:
                print("Error about District: ", response.status_code)
                print("Error about District Text: ", response.text)
                return None

    # -------------------------
    # Get ward function
    def get_ward_name(self, id_ward: uuid.UUID):
        # Check if id_ward is None
        if id_ward is None:
            return None
        # Check if id_ward is not None
        else:
            URL = f"http://localhost:8080/get_ward_info/{str(id_ward)}"
            response = requests.get(url=URL, headers=self.get_auth_headers())
            # response.status_code == 200: Success when getting ward info name
            if response.status_code == 200:
                json_data = response.json()
                return json_data
            # response.status_code == 404: Ward info not found -> Need to create ward info
            else:
                print("Error about Ward: ", response.status_code)
                print("Error about Ward Text: ", response.text)
                return None

    # -------------------------
    # Get founders info function
    def get_founders_info(self, request_image_id: uuid.UUID):
        if request_image_id is None:
            print("Request Image ID is None")
            return None
        else:
            URL = f"http://localhost:8080/find_similar_users/{str(request_image_id)}"
            response = requests.get(url=URL, headers=self.get_auth_headers())
            if response.status_code == 200:
                json_data = response.json()
                print("Founders Info: ", json_data)
                return json_data
            elif response.status_code == 404:
                return 404
            else:
                print("Error about Founders Info: ", response.status_code)
                print("Error about Founders Info Text: ", response.text)
                return None

    # -------------------------
    # Phan nay chua update the new version duoc nua vi phai lam xong cai pgvector truoc moi co the update duoc
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

    # -------------------------
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
