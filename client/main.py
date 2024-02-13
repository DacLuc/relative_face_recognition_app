import sys
from PyQt6 import QtWidgets, QtGui, QtCore
import sys
import os
import numpy as np
import math
import cv2

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../")
import frontend.home_page, frontend.signup_ui, frontend.login_ui, frontend.credit_ui, frontend.menu, frontend.user_info, frontend.found_users, frontend.get_responses_image, frontend.results
import frontend.check_fill_info, frontend.check_signup, frontend.check_wrong_signup, frontend.check_robot_ui, frontend.check_confirm_password, frontend.check_type, frontend.check_login, frontend.check_wrong_login, frontend.check_cancel_user_info, frontend.check_cancel_updated_user_info, frontend.check_right_update_user_info, frontend.check_wrong_update_user_info, frontend.check_upload_pic, frontend.check_finished_upload_image, frontend.check_wrong_upload_image, frontend.check_update_user_info, frontend.check_faces
from controllers.cities_districts_wards import LocationApp
from server.services.auth import user_auth_controller
from client.controllers.controllers import (
    print_available_user_info,
    display_main_user_info,
    display_update_user_info,
    display_user_uploaded_img,
    display_user_info,
    display_user_request_img,
    transform_found_user_info,
)

from insightface.app import FaceAnalysis
import cv2
import numpy as np
import pygame

user_auth_controller = user_auth_controller()

ui = ""
app = QtWidgets.QApplication(sys.argv)
Mainwindow = QtWidgets.QMainWindow()
id_image_global = None
id_request_image_global = None


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
        user_image_info = user_auth_controller.get_image_id(id_user)
        if user_image_info is not None:
            ui.download_pic.setText(
                QtCore.QCoreApplication.translate("Info_Users_Page", "Xóa ảnh đại diện")
            )
            ui.download_pic.clicked.connect(check_delete_user_image_auth_controller)
            display_user_uploaded_img(
                ui, user_auth_controller.get_user_credentials_id_from_auth_controller()
            )
        else:
            ui.download_pic.setText(
                QtCore.QCoreApplication.translate("Info_Users_Page", "Tải ảnh đại diện")
            )
            ui.download_pic.clicked.connect(check_upload_pic_auth_controller)
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
        id_user = user_auth_controller.get_user_credentials_id_from_auth_controller()
        user_image_info = user_auth_controller.get_image_id(id_user)
        if user_image_info is not None:
            ui.download_pic.setText(
                QtCore.QCoreApplication.translate("Info_Users_Page", "Xóa ảnh đại diện")
            )
            ui.download_pic.clicked.connect(check_delete_user_image_auth_controller)
            display_user_uploaded_img(ui, id_user)
        else:
            ui.download_pic.setText(
                QtCore.QCoreApplication.translate("Info_Users_Page", "Tải ảnh đại diện")
            )
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
    id_image = id_image_global
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
    found_users_controller()
    Mainwindow.show()


def found_users_controller():
    id_user = user_auth_controller.get_user_credentials_id_from_auth_controller()
    id_request_image_info = user_auth_controller.get_request_image_id(id_user)
    if id_request_image_info is not None:
        ui.upload_pic.setText(
            QtCore.QCoreApplication.translate("Found_Users_Page", "Xóa ảnh đại diện")
        )
        ui.upload_pic.clicked.connect(check_delete_request_image_auth_controller)
        display_user_request_img(
            ui,
            user_auth_controller.get_user_credentials_id_from_auth_controller(),
        )
    else:
        ui.upload_pic.setText(
            QtCore.QCoreApplication.translate("Found_Users_Page", "Tải ảnh đại diện")
        )
        ui.upload_pic.clicked.connect(check_upload_request_image_auth_controller)
    ui.cancel_button.clicked.connect(menu_ui)
    ui.apply_button.clicked.connect(check_find_user_auth_controller)


def check_find_user_auth_controller():
    id_user = user_auth_controller.get_user_credentials_id_from_auth_controller()
    id_request_image = id_request_image_global
    found_users_info = user_auth_controller.get_founders_info(id_request_image)
    if found_users_info != 404 and found_users_info is not None:
        json_data = transform_found_user_info(found_users_info)
        dlg = frontend.results.ResultsWindow(json_data)
        if dlg.exec() == QtWidgets.QDialog.DialogCode.Accepted:
            print("User clicked OK")
        else:
            print("User clicked Cancel")
    elif found_users_info == 404 and found_users_info is not None:
        QtWidgets.QMessageBox.warning(None, "Error", "Could not find users info.")
        print("Error: Could not find users.")
    else:
        QtWidgets.QMessageBox.warning(None, "Error", "Error when finding users !!!")


