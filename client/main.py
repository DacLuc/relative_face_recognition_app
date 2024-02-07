import sys
from PyQt6 import QtWidgets, QtGui, QtCore
import sys
import os
import uuid

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../")
import frontend.home_page, frontend.signup_ui, frontend.login_ui, frontend.credit_ui, frontend.menu, frontend.user_info, frontend.found_users, frontend.get_responses_image
import frontend.check_fill_info, frontend.check_signup, frontend.check_wrong_signup, frontend.check_robot_ui, frontend.check_confirm_password, frontend.check_type, frontend.check_login, frontend.check_wrong_login, frontend.check_cancel_user_info, frontend.check_cancel_updated_user_info, frontend.check_right_update_user_info, frontend.check_wrong_update_user_info, frontend.check_upload_pic, frontend.check_finished_upload_image, frontend.check_wrong_upload_image, frontend.check_update_user_info
from controllers.cities_districts_wards import LocationApp
from server.services.auth import user_auth_controller
from client.controllers.controllers import (
    print_available_user_info,
    display_main_user_info,
    display_update_user_info,
    display_user_uploaded_img,
)

user_auth_controller = user_auth_controller()

ui = ""
app = QtWidgets.QApplication(sys.argv)
Mainwindow = QtWidgets.QMainWindow()
id_image_global = None
id_updated_image_global = None


# ----------------UI MainWindow-----------------
# Home Page UI MainWindow ==> Done
def home_page_ui():
    global ui
    ui = frontend.home_page.Ui_Home_Page()
    ui.setupUi(Mainwindow)
    # sign up button
    ui.signup_button.clicked.connect(signup_ui_load)
    # login button
    ui.signin_button.clicked.connect(login_ui_load)
    # credit button
    ui.credit_button.clicked.connect(credit_ui_load)
    # exit button
    ui.exit_button.clicked.connect(Mainwindow.close)
    Mainwindow.show()


# ----------------UI MainWindow-----------------
# SignUp UI MainWindow ==> Done
def signup_ui_load():
    global ui
    ui = frontend.signup_ui.Ui_Sign_Up_Page()
    ui.setupUi(Mainwindow)
    # apply button
    ui.apply_button.clicked.connect(check_signup_user_auth_controller)
    # cancel button
    ui.cancel_button.clicked.connect(home_page_ui)
    Mainwindow.show()


# check signup controllers (from client layer to controller layer)
def check_signup_user_auth_controller():
    account_name = ui.account_name.text()
    account_email = ui.account_email.text()
    account_password = ui.account_password.text()
    check_robot = ui.check_robot.isChecked()
    confirm_password = ui.confirm_password.text()

    # ---
    # check if user is not robot
    if check_robot:
        if (
            not account_name
            or not account_email
            or not account_password
            or not confirm_password
        ):
            # Thuc hien bao loi (tra ve cho client) do khong dien day du thong tin
            check_fill_info_ui()
            signup_ui_load()
        elif account_email.find("@gmail.com") == -1:
            check_type_ui()
            signup_ui_load()
        elif account_password != confirm_password:
            # Thuc hien bao loi (tra ve cho client) do khong xac nhan dung mat khau (passWord)
            check_confirm_password_ui()
            signup_ui_load()
        elif user_auth_controller.register(
            account_name, account_email, account_password
        ):
            # Thuc hien day du khi dang ky thanh cong (tra ve cho client)
            check_right_signup_ui()
            login_ui_load()
        else:
            # Thuc hien bao loi (tra ve cho client) do khong the dang ky duoc tai khoan do da ton tai trong database
            check_wrong_signup_ui()
            signup_ui_load()
    else:
        # Thuc hien bao loi (tra ve cho client) do khong phai la nguoi dung that (la robot)
        check_robot_ui()
        signup_ui_load()


