import os
from PySide6.QtWidgets import QFileDialog, QMessageBox
from models.thread_download_single import DownloadThread
from models.thread_download_playlist import PlaylistDownloadThread
from controllers.download_dialog_controller import DownloadDialog

class DownloadHandler:
    def __init__(self, main_window):
        self.main = main_window
        self.ui = main_window.ui

    def _get_settings(self):
        """Trả về settings_manager từ main window nếu có."""
        return getattr(self.main, 'settings_manager', None)

    def start_single_download_with_dialog(self, url, path, opt, quality, title, initial_pixmap=None, initial_thumb_url=None):
        thread = DownloadThread(url, path, opt, quality)

        dialog = DownloadDialog(
            parent=self.main,
            title=title,
            is_playlist=False,
            thread=thread,
            initial_pixmap=initial_pixmap,
            initial_thumb_url=initial_thumb_url,
            video_title=title
        )

        thread.start()
        dialog.exec()

    def handle_single_download(self):
        url = self.ui.enterPlace.text().strip()
        opt = self.ui.comboBoxDownloadOption.currentText()
        if not url:
            return

        safe_title = self.main.clean_filename(self.main.current_video_title)
        sm = self._get_settings()
        use_default = sm.get("use_default_path", False) if sm else False
        default_path = sm.get("download_path", "") if sm else ""

        if use_default and default_path and os.path.isdir(default_path):
            # Dùng đường dẫn mặc định — không hỏi người dùng
            ext = ".mp4" if opt == "MP4" else ".mp3"
            path = os.path.join(default_path, safe_title + ext)
        else:
            # Hỏi người dùng chọn nơi lưu
            if opt == "MP4":
                path, _ = QFileDialog.getSaveFileName(self.main, "Lưu Video", safe_title, "Video Files (*.mp4)")
            else:
                path, _ = QFileDialog.getSaveFileName(self.main, "Lưu Nhạc", safe_title, "Audio Files (*.mp3)")

        if not path:
            return

        self.ui.enterPlace.setEnabled(False)
        self.ui.statusbar.showMessage("Đang tải video...")

        try:
            pixmap = self.ui.videoImg.pixmap()
            self.start_single_download_with_dialog(
                url, path, opt,
                self.ui.comboBoxDownloadQuality.currentText(),
                self.main.current_video_title,
                initial_pixmap=pixmap
            )
        finally:
            self.ui.enterPlace.setEnabled(True)
            self.ui.enterPlace.clear()
            self.ui.linkName.clear()
            self.ui.statusbar.showMessage("Sẵn sàng", 5000)

    def handle_download_all(self):
        total_widgets = 0
        for i in range(self.main.scroll_layout.count()):
            w = self.main.scroll_layout.itemAt(i).widget()
            if hasattr(w, 'get_download_info'):
                total_widgets += 1

        if total_widgets == 0:
            QMessageBox.warning(self.main, "Cảnh báo", "Vui lòng nhập link Playlist và bấm Find trước!")
            return

        items = []
        for i in range(self.main.scroll_layout.count()):
            w = self.main.scroll_layout.itemAt(i).widget()
            if hasattr(w, 'get_download_info'):
                if hasattr(w, 'ui') and hasattr(w.ui, 'checkBoxDownload') and w.ui.checkBoxDownload.isChecked():
                    items.append(w.get_download_info())

        if not items:
            QMessageBox.warning(self.main, "Cảnh báo", "Vui lòng chọn ít nhất một video để tải!")
            return

        sm = self._get_settings()
        use_default = sm.get("use_default_path", False) if sm else False
        default_path = sm.get("download_path", "") if sm else ""

        if use_default and default_path and os.path.isdir(default_path):
            root_dir = default_path
        else:
            root_dir = QFileDialog.getExistingDirectory(self.main, "Chọn thư mục lưu Playlist")

        if not root_dir:
            return

        safe_title = self.main.clean_filename(self.main.current_video_title)
        if not safe_title:
            safe_title = "Downloaded_Playlist"

        # Tạo subfolder nếu cài đặt bật
        create_sub = sm.get("create_subfolder_for_playlist", True) if sm else True
        if create_sub:
            save_path = os.path.join(root_dir, safe_title)
        else:
            save_path = root_dir
        os.makedirs(save_path, exist_ok=True)

        self.ui.downloadAllBtn.setEnabled(False)
        self.ui.downloadAllBtn.setText("Đang tải...")

        thread = PlaylistDownloadThread(items, save_path)

        dialog = DownloadDialog(
            parent=self.main,
            title=self.main.current_video_title,
            is_playlist=True,
            thread=thread,
            video_title="Starting playlist download..."
        )

        thread.start()

        try:
            dialog.exec()
        finally:
            self.ui.downloadAllBtn.setEnabled(True)
            self.main.update_download_all_btn_text()
            self.ui.statusbar.showMessage("Sẵn sàng", 5000)

            # Mở thư mục sau khi tải nếu cài đặt bật
            open_after = sm.get("open_folder_after_download", False) if sm else False
            if open_after and os.path.isdir(save_path):
                import subprocess
                subprocess.Popen(f'explorer "{save_path}"')