def check_upload_request_image_auth_controller():
    user_uploaded_request_img = get_response_upload_pic()
    if user_uploaded_request_img is not None:
        name_request_image = os.path.basename(user_uploaded_request_img)
        if name_request_image is None:
            check_wrong_upload_pic_ui()
            found_users_ui()
        else:
            id_request_image = user_auth_controller.upload_request_image(
                name_request_image, user_uploaded_request_img
            )
            global id_request_image_global
            if id_request_image != 400 and id_request_image is not None:
                id_request_image_global = id_request_image
                ui.upload_pic.setText(
                    QtCore.QCoreApplication.translate(
                        "Found_Users_Page", "Xóa ảnh đại diện"
                    )
                )
                ui.upload_pic.clicked.disconnect()
                ui.upload_pic.clicked.connect(
                    check_delete_request_image_auth_controller
                )
                check_upload_pic_ui()
                display_user_request_img(
                    ui,
                    user_auth_controller.get_user_credentials_id_from_auth_controller(),
                )

            elif id_request_image == 400 and id_request_image is not None:
                print("Error: Image has no faces or many faces.")
                check_faces_ui()
                found_users_ui()

            else:
                print("Error: Could not upload image.")
                check_wrong_upload_pic_ui()
                found_users_ui()
    else:
        # Handle the case where user_uploaded_img is None
        # You might want to show a message or take appropriate action
        print("Error: User did not upload an image.")
        check_finished_upload_pic_ui()
        found_users_ui()


def check_delete_request_image_auth_controller():
    id_user = user_auth_controller.get_user_credentials_id_from_auth_controller()
    if user_auth_controller.delete_request_image(id_user):
        # Update UI after deleting image
        global id_request_image_global
        id_request_image_global = None
        ui.label.setPixmap(
            QtGui.QPixmap(
                r"C:\Users\phatl\OneDrive - VNU-HCMUS\Desktop\relative_face_recognition_app\client\frontend\ui\picture\demo_ava.jpg"
            )
        )
        ui.upload_pic.setText(
            QtCore.QCoreApplication.translate("Info_Users_Page", "Tải ảnh đại diện")
        )
        ui.upload_pic.clicked.disconnect()
        ui.upload_pic.clicked.connect(check_upload_request_image_auth_controller)
        QtWidgets.QMessageBox.information(
            None, "Success", "Image deleted successfully."
        )
    else:
        QtWidgets.QMessageBox.warning(None, "Error", "Error: Image not found.")


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


# 5. check has faces dialog
def check_faces_ui():
    dlg = QtWidgets.QDialog()
    ui = frontend.check_faces.Ui_Dialog()
    ui.setupUi(dlg)
    ui.exit_button.accepted.connect(dlg.accept)
    ui.exit_button.rejected.connect(dlg.reject)
    dlg.exec()


# ----------------Controller-----------------
def check_upload_pic_auth_controller():
    user_uploaded_img = get_response_upload_pic()
    if user_uploaded_img is not None:
        name_image = os.path.basename(user_uploaded_img)
        if name_image is None:
            check_wrong_upload_pic_ui()
            user_info_ui()
        else:
            id_image = user_auth_controller.upload_image(name_image, user_uploaded_img)
            global id_image_global
            if id_image != 400 and id_image is not None:
                id_image_global = id_image
                ui.download_pic.setText(
                    QtCore.QCoreApplication.translate(
                        "Info_Users_Page", "Xóa ảnh đại diện"
                    )
                )
                ui.download_pic.clicked.disconnect()
                ui.download_pic.clicked.connect(check_delete_user_image_auth_controller)
                check_upload_pic_ui()
                display_user_uploaded_img(
                    ui,
                    user_auth_controller.get_user_credentials_id_from_auth_controller(),
                )

            elif id_image == 400 and id_image is not None:
                print("Error: Image has no faces or many faces.")
                check_faces_ui()
                user_info_ui()

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


def check_delete_user_image_auth_controller():
    id_user = user_auth_controller.get_user_credentials_id_from_auth_controller()
    if user_auth_controller.delete_image(id_user):
        # Update UI after deleting image
        global id_image_global
        id_image_global = None
        ui.label_user_img.setPixmap(
            QtGui.QPixmap(
                r"C:\Users\phatl\OneDrive - VNU-HCMUS\Desktop\relative_face_recognition_app\client\frontend\ui\picture\demo_ava.jpg"
            )
        )
        ui.download_pic.setText(
            QtCore.QCoreApplication.translate("Info_Users_Page", "Tải ảnh đại diện")
        )
        ui.download_pic.clicked.disconnect()
        ui.download_pic.clicked.connect(check_upload_pic_auth_controller)
        QtWidgets.QMessageBox.information(
            None, "Success", "Image deleted successfully."
        )
    else:
        QtWidgets.QMessageBox.warning(None, "Error", "Error: Image not found.")


def main():
    home_page_ui()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