# ----------------UI MainWindow-----------------
# Login UI MainWindow ==> Done
def login_ui_load():
    global ui
    ui = frontend.login_ui.Ui_Sign_In_Page()
    ui.setupUi(Mainwindow)
    # apply button
    ui.apply_button.clicked.connect(check_login_user_auth_controller)
    # signup button
    ui.signup_button.clicked.connect(signup_ui_load)
    # cancel button
    ui.cancel_button.clicked.connect(home_page_ui)
    Mainwindow.show()


# check login controllers (from client layer to controller layer)
def check_login_user_auth_controller():
    username = ui.account_name.text()
    password = ui.account_password.text()
    if not username or not password:
        # Thuc hien bao loi (tra ve cho client) do khong dien day du thong tin
        check_fill_info_ui()
        login_ui_load()
    elif user_auth_controller.log_in(username, password):
        # Thuc hien day du khi dang nhap thanh cong (tra ve cho client)
        check_right_login_ui()
        menu_ui()
    else:
        # Thuc hien bao loi (tra ve cho client) do khong the dang nhap duoc tai khoan do khong ton tai trong database
        check_wrong_login_ui()


# ----------------UI MainWindow-----------------
# Credit UI MainWindow ==> Done
def credit_ui_load():
    global ui
    ui = frontend.credit_ui.Ui_Credit_Page()
    ui.setupUi(Mainwindow)
    # back button
    ui.back_button.clicked.connect(home_page_ui)
    Mainwindow.show()


# ----------------UI MainWindow-----------------
# Menu UI MainWindow ==> Done
def menu_ui():
    global ui
    ui = frontend.menu.Ui_Specific_Task()
    ui.setupUi(Mainwindow)
    user_credentials_name = (
        user_auth_controller.get_user_credentials_name_from_auth_controller()
    )
    # user name account
    ui.name_account.setText(
        f'<html><head/><body><p align="center"><span style=" font-size:14pt;">{user_credentials_name}</span></p></body></html>'
    )
    # user info button
    ui.user_info_box.clicked.connect(user_info_ui)
    # found user button
    ui.found_user_box.clicked.connect(found_users_ui)
    # history finding button
    ui.history_finding.clicked.connect(history_finding_ui)
    # exit button
    ui.return_home_page.clicked.connect(home_page_ui)
    Mainwindow.show()


# ----------------UI MainWindow-----------------
# User Info UI MainWindow ==> Done
def user_info_ui():
    global ui
    ui = frontend.user_info.Ui_Info_Users_Page()
    ui.setupUi(Mainwindow)
    user_info_controller()
    Mainwindow.show()


# User Info Controller UI
def user_info_controller():
    id_user = user_auth_controller.get_user_credentials_id_from_auth_controller()
    user_info = user_auth_controller.get_user_info(id_user)
    # User da dien day du thong tin co san va co the update thong tin
    if user_info is not None:
        location_app = LocationApp(
            ui.nation_box, ui.city_box, ui.district_box, ui.ward_box
        )
        ui.location_app = location_app
        ui.download_pic.clicked.connect(check_update_user_image_auth_controller)
        user_info_display = print_available_user_info(user_info)
        user_info_name = user_info_display[0]
        user_info_gender = user_info_display[1]
        user_info_age = user_info_display[2]
        user_info_country = user_info_display[3]
        user_info_city = user_info_display[4]
        user_info_district = user_info_display[5]
        user_info_ward = user_info_display[6]
        user_info_feature = user_info_display[7]
        user_info_image = user_info_display[8]
        user_info_check_is_allowed = user_info_display[9]
        display_main_user_info(
            ui,
            user_info_name=user_info_name,
            user_info_gender=user_info_gender,
            user_info_age=user_info_age,
            user_info_country=user_info_country,
            user_info_city=user_info_city,
            user_info_district=user_info_district,
            user_info_ward=user_info_ward,
            user_info_feature=user_info_feature,
            user_info_image=user_info_image,
            user_info_check_is_allowed=user_info_check_is_allowed,
        )
        ui.apply_button.setText("UPDATE")
        ui.apply_button.clicked.connect(check_update_user_info_auth_controller)
        ui.cancel_button.clicked.connect(menu_ui)
    # User chua save thong tin ca nhan va co the save thong tin
    else:
        location_app = LocationApp(
            ui.nation_box, ui.city_box, ui.district_box, ui.ward_box
        )
        ui.location_app = location_app
        if id_image_global is not None:
            display_user_uploaded_img(
                user_auth_controller.get_user_credentials_id_from_auth_controller()
            )
        # download pic button
        ui.download_pic.clicked.connect(check_upload_pic_auth_controller)
        # save button
        ui.apply_button.clicked.connect(check_user_info_auth_controller)
        # cancel button
        ui.cancel_button.clicked.connect(menu_ui)


