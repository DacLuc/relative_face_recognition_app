from PyQt6 import QtCore, QtWidgets, QtQuick
import sys

sys.path.append("../../client")

import home_page, signup_ui, login_ui, menu, found_users, user_info, credit_ui, check_login, check_upload_pic, check_signup, cities_districts_wards, check_wrong_login
from models.user_validators import *
from controllers.auth import user_auth_controller
import os

user_auth_controller = user_auth_controller()

# processing ui
ui = ""
app = QtWidgets.QApplication(sys.argv)
Mainwindow = QtWidgets.QMainWindow()


def home_page_ui():
    global ui
    ui = home_page.Ui_Home_Page()
    ui.setupUi(Mainwindow)
    ui.signup_button.clicked.connect(signup_ui_load)
    ui.signin_button.clicked.connect(login_ui_load)
    ui.credit_button.clicked.connect(credit_ui_load)
    ui.exit_button.clicked.connect(Mainwindow.close)
    Mainwindow.show()


def check_login_ui(username: str, password: str):
    dlg = QtWidgets.QDialog()
    ui = check_login.Ui_check_login()
    ui.setupUi(dlg)

    new_user = UserSignIn(username=username, password=password)
    is_logged_in_successfully = user_auth_controller.log_in(username, password)
    dlg.exec()
    print("is_logged_in_successfully: ", is_logged_in_successfully)

    if is_logged_in_successfully:
        return ui.exit_button.accepted.connect(dlg.accept)
    else:
        return ui.exit_button.rejected.connect(check_login_ui)


def check_signup_ui(username: str, email: str, password: str):
    dlg = QtWidgets.QDialog()
    ui = check_signup.Ui_check_signup()
    ui.setupUi(dlg)

    new_user = UserSignUp(username=username, email=email, password=password)
    user_auth_controller.register(username, email, password)

    dlg.exec()
    return ui.exit_button.accepted.connect(check_signup_ui)


def signup_ui_load():
    global ui
    ui = signup_ui.Ui_Sign_Up_Page()
    ui.setupUi(Mainwindow)
    ui.cancel_button.clicked.connect(home_page_ui)
    ui.apply_button.clicked.connect(
        lambda: check_signup_ui(
            ui.account_name.text(), ui.account_email.text(), ui.account_password.text()
        )
    )
    ui.apply_button.clicked.connect(login_ui_load)
    Mainwindow.show()


def login_ui_load():
    global ui
    ui = login_ui.Ui_Sign_In_Page(user_auth_controller)
    ui.setupUi(Mainwindow)
    ui.cancel_button.clicked.connect(home_page_ui)
    ui.apply_button.clicked.connect(
        lambda: check_login_ui(ui.account_name.text(), ui.account_password.text())
    )
    ui.apply_button.clicked.connect(main_win_ui)
    Mainwindow.show()


def check_wrong_login_ui():
    dlg = QtWidgets.QDialog()
    ui = check_wrong_login.Ui_Dialog()
    ui.setupUi(dlg)
    dlg.exec()
    return ui.exit_button.accepted.connect(dlg.accept)


def credit_ui_load():
    global ui
    ui = credit_ui.Ui_Credit_Page()
    ui.setupUi(Mainwindow)
    ui.back_button.clicked.connect(home_page_ui)
    Mainwindow.show()


def main_win_ui():
    global ui
    ui = menu.Ui_Specific_Task()
    ui.setupUi(Mainwindow)
    ui.user_info_box.clicked.connect(user_info_ui)
    ui.found_user_box.clicked.connect(found_users_ui)
    ui.history_finding.clicked.connect(history_finding_ui)
    ui.return_home_page.clicked.connect(home_page_ui)
    Mainwindow.show()


def history_finding_ui():
    pass


def get_response_upload_pic():
    file_filter = "Image File (*.png *.jpg)"
    response = QtWidgets.QFileDialog.getOpenFileName(
        parent=Mainwindow,
        caption="Select a file",
        directory=os.getcwd(),
        filter=file_filter,
        initialFilter="Image File (*.png *.jpg)",
    )
    # print("!!! response from get_response_upload_pic: ", response)
    return response[0]


