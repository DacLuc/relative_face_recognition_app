from PyQt6 import QtCore, QtGui, QtWidgets

import check_login

from controllers.auth import UserAuthController
from models.user_validators import *

class Ui_Sign_In_Page(object):

    def __init__(self, user_auth_controller: UserAuthController):
        self.user_auth_controller = user_auth_controller

    def setupUi(self, Sign_In_Page):
        Sign_In_Page.setObjectName("Sign_In_Page")
        Sign_In_Page.resize(590, 370)
        self.centralwidget = QtWidgets.QWidget(parent=Sign_In_Page)
        self.centralwidget.setObjectName("centralwidget")
        self.title_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.title_label.setGeometry(QtCore.QRect(120, 10, 344, 27))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.title_label.setFont(font)
        self.title_label.setMouseTracking(True)
        self.title_label.setStyleSheet(
            "background-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375 rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0, 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255, 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625 rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));\n"
            "color: rgb(0, 0, 0);"
        )
        self.title_label.setObjectName("title_label")
        self.info_login = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.info_login.setGeometry(QtCore.QRect(60, 70, 461, 241))
        font = QtGui.QFont()
        font.setBold(True)
        self.info_login.setFont(font)
        self.info_login.setStyleSheet(
            "border-color: rgb(170, 0, 0);\n" "color: rgb(170, 0, 0);"
        )
        self.info_login.setObjectName("info_login")
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=self.info_login)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 50, 151, 71))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.name_label = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setBold(False)
        self.name_label.setFont(font)
        self.name_label.setStyleSheet("color: rgb(0, 0, 0);")
        self.name_label.setObjectName("name_label")
        self.verticalLayout.addWidget(self.name_label)
        self.password_label = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setBold(False)
        self.password_label.setFont(font)
        self.password_label.setStyleSheet("color: rgb(0, 0, 0);")
        self.password_label.setObjectName("password_label")
        self.verticalLayout.addWidget(self.password_label)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(parent=self.info_login)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(170, 50, 261, 71))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.account_name = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget_2)
        self.account_name.setStyleSheet(
            "background-color: rgb(255, 255, 255);\n" "color: rgb(0, 0, 0);"
        )
        self.account_name.setObjectName("account_name")
        self.verticalLayout_2.addWidget(self.account_name)
        self.account_password = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget_2)
        self.account_password.setMouseTracking(True)
        self.account_password.setStyleSheet(
            "color: rgb(0, 0, 0);\n" "background-color: rgb(255, 255, 255);"
        )
        self.account_password.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.account_password.setObjectName("account_password")
        self.verticalLayout_2.addWidget(self.account_password)
        self.horizontalLayoutWidget = QtWidgets.QWidget(parent=self.info_login)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(40, 190, 387, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.mov_register = QtWidgets.QLabel(parent=self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(True)
        self.mov_register.setFont(font)
        self.mov_register.setStyleSheet(
            'font: italic 9pt "Segoe UI";\n' "color: rgb(0, 0, 0);"
        )
        self.mov_register.setObjectName("mov_register")
        self.horizontalLayout.addWidget(self.mov_register)
        self.signup_button = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        self.signup_button.setStyleSheet(
            "color: rgb(170, 0, 0);\n"
            'font: 700 italic 9pt "Segoe UI";\n'
            "background-color: rgb(255, 255, 255);"
        )
        self.signup_button.setObjectName("signup_button")
        self.horizontalLayout.addWidget(self.signup_button)
        self.label_3 = QtWidgets.QLabel(parent=self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setBold(False)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(parent=self.info_login)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(140, 140, 169, 31))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.exit_dialog = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.exit_dialog.setContentsMargins(0, 0, 0, 0)
        self.exit_dialog.setObjectName("exit_dialog")
        self.apply_button = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget_2)
        self.apply_button.setStyleSheet(
            "color: rgb(0, 0, 127);\n"
            "background-color: rgb(255, 255, 255);\n"
            'font: 700 9pt "Segoe UI";'
        )
        self.apply_button.setObjectName("apply_button")
        self.exit_dialog.addWidget(self.apply_button)
        self.apply_button.clicked.connect(self.check_login)
        self.cancel_button = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget_2)
        self.cancel_button.setStyleSheet(
            "color: rgb(170, 0, 0);\n"
            "background-color: rgb(255, 255, 255);\n"
            'font: 700 9pt "Segoe UI";'
        )
        self.cancel_button.setObjectName("cancel_button")
        self.exit_dialog.addWidget(self.cancel_button)
        Sign_In_Page.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=Sign_In_Page)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 590, 25))
        self.menubar.setObjectName("menubar")
        Sign_In_Page.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=Sign_In_Page)
        self.statusbar.setObjectName("statusbar")
        Sign_In_Page.setStatusBar(self.statusbar)

        self.retranslateUi(Sign_In_Page)
        QtCore.QMetaObject.connectSlotsByName(Sign_In_Page)

    def check_login(self):
        dlg = QtWidgets.QDialog()
        ui = check_login.Ui_check_login()
        ui.setupUi(dlg)
        dlg.exec()
        username = self.account_name.text()
        password = self.account_password.text()
        new_user = UserSignIn(
            username=username, password=password)
        # if new_user:
        isLoggedInSuccessfully = self.user_auth_controller.log_in(username, password)
        print("isLoggedInSuccessfully: ", isLoggedInSuccessfully)
        if isLoggedInSuccessfully:
            return ui.exit_button.clicked.connect(self.check_login)
        else:
            return "LOGIN FAILED"

    def retranslateUi(self, Sign_In_Page):
        _translate = QtCore.QCoreApplication.translate
        Sign_In_Page.setWindowTitle(_translate("Sign_In_Page", "MainWindow"))
        self.title_label.setText(
            _translate(
                "Sign_In_Page",
                '<html><head/><body><p align="center">ỨNG DỤNG TÌM NGƯỜI MUỐN GẶP</p></body></html>',
            )
        )
        self.info_login.setTitle(
            _translate("Sign_In_Page", "THÔNG TIN ĐĂNG NHẬP TÀI KHOẢN")
        )
        self.name_label.setText(
            _translate(
                "Sign_In_Page",
                '<html><head/><body><p><span style=" font-weight:700;">TÊN ĐĂNG NHẬP</span></p></body></html>',
            )
        )
        self.password_label.setText(
            _translate(
                "Sign_In_Page",
                '<html><head/><body><p><span style=" font-weight:700;">MẬT KHẨU</span></p></body></html>',
            )
        )
        self.account_name.setPlaceholderText(
            _translate("Sign_In_Page", "Ten Dang Nhap")
        )
        self.account_password.setPlaceholderText(_translate("Sign_In_Page", "Password"))
        self.mov_register.setText(
            _translate("Sign_In_Page", "Nếu bạn chưa đăng ký tài khoản, hãy")
        )
        self.signup_button.setText(_translate("Sign_In_Page", "ĐĂNG KÝ"))
        self.label_3.setText(
            _translate(
                "Sign_In_Page",
                '<html><head/><body><p><span style=" font-style:italic;">ngay !!!</span></p></body></html>',
            )
        )
        self.apply_button.setText(_translate("Sign_In_Page", "APPLY"))
        self.cancel_button.setText(_translate("Sign_In_Page", "CANCEL"))
