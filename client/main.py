from PyQt6 import QtCore, QtWidgets, QtQuick
import sys
import home_page, signup_ui, login_ui, main_win, found_users, user_info, credit_ui
from controllers.auth import UserAuthController

user_auth_controller = UserAuthController()


# xu ly nut
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
    Mainwindow.show()


def signup_ui_load():
    global ui
    ui = signup_ui.Ui_Sign_Up_Page(user_auth_controller)
    ui.setupUi(Mainwindow)
    ui.cancel_button.clicked.connect(home_page_ui)
    ui.apply_button.clicked.connect(login_ui_load)
    Mainwindow.show()


def login_ui_load():
    global ui
    ui = login_ui.Ui_Sign_In_Page(user_auth_controller)
    ui.setupUi(Mainwindow)
    ui.cancel_button.clicked.connect(home_page_ui)
    ui.apply_button.clicked.connect(main_win_ui)
    ui.signup_button.clicked.connect(signup_ui_load)
    Mainwindow.show()


def credit_ui_load():
    global ui
    ui = credit_ui.Ui_Credit_Page()
    ui.setupUi(Mainwindow)
    ui.back_button.clicked.connect(home_page_ui)
    Mainwindow.show()


def main_win_ui():
    global ui
    ui = main_win.Ui_Specific_Task()
    ui.setupUi(Mainwindow)
    ui.pushButton.clicked.connect(user_info_ui)
    ui.pushButton_2.clicked.connect(found_users_ui)
    ui.return_home_page.clicked.connect(home_page_ui)
    Mainwindow.show()


def user_info_ui():
    global ui
    ui = user_info.Ui_Info_Users_Page()
    ui.setupUi(Mainwindow)
    ui.cancel_button.clicked.connect(main_win_ui)
    Mainwindow.show()


def found_users_ui():
    global ui
    ui = found_users.Ui_Found_Users_Page()
    ui.setupUi(Mainwindow)
    ui.cancel_button.clicked.connect(main_win_ui)
    Mainwindow.show()


home_page_ui()
sys.exit(app.exec())
