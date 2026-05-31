import re
from PySide6.QtCore import Qt, QSize
from PySide6.QtWidgets import QDialog, QMessageBox
from PySide6.QtGui import QPixmap, QIcon
from views.ui_download_dialog_ver1_0 import Ui_Dialog
from models.thread_thumbnail import ThumbnailThread
from utils.helpers import get_asset_path

class DownloadDialog(QDialog):
    def __init__(self, parent, title, is_playlist, thread, initial_pixmap=None, initial_thumb_url=None, video_title=""):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setModal(True)
        
        self.thread = thread
        self.is_playlist = is_playlist
        self._is_closing_automatically = False
        self.thumb_thread = None

        # Set title
        self.setWindowTitle(title)
        
        # Set window icon matching the app
        app_icon_path = get_asset_path("img/icon/app_logo.png")
        self.setWindowIcon(QIcon(app_icon_path))

        # Setup controls styling & settings
        self.ui.btnPauseContinue.setText("Pause")
        self.ui.btnCancel.setText("Cancel")
        self.ui.progressBar.setValue(0)
        self.ui.videoName.setReadOnly(True)
        self.ui.labelThumbnail.setFixedSize(180, 120)
        self.ui.labelThumbnail.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.ui.labelThumbnail.setText("No Image")

        # Premium Dark theme styling matching the main app
        self.setStyleSheet("""
            QDialog {
                background-color: #2b2b2b;
                color: white;
            }
            QLabel {
                color: white;
                font-family: "Segoe UI", sans-serif;
                font-size: 11pt;
            }
            QTextEdit {
                background-color: black;
                color: white;
                border: 1px solid #1ED761;
                border-radius: 10px;
                padding: 8px;
                font-family: "Segoe UI", sans-serif;
                font-size: 11pt;
            }
            QProgressBar {
                border: 2px solid #1ED761;
                border-radius: 10px;
                background-color: #434343;
                color: white;
                text-align: center;
                font-weight: bold;
                height: 25px;
            }
            QProgressBar::chunk {
                background-color: #1ED761;
                border-radius: 8px;
            }
        """)

        # Set initial content
        if video_title:
            self.ui.videoName.setPlainText(video_title)
            
        if initial_pixmap and not initial_pixmap.isNull():
            scaled = initial_pixmap.scaled(self.ui.labelThumbnail.size(), Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
            self.ui.labelThumbnail.setPixmap(scaled)
        elif initial_thumb_url:
            self.fetch_thumbnail(initial_thumb_url)

        # Connect button actions
        self.ui.btnPauseContinue.clicked.connect(self.toggle_pause_resume)
        self.ui.btnCancel.clicked.connect(self.confirm_cancel)

        # Connect thread signals
        self.thread.progress_update.connect(self.ui.progressBar.setValue)
        self.thread.status_update.connect(self.on_status_update)
        self.thread.finished.connect(self.on_finished)
        self.thread.error.connect(self.on_error)
        
        if hasattr(self.thread, 'item_started'):
            self.thread.item_started.connect(self.on_item_started)

    def fetch_thumbnail(self, url):
        if not url:
            self.ui.labelThumbnail.setText("No Image")
            return
        self.ui.labelThumbnail.setText("Loading...")
        self.thumb_thread = ThumbnailThread(url)
        self.thumb_thread.finished.connect(self.set_thumbnail_image)
        self.thumb_thread.start()

    def set_thumbnail_image(self, img_data):
        pixmap = QPixmap()
        pixmap.loadFromData(img_data)
        if not pixmap.isNull():
            scaled = pixmap.scaled(self.ui.labelThumbnail.size(), Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
            self.ui.labelThumbnail.setPixmap(scaled)
        else:
            self.ui.labelThumbnail.setText("No Image")

    def on_item_started(self, item):
        # Update current playing title
        self.ui.videoName.setPlainText(item.get('title', 'Unknown'))
        # Fetch current thumbnail
        self.fetch_thumbnail(item.get('thumbnail'))

    def on_status_update(self, status):
        pass

    def toggle_pause_resume(self):
        if self.thread._is_paused:
            self.thread.resume()
            self.ui.btnPauseContinue.setText("Pause")
        else:
            self.thread.pause()
            self.ui.btnPauseContinue.setText("Continue")

    def confirm_cancel(self):
        # Was paused, keep download paused during question box
        already_paused = self.thread._is_paused
        if not already_paused:
            self.thread.pause()
            
        reply = QMessageBox.question(
            self, 
            "Cancel Download", 
            "Are you sure you want to cancel the download?", 
            QMessageBox.Yes | QMessageBox.No
        )
        
        if reply == QMessageBox.Yes:
            self.thread.cancel()
            self._is_closing_automatically = True
            self.reject()
        else:
            if not already_paused:
                self.thread.resume()
                self.ui.btnPauseContinue.setText("Pause")

    def on_finished(self, path):
        # English confirmation completed message
        QMessageBox.information(
            self, 
            "Completed", 
            "Download completed successfully!"
        )
        self._is_closing_automatically = True
        self.accept()

    def on_error(self, err_msg):
        self._is_closing_automatically = True
        if err_msg == "CANCELLED":
            self.reject()
        else:
            QMessageBox.critical(
                self, 
                "Error", 
                f"An error occurred during download:\n{err_msg}"
            )
            self.reject()

    def closeEvent(self, event):
        if self._is_closing_automatically:
            event.accept()
            return
            
        already_paused = self.thread._is_paused
        if not already_paused:
            self.thread.pause()
            
        reply = QMessageBox.question(
            self, 
            "Cancel Download", 
            "Are you sure you want to cancel the download?", 
            QMessageBox.Yes | QMessageBox.No
        )
        
        if reply == QMessageBox.Yes:
            self.thread.cancel()
            self._is_closing_automatically = True
            event.accept()
        else:
            if not already_paused:
                self.thread.resume()
                self.ui.btnPauseContinue.setText("Pause")
            event.ignore()
