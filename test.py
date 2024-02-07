import os
import sys
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QLabel,
    QVBoxLayout,
    QWidget,
    QFileDialog,
    QMessageBox,
)
from typing import List
from PyQt6.QtGui import QPixmap
from sqlmodel import SQLModel, create_engine, Session, select, Field
from sqlalchemy.exc import OperationalError
from face_recognition import compare_faces, face_encodings, load_image_file
from pgvector.sqlalchemy import Vector
from sqlalchemy import Column


class Image(SQLModel, table=True):
    __tablename__ = "images"
    id: int = Field(primary_key=True)
    embedding: List[float] = Field(sa_column=Column(Vector(5)))


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Face Similarity Detection")
        self.setGeometry(100, 100, 600, 400)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.upload_button = QPushButton("Upload Image")
        self.upload_button.clicked.connect(self.upload_image)
        self.layout.addWidget(self.upload_button)

        self.image_label = QLabel()
        self.layout.addWidget(self.image_label)

        self.result_label = QLabel()
        self.layout.addWidget(self.result_label)

        self.image_path = ""

    def upload_image(self):
        file_filter = "Image File (*.png *.jpg *.jpeg)"
        response = QFileDialog.getOpenFileName(
            parent=self,
            caption="Select a file",
            directory=os.getcwd(),
            filter=file_filter,
            initialFilter="Image File (*.png *.jpg *.jpeg)",
        )
        file_path = response[0]
        if file_path:
            self.image_path = file_path
            pixmap = QPixmap(file_path)
            self.image_label.setPixmap(pixmap)

            try:
                self.detect_similarity()
            except Exception as e:
                QMessageBox.warning(self, "Error", str(e))

    def detect_similarity(self):
        if not self.image_path:
            QMessageBox.warning(self, "Error", "Please upload an image first.")
            return

        new_encoding = face_encodings(load_image_file(self.image_path))
        if not new_encoding:
            QMessageBox.warning(
                self, "Error", "No face detected in the uploaded image."
            )
            return

        new_vector = new_encoding[0].tolist()

        engine = create_engine(os.environ["DATABASE_URL"])
        try:
            SQLModel.metadata.create_all(engine)
            with Session(engine) as session:
                results = session.exec(select(Image))
                for image in results:
                    if compare_faces([image.embedding], new_vector)[0]:
                        self.result_label.setText("Similarity Detected!")
                        return
                self.result_label.setText("No similarity detected.")
        except OperationalError:
            QMessageBox.warning(self, "Error", "Database connection failed.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
