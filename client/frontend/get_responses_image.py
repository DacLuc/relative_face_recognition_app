from PyQt6.QtWidgets import QFileDialog, QMainWindow, QApplication, QProgressDialog
from PyQt6.QtCore import Qt, QTimer, QCoreApplication
import os


class Ui_Get_Response(QMainWindow):
    _progress = None  # Class attribute to store the QProgressDialog instance

    def __init__(self):
        super().__init__()

    def get_response_upload_pic_with_progress(self, progress):
        self._progress = progress  # Store the QProgressDialog instance
        file_filter = "Image File (*.png *.jpg *.jpeg)"
        response = QFileDialog.getOpenFileName(
            parent=self,
            caption="Select a file",
            directory=os.getcwd(),
            filter=file_filter,
            initialFilter="Image File (*.png *.jpg *.jpeg)",
        )
        responses = response[0]

        if responses:  # If a file is selected
            self._progress.setWindowTitle("Uploading")
            self._progress.setWindowModality(Qt.WindowModality.WindowModal)
            self._progress.setMinimumDuration(0)
            self._progress.setValue(0)
            self._progress.show()

            def upload_image():
                nonlocal progress
                total_steps = 100
                step = 0

                def update_progress():
                    nonlocal step
                    self._progress.setValue(step)
                    QApplication.processEvents()

                def finish_upload():
                    nonlocal progress
                    if self._progress is not None and self._progress.isVisible():
                        self._progress.setValue(total_steps)
                        self._progress.accept()

                def simulate_upload():
                    nonlocal step
                    if step <= total_steps and not (
                        self._progress is None
                        or not self._progress.isVisible()
                        or self._progress.wasCanceled()
                    ):
                        update_progress()
                        step += 1
                        QTimer.singleShot(10, simulate_upload)
                    else:
                        finish_upload()

                simulate_upload()

            # Start the upload process
            QTimer.singleShot(10, upload_image)

            result = self._progress.exec()
            if (
                self._progress is not None
                and self._progress.isVisible()
                and self._progress.wasCanceled()
            ):
                self._progress.close()
                return None
            else:
                return responses
        else:
            print("No file selected")
            return None
