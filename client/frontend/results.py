from PyQt6 import QtCore, QtGui, QtWidgets
from server.services.auth import user_auth_controller

user_auth_controller = user_auth_controller()


class Ui_Results_Dialog(object):
    def setupUi(self, Results_Dialog):
        Results_Dialog.setObjectName("Results_Dialog")
        Results_Dialog.resize(800, 600)
        self.verticalLayout = QtWidgets.QVBoxLayout(Results_Dialog)
        self.verticalLayout.setObjectName("verticalLayout")

        # Title label
        self.title_label = QtWidgets.QLabel(Results_Dialog)
        self.title_label.setObjectName("title_label")
        self.title_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.title_label.setText("<h2>User Search Results</h2>")
        self.verticalLayout.addWidget(self.title_label)

        # Found users label
        self.found_users_label = QtWidgets.QLabel(Results_Dialog)
        self.found_users_label.setObjectName("found_users_label")
        self.found_users_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.found_users_label.setText("<p>Found Users: 0</p>")
        self.verticalLayout.addWidget(self.found_users_label)

        self.scrollArea = QtWidgets.QScrollArea(Results_Dialog)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Preferred,
            QtWidgets.QSizePolicy.Policy.Expanding,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 780, 580))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)

        # Button box
        self.button_box = QtWidgets.QDialogButtonBox(Results_Dialog)
        self.button_box.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.button_box.setStandardButtons(
            QtWidgets.QDialogButtonBox.StandardButton.Cancel
        )
        self.button_box.setObjectName("button_box")
        self.verticalLayout.addWidget(self.button_box)

        self.retranslateUi(Results_Dialog)
        self.button_box.accepted.connect(Results_Dialog.accept)
        self.button_box.rejected.connect(Results_Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Results_Dialog)

    def retranslateUi(self, Results_Dialog):
        _translate = QtCore.QCoreApplication.translate
        Results_Dialog.setWindowTitle(
            _translate("Results_Dialog", "User Search Results")
        )
        self.title_label.setText(
            _translate("Results_Dialog", "<h2>User Search Results</h2>")
        )
        self.found_users_label.setText(
            _translate("Results_Dialog", "<p>Found Users: 0</p>")
        )


class ResultsWindow(QtWidgets.QDialog):
    def __init__(self, json_data):
        super().__init__()

        self.ui = Ui_Results_Dialog()
        self.ui.setupUi(self)

        self.display_user_info(json_data)

    def display_user_info(self, json_data):
        similar_users = json_data.get("similar_users", [])
        num_users = len(similar_users)
        self.ui.found_users_label.setText(f"<p>Found Users: {num_users}</p>")

        for idx, user_info in enumerate(similar_users):
            if idx > 0:
                # Add horizontal line
                line = QtWidgets.QFrame()
                line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
                line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
                self.ui.verticalLayout_2.addWidget(line)
            user_widget = QtWidgets.QWidget()
            user_layout = QtWidgets.QVBoxLayout(user_widget)

            if user_info.get("id_image", ""):
                # Add image (example)
                user_info_image = user_auth_controller.display_image(
                    user_info.get("id_user", "")
                )
                image_label = QtWidgets.QLabel()
                image_label.setScaledContents(True)
                image_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                pixmap = QtGui.QPixmap()
                pixmap.loadFromData(user_info_image)
                scaled_pixmap = pixmap.scaled(
                    image_label.size(),
                    QtCore.Qt.AspectRatioMode.KeepAspectRatio,
                    QtCore.Qt.TransformationMode.SmoothTransformation,
                )
                image_label.setPixmap(scaled_pixmap)
                user_layout.addWidget(image_label)
            else:
                # Add image (example)
                pixmap = QtGui.QPixmap(
                    r"C:\Users\phatl\OneDrive - VNU-HCMUS\Desktop\relative_face_recognition_app\client\frontend\ui\picture\demo_ava.jpg"
                )
                image_label = QtWidgets.QLabel()
                image_label.setPixmap(pixmap)
                image_label.setScaledContents(True)
                image_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                user_layout.addWidget(image_label)

            info_layout = QtWidgets.QVBoxLayout()

            full_name_label = QtWidgets.QLabel(
                f"<b>Họ và Tên:</b> {user_info.get('full_name', '')}"
            )
            info_layout.addWidget(full_name_label)

            gender_label = QtWidgets.QLabel(
                f"<b>Giới tính:</b> {user_info.get('gender', '')}"
            )
            info_layout.addWidget(gender_label)

            age_label = QtWidgets.QLabel(f"<b>Tuổi tác:</b> {user_info.get('age', '')}")
            info_layout.addWidget(age_label)

            city_label = QtWidgets.QLabel(
                f"<b>Quê quán:</b> {user_info.get('id_ward', '')}, {user_info.get('id_district', '')}, {user_info.get('id_city', '')}, {user_info.get('id_country', '')}"
            )
            info_layout.addWidget(city_label)

            feat_label = QtWidgets.QLabel(
                f"<b>Đặc điểm nhận dạng:</b> {user_info.get('face_feature', '')}"
            )
            info_layout.addWidget(feat_label)

            user_layout.addLayout(info_layout)

            user_layout.setContentsMargins(20, 20, 20, 20)
            user_layout.setSpacing(20)

            self.ui.verticalLayout_2.addWidget(user_widget)
