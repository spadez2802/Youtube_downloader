import re
from PySide6.QtWidgets import (
    QWidget, QFileDialog, QMessageBox, QSizePolicy, QMenu, QStyleOption, QStyle
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap, QGuiApplication, QPainter, QAction

# --- IMPORT VIEW (GIAO DIỆN) ---
from views.ui_config import Ui_VideoMini, Ui_HistorySidebar, Ui_HistoryDropdown

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
        self.thumb_url = thumb_url
        
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
            'quality': self.ui.comboBoxDQuality.currentText(),
            'thumbnail': self.thumb_url
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

            main_win = self.window()
            if hasattr(main_win, 'download_handler'):
                pixmap = self.ui.labelImg.pixmap()
                main_win.download_handler.start_single_download_with_dialog(
                    self.url, file_path, selected_option, quality_option, self.title, initial_pixmap=pixmap
                )
                self.ui.downloadVBtn.setText("Xong!")
            else:
                QMessageBox.critical(self, "Lỗi", "Không tìm thấy download handler của cửa sổ chính!")
            
        except Exception as e:
            QMessageBox.critical(self, "Lỗi Nút Download", f"Chi tiết lỗi:\n{str(e)}")
            print(f"Lỗi: {e}")
        finally:
            self.ui.downloadVBtn.setEnabled(True)


# ==========================================================
# WIDGET CARD LỊCH SỬ — SIDEBAR TRÁI
# (Di chuyển từ search_handler.py để tuân thủ MVC / High Cohesion)
# ==========================================================
class HistoryCard(QWidget):
    def __init__(self, title, url, time_str, parent_handler, item_type='video'):
        super().__init__()
        self.ui = Ui_HistorySidebar()
        self.ui.setupUi(self)

        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)

        self.url = url
        self.parent_handler = parent_handler

        # Dùng fontMetrics để tính toán chiều dài pixel chuẩn xác (~200px để tránh lỗi chữ hoa)
        fm = self.ui.labelName.fontMetrics()
        display_title = fm.elidedText(title, Qt.TextElideMode.ElideRight, 210)
        self.ui.labelName.setText(display_title)

        # --- Chỉ hiển thị giờ (HH:MM) ở labelDate ---
        time_only = ""
        if time_str:
            parts = time_str.strip().split(' ')
            if len(parts) >= 2:
                time_only = parts[1]
            else:
                time_only = time_str
        else:
            time_only = "Vừa xong"
        self.ui.labelDate.setText(time_only)
        self.ui.labelDate.setStyleSheet("color: #888888; font-size: 11px;")

        # --- Badge [Video] hoặc [Playlist] bên phải ---
        if item_type == 'playlist':
            badge_text = "[Playlist]"
            badge_color = "#1ED761"
        else:
            badge_text = "[Video]"
            badge_color = "#4A90D9"
        self.ui.labelType.setText(badge_text)
        self.ui.labelType.setStyleSheet(
            f"color: {badge_color}; font-size: 10px; font-weight: bold; "
            f"background: transparent; padding: 1px 3px; "
            f"border: 1px solid {badge_color}; border-radius: 3px;"
        )

        self.ui.labelName.setWordWrap(True)
        self.ui.labelName.setMaximumHeight(34)

        policy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        self.ui.labelName.setSizePolicy(policy)
        self.ui.labelName.setMinimumHeight(0)
        self.ui.widget.setMinimumHeight(0)
        self.setMinimumHeight(0)

        self.setStyleSheet("""
            HistoryCard:hover {
                background-color: #3e3e3e;
                border-radius: 4px;
            }
        """)

        self.ui.labelName.setCursor(Qt.CursorShape.PointingHandCursor)
        self.ui.labelDate.setCursor(Qt.CursorShape.PointingHandCursor)
        self.ui.cbbOpt.setCursor(Qt.CursorShape.PointingHandCursor)

        # Thiết lập QMenu cho QToolButton
        self.opt_menu = QMenu(self)
        self.act_copy = QAction("Copy link", self)
        self.act_delete = QAction("Delete from history", self)
        self.opt_menu.addAction(self.act_copy)
        self.opt_menu.addAction(self.act_delete)
        self.ui.cbbOpt.setMenu(self.opt_menu)

        self.act_copy.triggered.connect(self.copy_url)
        self.act_delete.triggered.connect(self.delete_item)

        self.ui.labelName.mousePressEvent = self.on_text_clicked
        self.ui.labelDate.mousePressEvent = self.on_text_clicked

    def on_text_clicked(self, event):
        self.parent_handler.load_history_url(self.url)

    def delete_item(self):
        self.parent_handler.delete_history_item(self.url)

    def copy_url(self):
        clipboard = QGuiApplication.clipboard()
        clipboard.setText(self.url)
        self.parent_handler.main.ui.statusbar.showMessage("Đã sao chép liên kết vào Clipboard!", 2000)

    def paintEvent(self, event):
        opt = QStyleOption()
        opt.initFrom(self)
        p = QPainter(self)
        self.style().drawPrimitive(QStyle.PrimitiveElement.PE_Widget, opt, p, self)


# ==========================================================
# WIDGET LỊCH SỬ — AUTOCOMPLETE DROPDOWN
# (Di chuyển từ search_handler.py để tuân thủ MVC / High Cohesion)
# ==========================================================
class HistoryItemWidget(QWidget):
    def __init__(self, title, url, parent_handler):
        super().__init__()
        self.ui = Ui_HistoryDropdown()
        self.ui.setupUi(self)

        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setStyleSheet("background: transparent;")

        self.url = url
        self.parent_handler = parent_handler

        self.ui.label.setText(title)
        self.ui.label.setAttribute(Qt.WidgetAttribute.WA_TransparentForMouseEvents)

        self.ui.deleteHistoryBtn.setCursor(Qt.CursorShape.PointingHandCursor)
        self.ui.deleteHistoryBtn.clicked.connect(self.delete_item)

    def delete_item(self):
        self.parent_handler.delete_history_item(self.url)
