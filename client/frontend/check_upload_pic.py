from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(402, 89)
        self.exit_box = QtWidgets.QDialogButtonBox(parent=Dialog)
        self.exit_box.setGeometry(QtCore.QRect(120, 50, 167, 29))
        self.exit_box.setStyleSheet(
            "color: rgb(0, 0, 0);\n"
            "background-color: rgb(255, 255, 255);\n"
            'font: 700 9pt "Segoe UI";'
        )
        self.exit_box.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.exit_box.setStandardButtons(
            QtWidgets.QDialogButtonBox.StandardButton.Cancel
            | QtWidgets.QDialogButtonBox.StandardButton.Ok
        )
        self.exit_box.setObjectName("exit_box")
        self.textBrowser = QtWidgets.QTextBrowser(parent=Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(40, 10, 306, 33))
        self.textBrowser.setStyleSheet(
            "color: rgb(170, 0, 0);\n" 'font: 700 9pt "Segoe UI";'
        )
        self.textBrowser.setObjectName("textBrowser")

        self.retranslateUi(Dialog)
        self.exit_box.accepted.connect(Dialog.accept)  # type: ignore
        self.exit_box.rejected.connect(Dialog.reject)  # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.textBrowser.setHtml(
            _translate(
                "Dialog",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><meta charset="utf-8" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "hr { height: 1px; border-width: 0; }\n"
                'li.unchecked::marker { content: "\\2610"; }\n'
                'li.checked::marker { content: "\\2612"; }\n'
                "</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:700; font-style:normal;\">\n"
                '<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">BẠN ĐÃ UPLOAD HÌNH THÀNH CÔNG !!!</p></body></html>',
            )
        )
