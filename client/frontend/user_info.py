# Form implementation generated from reading ui file '.\ui\new_app.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Info_Users_Page(object):
    def setupUi(self, Info_Users_Page):
        Info_Users_Page.setObjectName("Info_Users_Page")
        Info_Users_Page.resize(1074, 555)
        Info_Users_Page.setDocumentMode(True)
        self.centralwidget = QtWidgets.QWidget(parent=Info_Users_Page)
        self.centralwidget.setObjectName("centralwidget")
        self.title_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.title_label.setGeometry(QtCore.QRect(350, 10, 371, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.title_label.setFont(font)
        self.title_label.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.title_label.setMouseTracking(True)
        self.title_label.setTabletTracking(True)
        self.title_label.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.title_label.setAutoFillBackground(False)
        self.title_label.setStyleSheet("background-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375 rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0, 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255, 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625 rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));\n"
"color: rgb(0, 0, 0);")
        self.title_label.setScaledContents(True)
        self.title_label.setWordWrap(True)
        self.title_label.setOpenExternalLinks(True)
        self.title_label.setObjectName("title_label")
        self.users_info = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.users_info.setGeometry(QtCore.QRect(20, 60, 1031, 391))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        self.users_info.setFont(font)
        self.users_info.setStyleSheet("color: rgb(170, 0, 0);\n"
"font: 700 9pt \"Segoe UI\";")
        self.users_info.setCheckable(False)
        self.users_info.setObjectName("users_info")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(parent=self.users_info)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(360, 40, 132, 30))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.sex_box = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.sex_box.setContentsMargins(0, 0, 0, 0)
        self.sex_box.setObjectName("sex_box")
        self.gioi_tinh_label = QtWidgets.QLabel(parent=self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        self.gioi_tinh_label.setFont(font)
        self.gioi_tinh_label.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 700 9pt \"Segoe UI\";")
        self.gioi_tinh_label.setObjectName("gioi_tinh_label")
        self.sex_box.addWidget(self.gioi_tinh_label)
        self.gioi_tinh_box = QtWidgets.QComboBox(parent=self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        self.gioi_tinh_box.setFont(font)
        self.gioi_tinh_box.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 9pt \"Segoe UI\";")
        self.gioi_tinh_box.setInsertPolicy(QtWidgets.QComboBox.InsertPolicy.NoInsert)
        self.gioi_tinh_box.setObjectName("gioi_tinh_box")
        self.gioi_tinh_box.addItem("")
        self.gioi_tinh_box.addItem("")
        icon = QtGui.QIcon.fromTheme("accessories-calculator")
        self.gioi_tinh_box.addItem(icon, "")
        self.gioi_tinh_box.setItemText(2, "")
        self.sex_box.addWidget(self.gioi_tinh_box)
        self.horizontalLayoutWidget = QtWidgets.QWidget(parent=self.users_info)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(640, 40, 171, 30))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.age_box = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.age_box.setContentsMargins(0, 0, 0, 0)
        self.age_box.setSpacing(2)
        self.age_box.setObjectName("age_box")
        self.age_landmark = QtWidgets.QLabel(parent=self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        self.age_landmark.setFont(font)
        self.age_landmark.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 700 9pt \"Segoe UI\";")
        self.age_landmark.setObjectName("age_landmark")
        self.age_box.addWidget(self.age_landmark)
        self.age_range = QtWidgets.QSpinBox(parent=self.horizontalLayoutWidget)
        self.age_range.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 9pt \"Segoe UI\";")
        self.age_range.setObjectName("age_range")
        self.age_box.addWidget(self.age_range)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(parent=self.users_info)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(10, 40, 231, 30))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.name_box = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.name_box.setContentsMargins(0, 0, 0, 0)
        self.name_box.setObjectName("name_box")
        self.ho_ten_label = QtWidgets.QLabel(parent=self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        self.ho_ten_label.setFont(font)
        self.ho_ten_label.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 700 9pt \"Segoe UI\";")
        self.ho_ten_label.setObjectName("ho_ten_label")
        self.name_box.addWidget(self.ho_ten_label)
        self.ho_ten = QtWidgets.QLineEdit(parent=self.horizontalLayoutWidget_3)
        self.ho_ten.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 9pt \"Segoe UI\";")
        self.ho_ten.setObjectName("ho_ten")
        self.name_box.addWidget(self.ho_ten)
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(parent=self.users_info)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(10, 220, 421, 101))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.face_feature = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.face_feature.setContentsMargins(0, 0, 0, 0)
        self.face_feature.setObjectName("face_feature")
        self.info_face_label = QtWidgets.QLabel(parent=self.horizontalLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        self.info_face_label.setFont(font)
        self.info_face_label.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 700 9pt \"Segoe UI\";")
        self.info_face_label.setObjectName("info_face_label")
        self.face_feature.addWidget(self.info_face_label)
        self.info_face_text = QtWidgets.QTextEdit(parent=self.horizontalLayoutWidget_4)
        self.info_face_text.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 9pt \"Segoe UI\";")
        self.info_face_text.setObjectName("info_face_text")
        self.face_feature.addWidget(self.info_face_text)
        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(parent=self.users_info)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(290, 340, 475, 28))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.allowed_finding = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.allowed_finding.setContentsMargins(0, 0, 0, 0)
        self.allowed_finding.setObjectName("allowed_finding")
        self.allowed_label = QtWidgets.QLabel(parent=self.horizontalLayoutWidget_5)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        self.allowed_label.setFont(font)
        self.allowed_label.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 700 9pt \"Segoe UI\";")
        self.allowed_label.setObjectName("allowed_label")
        self.allowed_finding.addWidget(self.allowed_label)
        self.is_allowed = QtWidgets.QCheckBox(parent=self.horizontalLayoutWidget_5)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        self.is_allowed.setFont(font)
        self.is_allowed.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 700 9pt \"Segoe UI\";")
        self.is_allowed.setObjectName("is_allowed")
        self.allowed_finding.addWidget(self.is_allowed)
        self.horizontalLayoutWidget_6 = QtWidgets.QWidget(parent=self.users_info)
        self.horizontalLayoutWidget_6.setGeometry(QtCore.QRect(640, 220, 284, 31))
        self.horizontalLayoutWidget_6.setObjectName("horizontalLayoutWidget_6")
        self.pic = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_6)
        self.pic.setContentsMargins(0, 0, 0, 0)
        self.pic.setObjectName("pic")
        self.upload_avatar_label = QtWidgets.QLabel(parent=self.horizontalLayoutWidget_6)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        self.upload_avatar_label.setFont(font)
        self.upload_avatar_label.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 700 9pt \"Segoe UI\";")
        self.upload_avatar_label.setObjectName("upload_avatar_label")
        self.pic.addWidget(self.upload_avatar_label)
        self.download_pic = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget_6)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        self.download_pic.setFont(font)
        self.download_pic.setStyleSheet("font: 9pt \"Segoe UI\";\n"
"color: rgb(0, 0, 0);")
        self.download_pic.setObjectName("download_pic")
        self.pic.addWidget(self.download_pic)
        self.horizontalLayoutWidget_8 = QtWidgets.QWidget(parent=self.users_info)
        self.horizontalLayoutWidget_8.setGeometry(QtCore.QRect(10, 100, 241, 30))
        self.horizontalLayoutWidget_8.setObjectName("horizontalLayoutWidget_8")
        self.nation_place = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_8)
        self.nation_place.setContentsMargins(0, 0, 4, 0)
        self.nation_place.setSpacing(2)
        self.nation_place.setObjectName("nation_place")
        self.nation_label = QtWidgets.QLabel(parent=self.horizontalLayoutWidget_8)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        self.nation_label.setFont(font)
        self.nation_label.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 700 9pt \"Segoe UI\";")
        self.nation_label.setObjectName("nation_label")
        self.nation_place.addWidget(self.nation_label)
        self.nation_box = QtWidgets.QComboBox(parent=self.horizontalLayoutWidget_8)
        self.nation_box.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 9pt \"Segoe UI\";")
        self.nation_box.setObjectName("nation_box")
        self.nation_box.addItem("")
        self.nation_place.addWidget(self.nation_box)
        self.horizontalLayoutWidget_11 = QtWidgets.QWidget(parent=self.users_info)
        self.horizontalLayoutWidget_11.setGeometry(QtCore.QRect(360, 160, 271, 30))
        self.horizontalLayoutWidget_11.setObjectName("horizontalLayoutWidget_11")
        self.ward_place = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_11)
        self.ward_place.setContentsMargins(0, 0, 0, 0)
        self.ward_place.setSpacing(2)
        self.ward_place.setObjectName("ward_place")
        self.ward_label = QtWidgets.QLabel(parent=self.horizontalLayoutWidget_11)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        self.ward_label.setFont(font)
        self.ward_label.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 700 9pt \"Segoe UI\";")
        self.ward_label.setObjectName("ward_label")
        self.ward_place.addWidget(self.ward_label)
        self.ward_box = QtWidgets.QComboBox(parent=self.horizontalLayoutWidget_11)
        self.ward_box.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 9pt \"Segoe UI\";")
        self.ward_box.setSizeAdjustPolicy(QtWidgets.QComboBox.SizeAdjustPolicy.AdjustToContents)
        self.ward_box.setObjectName("ward_box")
        self.ward_place.addWidget(self.ward_box)
        self.horizontalLayoutWidget_10 = QtWidgets.QWidget(parent=self.users_info)
        self.horizontalLayoutWidget_10.setGeometry(QtCore.QRect(10, 160, 241, 30))
        self.horizontalLayoutWidget_10.setObjectName("horizontalLayoutWidget_10")
        self.district_place = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_10)
        self.district_place.setContentsMargins(0, 0, 0, 0)
        self.district_place.setSpacing(2)
        self.district_place.setObjectName("district_place")
        self.district_label = QtWidgets.QLabel(parent=self.horizontalLayoutWidget_10)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        self.district_label.setFont(font)
        self.district_label.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 700 9pt \"Segoe UI\";")
        self.district_label.setObjectName("district_label")
        self.district_place.addWidget(self.district_label)
        self.district_box = QtWidgets.QComboBox(parent=self.horizontalLayoutWidget_10)
        self.district_box.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 9pt \"Segoe UI\";")
        self.district_box.setSizeAdjustPolicy(QtWidgets.QComboBox.SizeAdjustPolicy.AdjustToContents)
        self.district_box.setObjectName("district_box")
        self.district_place.addWidget(self.district_box)
        self.horizontalLayoutWidget_9 = QtWidgets.QWidget(parent=self.users_info)
        self.horizontalLayoutWidget_9.setGeometry(QtCore.QRect(360, 100, 274, 30))
        self.horizontalLayoutWidget_9.setObjectName("horizontalLayoutWidget_9")
        self.city_place = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_9)
        self.city_place.setContentsMargins(0, 0, 0, 0)
        self.city_place.setSpacing(2)
        self.city_place.setObjectName("city_place")
        self.city_label = QtWidgets.QLabel(parent=self.horizontalLayoutWidget_9)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        self.city_label.setFont(font)
        self.city_label.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 700 9pt \"Segoe UI\";")
        self.city_label.setObjectName("city_label")
        self.city_place.addWidget(self.city_label)
        self.city_box = QtWidgets.QComboBox(parent=self.horizontalLayoutWidget_9)
        self.city_box.setAcceptDrops(False)
        self.city_box.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 9pt \"Segoe UI\";")
        self.city_box.setInsertPolicy(QtWidgets.QComboBox.InsertPolicy.InsertAlphabetically)
        self.city_box.setSizeAdjustPolicy(QtWidgets.QComboBox.SizeAdjustPolicy.AdjustToContents)
        self.city_box.setObjectName("city_box")
        self.city_place.addWidget(self.city_box)
        self.horizontalLayoutWidget_7 = QtWidgets.QWidget(parent=self.centralwidget)
        self.horizontalLayoutWidget_7.setGeometry(QtCore.QRect(450, 460, 169, 31))
        self.horizontalLayoutWidget_7.setObjectName("horizontalLayoutWidget_7")
        self.exit_page = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_7)
        self.exit_page.setContentsMargins(0, 0, 0, 0)
        self.exit_page.setObjectName("exit_page")
        self.apply_button = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget_7)
        font = QtGui.QFont()
        font.setBold(True)
        self.apply_button.setFont(font)
        self.apply_button.setStyleSheet("color: rgb(85, 255, 255);\n"
"color: rgb(0, 0, 127);\n"
"background-color: rgb(255, 255, 255);")
        self.apply_button.setObjectName("apply_button")
        self.exit_page.addWidget(self.apply_button)
        self.cancel_button = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget_7)
        font = QtGui.QFont()
        font.setBold(True)
        self.cancel_button.setFont(font)
        self.cancel_button.setStyleSheet("color: rgb(170, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.cancel_button.setObjectName("cancel_button")
        self.exit_page.addWidget(self.cancel_button)
        Info_Users_Page.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=Info_Users_Page)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1074, 25))
        self.menubar.setObjectName("menubar")
        Info_Users_Page.setMenuBar(self.menubar)

        self.retranslateUi(Info_Users_Page)
        QtCore.QMetaObject.connectSlotsByName(Info_Users_Page)

    def retranslateUi(self, Info_Users_Page):
        _translate = QtCore.QCoreApplication.translate
        Info_Users_Page.setWindowTitle(_translate("Info_Users_Page", "MainWindow"))
        self.title_label.setText(_translate("Info_Users_Page", "<html><head/><body><p align=\"center\">ỨNG DỤNG TÌM NGƯỜI MUỐN GẶP</p></body></html>"))
        self.users_info.setTitle(_translate("Info_Users_Page", "THÔNG TIN NGƯỜI DÙNG"))
        self.gioi_tinh_label.setText(_translate("Info_Users_Page", "Giới tính"))
        self.gioi_tinh_box.setItemText(0, _translate("Info_Users_Page", "Nam"))
        self.gioi_tinh_box.setItemText(1, _translate("Info_Users_Page", "Nữ"))
        self.age_landmark.setText(_translate("Info_Users_Page", "Mốc tuổi"))
        self.ho_ten_label.setText(_translate("Info_Users_Page", "Họ và Tên"))
        self.ho_ten.setPlaceholderText(_translate("Info_Users_Page", "Họ và Tên"))
        self.info_face_label.setText(_translate("Info_Users_Page", "Đặc điểm nhận dạng"))
        self.info_face_text.setPlaceholderText(_translate("Info_Users_Page", "Nêu các đặc điểm gương mặt của bạn"))
        self.allowed_label.setText(_translate("Info_Users_Page", "Cho phép người dùng khác tìm kiếm thông tin của bạn"))
        self.is_allowed.setText(_translate("Info_Users_Page", "Allowed"))
        self.upload_avatar_label.setText(_translate("Info_Users_Page", "Upload hình ảnh cá nhân"))
        self.download_pic.setText(_translate("Info_Users_Page", "Upload"))
        self.nation_label.setText(_translate("Info_Users_Page", "Quốc gia"))
        self.nation_box.setPlaceholderText(_translate("Info_Users_Page", "Quốc gia"))
        self.nation_box.setItemText(0, _translate("Info_Users_Page", "Việt Nam"))
        self.ward_label.setText(_translate("Info_Users_Page", "Phường / Xã"))
        self.ward_box.setPlaceholderText(_translate("Info_Users_Page", "Phường / Xã"))
        self.district_label.setText(_translate("Info_Users_Page", "Quận / Huyện"))
        self.district_box.setPlaceholderText(_translate("Info_Users_Page", "Quận / Huyện"))
        self.city_label.setText(_translate("Info_Users_Page", "Thành phố / Tỉnh"))
        self.city_box.setPlaceholderText(_translate("Info_Users_Page", "Thành phố / Tỉnh"))
        self.apply_button.setText(_translate("Info_Users_Page", "APPLY"))
        self.cancel_button.setText(_translate("Info_Users_Page", "CANCEL"))
