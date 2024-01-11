# from client.signup import SignUpWindow
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QVBoxLayout, QMainWindow, QLabel, QHBoxLayout, QPushButton, QButtonGroup, QRadioButton, QCheckBox
from PyQt6 import QtCore

# Only needed for access to command line arguments
import sys
sys.path.append("../../relative_face_recognition_app")


class HomeWindow(QMainWindow):
    def __init__(self):
        super(HomeWindow, self).__init__()

        layout = QVBoxLayout()
        # Show all user info

        # Allow people find me
        # self.isAllowed = QRadioButton("Allow people to find me!")
        self.is_allowed = QCheckBox("Allow people to find me!")
        self.upload_image = QPushButton("Upload images")

        # Upload image

        layout.addWidget(self.is_allowed)
        layout.addWidget(self.upload_image)
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
