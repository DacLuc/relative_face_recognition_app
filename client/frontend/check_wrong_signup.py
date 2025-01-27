from PyQt6 import QtCore, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(402, 89)
        self.exit_button = QtWidgets.QDialogButtonBox(parent=Dialog)
        self.exit_button.setGeometry(QtCore.QRect(110, 50, 167, 29))
        self.exit_button.setStyleSheet(
            "background-color: rgb(255, 255, 255);\n"
            'font: 700 9pt "Segoe UI";\n'
            "color: rgb(0, 0, 0);"
        )
        self.exit_button.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.exit_button.setStandardButtons(
            QtWidgets.QDialogButtonBox.StandardButton.Cancel
            | QtWidgets.QDialogButtonBox.StandardButton.Ok
        )
        self.exit_button.setObjectName("exit_button")
        self.text_dialog = QtWidgets.QTextBrowser(parent=Dialog)
        self.text_dialog.setGeometry(QtCore.QRect(10, 10, 380, 31))
        self.text_dialog.setStyleSheet(
            "color: rgb(170, 0, 0);\n" 'font: 700 9pt "Segoe UI";'
        )
        self.text_dialog.setObjectName("text_dialog")

        self.retranslateUi(Dialog)
        self.exit_button.accepted.connect(Dialog.accept)  # type: ignore
        self.exit_button.rejected.connect(Dialog.reject)  # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.text_dialog.setHtml(
            _translate(
                "Dialog",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><meta charset="utf-8" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "hr { height: 1px; border-width: 0; }\n"
                'li.unchecked::marker { content: "\\2610"; }\n'
                'li.checked::marker { content: "\\2612"; }\n'
                "</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:700; font-style:normal;\">\n"
                '<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">TÀI KHOẢN ĐĂNG KÝ ĐÃ TỒN TẠI 😓</p></body></html',
            )
        )
