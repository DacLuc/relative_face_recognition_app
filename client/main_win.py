from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Specific_Task(object):
    def setupUi(self, Specific_Task):
        Specific_Task.setObjectName("Specific_Task")
        Specific_Task.resize(601, 410)
        self.centralwidget = QtWidgets.QWidget(parent=Specific_Task)
        self.centralwidget.setObjectName("centralwidget")
        self.title_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.title_label.setGeometry(QtCore.QRect(130, 20, 344, 27))
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
        self.tasks_box = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.tasks_box.setGeometry(QtCore.QRect(130, 70, 340, 261))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        self.tasks_box.setFont(font)
        self.tasks_box.setStyleSheet(
            "color: rgb(170, 0, 0);\n"
            'font: 700 9pt "Segoe UI";\n'
            'font: 9pt "Segoe UI";\n'
            'font: 700 9pt "Segoe UI";'
        )
        self.tasks_box.setObjectName("tasks_box")
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=self.tasks_box)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(60, 80, 220, 144))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Showcard Gothic")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        self.label.setFont(font)
        self.label.setStyleSheet(
            "color: rgb(170, 0, 255);\n" 'font: 12pt "Showcard Gothic";'
        )
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.pushButton = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.pushButton.setStyleSheet(
            "background-color: rgb(255, 255, 255);\n" "color: rgb(0, 0, 0);"
        )
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.pushButton_2.setStyleSheet(
            "color: rgb(0, 0, 0);\n" "background-color: rgb(255, 255, 255);"
        )
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.return_home_page = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.return_home_page.setStyleSheet(
            "color: rgb(170, 0, 0);\n"
            'font: 700 9pt "Segoe UI";\n'
            "background-color: rgb(255, 255, 255);"
        )
        self.return_home_page.setObjectName("return_home_page")
        self.verticalLayout.addWidget(self.return_home_page)
        Specific_Task.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=Specific_Task)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 601, 25))
        self.menubar.setObjectName("menubar")
        Specific_Task.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=Specific_Task)
        self.statusbar.setObjectName("statusbar")
        Specific_Task.setStatusBar(self.statusbar)

        self.retranslateUi(Specific_Task)
        QtCore.QMetaObject.connectSlotsByName(Specific_Task)

    def retranslateUi(self, Specific_Task):
        _translate = QtCore.QCoreApplication.translate
        Specific_Task.setWindowTitle(_translate("Specific_Task", "MainWindow"))
        self.title_label.setText(
            _translate(
                "Specific_Task",
                '<html><head/><body><p align="center">ỨNG DỤNG TÌM NGƯỜI MUỐN GẶP</p></body></html>',
            )
        )
        self.tasks_box.setTitle(_translate("Specific_Task", "CÁC CHỨC NĂNG ỨND DỤNG"))
        self.label.setText(
            _translate(
                "Specific_Task",
                '<html><head/><body><p align="center"><span style=" font-size:12pt;">MENU</span></p></body></html>',
            )
        )
        self.pushButton.setText(_translate("Specific_Task", "NHẬP THÔNG TIN CÁ NHÂN "))
        self.pushButton_2.setText(
            _translate("Specific_Task", "NHẬP THÔNG TIN TÌM KIẾM")
        )
        self.return_home_page.setText(_translate("Specific_Task", "TRỞ VỀ TRANG CHỦ"))
