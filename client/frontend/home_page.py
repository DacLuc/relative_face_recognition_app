from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Home_Page(object):
    def setupUi(self, Home_Page):
        Home_Page.setObjectName("Home_Page")
        Home_Page.resize(1074, 555)
        self.centralwidget = QtWidgets.QWidget(parent=Home_Page)
        self.centralwidget.setObjectName("centralwidget")
        self.title_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.title_label.setGeometry(QtCore.QRect(360, 60, 344, 27))
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
        self.home_page_box = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.home_page_box.setGeometry(QtCore.QRect(350, 170, 361, 241))
        font = QtGui.QFont()
        font.setBold(True)
        self.home_page_box.setFont(font)
        self.home_page_box.setStyleSheet("color: rgb(170, 0, 0);")
        self.home_page_box.setObjectName("home_page_box")
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=self.home_page_box)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(60, 50, 258, 171))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
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
        self.verticalLayout.addWidget(self.title_label_1)
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
        self.verticalLayout.addWidget(self.signup_button)
        self.signin_button = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.signin_button.setStyleSheet(
            "color: rgb(0, 0, 0);\n"
            'font: 700 9pt "Segoe UI";\n'
            "background-color: rgb(255, 255, 255);"
        )
        self.signin_button.setObjectName("signin_button")
        self.verticalLayout.addWidget(self.signin_button)
        self.credit_button = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.credit_button.setStyleSheet(
            "color: rgb(0, 0, 0);\n"
            "background-color: rgb(255, 255, 255);\n"
            'font: 700 9pt "Segoe UI";'
        )
        self.credit_button.setObjectName("credit_button")
        self.verticalLayout.addWidget(self.credit_button)
        self.exit_button = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.exit_button.setStyleSheet(
            "color: rgb(170, 0, 0);\n"
            "background-color: rgb(255, 255, 255);\n"
            'font: 700 9pt "Segoe UI";'
        )
        self.exit_button.setObjectName("exit_button")
        self.verticalLayout.addWidget(self.exit_button)
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
        self.title_label.setText(
            _translate(
                "Home_Page",
                '<html><head/><body><p align="center">ỨNG DỤNG TÌM NGƯỜI MUỐN GẶP</p></body></html>',
            )
        )
        self.home_page_box.setTitle(_translate("Home_Page", "TRANG CHỦ"))
        self.title_label_1.setText(
            _translate(
                "Home_Page",
                '<html><head/><body><p align="center"><span style=" font-size:12pt;">WELCOME TO MY PROJECT</span></p></body></html>',
            )
        )
        self.signup_button.setText(_translate("Home_Page", "ĐĂNG KÝ"))
        self.signin_button.setText(_translate("Home_Page", "ĐĂNG NHẬP"))
        self.credit_button.setText(_translate("Home_Page", "CREDIT"))
        self.exit_button.setText(_translate("Home_Page", "EXIT"))
