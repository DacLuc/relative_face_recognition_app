# from client.signup import SignUpWindow
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QVBoxLayout, QMainWindow, QLabel, QHBoxLayout, QPushButton, QButtonGroup
from PyQt6 import QtCore

# Only needed for access to command line arguments
import sys
sys.path.append("../../relative_face_recognition_app")
from client.login import LoginWindow
from client.signup import SignUpWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Finding People")
        self.login_wd = LoginWindow()
        self.signup_wd = SignUpWindow()

        layout = QVBoxLayout()
        

        btn_layout = QHBoxLayout()
        cancel_btn = QPushButton("Cancel")
        cancel_btn.clicked.connect(self.cancel_btn_clicked)
        submit_btn = QPushButton("Sumbit")
        submit_btn.clicked.connect(self.submit_btn_clicked)
        btn_layout.addWidget(cancel_btn)
        btn_layout.addWidget(submit_btn)

        
        # layout.addLayout(self.login_wd)
        layout.addWidget(self.login_wd)
        layout.addLayout(btn_layout)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def cancel_btn_clicked(self):
        print("cancel btn clicked")

    def submit_btn_clicked(self):
        # signup_window = SignUpWindow()
        self.signup_wd.show()
        self.login_wd.hide()
        print("submit btn clicked")


app = QApplication(sys.argv)

main_window = MainWindow()
main_window.show()

app.exec()
