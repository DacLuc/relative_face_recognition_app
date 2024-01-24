from PyQt6 import QtWidgets
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../..")
import frontend.home_page, frontend.signup_ui, frontend.login_ui, frontend.menu, frontend.found_users, frontend.user_info, frontend.credit_ui, frontend.check_login, frontend.check_upload_pic, frontend.check_signup, frontend.check_wrong_login, frontend.results, frontend.check_wrong_signup, frontend.check_fill_info
from server.services.user_validators import *
from server.services.auth import user_auth_controller
from client.controllers.cities_districts_wards import LocationApp

user_auth_controller = user_auth_controller()

# processing ui for home page
ui = ""
app = QtWidgets.QApplication(sys.argv)
Mainwindow = QtWidgets.QMainWindow()


# -----------------------------------------------------
# Check Fill Info UI (Step Page 00)
def check_fill_info_ui():
    dlg = QtWidgets.QDialog()
    ui = frontend.check_fill_info.Ui_Dialog()
    ui.setupUi(dlg)
    dlg.exec()
    ui.exit_button.accepted.connect(signup_ui_load)
    ui.exit_button.rejected.connect(dlg.reject)


# -----------------------------------------------------


# Home Page UI (Step Page 01)
def home_page_ui():
    global ui
    ui = frontend.home_page.Ui_Home_Page()
    ui.setupUi(Mainwindow)
    ui.signup_button.clicked.connect(signup_ui_load)
    ui.signin_button.clicked.connect(login_ui_load)
    ui.credit_button.clicked.connect(credit_ui_load)
    ui.exit_button.clicked.connect(Mainwindow.close)
    Mainwindow.show()


# -----------------------------------------------------
# SIGN IN
# SignUp UI (Step Page 02)
def signup_ui_load():
    global ui
    ui = frontend.signup_ui.Ui_Sign_Up_Page()
    ui.setupUi(Mainwindow)
    ui.apply_button.clicked.connect(check_signup_user_auth_controller)
    # ui.apply_button.clicked.connect(login_ui_load)
    ui.cancel_button.clicked.connect(home_page_ui)

    Mainwindow.show()


# check right signup dialog
def check_right_signup_ui():
    dlg = QtWidgets.QDialog()
    ui = frontend.check_signup.Ui_check_signup()
    ui.setupUi(dlg)
    dlg.exec()
    return ui.exit_button.accepted.connect(dlg.accept)


# check wrong signup dialog
def check_wrong_signup_ui():
    dlg = QtWidgets.QDialog()
    ui = frontend.check_wrong_signup.Ui_Dialog()
    ui.setupUi(dlg)
    dlg.exec()
    return ui.exit_button.accepted.connect(dlg.accept)


# check signup controllers (from client layer to controller layer)
def check_signup_user_auth_controller():
    account_name = ui.account_name.text()
    account_email = ui.account_email.text()
    account_password = ui.account_password.text()

    # ---
    if not account_name or not account_email or not account_password:
        # Thuc hien bao loi (tra ve cho client) do khong dien day du thong tin
        check_fill_info_ui()
    elif user_auth_controller.register(account_name, account_email, account_password):
        # Thuc hien day du khi dang ky thanh cong (tra ve cho client)
        check_right_signup_ui()
    else:
        # Thuc hien bao loi (tra ve cho client) do khong the dang ky duoc tai khoan do da ton tai trong database
        check_wrong_signup_ui()


# -----------------------------------------------------'
# LOGIN IN
# Login UI (Step Page 03)
def login_ui_load():
    global ui
    ui = frontend.login_ui.Ui_Sign_In_Page(user_auth_controller)
    ui.setupUi(Mainwindow)
    ui.apply_button.clicked.connect(check_login_user_auth_controller)
    ui.signup_button.clicked.connect(signup_ui_load)
    ui.cancel_button.clicked.connect(home_page_ui)
    Mainwindow.show()


# check right login dialog
def check_right_login_ui(username: str, password: str):
    dlg = QtWidgets.QDialog()
    ui = frontend.check_login.Ui_check_login()
    ui.setupUi(dlg)
    dlg.exec()
    return ui.exit_button.accepted.connect(dlg.accept)


