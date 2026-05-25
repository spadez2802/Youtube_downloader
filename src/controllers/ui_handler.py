from PySide6.QtCore import Qt, QPropertyAnimation, QEasingCurve, QSize
from PySide6.QtWidgets import QFrame, QSizePolicy
from PySide6.QtGui import QIcon # --- CẦN IMPORT THÊM QICON ---
from utils.helpers import get_asset_path

class UIHandler:
    def __init__(self, main_window):
        self.main = main_window
        self.ui = main_window.ui

    def setup_styling(self):
        # --- FIX 1: LÀM MẤT CHỮ MAINWINDOW Ở GÓC TRÁI ---
        # Chúng ta đặt tiêu đề cửa sổ thành một chuỗi rỗng
        self.main.setWindowTitle("TheDownloader")

        # --- FIX 2: THÊM LOGO APP (GÓC TRÁI MÀN HÌNH & TASKBAR) ---
        # Zun hãy kiểm tra xem trong thư mục img/icon/ đã có file logo chưa nhé.
        # Mình giả định file logo tên là 'app_logo.png' nằm trong img/icon/.
        # Nếu tên file khác, bạn hãy sửa lại dòng dưới đây cho khớp.
        app_icon_path = get_asset_path("img/icon/app_logo.png")
        self.main.setWindowIcon(QIcon(app_icon_path))

        # --- FIX 3: KHÔI PHỤC MÀU SẮC VÀ KÍCH THƯỚC NÚT SIDEBAR ---
        # Ép CSS cho nút sidebar to, đậm, màu xanh lục bảo đặc trưng
        self.ui.miniSideBarBtn.setStyleSheet("""
            QPushButton { 
                color: #1ED761; 
                font-size: 28px; 
                font-weight: bold; 
                background: transparent; 
                border: none; 
                padding: 0px;
                margin: 0px;
            }
            QPushButton:hover { color: white; }
            QPushButton:disabled { color: #555; } /* Màu xám khi bị khóa */
        """)

        # (Giữ nguyên các phần styling khác...)
        self.main.setCursor(Qt.CursorShape.ArrowCursor)
        self.ui.centralwidget.setCursor(Qt.CursorShape.ArrowCursor)
        self.ui.scrollArea.setWidgetResizable(True)
        self.ui.scrollArea.setFrameShape(QFrame.NoFrame)
        self.ui.scrollArea.setStyleSheet("QScrollArea { border: none; background: transparent; }")
        
        self.ui.clearBtn.setText("✕") 
        self.ui.clearBtn.setStyleSheet("""
            QPushButton { background: transparent; color: #888; font-size: 18px; font-weight: bold; border: none; }
            QPushButton:hover { color: #1ED761; }
        """)
        self.ui.clearBtn.setVisible(False) 

        arrow_icon = get_asset_path("img/icon/down_arrow.png")
        for combo in [self.ui.comboBoxDownloadOption, self.ui.comboBoxDownloadAllOpt]:
            combo.setStyleSheet(combo.styleSheet().replace("E:/design/ytb_playlist_downloader/img/icon/down_arrow.png", arrow_icon))

        qual_style = self.ui.comboBoxDownloadQuality.styleSheet().replace("E:/design/ytb_playlist_downloader/img/icon/down_arrow.png", arrow_icon)
        qual_style = qual_style.replace("#comboBoxDowloadQuality:disabled", "#comboBoxDownloadQuality:disabled")
        qual_style += "\n#comboBoxDownloadQuality::down-arrow:disabled { image: none; }"
        self.ui.comboBoxDownloadQuality.setStyleSheet(qual_style)

        # Mở khóa chiều cao và ép lề (Giữ nguyên)
        self.main.setMaximumHeight(16777215)
        self.ui.centralwidget.setMaximumHeight(16777215)
        self.ui.widget_3.setMaximumHeight(16777215) 
        self.ui.sideBarWidget.setMaximumHeight(16777215)
        self.ui.widget.setMaximumHeight(16777215)
        self.ui.widget_9.setMaximumHeight(16777215)
        self.ui.widget_6.setMaximumHeight(16777215)
        # --- FIX LỖI TÀNG HÌNH WIDGET CON (BỔ SUNG 2 DÒNG NÀY) ---
        self.ui.scrollArea.setMaximumSize(16777215, 16777215)
        self.ui.scrollAreaWidgetContents.setMaximumSize(16777215, 16777215)

        self.ui.horizontalLayout_2.setAlignment(self.ui.sideBarWidget, Qt.AlignmentFlag(0))
        self.ui.sideBarWidget.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        self.ui.horizontalLayout_2.setSpacing(0)
        self.ui.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.ui.horizontalLayout_2.insertStretch(1, 1)

        self.ui.verticalLayout_4.setAlignment(self.ui.scrollArea, Qt.AlignmentFlag(0))
        self.ui.scrollArea.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.ui.verticalLayout_4.setStretchFactor(self.ui.scrollArea, 1)

    def init_state(self):
        self.ui.widget_7.setVisible(False)
        self.ui.downloadAllBtn.setVisible(False)
        self.ui.comboBoxDownloadAllOpt.setVisible(False)
        self.ui.scrollArea.setVisible(False)
        self.ui.sideBarWidget.setMinimumWidth(50)
        self.ui.sideBarWidget.setMaximumWidth(50)

        # --- THÊM 3 DÒNG NÀY ĐỂ ÉP LISTWIDGET BIẾN MẤT HOÀN TOÀN ---
        self.ui.listWidget.setVisible(False)
        #self.ui.listWidget.setMinimumHeight(0)
        #self.ui.listWidget.setMaximumHeight(0)
        
        # --- FIX 4: ĐẶT MP4 LÀM ĐỊNH DẠNG MẶC ĐỊNH CHO MAIN COMBOBOX ---
        # Đảm bảo ComboBox chính luôn là MP4 lúc khởi động
        self.ui.comboBoxDownloadOption.setCurrentText("MP4")
        # Đặt luôn cho nút Download ALL cho đồng bộ
        self.ui.comboBoxDownloadAllOpt.setCurrentText("MP4")

        self.ui.miniSideBarBtn.setText("◀")
        self.main.resize(730, 650)
        
        self.ui.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.ui.verticalLayout_4.setSpacing(0)
        self.ui.miniSideBarBtn.setEnabled(False)

        self.ui.downloadBtn.setEnabled(False)
        self.ui.comboBoxDownloadOption.setEnabled(False)
        self.ui.comboBoxDownloadQuality.setEnabled(False)

    def toggle_sidebar(self):
        is_opening = self.ui.sideBarWidget.width() < 500
        new_width = 500 if is_opening else 50
        new_scroll_width = 500 if is_opening else 50
        new_window_w = self.main.width() + (450 if is_opening else -450)

        self.ui.downloadAllBtn.setVisible(is_opening)
        self.ui.comboBoxDownloadAllOpt.setVisible(is_opening)
        self.ui.scrollArea.setVisible(is_opening)
        
        # Cập nhật mũi tên
        self.ui.miniSideBarBtn.setText("▶" if is_opening else "◀")

        # --- KHÔI PHỤC 5 HOẠT ẢNH CHẠY SONG SONG ĐỂ GIAO DIỆN MƯỢT MÀ ---
        self.anim_side_min = QPropertyAnimation(self.ui.sideBarWidget, b"minimumWidth")
        self.anim_side_max = QPropertyAnimation(self.ui.sideBarWidget, b"maximumWidth")
        self.anim_window = QPropertyAnimation(self.main, b"size")
        self.anim_scroll = QPropertyAnimation(self.ui.scrollArea, b"minimumWidth")
        self.anim_content = QPropertyAnimation(self.ui.scrollAreaWidgetContents, b"minimumWidth")
        
        animations = [self.anim_side_min, self.anim_side_max, self.anim_window, self.anim_scroll, self.anim_content]
        
        for anim in animations:
            anim.setDuration(300)
            anim.setEasingCurve(QEasingCurve.InOutQuart)

        self.anim_side_min.setEndValue(new_width)
        self.anim_side_max.setEndValue(new_width)
        self.anim_window.setEndValue(QSize(new_window_w, self.main.height()))
        self.anim_scroll.setEndValue(new_scroll_width)
        self.anim_content.setEndValue(new_scroll_width)

        for anim in animations:
            anim.start()