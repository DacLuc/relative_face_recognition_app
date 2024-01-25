from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_check_box(object):
    def setupUi(self, check_box):
        check_box.setObjectName("check_box")
        check_box.resize(402, 89)
        self.exit_button = QtWidgets.QDialogButtonBox(parent=check_box)
        self.exit_button.setGeometry(QtCore.QRect(110, 50, 167, 29))
        self.exit_button.setStyleSheet(
            'font: 700 9pt "Segoe UI";\n'
            "background-color: rgb(255, 255, 255);\n"
            "color: rgb(0, 0, 0);"
        )
        self.exit_button.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.exit_button.setStandardButtons(
            QtWidgets.QDialogButtonBox.StandardButton.Cancel
            | QtWidgets.QDialogButtonBox.StandardButton.Ok
        )
        self.exit_button.setObjectName("exit_button")
        self.text_info = QtWidgets.QTextBrowser(parent=check_box)
        self.text_info.setGeometry(QtCore.QRect(10, 10, 380, 31))
        self.text_info.setStyleSheet(
            "color: rgb(170, 0, 0);\n" 'font: 700 9pt "Segoe UI";'
        )
        self.text_info.setObjectName("text_info")

        self.retranslateUi(check_box)
        self.exit_button.accepted.connect(check_box.accept)  # type: ignore
        self.exit_button.rejected.connect(check_box.reject)  # type: ignore
        QtCore.QMetaObject.connectSlotsByName(check_box)

    def retranslateUi(self, check_box):
        _translate = QtCore.QCoreApplication.translate
        check_box.setWindowTitle(_translate("check_box", "Dialog"))
        self.text_info.setHtml(
            _translate(
                "check_box",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><meta charset="utf-8" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "hr { height: 1px; border-width: 0; }\n"
                'li.unchecked::marker { content: "\\2610"; }\n'
                'li.checked::marker { content: "\\2612"; }\n'
                "</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:700; font-style:normal;\">\n"
                '<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">TÀI KHOẢN NÀY KHÔNG TỒN TẠI  😓</p></body></html',
            )
        )
