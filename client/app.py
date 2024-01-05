# from client.signup import SignUpWindow
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QVBoxLayout, QMainWindow, QLabel, QHBoxLayout, QPushButton, QButtonGroup, QFrame, QFileDialog
from PyQt6 import QtCore
from sqlmodel import Field, Session, SQLModel, create_engine
import requests

# Only needed for access to command line arguments
import sys
sys.path.append("../../relative_face_recognition_app")
from client.login import LoginWindow
from client.signup import SignUpWindow
from client.home import HomeWindow
from models.user import User
from database.engine import engine
from controllers.auth import UserAuth

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Finding People")
        self.login_wd = LoginWindow()
        self.signup_wd = SignUpWindow()
        self.home_wd = HomeWindow()

        self.btn_frame = QFrame()

        layout = QVBoxLayout()

        self.btn_layout = QHBoxLayout()
        self.cancel_btn = QPushButton("Cancel")
        self.cancel_btn.clicked.connect(self.cancel_btn_clicked)
        self.submit_btn = QPushButton("Login")
        self.submit_btn.clicked.connect(self.submit_btn_clicked)
        self.btn_layout.addWidget(self.cancel_btn)
        self.btn_layout.addWidget(self.submit_btn)

        self.register_label = QLabel("Don't have an account? Register now!")
        self.register_label.mousePressEvent = self.register_label_clicked

        self.btn_frame.setLayout(self.btn_layout)

        self.home_wd.upload_image.clicked.connect(self.upload_image_clicked)
        
        # layout.addLayout(self.login_wd)
        layout.addWidget(self.login_wd)
        layout.addWidget(self.signup_wd)
        layout.addWidget(self.home_wd)
        # layout.addLayout(self.btn_layout)
        layout.addWidget(self.btn_frame)
        layout.addWidget(self.register_label)

        self.signup_wd.hide()
        self.home_wd.hide()

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def cancel_btn_clicked(self):
        print("cancel btn clicked")

    def submit_btn_clicked(self):
        if self.signup_wd.isVisible():
            signup_username = self.signup_wd.username.text()
            signup_email = self.signup_wd.email.text()
            signup_password = self.signup_wd.password.text()
            print(signup_username, signup_email, signup_password)
            new_user = User(username=signup_username, email=signup_email, password=signup_password)
            # session = Session(engine)
            # session.add(new_user)
            # session.commit()
            # session.close()

            # backend
            with Session(engine) as session:
                session.add(new_user)
                session.commit()
        else:
            login_username = self.login_wd.username.text()
            login_password = self.login_wd.password.text()
            print(login_username, login_password)
            user = User(login_username, login_password)
            

            # controller
            URL = "http://localhost:8080/users/1"
            data = requests.get(url=URL)
            json_data = data.json()
            username = json_data['username']
            password = json_data['password']
            if (login_username == username) & (login_password == password):
                self.home_wd.show()
                self.login_wd.hide()
                self.signup_wd.hide()
                # self.btn_layout.hide()
                self.btn_frame.hide()
                self.register_label.hide()
            print("DATA: ", json_data)
        # print("submit btn clicked")

    def register_label_clicked(self, event):
        self.signup_wd.show()
        self.login_wd.hide()
        if self.signup_wd.isVisible():
            self.submit_btn.setText("Register")
            self.register_label.hide()
        else:
            self.submit_btn.setText("Login")
            self.register_label.show()

    def upload_image_clicked(self):
        self.upload_file = QFileDialog.getOpenFileNames(self, "Select image", ".")
        print(self.upload_file)


app = QApplication(sys.argv)

main_window = MainWindow()
main_window.show()

app.exec()
