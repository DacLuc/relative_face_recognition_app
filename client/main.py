from PyQt6 import QtCore, QtWidgets, QtQuick
import sys
import main_win, found_users, user_info

# xu ly nut
ui = ""
app = QtWidgets.QApplication(sys.argv)
Mainwindow = QtWidgets.QMainWindow()


def home_ui():
    global ui
    ui = main_win.Ui_MainWindow()
    ui.setupUi(Mainwindow)
    ui.pushButton.clicked.connect(page_1_ui)
    ui.pushButton_2.clicked.connect(page_2_ui)
    Mainwindow.show()


def page_1_ui():
    global ui
    ui = user_info.Ui_MainWindow()
    ui.setupUi(Mainwindow)
    ui.cancel_button.clicked.connect(home_ui)
    Mainwindow.show()


def page_2_ui():
    global ui
    ui = found_users.Ui_MainWindow()
    ui.setupUi(Mainwindow)
    ui.cancel_button.clicked.connect(home_ui)
    Mainwindow.show()


home_ui()
sys.exit(app.exec())
