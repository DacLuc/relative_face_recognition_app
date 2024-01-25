from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_check_signup(object):
    def setupUi(self, check_signup):
        check_signup.setObjectName("check_signup")
        check_signup.resize(402, 89)
        check_signup.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.info = QtWidgets.QTextBrowser(parent=check_signup)
        self.info.setGeometry(QtCore.QRect(11, 11, 380, 31))
        self.info.setStyleSheet("color: rgb(170, 0, 0);\n" 'font: 700 9pt "Segoe UI";')
        self.info.setObjectName("info")
        self.exit_button = QtWidgets.QDialogButtonBox(parent=check_signup)
        self.exit_button.setGeometry(QtCore.QRect(120, 50, 167, 29))
        self.exit_button.setStyleSheet(
            "color: rgb(0, 0, 0);\n"
            "background-color: rgb(255, 255, 255);\n"
            'font: 700 9pt "Segoe UI";'
        )
        self.exit_button.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.exit_button.setStandardButtons(
            QtWidgets.QDialogButtonBox.StandardButton.Cancel
            | QtWidgets.QDialogButtonBox.StandardButton.Ok
        )
        self.exit_button.setObjectName("exit_button")

        self.retranslateUi(check_signup)
        self.exit_button.accepted.connect(check_signup.accept)  # type: ignore
        self.exit_button.rejected.connect(check_signup.reject)  # type: ignore
        QtCore.QMetaObject.connectSlotsByName(check_signup)

    def retranslateUi(self, check_signup):
        _translate = QtCore.QCoreApplication.translate
        check_signup.setWindowTitle(_translate("check_signup", "Dialog"))
        self.info.setHtml(
            _translate(
                "check_signup",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><meta charset="utf-8" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "hr { height: 1px; border-width: 0; }\n"
                'li.unchecked::marker { content: "\\2610"; }\n'
                'li.checked::marker { content: "\\2612"; }\n'
                "</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:700; font-style:normal;\">\n"
                '<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">BẠN ĐÃ ĐĂNG KÝ TÀI KHOẢN THÀNH CÔNG !!!</p></body></html>',
            )
        )
