from server.services.auth import user_auth_controller
from PyQt6 import QtCore, QtGui
import uuid


user_auth_controller = user_auth_controller()


def print_available_user_info(user_info: dict):
    user_info_id = user_info["id_user"]
    user_info_name = user_info["full_name"]
    user_info_age = user_info["age"]
    user_info_gender = user_info["gender"]
    user_info_country = user_auth_controller.get_country_name(user_info["id_country"])
    if user_info_country is not None:
        user_info_country = user_info_country["name_country"]
    else:
        user_info_country = "Error"
    user_info_city = user_auth_controller.get_city_name(user_info["id_city"])
    if user_info_city is not None:
        user_info_city = user_info_city["name_city"]
    else:
        user_info_city = "Error"

    user_info_district = user_auth_controller.get_district_name(
        user_info["id_district"]
    )
    if user_info_district is not None:
        user_info_district = user_info_district["name_district"]
    else:
        user_info_district = "Error"

    user_info_ward = user_auth_controller.get_ward_name(user_info["id_ward"])
    if user_info_ward is not None:
        user_info_ward = user_info_ward["name_ward"]
    else:
        user_info_ward = "Error"
    user_info_feature = user_info["face_feature"]
    user_info_image = user_auth_controller.display_image(user_info_id)
    user_check_is_allowed = user_info["is_allowed"]
    return (
        user_info_name,
        user_info_gender,
        user_info_age,
        user_info_country,
        user_info_city,
        user_info_district,
        user_info_ward,
        user_info_feature,
        user_info_image,
        user_check_is_allowed,
    )


def transform_found_user_info(json_data: list):
    similar_users = json_data.get("similar_users", [])
    transformed_json_data_list = []
    for user_info in similar_users:
        user_info_id = user_info.get("id", "")
        user_info_id_user = user_info.get("id_user", "")
        user_info_name = user_info.get("full_name", "")
        user_info_age = user_info.get("age", "")
        user_info_gender = user_info.get("gender", "")
        if user_info_gender == True:
            user_info_gender = "Nam"
        else:
            user_info_gender = "Nữ"

        user_info_country = user_auth_controller.get_country_name(
            user_info.get("id_country", "")
        )
        if user_info_country is not None:
            user_info_country = user_info_country["name_country"]
        else:
            user_info_country = "Error"

        user_info_city = user_auth_controller.get_city_name(
            user_info.get("id_city", "")
        )
        if user_info_city is not None:
            user_info_city = user_info_city["name_city"]
        else:
            user_info_city = "Error"

        user_info_district = user_auth_controller.get_district_name(
            user_info.get("id_district", "")
        )
        if user_info_district is not None:
            user_info_district = user_info_district["name_district"]
        else:
            user_info_district = "Error"
        user_info_ward = user_auth_controller.get_ward_name(
            user_info.get("id_ward", "")
        )
        if user_info_ward is not None:
            user_info_ward = user_info_ward["name_ward"]
        else:
            user_info_ward = "Error"
        user_info_feature = user_info.get("face_feature", "")
        user_info_id_image = user_info.get("id_image", "")

        transformed_json_data = {
            "id": user_info_id,
            "id_user": user_info_id_user,
            "full_name": user_info_name,
            "age": user_info_age,
            "gender": user_info_gender,
            "id_country": user_info_country,
            "id_city": user_info_city,
            "id_district": user_info_district,
            "id_ward": user_info_ward,
            "face_feature": user_info_feature,
            "id_image": user_info_id_image,
        }

        transformed_json_data_list.append(transformed_json_data)
    return {"similar_users": transformed_json_data_list}


