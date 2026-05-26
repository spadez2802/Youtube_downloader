import re
from PySide6.QtWidgets import QWidget, QFileDialog, QMessageBox
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap

# --- IMPORT VIEW (GIAO DIỆN) ---
# Đảm bảo bạn đã di chuyển file ui_video_ver... vào trong thư mục views
from views.ui_video_ver6_1 import Ui_miniCard as Ui_VideoMini 

# --- IMPORT MODELS (LUỒNG XỬ LÝ) ---
from models.thread_thumbnail import ThumbnailThread
from models.thread_download_single import DownloadThread

# --- IMPORT UTILS (HÀM PHỤ TRỢ) ---
from utils.helpers import get_asset_path

class VideoItemWidget(QWidget):
    def __init__(self, title, url, thumb_url):
        super().__init__()
        self.ui = Ui_VideoMini()
        self.ui.setupUi(self)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.url = url
        self.title = title 
        
        # --- FIX KÍCH THƯỚC THUMBNAIL TO VÀ CỐ ĐỊNH ---
        self.ui.labelImg.setFixedSize(150, 100)

        display_title = title if len(title) < 40 else title[:37] + "..."
        self.ui.labelName.setText(display_title)
        self.ui.labelName.setWordWrap(True) 
        
        # --- THÊM CHẤT LƯỢNG CHO TỪNG THẺ ---
        self.ui.comboBoxDQuality.addItems(["Best", "1080p", "720p", "480p", "360p", "Worst"])
        
        # Kết nối sự kiện thay đổi Option (MP3/MP4)
        self.ui.comboBoxDownloadOpt.currentTextChanged.connect(self.toggle_quality)
        
        # --- FIX 5: ĐẶT MP4 LÀM ĐỊNH DẠNG MẶC ĐỊNH CHO TỪNG THẺ MINI ---
        self.ui.comboBoxDownloadOpt.setCurrentText("MP4") 
        
        self.ui.downloadVBtn.clicked.connect(self.handle_download_single)

        # --- KẾT NỐI SỰ KIỆN CHECKBOX ---
        self.ui.checkBoxDownload.stateChanged.connect(self.update_controls_state)
        
        # Mặc định tất cả video sẽ được tick khi mới tìm thấy
        self.ui.checkBoxDownload.setChecked(True)
        self.update_controls_state()

        if thumb_url:
            self.ui.labelImg.setText("Đang tải...")
            self.thumb_thread = ThumbnailThread(thumb_url)
            self.thumb_thread.finished.connect(self.set_image)
            self.thumb_thread.start()
        else:
            self.ui.labelImg.setText("No Image")

        # --- FIX ĐƯỜNG DẪN ẢNH MŨI TÊN COMBOBOX CHO FILE .EXE ---
        arrow_icon = get_asset_path("img/icon/down_arrow.png")
        
        style_opt = self.ui.comboBoxDownloadOpt.styleSheet()
        style_opt = style_opt.replace("E:/design/ytb_playlist_downloader/img/icon/down_arrow.png", arrow_icon)
        self.ui.comboBoxDownloadOpt.setStyleSheet(style_opt)
        
        style_qual = self.ui.comboBoxDQuality.styleSheet()
        style_qual = style_qual.replace("E:/design/ytb_playlist_downloader/img/icon/down_arrow.png", arrow_icon)
        self.ui.comboBoxDQuality.setStyleSheet(style_qual)

    # Hàm cập nhật trạng thái các nút dựa trên Checkbox
    def update_controls_state(self):
        is_checked = self.ui.checkBoxDownload.isChecked()
        self.ui.downloadVBtn.setEnabled(is_checked)
        self.ui.comboBoxDownloadOpt.setEnabled(is_checked)
        self.toggle_quality(self.ui.comboBoxDownloadOpt.currentText())

    # Hàm ẩn/hiện nút chất lượng
    def toggle_quality(self, text):
        is_checked = self.ui.checkBoxDownload.isChecked()
        self.ui.comboBoxDQuality.setEnabled(is_checked and text != "MP3")

    # Hàm xuất dữ liệu cho Download ALL đọc
    def get_download_info(self):
        clean_name = re.sub(r'[\\/*?:"<>|]', '-', self.title)[:150].strip()
        return {
            'title': self.title,
            'clean_name': clean_name,
            'url': self.url,
            'type': self.ui.comboBoxDownloadOpt.currentText(),
            'quality': self.ui.comboBoxDQuality.currentText()
        }

    def set_image(self, img_data):
        pixmap = QPixmap()
        pixmap.loadFromData(img_data)
        if not pixmap.isNull():
            scaled_pixmap = pixmap.scaled(self.ui.labelImg.size(), Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
            self.ui.labelImg.setPixmap(scaled_pixmap)
            self.ui.labelImg.setAlignment(Qt.AlignmentFlag.AlignCenter)

    def handle_download_single(self):
        try:
            selected_option = self.ui.comboBoxDownloadOpt.currentText()
            quality_option = self.ui.comboBoxDQuality.currentText()
            
            clean_name = re.sub(r'[\\/*?:"<>|]', '-', self.title)[:150].strip()
            default_name = f"{clean_name}.mp4" if selected_option == "MP4" else f"{clean_name}.mp3"
            
            if selected_option == "MP4":
                file_path, _ = QFileDialog.getSaveFileName(self, "Lưu Video", default_name, "Video Files (*.mp4)")
            else:
                file_path, _ = QFileDialog.getSaveFileName(self, "Lưu Nhạc", default_name, "Audio Files (*.mp3)")
                
            if not file_path: return
            
            self.ui.downloadVBtn.setEnabled(False)
            self.ui.downloadVBtn.setText("Đang tải...")

            # Truyền thêm quality vào DownloadThread
            self.thread = DownloadThread(self.url, file_path, selected_option, quality_option)
            self.thread.finished.connect(self.on_dl_success)
            self.thread.error.connect(self.on_dl_fail)
            self.thread.start()
            
        except Exception as e:
            QMessageBox.critical(self, "Lỗi Nút Download", f"Chi tiết lỗi:\n{str(e)}")
            print(f"Lỗi: {e}")

    def on_dl_success(self, path):
        self.ui.downloadVBtn.setEnabled(True)
        self.ui.downloadVBtn.setText("Xong!")
        QMessageBox.information(self, "Xong!", f"Đã tải xong:\n{self.title}")

    def on_dl_fail(self, msg):
        self.ui.downloadVBtn.setEnabled(True)
        self.ui.downloadVBtn.setText("Lỗi")
        QMessageBox.critical(self, "Lỗi", f"Thất bại:\n{msg}")
