# Form implementation generated from reading ui file '.\ui\signup.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Sign_Up_Page(object):
    def setupUi(self, Sign_Up_Page):
        Sign_Up_Page.setObjectName("Sign_Up_Page")
        Sign_Up_Page.resize(1074, 555)
        self.REGISTER_ACCOUNT = QtWidgets.QWidget(parent=Sign_Up_Page)
        self.REGISTER_ACCOUNT.setObjectName("REGISTER_ACCOUNT")
        self.info_account = QtWidgets.QGroupBox(parent=self.REGISTER_ACCOUNT)
        self.info_account.setGeometry(QtCore.QRect(280, 90, 511, 321))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        self.info_account.setFont(font)
        self.info_account.setAcceptDrops(True)
        self.info_account.setAutoFillBackground(False)
        self.info_account.setStyleSheet(
            "color: rgb(255, 255, 255);\n"
            "border-color: rgb(255, 255, 127);\n"
            'font: 700 9pt "Segoe UI";'
        )
        self.info_account.setObjectName("info_account")
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=self.info_account)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 60, 191, 161))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.text_labe_box = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.text_labe_box.setSizeConstraint(
            QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint
        )
        self.text_labe_box.setContentsMargins(0, 0, 0, 0)
        self.text_labe_box.setObjectName("text_labe_box")
        self.user_name_label = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        self.user_name_label.setFont(font)
        self.user_name_label.setStyleSheet(
            'font: 700 9pt "Segoe UI";\n' "color: rgb(255, 255, 255);"
        )
        self.user_name_label.setObjectName("user_name_label")
        self.text_labe_box.addWidget(self.user_name_label)
        self.emai_label = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.emai_label.setStyleSheet(
            "color: rgb(255, 255, 255);\n" 'font: 700 9pt "Segoe UI";'
        )
        self.emai_label.setObjectName("emai_label")
        self.text_labe_box.addWidget(self.emai_label)
        self.password_label = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        self.password_label.setFont(font)
        self.password_label.setStyleSheet(
            "color: rgb(255, 255, 255);\n" 'font: 700 9pt "Segoe UI";'
        )
        self.password_label.setObjectName("password_label")
        self.text_labe_box.addWidget(self.password_label)
        self.confirm_password_label = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        self.confirm_password_label.setFont(font)
        self.confirm_password_label.setStyleSheet(
            "color: rgb(255, 255, 255);\n" 'font: 700 9pt "Segoe UI";'
        )
        self.confirm_password_label.setObjectName("confirm_password_label")
        self.text_labe_box.addWidget(self.confirm_password_label)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(parent=self.info_account)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(220, 60, 251, 161))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.fill_in_user_info = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.fill_in_user_info.setSizeConstraint(
            QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint
        )
        self.fill_in_user_info.setContentsMargins(0, 0, 0, 0)
        self.fill_in_user_info.setObjectName("fill_in_user_info")
        self.account_name = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget_2)
        self.account_name.setStyleSheet(
            "color: rgb(0, 0, 0);\n"
            "background-color: rgb(255, 255, 255);\n"
            'font: 9pt "Segoe UI";'
        )
        self.account_name.setObjectName("account_name")
        self.fill_in_user_info.addWidget(self.account_name)
        self.account_email = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget_2)
        self.account_email.setStyleSheet(
            "color: rgb(0, 0, 0);\n"
            "background-color: rgb(255, 255, 255);\n"
            'font: 9pt "Segoe UI";'
        )
        self.account_email.setObjectName("account_email")
        self.fill_in_user_info.addWidget(self.account_email)
        self.account_password = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget_2)
        self.account_password.setStyleSheet(
            "color: rgb(0, 0, 0);\n"
            "background-color: rgb(255, 255, 255);\n"
            'font: 9pt "Segoe UI";'
        )
        self.account_password.setObjectName("account_password")
        self.fill_in_user_info.addWidget(self.account_password)
        self.confirm_password = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget_2)
        self.confirm_password.setStyleSheet(
            "color: rgb(0, 0, 0);\n"
            "background-color: rgb(255, 255, 255);\n"
            'font: 9pt "Segoe UI";'
        )
        self.confirm_password.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.confirm_password.setObjectName("confirm_password")
        self.fill_in_user_info.addWidget(self.confirm_password)
        self.horizontalLayoutWidget = QtWidgets.QWidget(parent=self.info_account)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(30, 250, 441, 28))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.check_robot_box = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.check_robot_box.setContentsMargins(0, 0, 0, 0)
        self.check_robot_box.setSpacing(7)
        self.check_robot_box.setObjectName("check_robot_box")
        self.check_robot_text = QtWidgets.QLabel(parent=self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        self.check_robot_text.setFont(font)
        self.check_robot_text.setStyleSheet(
            "color: rgb(255, 255, 255);\n" 'font: 700 9pt "Segoe UI";'
        )
        self.check_robot_text.setObjectName("check_robot_text")
        self.check_robot_box.addWidget(self.check_robot_text)
        self.check_robot = QtWidgets.QCheckBox(parent=self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        self.check_robot.setFont(font)
        self.check_robot.setStyleSheet(
            "color: rgb(255, 255, 127);\n" 'font: 700 9pt "Segoe UI";'
        )
        self.check_robot.setObjectName("check_robot")
        self.check_robot_box.addWidget(
            self.check_robot, 0, QtCore.Qt.AlignmentFlag.AlignHCenter
        )
        self.label = QtWidgets.QLabel(parent=self.info_account)
        self.label.setGeometry(QtCore.QRect(170, 290, 191, 20))
        self.label.setObjectName("label")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(parent=self.REGISTER_ACCOUNT)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(470, 450, 169, 31))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.exit_box = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.exit_box.setContentsMargins(0, 0, 0, 0)
        self.exit_box.setObjectName("exit_box")
        self.apply_button = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget_2)
        self.apply_button.setStyleSheet(
            "color: rgb(0, 0, 127);\n"
            "background-color: rgb(255, 255, 255);\n"
            'font: 700 9pt "Segoe UI";'
        )
        self.apply_button.setObjectName("apply_button")
        self.exit_box.addWidget(self.apply_button)
        self.cancel_button = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget_2)
        self.cancel_button.setStyleSheet(
            "color: rgb(170, 0, 0);\n"
            "background-color: rgb(255, 255, 255);\n"
            'font: 700 9pt "Segoe UI";'
        )
        self.cancel_button.setObjectName("cancel_button")
        self.exit_box.addWidget(self.cancel_button)
        self.image_1 = QtWidgets.QLabel(parent=self.REGISTER_ACCOUNT)
        self.image_1.setGeometry(QtCore.QRect(0, 110, 281, 301))
        self.image_1.setText("")
        self.image_1.setPixmap(
            QtGui.QPixmap(
                r"C:\Users\phatl\OneDrive - VNU-HCMUS\Desktop\relative_face_recognition_app\client\frontend\ui\picture\new_icon_3.png"
            )
        )
        self.image_1.setScaledContents(True)
        self.image_1.setWordWrap(True)
        self.image_1.setOpenExternalLinks(True)
        self.image_1.setObjectName("image_1")
        self.back_ground = QtWidgets.QLabel(parent=self.REGISTER_ACCOUNT)
        self.back_ground.setGeometry(QtCore.QRect(-10, 0, 1091, 555))
        self.back_ground.setMouseTracking(True)
        self.back_ground.setTabletTracking(True)
        self.back_ground.setAcceptDrops(True)
        self.back_ground.setAutoFillBackground(True)
        self.back_ground.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.back_ground.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.back_ground.setText("")
        self.back_ground.setPixmap(
            QtGui.QPixmap(
                r"C:\Users\phatl\OneDrive - VNU-HCMUS\Desktop\relative_face_recognition_app\client\frontend\ui\picture\background_4.jpg"
            )
        )
        self.back_ground.setScaledContents(True)
        self.back_ground.setWordWrap(True)
        self.back_ground.setOpenExternalLinks(True)
        self.back_ground.setObjectName("back_ground")
        self.image_2 = QtWidgets.QLabel(parent=self.REGISTER_ACCOUNT)
        self.image_2.setGeometry(QtCore.QRect(790, 110, 281, 301))
        self.image_2.setText("")
        self.image_2.setPixmap(
            QtGui.QPixmap(
                r"C:\Users\phatl\OneDrive - VNU-HCMUS\Desktop\relative_face_recognition_app\client\frontend\ui\picture\new_icon_2.png"
            )
        )
        self.image_2.setScaledContents(True)
        self.image_2.setWordWrap(True)
        self.image_2.setOpenExternalLinks(True)
        self.image_2.setObjectName("image_2")
        self.label_5 = QtWidgets.QLabel(parent=self.REGISTER_ACCOUNT)
        self.label_5.setGeometry(QtCore.QRect(450, 30, 181, 41))
        self.label_5.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "border-color: rgb(255, 255, 255);"
        )
        self.label_5.setFrameShape(QtWidgets.QFrame.Shape.WinPanel)
        self.label_5.setObjectName("label_5")
        self.label_2 = QtWidgets.QLabel(parent=self.REGISTER_ACCOUNT)
        self.label_2.setGeometry(QtCore.QRect(890, 0, 191, 171))
        self.label_2.setText("")
        self.label_2.setPixmap(
            QtGui.QPixmap(
                r"C:\Users\phatl\OneDrive - VNU-HCMUS\Desktop\relative_face_recognition_app\client\frontend\ui\picture\planet.png"
            )
        )
        self.label_2.setScaledContents(True)
        self.label_2.setWordWrap(True)
        self.label_2.setOpenExternalLinks(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.REGISTER_ACCOUNT)
        self.label_3.setGeometry(QtCore.QRect(0, 360, 191, 171))
        self.label_3.setText("")
        self.label_3.setPixmap(
            QtGui.QPixmap(
                r"C:\Users\phatl\OneDrive - VNU-HCMUS\Desktop\relative_face_recognition_app\client\frontend\ui\picture\star_new.png"
            )
        )
        self.label_3.setScaledContents(True)
        self.label_3.setWordWrap(True)
        self.label_3.setOpenExternalLinks(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.REGISTER_ACCOUNT)
        self.label_4.setGeometry(QtCore.QRect(360, 0, 101, 81))
        self.label_4.setText("")
        self.label_4.setPixmap(
            QtGui.QPixmap(
                r"C:\Users\phatl\OneDrive - VNU-HCMUS\Desktop\relative_face_recognition_app\client\frontend\ui\picture\star_line.png"
            )
        )
        self.label_4.setScaledContents(True)
        self.label_4.setWordWrap(True)
        self.label_4.setOpenExternalLinks(True)
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(parent=self.REGISTER_ACCOUNT)
        self.label_6.setGeometry(QtCore.QRect(620, 0, 101, 81))
        self.label_6.setText("")
        self.label_6.setPixmap(
            QtGui.QPixmap(
                r"C:\Users\phatl\OneDrive - VNU-HCMUS\Desktop\relative_face_recognition_app\client\frontend\ui\picture\star_line_2.png"
            )
        )
        self.label_6.setScaledContents(True)
        self.label_6.setWordWrap(True)
        self.label_6.setOpenExternalLinks(True)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(parent=self.REGISTER_ACCOUNT)
        self.label_7.setGeometry(QtCore.QRect(790, 380, 161, 151))
        self.label_7.setText("")
        self.label_7.setPixmap(
            QtGui.QPixmap(
                r"C:\Users\phatl\OneDrive - VNU-HCMUS\Desktop\relative_face_recognition_app\client\frontend\ui\picture\star_combo.png"
            )
        )
        self.label_7.setScaledContents(True)
        self.label_7.setWordWrap(True)
        self.label_7.setOpenExternalLinks(True)
        self.label_7.setObjectName("label_7")
        self.back_ground.raise_()
        self.info_account.raise_()
        self.horizontalLayoutWidget_2.raise_()
        self.image_1.raise_()
        self.image_2.raise_()
        self.label_5.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        Sign_Up_Page.setCentralWidget(self.REGISTER_ACCOUNT)
        self.menubar = QtWidgets.QMenuBar(parent=Sign_Up_Page)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1074, 25))
        self.menubar.setObjectName("menubar")
        self.menu_login_page = QtWidgets.QMenu(parent=self.menubar)
        self.menu_login_page.setObjectName("menu_login_page")
        self.menu_credit_page = QtWidgets.QMenu(parent=self.menubar)
        self.menu_credit_page.setObjectName("menu_credit_page")
        Sign_Up_Page.setMenuBar(self.menubar)
        self.menubar.addAction(self.menu_login_page.menuAction())
        self.menubar.addAction(self.menu_credit_page.menuAction())

        self.retranslateUi(Sign_Up_Page)
        QtCore.QMetaObject.connectSlotsByName(Sign_Up_Page)

    def retranslateUi(self, Sign_Up_Page):
        _translate = QtCore.QCoreApplication.translate
        Sign_Up_Page.setWindowTitle(_translate("Sign_Up_Page", "MainWindow"))
        self.info_account.setTitle(
            _translate("Sign_Up_Page", "📝 THÔNG TIN ĐĂNG KÝ TÀI KHOẢN")
        )
        self.user_name_label.setText(
            _translate(
                "Sign_Up_Page",
                '<html><head/><body><p>TÊN ĐĂNG KÝ <span style=" font-style:italic; color:#ffff7f;">(*)</span></p></body></html>',
            )
        )
        self.emai_label.setText(
            _translate(
                "Sign_Up_Page",
                '<html><head/><body><p>EMAIL ĐĂNG KÝ <span style=" font-style:italic; color:#ffff7f;">(*)</span></p></body></html>',
            )
        )
        self.password_label.setText(
            _translate(
                "Sign_Up_Page",
                '<html><head/><body><p>NHẬP MẬT KHẨU <span style=" font-style:italic; color:#ffff7f;">(*)</span></p></body></html>',
            )
        )
        self.confirm_password_label.setText(
            _translate(
                "Sign_Up_Page",
                '<html><head/><body><p>XÁC NHẬN MẬT KHẨU <span style=" font-style:italic; color:#ffff7f;">(*)</span></p></body></html>',
            )
        )
        self.account_name.setPlaceholderText(
            _translate("Sign_Up_Page", "Enter Your Username Account")
        )
        self.account_email.setPlaceholderText(
            _translate("Sign_Up_Page", "Email (ex: name_email@gmail.com)")
        )
        self.account_password.setPlaceholderText(
            _translate("Sign_Up_Page", "Enter Your Password")
        )
        self.confirm_password.setPlaceholderText(
            _translate("Sign_Up_Page", "Confirm Your Password")
        )
        self.check_robot_text.setText(
            _translate(
                "Sign_Up_Page",
                '<html><head/><body><p>BẠN CÓ PHẢI <span style=" color:#ffff7f;">ROBOT</span> KHÔNG ?</p></body></html>',
            )
        )
        self.check_robot.setText(_translate("Sign_Up_Page", "Not Robot 🤖"))
        self.label.setText(
            _translate(
                "Sign_Up_Page",
                '<html><head/><body><p><span style=" font-weight:400; font-style:italic; color:#ffffff;">(*) Đây là thông tin </span><span style=" font-weight:400; font-style:italic; text-decoration: underline; color:#ffffff;">bắt buộc.</span></p></body></html>',
            )
        )
        self.apply_button.setText(_translate("Sign_Up_Page", "APPLY"))
        self.cancel_button.setText(_translate("Sign_Up_Page", "CANCEL"))
        self.label_5.setText(
            _translate(
                "Sign_Up_Page",
                '<html><head/><body><p align="center"><span style=" font-size:14pt; font-weight:700; color:#ffffff;">FUInfo Apps</span></p></body></html>',
            )
        )
        self.menu_login_page.setTitle(_translate("Sign_Up_Page", "Login Page"))
        self.menu_credit_page.setTitle(_translate("Sign_Up_Page", "Credit Page"))
