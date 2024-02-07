from PyQt6 import QtCore, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1074, 555)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.results_box = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.results_box.setGeometry(QtCore.QRect(30, 20, 1021, 421))
        self.results_box.setStyleSheet(
            "color: rgb(0, 0, 0);\n" 'font: 700 9pt "Segoe UI";'
        )
        self.results_box.setObjectName("results_box")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(parent=self.results_box)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(80, 100, 431, 261))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.textBrowser = QtWidgets.QTextBrowser(parent=self.horizontalLayoutWidget_2)
        self.textBrowser.setObjectName("textBrowser")
        self.horizontalLayout_2.addWidget(self.textBrowser)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(parent=self.horizontalLayoutWidget_2)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_5 = QtWidgets.QLabel(parent=self.horizontalLayoutWidget_2)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.label_2 = QtWidgets.QLabel(parent=self.horizontalLayoutWidget_2)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(parent=self.horizontalLayoutWidget_2)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(parent=self.horizontalLayoutWidget_2)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(470, 460, 169, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.exit_place = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.exit_place.setContentsMargins(0, 0, 0, 0)
        self.exit_place.setObjectName("exit_place")
        self.select_button = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        self.select_button.setStyleSheet(
            "color: rgb(0, 0, 0);\n"
            "background-color: rgb(255, 255, 255);\n"
            'font: 700 9pt "Segoe UI";'
        )
        self.select_button.setObjectName("select_button")
        self.exit_place.addWidget(self.select_button)
        self.cancel_button = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        self.cancel_button.setStyleSheet(
            "color: rgb(0, 0, 0);\n"
            "color: rgb(170, 0, 0);\n"
            'font: 700 9pt "Segoe UI";\n'
            "background-color: rgb(255, 255, 255);"
        )
        self.cancel_button.setObjectName("cancel_button")
        self.exit_place.addWidget(self.cancel_button)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1074, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.results_box.setTitle(_translate("MainWindow", "KẾT QUẢ TÌM KIẾM "))
        self.label.setText(_translate("MainWindow", "Họ tên:"))
        self.label_5.setText(_translate("MainWindow", "Giới tính: "))
        self.label_2.setText(_translate("MainWindow", "Tuổi:"))
        self.label_3.setText(_translate("MainWindow", "Quê quán:"))
        self.label_4.setText(_translate("MainWindow", "Đặc điểm nhận dạng:"))
        self.select_button.setText(_translate("MainWindow", "SELECT"))
        self.cancel_button.setText(_translate("MainWindow", "CANCEL"))
