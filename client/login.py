from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QVBoxLayout, QMainWindow, QLabel, QHBoxLayout, QPushButton, QButtonGroup
from PyQt6 import QtCore

# Only needed for access to command line arguments
import sys
sys.path.append("../../relative_face_recognition_app")
from client.signup import SignUpWindow

class LoginWindow(QMainWindow):
    def __init__(self):
        super(LoginWindow, self).__init__()

        self.setWindowTitle("Finding People")

        layout = QVBoxLayout()
        username_label = QLabel("Username: ")
        username = QLineEdit()
        password_label = QLabel("Password: ")
        password = QLineEdit()
        password.setEchoMode(QLineEdit.EchoMode.Password)

        btn_layout = QHBoxLayout()
        cancel_btn = QPushButton("Cancel")
        cancel_btn.clicked.connect(self.cancel_btn_clicked)
        submit_btn = QPushButton("Sumbit")
        submit_btn.clicked.connect(self.submit_btn_clicked)
        btn_layout.addWidget(cancel_btn)
        btn_layout.addWidget(submit_btn)

        layout.addWidget(username_label)
        layout.addWidget(username)
        layout.addWidget(password_label)
        layout.addWidget(password)
        layout.addLayout(btn_layout)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def cancel_btn_clicked(self):
        print("cancel btn clicked")

    def submit_btn_clicked(self):
        signup_window = SignUpWindow()
        signup_window.show()
        print("submit btn clicked")


app = QApplication(sys.argv)

login_window = LoginWindow()
login_window.show()

app.exec()