# check wrong login dialog
def check_wrong_login_ui():
    dlg = QtWidgets.QDialog()
    ui = frontend.check_wrong_login.Ui_check_box()
    ui.setupUi(dlg)
    dlg.exec()
    return ui.exit_button.accepted.connect(dlg.accept)


# check login controllers (from client layer to controller layer)
def check_login_user_auth_controller():
    username = ui.account_name.text()
    password = ui.account_password.text()
    print("username: ", username)
    print("password: ", password)
    if not username or not password:
        # Thuc hien bao loi (tra ve cho client) do khong dien day du thong tin
        check_fill_info_ui()
    elif user_auth_controller.log_in(username, password):
        # Thuc hien day du khi dang nhap thanh cong (tra ve cho client)
        check_right_login_ui(username, password)
    else:
        # Thuc hien bao loi (tra ve cho client) do khong the dang nhap duoc tai khoan do khong ton tai trong database
        check_wrong_login_ui()


# -----------------------------------------------------'


# Credit UI (Step Page 04)
def credit_ui_load():
    global ui
    ui = frontend.credit_ui.Ui_Credit_Page()
    ui.setupUi(Mainwindow)
    ui.back_button.clicked.connect(home_page_ui)
    Mainwindow.show()


# -----------------------------------------------------'


# menu UI (Step Page 05)
def menu_ui():
    global ui
    ui = frontend.menu.Ui_Specific_Task()
    ui.setupUi(Mainwindow)
    ui.user_info_box.clicked.connect(user_info_ui)
    ui.found_user_box.clicked.connect(found_users_ui)
    ui.history_finding.clicked.connect(history_finding_ui)
    ui.return_home_page.clicked.connect(home_page_ui)
    Mainwindow.show()


# -----------------------------------------------------
# history finding UI (Step Page 06)
def history_finding_ui():
    pass


# -----------------------------------------------------
def get_response_upload_pic():
    file_filter = "Image File (*.png *.jpg)"
    response = QtWidgets.QFileDialog.getOpenFileName(
        parent=Mainwindow,
        caption="Select a file",
        directory=os.getcwd(),
        filter=file_filter,
        initialFilter="Image File (*.png *.jpg)",
    )
    return response[0]


def launch_upload_pic_ui(response):
    user_uploaded_img = get_response_upload_pic()
    dlg = QtWidgets.QDialog()
    ui = frontend.check_upload_pic.Ui_Dialog()
    ui.setupUi(dlg)
    ui.exit_box.accepted.connect(dlg.accept)
    ui.exit_box.rejected.connect(dlg.reject)
    if user_uploaded_img[0] != "":
        dlg.exec()
        print("!!! response from launch_upload_pic_ui: ", user_uploaded_img)
        response.append(user_uploaded_img)


def check_user_info_ui(
    user_info_name=None,
    user_info_gender=None,
    user_info_age=None,
    user_info_country=None,
    user_info_city=None,
    user_info_district=None,
    user_info_ward=None,
    user_info_feature=None,
    user_info_allowed=None,
    user_info_img=None,
):
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
        user_info_name,
        user_info_age,
        user_info_gender,
        user_info_country,
        user_info_city,
        user_info_district,
        user_info_ward,
    )


def user_info_ui():
    global ui
    ui = frontend.user_info.Ui_Info_Users_Page()
    ui.setupUi(Mainwindow)

    user_info_img = []
    ui.download_pic.clicked.connect(lambda: launch_upload_pic_ui(user_info_img))
    ui.cancel_button.clicked.connect(menu_ui)
    ui.location_app = LocationApp(
        ui.nation_box, ui.city_box, ui.district_box, ui.ward_box
    )
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
            user_info_img,
        )
    )
    ui.apply_button.clicked.connect(menu_ui)
    ui.cancel_button.clicked.connect(home_page_ui)
    Mainwindow.show()


def found_users_ui():
    global ui
    ui = frontend.found_users.Ui_Found_Users_Page()
    ui.setupUi(Mainwindow)
    found_user_img = []
    ui.pushButton.clicked.connect(lambda: launch_upload_pic_ui(found_user_img))
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
    ui.display_user_info(
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


home_page_ui()
sys.exit(app.exec())
