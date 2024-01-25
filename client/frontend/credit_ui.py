from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Credit_Page(object):
    def setupUi(self, Credit_Page):
        Credit_Page.setObjectName("Credit_Page")
        Credit_Page.resize(1074, 555)
        Credit_Page.setStyleSheet("image: url(:/pic/icon.png);")
        self.centralwidget = QtWidgets.QWidget(parent=Credit_Page)
        self.centralwidget.setObjectName("centralwidget")
        self.credit_info_box = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.credit_info_box.setGeometry(QtCore.QRect(330, 150, 401, 171))
        self.credit_info_box.setStyleSheet(
            'font: 700 9pt "Segoe UI";\n'
            "color: rgb(170, 0, 0);\n"
            "border-color: rgb(170, 0, 0);"
        )
        self.credit_info_box.setObjectName("credit_info_box")
        self.label = QtWidgets.QLabel(parent=self.credit_info_box)
        self.label.setGeometry(QtCore.QRect(100, 80, 63, 21))
        self.label.setText("")
        self.label.setObjectName("label")
        self.credit_info_text = QtWidgets.QTextBrowser(parent=self.credit_info_box)
        self.credit_info_text.setGeometry(QtCore.QRect(10, 30, 381, 131))
        self.credit_info_text.setStyleSheet(
            "color: rgb(0, 0, 0);\n" 'font: 700 9pt "Segoe UI";'
        )
        self.credit_info_text.setObjectName("credit_info_text")
        self.title_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.title_label.setGeometry(QtCore.QRect(360, 110, 344, 27))
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
        self.back_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.back_button.setGeometry(QtCore.QRect(480, 350, 83, 29))
        self.back_button.setMaximumSize(QtCore.QSize(83, 29))
        self.back_button.setStyleSheet(
            "color: rgb(170, 0, 0);\n"
            "background-color: rgb(255, 255, 255);\n"
            'font: 700 9pt "Segoe UI";'
        )
        self.back_button.setObjectName("back_button")
        self.back_button.raise_()
        self.credit_info_box.raise_()
        self.title_label.raise_()
        Credit_Page.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=Credit_Page)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1074, 22))
        self.menubar.setObjectName("menubar")
        Credit_Page.setMenuBar(self.menubar)

        self.retranslateUi(Credit_Page)
        QtCore.QMetaObject.connectSlotsByName(Credit_Page)

    def retranslateUi(self, Credit_Page):
        _translate = QtCore.QCoreApplication.translate
        Credit_Page.setWindowTitle(_translate("Credit_Page", "MainWindow"))
        self.credit_info_box.setTitle(
            _translate("Credit_Page", "THÔNG TIN CHƯƠNG TRÌNH ỨNG DỤNG")
        )
        self.credit_info_text.setHtml(
            _translate(
                "Credit_Page",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><meta charset="utf-8" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "hr { height: 1px; border-width: 0; }\n"
                'li.unchecked::marker { content: "\\2610"; }\n'
                'li.checked::marker { content: "\\2612"; }\n'
                "</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:700; font-style:normal;\">\n"
                '<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">CHƯƠNG TRÌNH ỨNG DỤNG TÌM NGƯỜI MUỐN GẶP</p>\n'
                '<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-weight:400;">Được thực hiện bởi:</span></p>\n'
                '<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Lê Phước Phát</p>\n'
                '<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Hồ Đắc Lực</p>\n'
                '<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-weight:400;">Được hướng dẫn bởi anh </span>Lê Nguyễn Thanh Huy</p></body></html>',
            )
        )
        self.title_label.setText(
            _translate(
                "Credit_Page",
                '<html><head/><body><p align="center">ỨNG DỤNG TÌM NGƯỜI MUỐN GẶP</p></body></html>',
            )
        )
        self.back_button.setText(_translate("Credit_Page", "BACK"))