def check_update_user_info_auth_controller():
    id_user = user_auth_controller.get_user_credentials_id_from_auth_controller()
    full_name = str(ui.ho_ten.text())
    age = int(ui.age_range.text())
    check_gioi_tinh = str(ui.gioi_tinh_box.currentText())
    gioi_tinh = None
    if check_gioi_tinh == "Nam":
        gioi_tinh = True
    else:
        gioi_tinh = False
    id_image = id_updated_image_global
    id_country = ui.location_app.selected_country_id
    id_city = ui.location_app.selected_city_id
    id_district = ui.location_app.selected_district_id
    id_ward = ui.location_app.selected_ward_id
    info_face = str(ui.info_face_text.toPlainText())
    is_allowed = bool(ui.is_allowed.isChecked())

    if user_auth_controller.update_user_info(
        id_user,
        full_name,
        age,
        gioi_tinh,
        id_image,
        id_country,
        id_city,
        id_district,
        id_ward,
        info_face,
        is_allowed,
    ):
        check_right_user_info_from_auth_controller()
        menu_ui()
    else:
        print("Error: Could not update user info.")
        check_wrong_user_info_ui()


def check_cancel_user_info_auth_controller():
    id_user = user_auth_controller.get_user_credentials_id_from_auth_controller()
    user_info = user_auth_controller.get_user_info(id_user)
    if user_info is None:
        check_cancel_user_info_ui()


# ----------------UI MainWindow-----------------
# Found Users UI MainWindow
def found_users_ui():
    global ui
    ui = frontend.found_users.Ui_Found_Users_Page()
    ui.setupUi(Mainwindow)
    found_user_img = []
    # ui.pushButton.clicked.connect(lambda: launch_upload_pic_ui(found_user_img))
    ui.cancel_button.clicked.connect(menu_ui)
    ui.location_app = LocationApp(
        ui.nation_box, ui.city_box, ui.district_box, ui.ward_box
    )
    ui.apply_button.clicked.connect(
        lambda: check_found_user_ui(
            ui.ho_ten_box.text(),
            str(ui.gioi_tinh.currentText()),
            ui.age_1.isChecked(),
            str(ui.nation_box.currentText()),
            str(ui.city_box.currentText()),
            str(ui.district_box.currentText()),
            str(ui.ward_box.currentText()),
            ui.info_face.toPlainText(),
            found_user_img,
        )
    )
    Mainwindow.show()


# ----------------UI MainWindow-----------------
# History Finding UI MainWindow
def history_finding_ui():
    pass


# ----------------Dialog UI-----------------
# SIGNUP UI
# 1. check fill info dialog
def check_fill_info_ui():
    dlg = QtWidgets.QDialog()
    ui = frontend.check_fill_info.Ui_Dialog()
    ui.setupUi(dlg)
    ui.exit_button.accepted.connect(dlg.accept)
    ui.exit_button.rejected.connect(dlg.reject)
    dlg.exec()


# 2. check right signup dialog
def check_right_signup_ui():
    dlg = QtWidgets.QDialog()
    ui = frontend.check_signup.Ui_check_signup()
    ui.setupUi(dlg)
    ui.exit_button.accepted.connect(dlg.accept)
    ui.exit_button.rejected.connect(dlg.reject)
    dlg.exec()


