# Form implementation generated from reading ui file '.\ui\check_finished_upload_image.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Check_Upload(object):
    def setupUi(self, Check_Upload):
        Check_Upload.setObjectName("Check_Upload")
        Check_Upload.resize(402, 89)
        self.exit_button = QtWidgets.QDialogButtonBox(parent=Check_Upload)
        self.exit_button.setGeometry(QtCore.QRect(110, 50, 167, 29))
        self.exit_button.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"font: 700 9pt \"Segoe UI\";")
        self.exit_button.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.exit_button.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Cancel|QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.exit_button.setObjectName("exit_button")
        self.text_info = QtWidgets.QTextBrowser(parent=Check_Upload)
        self.text_info.setGeometry(QtCore.QRect(0, 10, 401, 33))
        self.text_info.setStyleSheet("color: rgb(170, 0, 0);\n"
"font: 700 9pt \"Segoe UI\";")
        self.text_info.setObjectName("text_info")

        self.retranslateUi(Check_Upload)
        self.exit_button.accepted.connect(Check_Upload.accept) # type: ignore
        self.exit_button.rejected.connect(Check_Upload.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Check_Upload)

    def retranslateUi(self, Check_Upload):
        _translate = QtCore.QCoreApplication.translate
        Check_Upload.setWindowTitle(_translate("Check_Upload", "Dialog"))
        self.text_info.setHtml(_translate("Check_Upload", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:700; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> BẠN CHƯA UPLOAD HÌNH CÁ NHÂN 😰</p></body></html>"))
