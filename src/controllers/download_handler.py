import os
from PySide6.QtWidgets import QFileDialog, QMessageBox
from models.thread_download_single import DownloadThread
from models.thread_download_playlist import PlaylistDownloadThread

class DownloadHandler:
    def __init__(self, main_window):
        self.main = main_window
        self.ui = main_window.ui

    def handle_single_download(self):
        url = self.ui.enterPlace.text().strip()
        opt = self.ui.comboBoxDownloadOption.currentText()
        if not url: return
        
        # --- KHÔI PHỤC LÀM SẠCH TÊN FILE ---
        safe_title = self.main.clean_filename(self.main.current_video_title)
        
        # --- KHÔI PHỤC BỘ LỌC FILE ---
        if opt == "MP4":
            path, _ = QFileDialog.getSaveFileName(self.main, "Lưu Video", safe_title, "Video Files (*.mp4)")
        else:
            path, _ = QFileDialog.getSaveFileName(self.main, "Lưu Nhạc", safe_title, "Audio Files (*.mp3)")
            
        if not path: return

        # --- KHÔI PHỤC TRẠNG THÁI UI ---
        self.ui.enterPlace.setEnabled(False)
        self.ui.statusbar.showMessage("Đang tải video...")

        self.dl_thread = DownloadThread(url, path, opt, self.ui.comboBoxDownloadQuality.currentText())
        self.dl_thread.finished.connect(self.on_dl_single_success)
        self.dl_thread.error.connect(self.on_dl_single_fail)
        self.dl_thread.start()

    def on_dl_single_success(self, path):
        self.ui.enterPlace.setEnabled(True)
        self.ui.enterPlace.clear()
        self.ui.linkName.clear()
        QMessageBox.information(self.main, "Xong!", f"Đã tải về:\n{path}")
        self.ui.statusbar.showMessage("Sẵn sàng", 5000)

    def on_dl_single_fail(self, msg):
        self.ui.enterPlace.setEnabled(True)
        QMessageBox.critical(self.main, "Lỗi", f"Thất bại: {msg}")
        self.ui.statusbar.showMessage("Lỗi tải video")

    def handle_download_all(self):
        items = []
        for i in range(self.main.scroll_layout.count()):
            w = self.main.scroll_layout.itemAt(i).widget()
            if hasattr(w, 'get_download_info'): items.append(w.get_download_info())
            
        if not items: 
            QMessageBox.warning(self.main, "Cảnh báo", "Vui lòng nhập link Playlist và bấm Find trước!")
            return
        
        root_dir = QFileDialog.getExistingDirectory(self.main, "Chọn thư mục lưu Playlist")
        if not root_dir: return
        
        safe_title = self.main.clean_filename(self.main.current_video_title)
        if not safe_title: safe_title = "Downloaded_Playlist"
        
        save_path = os.path.join(root_dir, safe_title)
        os.makedirs(save_path, exist_ok=True)

        self.ui.downloadAllBtn.setEnabled(False)
        self.ui.downloadAllBtn.setText("Đang tải...") 
        self.ui.widget_7.setVisible(True)
        self.ui.label_2.setText("Đang chuẩn bị dữ liệu...")
        self.ui.progressBar.setValue(0)

        self.pl_thread = PlaylistDownloadThread(items, save_path)
        self.pl_thread.progress_update.connect(self.ui.progressBar.setValue)
        self.pl_thread.status_update.connect(self.ui.label_2.setText)
        self.pl_thread.finished.connect(self.on_dl_all_success)
        self.pl_thread.error.connect(self.on_dl_all_fail)
        self.pl_thread.start()

    def on_dl_all_success(self, path):
        self.ui.downloadAllBtn.setEnabled(True)
        self.ui.downloadAllBtn.setText("Download ALL") 
        self.ui.label_2.setText("Hoàn tất!")
        self.ui.progressBar.setValue(100)
        QMessageBox.information(self.main, "Xong!", f"Đã tải thành công toàn bộ playlist vào:\n{path}")
        self.ui.statusbar.showMessage("Tải playlist xong!", 5000)
        self.ui.widget_7.setVisible(False)
        
    def on_dl_all_fail(self, msg):
        self.ui.downloadAllBtn.setEnabled(True)
        self.ui.downloadAllBtn.setText("Download ALL")
        self.ui.label_2.setText("Lỗi tải xuống!")
        QMessageBox.critical(self.main, "Lỗi", f"Thất bại trong quá trình tải:\n{msg}")