# 3. check wrong signup dialog
def check_wrong_signup_ui():
    dlg = QtWidgets.QDialog()
    ui = frontend.check_wrong_signup.Ui_Dialog()
    ui.setupUi(dlg)
    ui.exit_button.accepted.connect(dlg.accept)
    ui.exit_button.rejected.connect(dlg.reject)
    dlg.exec()


# 4. check robot ui dialog
def check_robot_ui():
    dlg = QtWidgets.QDialog()
    ui = frontend.check_robot_ui.Ui_CheckRobot()
    ui.setupUi(dlg)
    ui.exit_button.accepted.connect(dlg.accept)
    ui.exit_button.rejected.connect(dlg.reject)
    dlg.exec()


# 5. check confirm password ui dialog
def check_confirm_password_ui():
    dlg = QtWidgets.QDialog()
    ui = frontend.check_confirm_password.Ui_Dialog()
    ui.setupUi(dlg)
    ui.exit_button.accepted.connect(dlg.accept)
    ui.exit_button.rejected.connect(dlg.reject)
    dlg.exec()


# 6. check type ui dialog
def check_type_ui():
    dlg = QtWidgets.QDialog()
    ui = frontend.check_type.Ui_check_dialog()
    ui.setupUi(dlg)
    ui.exit_button.accepted.connect(dlg.accept)
    ui.exit_button.rejected.connect(dlg.reject)
    dlg.exec()


# LOGIN UI
# 1. check right login dialog
def check_right_login_ui():
    dlg = QtWidgets.QDialog()
    ui = frontend.check_login.Ui_check_login()
    ui.setupUi(dlg)
    ui.exit_button.accepted.connect(dlg.accept)
    ui.exit_button.rejected.connect(dlg.reject)
    dlg.exec()


# 2. check wrong login dialog
def check_wrong_login_ui():
    dlg = QtWidgets.QDialog()
    ui = frontend.check_wrong_login.Ui_check_box()
    ui.setupUi(dlg)
    ui.exit_button.accepted.connect(dlg.accept)
    ui.exit_button.rejected.connect(dlg.reject)
    dlg.exec()


# USER INFO UI
# 1. check cancel user info ui dialog
def check_cancel_user_info_ui():
    dlg = QtWidgets.QDialog()
    ui = frontend.check_cancel_user_info.Ui_Check_Cancel()
    ui.setupUi(dlg)
    ui.exit_button.accepted.connect(dlg.accept)
    ui.exit_button.rejected.connect(user_info_ui)
    dlg.exec()


# 2. check cancel updated user info ui dialog
def check_cancel_updated_user_info_ui():
    dlg = QtWidgets.QDialog()
    ui = frontend.check_cancel_updated_user_info.Ui_Dialog()
    ui.setupUi(dlg)
    ui.exit_button.accepted.connect(menu_ui)
    ui.exit_button.rejected.connect(user_info_ui)
    dlg.exec()


# 3. check right user info dialog
def check_right_user_info_ui():
    dlg = QtWidgets.QDialog()
    ui = frontend.check_right_update_user_info.Ui_Dialog()
    ui.setupUi(dlg)
    ui.exit_button.accepted.connect(dlg.accept)
    ui.exit_button.rejected.connect(dlg.reject)
    dlg.exec()


# 4. Check wrong user info dialog
def check_wrong_user_info_ui():
    dlg = QtWidgets.QDialog()
    ui = frontend.check_wrong_update_user_info.Ui_Dialog()
    ui.setupUi(dlg)
    ui.exit_button.accepted.connect(dlg.accept)
    ui.exit_button.rejected.connect(dlg.reject)
    dlg.exec()


