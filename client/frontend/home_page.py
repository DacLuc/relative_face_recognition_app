# Form implementation generated from reading ui file '.\ui\home_page.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Home_Page(object):
    def setupUi(self, Home_Page):
        Home_Page.setObjectName("Home_Page")
        Home_Page.resize(1074, 555)
        self.centralwidget = QtWidgets.QWidget(parent=Home_Page)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 241, 241))
        self.label.setAutoFillBackground(False)
        self.label.setText("")
        self.label.setPixmap(
            QtGui.QPixmap(
                r"C:\Users\phatl\OneDrive - VNU-HCMUS\Desktop\relative_face_recognition_app\client\frontend\ui\picture\new.png"
            )
        )
        self.label.setScaledContents(True)
        self.label.setWordWrap(True)
        self.label.setOpenExternalLinks(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(-10, 320, 231, 211))
        self.label_2.setAutoFillBackground(False)
        self.label_2.setText("")
        self.label_2.setPixmap(
            QtGui.QPixmap(
                r"C:\Users\phatl\OneDrive - VNU-HCMUS\Desktop\relative_face_recognition_app\client\frontend\ui\picture\planet_icon.png"
            )
        )
        self.label_2.setScaledContents(True)
        self.label_2.setWordWrap(True)
        self.label_2.setOpenExternalLinks(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(240, 80, 571, 411))
        self.label_3.setText("")
        self.label_3.setPixmap(
            QtGui.QPixmap(
                r"C:\Users\phatl\OneDrive - VNU-HCMUS\Desktop\relative_face_recognition_app\client\frontend\ui\picture\backdrop.png"
            )
        )
        self.label_3.setScaledContents(True)
        self.label_3.setWordWrap(True)
        self.label_3.setOpenExternalLinks(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(0, 0, 1074, 555))
        self.label_4.setText("")
        self.label_4.setPixmap(
            QtGui.QPixmap(
                r"C:\Users\phatl\OneDrive - VNU-HCMUS\Desktop\relative_face_recognition_app\client\frontend\ui\picture\272978352_d5dde1.jpg"
            )
        )
        self.label_4.setScaledContents(True)
        self.label_4.setWordWrap(True)
        self.label_4.setOpenExternalLinks(True)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(420, 20, 181, 41))
        self.label_5.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "border-color: rgb(255, 255, 255);"
        )
        self.label_5.setFrameShape(QtWidgets.QFrame.Shape.WinPanel)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(860, 0, 211, 191))
        self.label_6.setAutoFillBackground(False)
        self.label_6.setText("")
        self.label_6.setPixmap(
            QtGui.QPixmap(
                r"C:\Users\phatl\OneDrive - VNU-HCMUS\Desktop\relative_face_recognition_app\client\frontend\ui\picture\sao_tho.png"
            )
        )
        self.label_6.setScaledContents(True)
        self.label_6.setWordWrap(True)
        self.label_6.setOpenExternalLinks(True)
        self.label_6.setObjectName("label_6")
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(400, 200, 217, 171))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.name_label_box = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.name_label_box.setContentsMargins(0, 0, 0, 0)
        self.name_label_box.setObjectName("name_label_box")
        self.title_label_1 = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Showcard Gothic")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        self.title_label_1.setFont(font)
        self.title_label_1.setStyleSheet(
            "color: rgb(255, 85, 255);\n" 'font: 12pt "Showcard Gothic";'
        )
        self.title_label_1.setObjectName("title_label_1")
        self.name_label_box.addWidget(self.title_label_1)
        self.signup_button = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        self.signup_button.setFont(font)
        self.signup_button.setStyleSheet(
            "background-color: rgb(255, 255, 255);\n"
            'font: 700 9pt "Segoe UI";\n'
            "color: rgb(0, 0, 0);"
        )
        self.signup_button.setObjectName("signup_button")
        self.name_label_box.addWidget(self.signup_button)
        self.signin_button = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.signin_button.setStyleSheet(
            "color: rgb(0, 0, 0);\n"
            'font: 700 9pt "Segoe UI";\n'
            "background-color: rgb(255, 255, 255);"
        )
        self.signin_button.setObjectName("signin_button")
        self.name_label_box.addWidget(self.signin_button)
        self.credit_button = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.credit_button.setStyleSheet(
            "color: rgb(0, 0, 0);\n"
            "background-color: rgb(255, 255, 255);\n"
            'font: 700 9pt "Segoe UI";'
        )
        self.credit_button.setObjectName("credit_button")
        self.name_label_box.addWidget(self.credit_button)
        self.exit_button = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.exit_button.setStyleSheet(
            "color: rgb(170, 0, 0);\n"
            "background-color: rgb(255, 255, 255);\n"
            'font: 700 9pt "Segoe UI";'
        )
        self.exit_button.setObjectName("exit_button")
        self.name_label_box.addWidget(self.exit_button)
        self.label_9 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(240, 80, 136, 21))
        self.label_9.setStyleSheet(
            "color: rgb(255, 255, 255);\n" 'font: 700 9pt "Segoe UI";'
        )
        self.label_9.setObjectName("label_9")
        self.label_7 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(830, 290, 241, 241))
        self.label_7.setAutoFillBackground(False)
        self.label_7.setText("")
        self.label_7.setPixmap(
            QtGui.QPixmap(
                r"C:\Users\phatl\OneDrive - VNU-HCMUS\Desktop\relative_face_recognition_app\client\frontend\ui\picture\icon_2.png"
            )
        )
        self.label_7.setScaledContents(True)
        self.label_7.setWordWrap(True)
        self.label_7.setOpenExternalLinks(True)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(320, 0, 111, 81))
        self.label_8.setAutoFillBackground(False)
        self.label_8.setText("")
        self.label_8.setPixmap(
            QtGui.QPixmap(
                r"C:\Users\phatl\OneDrive - VNU-HCMUS\Desktop\relative_face_recognition_app\client\frontend\ui\picture\star_line.png"
            )
        )
        self.label_8.setScaledContents(True)
        self.label_8.setWordWrap(True)
        self.label_8.setOpenExternalLinks(True)
        self.label_8.setObjectName("label_8")
        self.label_10 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(590, 0, 111, 81))
        self.label_10.setAutoFillBackground(False)
        self.label_10.setText("")
        self.label_10.setPixmap(
            QtGui.QPixmap(
                r"C:\Users\phatl\OneDrive - VNU-HCMUS\Desktop\relative_face_recognition_app\client\frontend\ui\picture\star_line_2.png"
            )
        )
        self.label_10.setScaledContents(True)
        self.label_10.setWordWrap(True)
        self.label_10.setOpenExternalLinks(True)
        self.label_10.setObjectName("label_10")
        self.label_4.raise_()
        self.label_3.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.verticalLayoutWidget.raise_()
        self.label_9.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.label_10.raise_()
        Home_Page.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=Home_Page)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1074, 25))
        self.menubar.setObjectName("menubar")
        Home_Page.setMenuBar(self.menubar)

        self.retranslateUi(Home_Page)
        QtCore.QMetaObject.connectSlotsByName(Home_Page)

    def retranslateUi(self, Home_Page):
        _translate = QtCore.QCoreApplication.translate
        Home_Page.setWindowTitle(_translate("Home_Page", "MainWindow"))
        self.label_5.setText(
            _translate(
                "Home_Page",
                '<html><head/><body><p align="center"><span style=" font-size:14pt; font-weight:700; color:#ffffff;">FUInfo Apps</span></p></body></html>',
            )
        )
        self.title_label_1.setText(
            _translate(
                "Home_Page",
                '<html><head/><body><p align="center"><span style=" color:#ffffff;">WELCOME TO MY APP</span></p></body></html>',
            )
        )
        self.signup_button.setText(_translate("Home_Page", "ĐĂNG KÝ"))
        self.signin_button.setText(_translate("Home_Page", "ĐĂNG NHẬP"))
        self.credit_button.setText(_translate("Home_Page", "THÔNG TIN CHƯƠNG TRÌNH"))
        self.exit_button.setText(_translate("Home_Page", "THOÁT CHƯƠNG TRÌNH"))
        self.label_9.setText(_translate("Home_Page", "🌍🌞 TRANG CHỦ"))