def launch_upload_pic_ui(response):
    user_uploaded_img = get_response_upload_pic()
    dlg = QtWidgets.QDialog()
    ui = check_upload_pic.Ui_Dialog()
    ui.setupUi(dlg)
    ui.exit_box.accepted.connect(dlg.accept)
    ui.exit_box.rejected.connect(dlg.reject)
    if user_uploaded_img[0] != "":
        dlg.exec()
        print("!!! response from launch_upload_pic_ui: ", user_uploaded_img)
        response.append(user_uploaded_img)


def check_user_info_ui(user_info_name = None, user_info_gender = None, user_info_age = None, user_info_country = None, user_info_city = None, user_info_district = None, user_info_ward = None, user_info_feature = None, user_info_allowed = None, user_info_img = None):
    print("      ===---=== BIG DATA ===---===      ")
    print("- user_info_name: ", user_info_name)
    print("- user_info_gender: ", user_info_gender)
    print("- user_info_age: ", user_info_age)
    print("- user_info_country: ", user_info_country)
    print("- user_info_city: ", user_info_city)
    print("- user_info_district: ", user_info_district)
    print("- user_info_ward: ", user_info_ward)
    print("- user_info_feature: ", user_info_feature)
    print("- user_info_allowed: ", user_info_allowed)
    print("- user_info_img: ", user_info_img)
    print("________________________________________")
    user_auth_controller.update_user_info(
        user_info_name, user_info_age, user_info_gender)

def user_info_ui():
    global ui
    ui = user_info.Ui_Info_Users_Page()
    ui.setupUi(Mainwindow)
    # ui.download_pic.clicked.connect(launch_upload_pic_ui)
    user_info_img = []
    ui.download_pic.clicked.connect(
        lambda: launch_upload_pic_ui(user_info_img))
    ui.cancel_button.clicked.connect(main_win_ui)
    ui.location_app = cities_districts_wards.LocationApp(
        ui.nation_box, ui.city_box, ui.district_box, ui.ward_box
    )
    # user_info_name = ui.ho_ten.text()
    # user_info_gender = str(ui.gioi_tinh_box.currentText())
    # user_info_age = ui.age_1.isChecked()
    # user_info_country = str(ui.nation_box.currentText())
    # user_info_city = str(ui.city_box.currentText())
    # user_info_district = str(ui.district_box.currentText())
    # user_info_ward = str(ui.ward_box.currentText())
    # user_info_feature = ui.info_face_text.toPlainText()
    # user_info_upload = ui.download_pic.clicked()
    # user_info_img = get_response_upload_pic()
    # user_info_allowed = ui.is_allowed.isChecked()
    
    ui.apply_button.clicked.connect(
        lambda: check_user_info_ui(
            ui.ho_ten.text(),
            str(ui.gioi_tinh_box.currentText()),
            ui.age_1.isChecked(),
            str(ui.nation_box.currentText()),
            str(ui.city_box.currentText()),
            str(ui.district_box.currentText()),
            str(ui.ward_box.currentText()),
            ui.info_face_text.toPlainText(),
            ui.is_allowed.isChecked(),
            user_info_img
        )
    )
    # ui.apply_button.clicked.connect(main_win_ui)
    # ui.cancel_button.clicked.connect(home_page_ui)
    Mainwindow.show()

def check_found_user_ui(user_info_name = None, user_info_gender = None, user_info_age = None, user_info_country = None, user_info_city = None, user_info_district = None, user_info_ward = None, user_info_feature = None, user_info_img = None):
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
    user_auth_controller.find_people(user_info_name, user_info_gender, user_info_age, user_info_country, user_info_city, user_info_district, user_info_ward, user_info_feature, user_info_img)

def found_users_ui():
    global ui
    ui = found_users.Ui_Found_Users_Page()
    ui.setupUi(Mainwindow)
    # ui.pushButton.clicked.connect(launch_upload_pic_ui)
    found_user_img = []
    ui.pushButton.clicked.connect(
        lambda: launch_upload_pic_ui(found_user_img))
    ui.cancel_button.clicked.connect(main_win_ui)
    ui.location_app = cities_districts_wards.LocationApp(
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
            found_user_img
        )
    )
    Mainwindow.show()


home_page_ui()
sys.exit(app.exec())
