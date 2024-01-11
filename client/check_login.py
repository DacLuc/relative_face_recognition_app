from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_check_login(object):
    def setupUi(self, check_login):
        check_login.setObjectName("check_login")
        check_login.resize(311, 132)
        self.exit_button = QtWidgets.QDialogButtonBox(parent=check_login)
        self.exit_button.setGeometry(QtCore.QRect(70, 80, 167, 29))
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
        self.textBrowser = QtWidgets.QTextBrowser(parent=check_login)
        self.textBrowser.setGeometry(QtCore.QRect(10, 30, 291, 31))
        self.textBrowser.setStyleSheet(
            "color: rgb(170, 0, 0);\n" 'font: 700 9pt "Segoe UI";'
        )
        self.textBrowser.setObjectName("textBrowser")

        self.retranslateUi(check_login)
        self.exit_button.accepted.connect(check_login.accept)  # type: ignore
        self.exit_button.rejected.connect(check_login.reject)  # type: ignore
        QtCore.QMetaObject.connectSlotsByName(check_login)

    def retranslateUi(self, check_login):
        _translate = QtCore.QCoreApplication.translate
        check_login.setWindowTitle(_translate("check_login", "Dialog"))
        self.textBrowser.setHtml(
            _translate(
                "check_login",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><meta charset="utf-8" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "hr { height: 1px; border-width: 0; }\n"
                'li.unchecked::marker { content: "\\2610"; }\n'
                'li.checked::marker { content: "\\2612"; }\n'
                "</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:700; font-style:normal;\">\n"
                '<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">BẠN ĐÃ ĐĂNG NHẬP THÀNH CÔNG !!!</p></body></html>',
            )
        )