# 5. Check right user info from auth controller
def check_right_user_info_from_auth_controller():
    id_user = user_auth_controller.get_user_credentials_id_from_auth_controller()
    user_info = user_auth_controller.get_user_info(id_user)
    user_info_display = print_available_user_info(user_info)
    dlg = QtWidgets.QDialog()
    ui = frontend.check_update_user_info.Ui_Check_Update_User()
    ui.setupUi(dlg)
    user_info_name = user_info_display[0]
    user_info_gender = user_info_display[1]
    user_info_age = user_info_display[2]
    user_info_country = user_info_display[3]
    user_info_city = user_info_display[4]
    user_info_district = user_info_display[5]
    user_info_ward = user_info_display[6]
    user_info_feature = user_info_display[7]
    user_info_image = user_info_display[8]
    display_update_user_info(
        ui,
        user_info_name,
        user_info_gender,
        user_info_age,
        user_info_country,
        user_info_city,
        user_info_district,
        user_info_ward,
        user_info_feature,
        user_info_image,
    )
    ui.exit_button.accepted.connect(dlg.accept)
    ui.exit_button.rejected.connect(dlg.reject)
    dlg.exec()


def check_user_info_auth_controller():
    id_user = user_auth_controller.get_user_credentials_id_from_auth_controller()
    full_name = str(ui.ho_ten.text())
    age = int(ui.age_range.text())
    check_gioi_tinh = str(ui.gioi_tinh_box.currentText())
    gioi_tinh = None
    if check_gioi_tinh == "Nam":
        gioi_tinh = True
    else:
        gioi_tinh = False
    id_image = id_image_global
    id_country = ui.location_app.selected_country_id or None
    id_city = ui.location_app.selected_city_id or None
    id_district = ui.location_app.selected_district_id or None
    id_ward = ui.location_app.selected_ward_id or None
    info_face = str(ui.info_face_text.toPlainText())
    is_allowed = bool(ui.is_allowed.isChecked())

    if (
        user_auth_controller.create_user_info(
            id_user,
            full_name,
            age,
            gioi_tinh,
            id_image,
            id_country,
            id_city,
            id_district,
            id_ward,
            info_face,
            is_allowed,
        )
        == 0
    ):
        check_right_user_info_from_auth_controller()
        menu_ui()
    elif (
        user_auth_controller.create_user_info(
            id_user,
            full_name,
            age,
            gioi_tinh,
            id_image,
            id_country,
            id_city,
            id_district,
            id_ward,
            info_face,
            is_allowed,
        )
        == 1
    ):
        print("Error: User info already exists.")
        check_wrong_user_info_ui()
    else:
        print("Error: Could not create user info.")
        check_wrong_user_info_ui()


# Upload Pic UI
# 1. check upload pic dialog
def check_upload_pic_ui():
    dlg = QtWidgets.QDialog()
    ui = frontend.check_upload_pic.Ui_Dialog()
    ui.setupUi(dlg)
    ui.exit_box.accepted.connect(dlg.accept)
    ui.exit_box.rejected.connect(dlg.reject)
    dlg.exec()


# 2. check finished upload pic dialog
def check_finished_upload_pic_ui():
    dlg = QtWidgets.QDialog()
    ui = frontend.check_finished_upload_image.Ui_Check_Upload()
    ui.setupUi(dlg)
    ui.exit_button.accepted.connect(dlg.accept)
    ui.exit_button.rejected.connect(dlg.reject)
    dlg.exec()


# 3. check wrong upload pic dialog
def check_wrong_upload_pic_ui():
    dlg = QtWidgets.QDialog()
    ui = frontend.check_wrong_upload_image.Ui_Dialog()
    ui.setupUi(dlg)
    ui.exit_button.accepted.connect(dlg.accept)
    ui.exit_button.rejected.connect(dlg.reject)
    dlg.exec()


# 4. Upload image ui
def get_response_upload_pic():
    ui = frontend.get_responses_image.Ui_Get_Response()
    progress = QtWidgets.QProgressDialog("Please waiting ...", "Cancel", 0, 100, ui)
    response = ui.get_response_upload_pic_with_progress(progress)
    progress.close()
    return response


