from PyQt6 import QtWidgets
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../")
import frontend.home_page, frontend.signup_ui, frontend.login_ui, frontend.menu, frontend.found_users, frontend.user_info, frontend.credit_ui, frontend.check_login, frontend.check_upload_pic, frontend.check_signup, frontend.check_wrong_login, frontend.results, frontend.check_wrong_signup, frontend.check_fill_info, frontend.check_right_update_user_info, frontend.check_wrong_update_user_info
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
        login_ui_load()
    else:
        # Thuc hien bao loi (tra ve cho client) do khong the dang ky duoc tai khoan do da ton tai trong database
        check_wrong_signup_ui()


# -----------------------------------------------------'
# LOGIN IN
# Login UI (Step Page 03)
def login_ui_load():
    global ui
    ui = frontend.login_ui.Ui_Sign_In_Page()
    ui.setupUi(Mainwindow)
    ui.apply_button.clicked.connect(check_login_user_auth_controller)
    ui.signup_button.clicked.connect(signup_ui_load)
    ui.cancel_button.clicked.connect(home_page_ui)
    Mainwindow.show()


# check right login dialog
def check_right_login_ui():
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
    if not username or not password:
        # Thuc hien bao loi (tra ve cho client) do khong dien day du thong tin
        check_fill_info_ui()
    elif user_auth_controller.log_in(username, password):
        # Thuc hien day du khi dang nhap thanh cong (tra ve cho client)
        check_right_login_ui()
        menu_ui()
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
# User Info UI (Step Page 06)
def user_info_ui():
    global ui
    ui = frontend.user_info.Ui_Info_Users_Page()
    ui.setupUi(Mainwindow)

    user_info_img = []
    ui.download_pic.clicked.connect(lambda: launch_upload_pic_ui(user_info_img))
    ui.cancel_button.clicked.connect(menu_ui)
    location_app = LocationApp(ui.nation_box, ui.city_box, ui.district_box, ui.ward_box)
    ui.location_app = location_app
    ui.apply_button.clicked.connect(check_user_info_auth_controller)
    Mainwindow.show()


def check_right_user_info_ui():
    dlg = QtWidgets.QDialog()
    ui = frontend.check_right_update_user_info.Ui_Dialog()
    ui.setupUi(dlg)
    dlg.exec()
    return ui.exit_button.accepted.connect(dlg.accept)


def check_wrong_user_info_ui():
    dlg = QtWidgets.QDialog()
    ui = frontend.check_wrong_update_user_info.Ui_Dialog()
    ui.setupUi(dlg)
    dlg.exec()
    return ui.exit_button.accepted.connect(dlg.accept)


def check_user_info_auth_controller():  # Create an instance
    id_user = user_auth_controller.get_user_id_from_auth_controller()
    full_name = ui.ho_ten.text()
    age = int(ui.age_range.text())
    check_gioi_tinh = str(ui.gioi_tinh_box.currentText())
    gioi_tinh = None
    if check_gioi_tinh == "Nam":
        gioi_tinh = True
    else:
        gioi_tinh = False
    id_image = "123e4567-e89b-12d3-a456-426614174001"
    id_country = ui.location_app.selected_country_id
    id_city = ui.location_app.selected_city_id
    id_district = ui.location_app.selected_district_id
    id_ward = ui.location_app.selected_ward_id
    info_face = str(ui.info_face_text.toPlainText())
    is_allowed = ui.is_allowed.isChecked()

    print(
        "      ===---=== BIG DATA from check_user_info_auth_controller ===---===      "
    )
    print("- id_user: ", id_user)
    print("- full_name: ", full_name)
    print("- age: ", age)
    print("- gioi_tinh: ", gioi_tinh)
    print("- id_image: ", id_image)
    print("- id_country: ", id_country)
    print("- id_city: ", id_city)
    print("- id_district: ", id_district)
    print("- id_ward: ", id_ward)
    print("- info_face: ", info_face)
    print("- is_allowed: ", is_allowed)
    print("________________________________________")

    if user_auth_controller.create_user_info(
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
        check_right_user_info_ui()
        menu_ui()
    else:
        check_wrong_user_info_ui()


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


# -----------------------------------------------------
# Found Users UI (Step Page 07)
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


# -----------------------------------------------------
# history finding UI (Step Page 08)
def history_finding_ui():
    pass


# -----------------------------------------------------
home_page_ui()
sys.exit(app.exec())
