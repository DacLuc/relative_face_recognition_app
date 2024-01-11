from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QLineEdit,
    QVBoxLayout,
    QMainWindow,
    QLabel,
    QHBoxLayout,
    QPushButton,
    QButtonGroup,
)
from PyQt6 import QtCore

# Only needed for access to command line arguments
import sys


class SignUpWindow(QMainWindow):
    def __init__(self):
        super(SignUpWindow, self).__init__()

        self.setWindowTitle("Finding People")

        layout = QVBoxLayout()
        username_label = QLabel("Username: ")
        self.username = QLineEdit()
        email_label = QLabel("Email: ")
        self.email = QLineEdit()
        password_label = QLabel("Password: ")
        self.password = QLineEdit()
        self.password.setEchoMode(QLineEdit.EchoMode.Password)

        btn_layout = QHBoxLayout()
        cancel_btn = QPushButton("Cancel")
        cancel_btn.clicked.connect(self.cancel_btn_clicked)
        submit_btn = QPushButton("Sumbit")
        submit_btn.clicked.connect(self.submit_btn_clicked)
        btn_layout.addWidget(cancel_btn)
        btn_layout.addWidget(submit_btn)

        layout.addWidget(username_label)
        layout.addWidget(self.username)
        layout.addWidget(email_label)
        layout.addWidget(self.email)
        layout.addWidget(password_label)
        layout.addWidget(self.password)
        # layout.addLayout(btn_layout)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def cancel_btn_clicked(self):
        print("cancel btn clicked")

    def submit_btn_clicked(self):
        print("submit btn clicked")


app = QApplication(sys.argv)

signup_window = SignUpWindow()
signup_window.show()

app.exec()
