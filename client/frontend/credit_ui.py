# Form implementation generated from reading ui file '.\ui\credit_page.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Credit_Page(object):
    def setupUi(self, Credit_Page):
        Credit_Page.setObjectName("Credit_Page")
        Credit_Page.resize(1074, 555)
        Credit_Page.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(parent=Credit_Page)
        self.centralwidget.setObjectName("centralwidget")
        self.credit_info_box = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.credit_info_box.setGeometry(QtCore.QRect(310, 110, 436, 251))
        self.credit_info_box.setStyleSheet(
            'font: 700 9pt "Segoe UI";\n'
            "border-color: rgb(170, 0, 0);\n"
            "color: rgb(255, 255, 255);"
        )
        self.credit_info_box.setObjectName("credit_info_box")
        self.label = QtWidgets.QLabel(parent=self.credit_info_box)
        self.label.setGeometry(QtCore.QRect(100, 80, 63, 21))
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_6 = QtWidgets.QLabel(parent=self.credit_info_box)
        self.label_6.setGeometry(QtCore.QRect(0, 40, 431, 201))
        self.label_6.setObjectName("label_6")
        self.back_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.back_button.setGeometry(QtCore.QRect(500, 410, 80, 29))
        self.back_button.setMaximumSize(QtCore.QSize(83, 29))
        self.back_button.setStyleSheet(
            "color: rgb(170, 0, 0);\n"
            "background-color: rgb(255, 255, 255);\n"
            'font: 700 9pt "Segoe UI";'
        )
        self.back_button.setObjectName("back_button")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 1074, 555))
        self.label_2.setAutoFillBackground(False)
        self.label_2.setText("")
        self.label_2.setPixmap(
            QtGui.QPixmap(
                r"C:\Users\phatl\OneDrive - VNU-HCMUS\Desktop\relative_face_recognition_app\client\frontend\ui\picture\Outer Space Flipgrid Background.png"
            )
        )
        self.label_2.setScaledContents(True)
        self.label_2.setWordWrap(True)
        self.label_2.setOpenExternalLinks(True)
        self.label_2.setObjectName("label_2")
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(440, 20, 181, 41))
        self.label_5.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "border-color: rgb(255, 255, 255);"
        )
        self.label_5.setFrameShape(QtWidgets.QFrame.Shape.WinPanel)
        self.label_5.setObjectName("label_5")
        self.label_8 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(340, -10, 111, 81))
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
        self.label_10.setGeometry(QtCore.QRect(610, -10, 111, 81))
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
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(690, 50, 161, 141))
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
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(230, 290, 161, 141))
        self.label_4.setText("")
        self.label_4.setPixmap(
            QtGui.QPixmap(
                r"C:\Users\phatl\OneDrive - VNU-HCMUS\Desktop\relative_face_recognition_app\client\frontend\ui\picture\planet.png"
            )
        )
        self.label_4.setScaledContents(True)
        self.label_4.setWordWrap(True)
        self.label_4.setOpenExternalLinks(True)
        self.label_4.setObjectName("label_4")
        self.label_2.raise_()
        self.back_button.raise_()
        self.credit_info_box.raise_()
        self.label_5.raise_()
        self.label_8.raise_()
        self.label_10.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        Credit_Page.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=Credit_Page)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1074, 25))
        self.menubar.setObjectName("menubar")
        Credit_Page.setMenuBar(self.menubar)

        self.retranslateUi(Credit_Page)
        QtCore.QMetaObject.connectSlotsByName(Credit_Page)

    def retranslateUi(self, Credit_Page):
        _translate = QtCore.QCoreApplication.translate
        Credit_Page.setWindowTitle(_translate("Credit_Page", "MainWindow"))
        self.credit_info_box.setTitle(
            _translate("Credit_Page", "📚 THÔNG TIN CHƯƠNG TRÌNH ỨNG DỤNG")
        )
        self.label_6.setText(
            _translate(
                "Credit_Page",
                '<html><head/><body><p align="center"><span style=" font-weight:700;">CHƯƠNG TRÌNH ỨNG DỤNG TÌM NGƯỜI MUỐN GẶP</span></p><p align="center">Được thực hiện bởi:</p><p align="center"><span style=" font-weight:700;">Lê Phước Phát</span></p><p align="center"><span style=" font-weight:700;">Hồ Đắc Lực</span></p><p align="center">Được hướng dẫn bởi anh <span style=" font-weight:700;">Lê Nguyễn Thanh Huy</span></p></body></html>',
            )
        )
        self.back_button.setText(_translate("Credit_Page", "BACK"))
        self.label_5.setText(
            _translate(
                "Credit_Page",
                '<html><head/><body><p align="center"><span style=" font-size:14pt; font-weight:700; color:#ffffff;">FUInfo Apps</span></p></body></html>',
            )
        )