def display_main_user_info(
    ui,
    user_info_name: str,
    user_info_gender: str,
    user_info_age: int,
    user_info_country: str,
    user_info_city: str,
    user_info_district: str,
    user_info_ward: str,
    user_info_feature: str,
    user_info_image: bytes,
    user_info_check_is_allowed: bool,
):
    ui.ho_ten.setText(user_info_name)
    ui.age_range.setValue(user_info_age)
    ui.gioi_tinh_box.setCurrentText(user_info_gender)
    ui.label_user_img.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
    pixmap = QtGui.QPixmap()
    pixmap.loadFromData(user_info_image)
    scaled_pixmap = pixmap.scaled(
        ui.label_user_img.size(),
        QtCore.Qt.AspectRatioMode.KeepAspectRatio,
        QtCore.Qt.TransformationMode.SmoothTransformation,
    )
    ui.label_user_img.setPixmap(scaled_pixmap)
    ui.label_user_img.setScaledContents(True)
    ui.info_face_text.setText(user_info_feature)
    ui.nation_box.setPlaceholderText(user_info_country)
    ui.city_box.setPlaceholderText(user_info_city)
    ui.district_box.setPlaceholderText(user_info_district)
    ui.ward_box.setPlaceholderText(user_info_ward)
    ui.is_allowed.setChecked(user_info_check_is_allowed)


def display_update_user_info(
    ui,
    user_info_name: str,
    user_info_gender: str,
    user_info_age: int,
    user_info_country: str,
    user_info_city: str,
    user_info_district: str,
    user_info_ward: str,
    user_info_feature: str,
    user_info_image: bytes,
):
    ui.name_text.setText(user_info_name)
    ui.age_text.setText(str(user_info_age))
    ui.sex_text.setText(user_info_gender)
    ui.place_text.setText(
        f"{user_info_ward}, {user_info_district}, \n{user_info_city}, {user_info_country}"
    )
    ui.feat_text.setText(user_info_feature)
    ui.image_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
    pixmap = QtGui.QPixmap()
    pixmap.loadFromData(user_info_image)
    scaled_pixmap = pixmap.scaled(
        ui.image_label.size(),
        QtCore.Qt.AspectRatioMode.KeepAspectRatio,
        QtCore.Qt.TransformationMode.SmoothTransformation,
    )
    ui.image_label.setPixmap(scaled_pixmap)
    ui.image_label.setScaledContents(True)


def display_user_uploaded_img(ui, id_user_info: uuid.UUID):
    ui.label_user_img.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
    image_data = user_auth_controller.display_image(id_user_info)
    pixmap = QtGui.QPixmap()
    pixmap.loadFromData(image_data)
    scaled_pixmap = pixmap.scaled(
        ui.label_user_img.size(),
        QtCore.Qt.AspectRatioMode.KeepAspectRatio,
        QtCore.Qt.TransformationMode.SmoothTransformation,
    )
    ui.label_user_img.setPixmap(scaled_pixmap)


def display_user_request_img(ui, id_user_info: uuid.UUID):
    ui.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
    image_data = user_auth_controller.display_request_image(id_user_info)
    pixmap = QtGui.QPixmap()
    pixmap.loadFromData(image_data)
    scaled_pixmap = pixmap.scaled(
        ui.label.size(),
        QtCore.Qt.AspectRatioMode.KeepAspectRatio,
        QtCore.Qt.TransformationMode.SmoothTransformation,
    )
    ui.label.setPixmap(scaled_pixmap)


# Display user info after finding user
def display_user_info(
    ui,
    user_info_name: str,
    user_info_gioi_tinh: str,
    user_info_age,
    user_info_country: str,
    user_info_city: str,
    user_info_district: str,
    user_info_ward: str,
    user_info_feature: str,
):
    ui.name_info.setText(user_info_name)
    ui.sex_info.setText(user_info_gioi_tinh)
    ui.age_info.setText(str(user_info_age))
    ui.place_info.setText(
        f"{user_info_ward}, {user_info_district}, \n{user_info_city}, {user_info_country}"
    )
    ui.feat_info.setText(user_info_feature)
    # ui.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
    # ui.label.setPixmap(QtGui.QPixmap().loadFromData(user_info_image))
    # ui.label.setScaledContents(True)
    # ui.label.show()