# ----------------Controller-----------------
def check_upload_pic_auth_controller():
    user_uploaded_img = get_response_upload_pic()
    if user_uploaded_img is not None:
        name_image = os.path.basename(user_uploaded_img)
        if name_image is None:
            check_wrong_upload_pic_ui()
            user_info_ui()
        id_image = user_auth_controller.upload_image(name_image, user_uploaded_img)
        global id_image_global
        id_image_global = id_image
        if id_image is not None:
            check_upload_pic_ui()
            display_user_uploaded_img(
                ui, user_auth_controller.get_user_credentials_id_from_auth_controller()
            )
        else:
            print("Error: Could not upload image.")
            check_wrong_upload_pic_ui()
            user_info_ui()
    else:
        # Handle the case where user_uploaded_img is None
        # You might want to show a message or take appropriate action
        print("Error: User did not upload an image.")
        check_finished_upload_pic_ui()
        user_info_ui()


def check_update_user_image_auth_controller():
    user_updated_img = get_response_upload_pic()
    if user_updated_img is not None:
        name_image = os.path.basename(user_updated_img)
        if name_image is None:
            check_wrong_upload_pic_ui()
            user_info_ui()
        id_user = user_auth_controller.get_user_credentials_id_from_auth_controller()
        id_image = user_auth_controller.update_image(
            id_user, name_image, user_updated_img
        )

        global id_updated_image_global
        id_updated_image_global = id_image
        if id_image is not None:
            check_upload_pic_ui()
            display_user_uploaded_img(
                ui, user_auth_controller.get_user_credentials_id_from_auth_controller()
            )
        else:
            print("Error: Could not upload image.")
            check_wrong_upload_pic_ui()
            user_info_ui()
    else:
        # Handle the case where user_uploaded_img is None
        # You might want to show a message or take appropriate action
        print("Error: User did not upload an image.")
        check_finished_upload_pic_ui()
        user_info_ui()


# ----------------Controller-----------------
# Check found user auth controllers (from client layer to controller layer)
def check_found_user_ui(
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
    print("      ===---=== BIG DATA from check_found_user_ui ===---===      ")
    print("- user_info_name: ", user_info_name)
    print("- user_info_gender: ", user_info_gender)
    print("- user_info_age: ", user_info_age)
    print("- user_info_country: ", user_info_country)
    print("- user_info_city: ", user_info_city)
    print("- user_info_district: ", user_info_district)
    print("- user_info_ward: ", user_info_ward)
    print("- user_info_feature: ", user_info_feature)
    print("- user_info_img: ", user_info_img)
    print("________________________________________")
    global ui
    ui = frontend.results.Ui_MainWindow()
    ui.setupUi(Mainwindow)
    display_user_info(
        ui,
        user_info_name,
        user_info_gender,
        user_info_age,
        user_info_country,
        user_info_city,
        user_info_district,
        user_info_ward,
        user_info_feature,
        user_info_img,
    )
    user_auth_controller.find_people(
        user_info_name,
        user_info_gender,
        user_info_age,
        user_info_country,
        user_info_city,
        user_info_district,
        user_info_ward,
        user_info_feature,
        user_info_img,
    )
    ui.cancel_button.clicked.connect(menu_ui)
    Mainwindow.show()


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
    found_user_img,
):
    ui.label.setText(f"Họ tên: {user_info_name}")
    ui.label_5.setText(f"Giới tính: {user_info_gioi_tinh}")
    ui.label_2.setText(f"Tuổi: {user_info_age}")
    ui.label_3.setText(
        f"Quê quán: {user_info_ward}, {user_info_district}, {user_info_city}, {user_info_country}"
    )
    ui.label_4.setText(f"Đặc điểm nhận dạng: {user_info_feature}")


def main():
    home_page_ui()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
