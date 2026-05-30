import os
import re
from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QSizePolicy
from PySide6.QtCore import Qt

# --- IMPORT VIEW ---
from views.ui_main_ver8_5 import Ui_MainWindow
from views.custom_widgets import VideoItemWidget

# --- IMPORT MODELS ---
from models.history_manager import HistoryManager
from models.thread_network_checker import NetworkChecker

# --- IMPORT HANDLERS ---
from controllers.ui_handler import UIHandler
from controllers.search_handler import SearchHandler
from controllers.download_handler import DownloadHandler
from utils.helpers import get_asset_path, get_node_path, get_ffmpeg_path 

class MyDownloader(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # --- 1. KHAI BÁO CÁC BIẾN QUAN TRỌNG (Đã được khôi phục) ---
        node_path = get_node_path()
        self.YDL_OPTIONS = {
            'quiet': True, 'noplaylist': False, 'extract_flat': True,
            'remote_components': ['ejs:github'], 'skip_download': True,
            'allow_remote_scripts': True, 'check_formats': False
        }
        if node_path:
            self.YDL_OPTIONS['js_runtimes'] = {'node': {'path': node_path}}


        # --- 2. KHỞI TẠO MODEL & HANDLER ---
        self.history_manager = HistoryManager()
        self.history_data = self.history_manager.load_history()
        
        self.ui_handler = UIHandler(self)
        self.search_handler = SearchHandler(self)
        self.download_handler = DownloadHandler(self)
        
        # --- 3. GỌI HÀM KHỞI TẠO GIAO DIỆN VÀ KẾT NỐI ---
        self.init_data()
        self.ui_handler.setup_styling()
        self.ui_handler.init_state()
        self.setup_connections()

        # --- 4. KHỞI TẠO VÀ CHẠY LUỒNG KIỂM TRA MẠNG ---
        self.is_first_network_check = True
        self.network_checker = NetworkChecker()
        self.network_checker.connection_changed.connect(self.handle_connection_change)
        self.network_checker.start()

    # --- CÁC HÀM CƠ BẢN CỦA NHẠC TRƯỞNG ---
    def init_data(self):
        self.ui.label_2.setText("")
        self.ui.progressBar.setValue(0)
        self.scroll_layout = QVBoxLayout(self.ui.scrollAreaWidgetContents)
        self.scroll_layout.setSpacing(10)
        self.scroll_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.scroll_layout.setContentsMargins(0, 10, 0, 10)
        self.current_video_title = ""

    def setup_connections(self):
        self.ui.enterPlace.textChanged.connect(self.search_handler.on_text_changed)
        self.ui.findBtn.clicked.connect(self.search_handler.handle_find)
        self.ui.downloadBtn.clicked.connect(self.download_handler.handle_single_download)
        self.ui.downloadAllBtn.clicked.connect(self.download_handler.handle_download_all)
        self.ui.miniSideBarBtn.clicked.connect(self.ui_handler.toggle_sidebar)
        
        # Kết nối History & Text
        self.ui.clearBtn.clicked.connect(self.ui.enterPlace.clear)
        self.ui.listWidget.itemClicked.connect(self.search_handler.on_history_item_clicked)

        # Mở lịch sử khi click vào ô trống
        self.original_mouse_press = self.ui.enterPlace.mousePressEvent
        def custom_mouse_press(event):
            self.original_mouse_press(event) 
            self.search_handler.on_text_changed(self.ui.enterPlace.text())
        self.ui.enterPlace.mousePressEvent = custom_mouse_press

        # --- ĐỒNG BỘ COMBOBOX KHI ĐỔI MP3/MP4 (MỚI) ---
        def toggle_quality_btn(text):
            # Lấy trạng thái xem có phải đang ở playlist không (mặc định là False nếu chưa load)
            is_playlist = getattr(self, 'current_is_playlist', False)
            # Chỉ bật nếu chọn MP4 VÀ là video lẻ
            self.ui.comboBoxDownloadQuality.setEnabled(text == "MP4" and not is_playlist)
            
        self.ui.comboBoxDownloadOption.currentTextChanged.connect(toggle_quality_btn)
        
        # Cập nhật cho nút Download All
        self.ui.comboBoxDownloadAllOpt.currentTextChanged.connect(self.sync_all_download_options)
        

    # --- CÁC HÀM CÔNG CỤ DÙNG CHUNG CHO CÁC HANDLER ---
    def sync_all_download_options(self, text):
        for i in range(self.scroll_layout.count()):
            item = self.scroll_layout.itemAt(i)
            if item and item.widget() and isinstance(item.widget(), VideoItemWidget):
                item.widget().ui.comboBoxDownloadOpt.setCurrentText(text)

    def clean_filename(self, filename):
        clean_name = re.sub(r'[\\/*?:"<>|]', '-', filename)
        return clean_name[:150].strip()

    def clear_scroll_area(self):
        while self.scroll_layout.count():
            item = self.scroll_layout.takeAt(0)
            if item.widget(): item.widget().deleteLater()

    def update_download_all_btn_text(self):
        all_checked = True
        has_items = False
        for i in range(self.scroll_layout.count()):
            item = self.scroll_layout.itemAt(i)
            if item and item.widget() and isinstance(item.widget(), VideoItemWidget):
                has_items = True
                if not item.widget().ui.checkBoxDownload.isChecked():
                    all_checked = False
                    break
        
        if has_items and all_checked:
            self.ui.downloadAllBtn.setText("Download ALL")
        else:
            self.ui.downloadAllBtn.setText("Download")

    def handle_connection_change(self, is_online):
        if is_online:
            # Chuyển nền QMainWindow sang màu xanh Spotify
            self.setStyleSheet("QMainWindow { background-color: #1ED761; }")
            # Style text statusbar là màu đen và in đậm để nổi bật trên nền xanh
            self.ui.statusbar.setStyleSheet("QStatusBar { color: black; font-weight: bold; }")
            
            # Hiển thị log thông báo màu đen bằng tiếng anh trong 3 giây nếu không phải khởi động lần đầu
            if not self.is_first_network_check:
                self.ui.statusbar.showMessage("Internet connection restored", 3000)
            else:
                self.is_first_network_check = False
        else:
            # Chuyển nền QMainWindow sang màu xám như màu các khung widget (#2b2b2b)
            self.setStyleSheet("QMainWindow { background-color: #2b2b2b; }")
            # Thiết lập màu text statusbar là màu trắng
            self.ui.statusbar.setStyleSheet("QStatusBar { color: white; }")
            self.ui.statusbar.clearMessage()
            self.is_first_network_check = False

    def closeEvent(self, event):
        if hasattr(self, 'network_checker') and self.network_checker.isRunning():
            self.network_checker.stop()
        super().closeEvent(event)