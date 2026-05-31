import os
from PySide6.QtWidgets import QFileDialog, QMessageBox
from models.thread_download_single import DownloadThread
from models.thread_download_playlist import PlaylistDownloadThread
from controllers.download_dialog_controller import DownloadDialog

class DownloadHandler:
    def __init__(self, main_window):
        self.main = main_window
        self.ui = main_window.ui

    def start_single_download_with_dialog(self, url, path, opt, quality, title, initial_pixmap=None, initial_thumb_url=None):
        thread = DownloadThread(url, path, opt, quality)
        
        dialog = DownloadDialog(
            parent=self.main,
            title=title, # dialog window title is video name
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
        if not url: return
        
        safe_title = self.main.clean_filename(self.main.current_video_title)
        
        if opt == "MP4":
            path, _ = QFileDialog.getSaveFileName(self.main, "Lưu Video", safe_title, "Video Files (*.mp4)")
        else:
            path, _ = QFileDialog.getSaveFileName(self.main, "Lưu Nhạc", safe_title, "Audio Files (*.mp3)")
            
        if not path: return

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
        
        root_dir = QFileDialog.getExistingDirectory(self.main, "Chọn thư mục lưu Playlist")
        if not root_dir: return
        
        safe_title = self.main.clean_filename(self.main.current_video_title)
        if not safe_title: safe_title = "Downloaded_Playlist"
        
        save_path = os.path.join(root_dir, safe_title)
        os.makedirs(save_path, exist_ok=True)

        self.ui.downloadAllBtn.setEnabled(False)
        self.ui.downloadAllBtn.setText("Đang tải...") 

        thread = PlaylistDownloadThread(items, save_path)
        
        dialog = DownloadDialog(
            parent=self.main,
            title=self.main.current_video_title, # playlist title
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