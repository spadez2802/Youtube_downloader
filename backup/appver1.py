import sys
import yt_dlp
import re
import yt_dlp
import os
import json
from urllib.request import urlopen
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox, QWidget, QProgressBar, QLabel, QListWidgetItem, QPushButton, QSizePolicy
from PySide6.QtCore import QThread, Signal, QPropertyAnimation, QEasingCurve,  QSize
from PySide6.QtWidgets import QVBoxLayout,QFrame # Thêm import này
from urllib.request import urlopen, Request
from views.ui_video_ver5_7 import Ui_miniCard as Ui_VideoMini # Import giao diện thẻ mini
from backup.old_ui_main.ui_main_ver8 import Ui_MainWindow # Tên file .py bạn đã lưu

def get_asset_path(relative_path):
    """
    Hàm tự động lấy đường dẫn tuyệt đối cho tài nguyên (hình ảnh, icon...)
    - Khi chạy code bình thường: Tính từ thư mục gốc của project
    - Khi chạy file .exe: Lấy từ thư mục tạm _MEIPASS của PyInstaller
    """
    if getattr(sys, 'frozen', False):
        base_path = sys._MEIPASS
    else:
        # Code của bạn nằm trong thư mục src, nên lùi ra 1 cấp để đến thư mục chứa img
        base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        
    # Ép dấu chéo \ thành / để CSS của Qt đọc được mà không bị lỗi
    return os.path.join(base_path, relative_path).replace("\\", "/")

def get_format_string(quality_text):
    if quality_text in ["Best", "Best Quality"]:
        return 'bestvideo+bestaudio/best'
    elif quality_text in ["Worst", "Worst Quality"]:
        return 'worstvideo+worstaudio/worst'
    elif quality_text == "1080p": return 'bestvideo[height<=1080]+bestaudio/best'
    elif quality_text == "720p":  return 'bestvideo[height<=720]+bestaudio/best'
    elif quality_text == "480p":  return 'bestvideo[height<=480]+bestaudio/best'
    elif quality_text == "360p":  return 'bestvideo[height<=360]+bestaudio/best'
    return 'bestvideo+bestaudio/best'

# Luồng tải ảnh siêu nhẹ cho từng thẻ video
class ThumbnailThread(QThread):
    finished = Signal(bytes)
    def __init__(self, url):
        super().__init__()
        self.url = url
    def run(self):
        try:
            if self.url:
                # Thêm User-Agent để giả lập trình duyệt, tránh bị YouTube chặn
                req = Request(self.url, headers={'User-Agent': 'Mozilla/5.0'})
                with urlopen(req) as response:
                    self.finished.emit(response.read())
        except Exception as e:
            print(f"Lỗi tải ảnh mini: {e}")

# Lớp định nghĩa Thẻ video con
class VideoItemWidget(QWidget):
    def __init__(self, title, url, thumb_url):
        super().__init__()
        self.ui = Ui_VideoMini()
        self.ui.setupUi(self)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.url = url
        self.title = title 
        
        display_title = title if len(title) < 40 else title[:37] + "..."
        self.ui.labelName.setText(display_title)
        self.ui.labelName.setWordWrap(True) 
        
        # --- THÊM CHẤT LƯỢNG CHO TỪNG THẺ ---
        self.ui.comboBoxDQuality.addItems(["Best", "1080p", "720p", "480p", "360p", "Worst"])
        self.ui.comboBoxDownloadOpt.currentTextChanged.connect(self.toggle_quality)
        
        self.ui.downloadVBtn.clicked.connect(self.handle_download_single)

        # Kết nối sự kiện thay đổi
        self.ui.comboBoxDownloadOpt.currentTextChanged.connect(self.toggle_quality)
        
        # QUAN TRỌNG: Gọi hàm này ngay lập tức để set trạng thái ban đầu
        self.toggle_quality(self.ui.comboBoxDownloadOpt.currentText())

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

    # Hàm ẩn/hiện nút chất lượng
    def toggle_quality(self, text):
        self.ui.comboBoxDQuality.setEnabled(text != "MP3")

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

# 1. Lớp xử lý tải ngầm (Tránh treo máy)
class DownloadThread(QThread):
    finished = Signal(str)
    error = Signal(str)

    def __init__(self, url, save_path, selected_option, quality="Best"):
        super().__init__()
        self.url = url
        self.save_path = save_path
        self.selected_option = selected_option
        self.quality = quality # Thêm biến chất lượng

    def run(self): 
        # TÌM TRỰC TIẾP TRONG APP CHỨ KHÔNG DỰA VÀO MÁY NGƯỜI DÙNG NỮA
        node_path = get_asset_path("bin/node.exe")
        ffmpeg_path = get_asset_path("bin/ffmpeg.exe")
        try:
            if self.selected_option == "MP4":
                ydl_opts = {
                    'js_runtimes': {'node': {'path': node_path}},
                    'allow_remote_scripts': True,
                    'remote_components': ['ejs:github'],
                    'outtmpl': self.save_path,
                    'format': get_format_string(self.quality), # SỬ DỤNG BỘ LỌC CHẤT LƯỢNG
                    'merge_output_format': 'mp4',
                    'ffmpeg_location': ffmpeg_path,
                }
            else:  # MP3
                ydl_opts = {
                    'js_runtimes': {'node': {'path': node_path}},
                    'allow_remote_scripts': True,
                    'remote_components': ['ejs:github'],
                    'outtmpl': self.save_path.replace('.mp3', ''),
                    'format': 'bestaudio/best',
                    'ffmpeg_location': ffmpeg_path,
                    'postprocessors': [{
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': 'mp3',
                        'preferredquality': '192',
                    }],
                }

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([self.url])
            
            self.finished.emit(self.save_path)
        except Exception as e:
            self.error.emit(str(e))

class PlaylistDownloadThread(QThread):
    finished = Signal(str)
    error = Signal(str)
    progress_update = Signal(int)
    status_update = Signal(str)

    def __init__(self, download_list, folder_path):
        super().__init__()
        self.download_list = download_list # Nhận một danh sách cấu hình chi tiết
        self.folder_path = folder_path

    def run(self): 
        # TÌM TRỰC TIẾP TRONG APP CHỨ KHÔNG DỰA VÀO MÁY NGƯỜI DÙNG NỮA
        node_path = get_asset_path("bin/node.exe")
        ffmpeg_path = get_asset_path("bin/ffmpeg.exe")
        total = len(self.download_list)
        
        def progress_hook(d):
            if d['status'] == 'downloading':
                p_str = d.get('_percent_str', '0%')
                clean_p = re.sub(r'\x1b\[[0-9;]*m', '', p_str).replace('%', '').strip()
                try: self.progress_update.emit(int(float(clean_p)))
                except: pass

        try:
            # Tải TỪNG VIDEO một theo cấu hình riêng biệt của nó
            for i, item in enumerate(self.download_list):
                self.status_update.emit(f"Đang tải [{i+1}/{total}]: {item['title']}")
                self.progress_update.emit(0)

                outtmpl = os.path.join(self.folder_path, f"{item['clean_name']}.%(ext)s")
                
                base_opts = {
                    'noplaylist': True, # Chỉ tải link đơn
                    'ignoreerrors': True, 
                    'js_runtimes': {'node': {'path': node_path}},
                    'allow_remote_scripts': True,
                    'remote_components': ['ejs:github'],
                    'outtmpl': outtmpl,
                    'ffmpeg_location': ffmpeg_path,
                    'progress_hooks': [progress_hook], 
                }

                if item['type'] == "MP4":
                    base_opts.update({'format': get_format_string(item['quality']), 'merge_output_format': 'mp4'})
                else:
                    base_opts.update({
                        'format': 'bestaudio/best',
                        'postprocessors': [{'key': 'FFmpegExtractAudio', 'preferredcodec': 'mp3', 'preferredquality': '192'}],
                    })

                try:
                    with yt_dlp.YoutubeDL(base_opts) as ydl:
                        ydl.download([item['url']])
                except Exception as ex:
                    print(f"Bỏ qua lỗi video {item['title']}: {ex}")
                    continue # Lỗi bài này thì bỏ qua tải tiếp bài sau
            
            self.finished.emit(self.folder_path)
        except Exception as e:
            self.error.emit(str(e))

class FetchInfoThread(QThread):
    finished = Signal(dict)
    error = Signal(str)

    def __init__(self, url, ydl_options):
        super().__init__()
        self.url = url
        self.ydl_options = ydl_options

    # Hàm chuyên dụng để trích xuất link ảnh an toàn
    def get_thumb_url(self, data):
        thumbs = data.get('thumbnails')
        # Nếu data trả về là một danh sách, lấy cái ảnh ở vị trí cuối cùng (thường là nét nhất)
        if thumbs and isinstance(thumbs, list):
            return thumbs[-1].get('url') 
        # Nếu nó trả về trực tiếp một đường link
        elif data.get('thumbnail') and isinstance(data.get('thumbnail'), str):
            return data.get('thumbnail')
        return ""

    def run(self):
        try:
            with yt_dlp.YoutubeDL(self.ydl_options) as ydl:
                info = ydl.extract_info(self.url, download=False)

            title = info.get('title', 'Unknown_Title')
            is_playlist = 'entries' in info
            
            thumbnail_url = self.get_thumb_url(info)
            entries_data = [] 
            
            if is_playlist:
                raw_entries = list(info.get('entries', []))
                
                # Nếu playlist không có ảnh chung, mượn tạm ảnh của video đầu tiên
                if not thumbnail_url and len(raw_entries) > 0:
                    thumbnail_url = self.get_thumb_url(raw_entries[0])
                
                for item in raw_entries:
                    if item: 
                        entries_data.append({
                            'title': item.get('title', 'Unknown'),
                            'url': item.get('url', ''),
                            'thumbnail': self.get_thumb_url(item), # Lấy URL an toàn
                            
                        })

            img_data = None
            if thumbnail_url:
                # Thêm User-Agent cho ảnh bìa chính
                req = Request(thumbnail_url, headers={'User-Agent': 'Mozilla/5.0'})
                with urlopen(req) as response:
                    img_data = response.read()

            result = {
                'title': title,
                'is_playlist': is_playlist,
                'img_data': img_data,
                'entries': entries_data ,
                'url': self.url # <--- THÊM DÒNG NÀY ĐỂ TRẢ VỀ URL
            }
            self.finished.emit(result)

        except Exception as e:
            self.error.emit(str(e))


# 2. Lớp điều khiển giao diện
class MyDownloader(QMainWindow):
    node_path = get_asset_path("bin/node.exe")
    YDL_OPTIONS = {
        'quiet': True,
        'noplaylist': False,
        'extract_flat': True,
        'js_runtimes': {
        'node': {
            'path': node_path
        }
    },
        'remote_components': ['ejs:github'],
        'skip_download': True  ,  # Mặc định là không tải, khi nào cần tải sẽ ghi đè sau
        'allow_remote_scripts': True,  # Cho phép tải bộ giải mã từ GitHub
        'check_formats': False
    }

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # 1. Khởi tạo dữ liệu & Trạng thái ban đầu
        self.init_data()
        
        # 2. Thiết lập cấu hình UI (Style, Margins, Constraints)
        self.setup_ui_styling()
        
        # 3. Kết nối tín hiệu (Signals & Slots)
        self.setup_connections()

        # 4. Thiết lập trạng thái Sidebar lúc khởi động (Trạng thái Đóng)
        self.init_sidebar_state()

    def init_data(self):
        self.history_data = self.load_history()
        self.ui.label_2.setText("")
        self.ui.progressBar.setValue(0)
        # Khởi tạo layout cho vùng cuộn
        self.scroll_layout = QVBoxLayout(self.ui.scrollAreaWidgetContents)
        self.scroll_layout.setSpacing(10)
        self.scroll_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.scroll_layout.setContentsMargins(0, 10, 0, 10)

    def setup_ui_styling(self):
        # Cấu hình thanh cuộn và vùng chứa
        self.ui.scrollArea.setWidgetResizable(True)
        self.ui.scrollArea.setFrameShape(QFrame.NoFrame)
        self.ui.scrollArea.setStyleSheet("QScrollArea { border: none; background: transparent; }")
        self.ui.scrollAreaWidgetContents.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        
        # 1. Phá bỏ "vòng kim cô" 600px để các thẻ video không bị đè lên nhau
        self.ui.scrollArea.setMaximumSize(16777215, 16777215)
        self.ui.scrollAreaWidgetContents.setMaximumSize(16777215, 16777215)
        
        # 2. Ép thanh cuộn và nội dung luôn dạt sang lề trái + trên cùng
        self.ui.scrollArea.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
        # ---------------------------------------------------------
        
        self.ui.scrollAreaWidgetContents.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        
        # --- TẠO ICON VÀ CSS CHO NÚT CLEAR (X) ---
        self.ui.clearBtn.setText("✕") # Dùng ký tự Unicode siêu nét
        self.ui.clearBtn.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                color: rgb(150, 150, 150);
                font-size: 18px;
                font-weight: bold;
                border: none;
            }
            QPushButton:hover {
                color: #1ED761; /* Chuyển màu đỏ khi di chuột qua */
            }
        """)
        self.ui.clearBtn.setVisible(False) # Ẩn đi khi chưa có chữ

        # Cấu hình List gợi ý (History)
        self.ui.listWidget.setVisible(False)

        # Cấu hình List gợi ý (History)
        self.ui.listWidget.setVisible(False)
        self.ui.listWidget.setMaximumHeight(0)
        self.ui.listWidget.setStyleSheet("""
            QListWidget {
                background-color: rgb(35, 35, 35); color: white;
                border-radius: 10px; border: 1px solid #1ED761;
                padding: 5px; outline: 0;
            }
            QListWidget::item { padding: 5px; border-radius: 5px; }
            QListWidget::item:hover { background-color: rgb(67, 67, 67); color: #1ED761; }
        """)

        # Cấu hình Nút thu nhỏ Sidebar
        self.ui.miniSideBarBtn.setStyleSheet("""
            QPushButton { color: #1ED761; font-size: 24px; font-weight: bold; background: transparent; border: none; }
            QPushButton:hover { color: white; }
        """)
        
        # Cài đặt ComboBox và Label
        self.ui.comboBoxDownloadQuality.addItems(["Best Quality", "Worst Quality"])
        self.ui.label_2.setWordWrap(True)
        self.ui.label_2.setStyleSheet("color: white;")
        self.ui.centralwidget.setCursor(Qt.CursorShape.ArrowCursor)

        # --- MỞ KHÓA CHIỀU CAO CHO TOÀN BỘ ỨNG DỤNG ---
        self.setMaximumHeight(16777215)
        self.ui.centralwidget.setMaximumHeight(16777215)
        
        # Mở khóa cho Cột trái
        self.ui.widget_3.setMaximumHeight(16777215) 
        
        # Mở khóa cho Sidebar
        self.ui.sideBarWidget.setMaximumHeight(16777215)

        # Mở khóa cho các khung chứa thanh tìm kiếm để danh sách lịch sử giãn tự do
        self.ui.widget.setMaximumHeight(16777215)
        self.ui.widget_9.setMaximumHeight(16777215)
        self.ui.widget_6.setMaximumHeight(16777215)

        # --- ÉP SIDEBAR KÉO DÀI THEO CHIỀU DỌC CỦA CỬA SỔ ---

        # 1. Xóa bỏ cờ "AlignTop" (ép dính trần) của Sidebar trong Layout tổng
        # Khi tham số Alignment = 0, Layout sẽ tự động cho phép Widget giãn đầy chiều dọc
        self.ui.horizontalLayout_2.setAlignment(self.ui.sideBarWidget, Qt.AlignmentFlag(0))

        # 2. Kích hoạt tính năng Expanding (Co giãn vô cực) theo chiều dọc cho vỏ Sidebar
        self.ui.sideBarWidget.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)

        

        # --- ÉP SCROLLAREA KHÍT LẠI VÀ TRÀN XUỐNG ĐÁY ---
        
        # 1. Gỡ bỏ lệnh "AlignTop" của Layout đối với scrollArea để nó được phép giãn ra
        self.ui.verticalLayout_4.setAlignment(self.ui.scrollArea, Qt.AlignmentFlag(0))
        
        # 2. Bắt vỏ scrollArea phải giãn nở tối đa (Expanding) theo chiều dọc
        self.ui.scrollArea.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        
        # 3. Trao quyền ưu tiên tuyệt đối: Mọi không gian dọc dôi ra đều thuộc về scrollArea
        self.ui.verticalLayout_4.setStretchFactor(self.ui.scrollArea, 1)

        # --- TỰ ĐỘNG FIX ĐƯỜNG DẪN ẢNH MŨI TÊN CHO COMBOBOX ---
        arrow_icon = get_asset_path("img/icon/down_arrow.png")
        
        comboboxes = [
            self.ui.comboBoxDownloadOption, 
            self.ui.comboBoxDownloadQuality, 
            self.ui.comboBoxDownloadAllOpt
        ]
        
        for combo in comboboxes:
            style = combo.styleSheet()
            # Tìm và thay thế đường dẫn E:/... cứng nhắc bằng đường dẫn động
            style = style.replace("E:/design/ytb_playlist_downloader/img/icon/down_arrow.png", arrow_icon)
            combo.setStyleSheet(style)

        

    def setup_connections(self):
        # Nút bấm chính
        self.ui.findBtn.clicked.connect(self.handle_find_btn)
        self.ui.downloadBtn.clicked.connect(self.handle_download_video_request)
        self.ui.downloadAllBtn.clicked.connect(self.handle_download_all)
        self.ui.miniSideBarBtn.clicked.connect(self.toggle_sidebar)

        # ---> THÊM KẾT NỐI NÚT XÓA Ở ĐÂY <---
        self.ui.clearBtn.clicked.connect(self.ui.enterPlace.clear)

        # Search & History
        self.ui.enterPlace.textChanged.connect(self.on_search_text_changed)
        self.ui.listWidget.itemClicked.connect(self.on_history_item_clicked)

        # Logic ComboBox
        self.ui.comboBoxDownloadOption.currentTextChanged.connect(
            lambda text: self.ui.comboBoxDownloadQuality.setEnabled(text != "MP3")
        )
        self.ui.comboBoxDownloadAllOpt.currentTextChanged.connect(self.sync_all_download_options)

        # Bắt sự kiện Click chuột vào ô nhập để hiện lịch sử khi ô đang trống
        self.original_mouse_press = self.ui.enterPlace.mousePressEvent
        def custom_mouse_press(event):
            self.original_mouse_press(event) 
            self.on_search_text_changed(self.ui.enterPlace.text())
        self.ui.enterPlace.mousePressEvent = custom_mouse_press

    def init_sidebar_state(self):
        # 1. Ẩn các thành phần con của Sidebar
        self.ui.widget_7.setVisible(False)
        self.ui.downloadAllBtn.setVisible(False)
        self.ui.comboBoxDownloadAllOpt.setVisible(False)
        self.ui.scrollArea.setVisible(False)
        
        # 2. Xóa bỏ giới hạn để thu nhỏ được
        widgets_to_unlock = [
            self.ui.widget_5, self.ui.downloadAllBtn, self.ui.comboBoxDownloadAllOpt,
            self.ui.widget_7, self.ui.progressBar, self.ui.label_2, 
            self.ui.scrollArea, self.ui.scrollAreaWidgetContents
        ]
        for w in widgets_to_unlock:
            w.setMinimumWidth(0)

        # 3. Thiết lập Sidebar ở trạng thái đóng (50px)
        self.ui.sideBarWidget.setMinimumWidth(50)
        self.ui.sideBarWidget.setMaximumWidth(50)
        self.ui.miniSideBarBtn.setText("◀")
        
        # 4. Kích thước cửa sổ tổng thể khi đóng Sidebar
        self.setMinimumSize(730, 450)
        self.resize(730, 450)
        
        # Reset layout margins của sidebar
        self.ui.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.ui.verticalLayout_4.setSpacing(0)
        
        # Khóa nút Toggle mặc định vì chưa có Playlist
        self.ui.miniSideBarBtn.setEnabled(False)

    def sync_all_download_options(self, text):
        # Duyệt qua tất cả các thẻ video đang có trong Layout của Scroll Area
        for i in range(self.scroll_layout.count()):
            item = self.scroll_layout.itemAt(i)
            if item and item.widget():
                widget = item.widget()
                # Kiểm tra nếu đúng là thẻ VideoItemWidget thì mới đổi option
                if isinstance(widget, VideoItemWidget):
                    widget.ui.comboBoxDownloadOpt.setCurrentText(text)

    def handle_download_video_request(self):
        url = self.ui.enterPlace.text().strip()
        selected_option = self.ui.comboBoxDownloadOption.currentText()
        selected_quality = self.ui.comboBoxDownloadQuality.currentText() # ĐỌC CHẤT LƯỢNG TỪ MAIN UI
        
        if not url: return
        safe_title = self.clean_filename(self.current_video_title)
        
        if selected_option == "MP4":
            file_path, _ = QFileDialog.getSaveFileName(self, "Lưu Video", f"{safe_title}", "Video Files (*.mp4)")
            if not file_path: return
        if selected_option == "MP3":
            file_path, _ = QFileDialog.getSaveFileName(self, "Lưu Nhạc", f"{safe_title}", "Audio Files (*.mp3)")
            if not file_path: return    

        self.ui.enterPlace.setEnabled(False)
        self.ui.statusbar.showMessage("Đang tải video...")

        # Truyền quality vào
        self.thread = DownloadThread(url, file_path, selected_option, selected_quality)
        self.thread.finished.connect(self.on_success)
        self.thread.error.connect(self.on_fail)
        self.thread.start()

    # ... (Giữ nguyên on_success, on_fail) ...

    def handle_download_all(self):
        # 1. ĐI GOM DỮ LIỆU TỪ CÁC THẺ CON
        download_list = []
        for i in range(self.scroll_layout.count()):
            item = self.scroll_layout.itemAt(i)
            if item and item.widget():
                widget = item.widget()
                if isinstance(widget, VideoItemWidget):
                    download_list.append(widget.get_download_info()) # Lấy cấu hình riêng của thẻ này

        if not download_list:
            QMessageBox.warning(self, "Cảnh báo", "Vui lòng nhập link Playlist và bấm Find để hiện danh sách trước!")
            return
            
        # 2. CHỌN CHỖ LƯU
        dir_path = QFileDialog.getExistingDirectory(self, "Chọn thư mục lưu Playlist")
        if not dir_path: return
            
        safe_title = self.clean_filename(self.current_video_title)
        if not safe_title: safe_title = "Downloaded_Playlist"
        
        playlist_folder = os.path.join(dir_path, safe_title)
        os.makedirs(playlist_folder, exist_ok=True) 
        
        # 3. CHẠY GIAO DIỆN TẢI
        self.ui.downloadAllBtn.setEnabled(False)
        self.ui.downloadAllBtn.setText("Đang tải...") 
        
        self.ui.widget_7.setVisible(True) 
        self.ui.label_2.setText("Đang chuẩn bị dữ liệu...")
        self.ui.progressBar.setValue(0)
        
        # TRUYỀN TOÀN BỘ DANH SÁCH VÀO THREAD
        self.dl_all_thread = PlaylistDownloadThread(download_list, playlist_folder)
        
        self.dl_all_thread.progress_update.connect(self.ui.progressBar.setValue)
        self.dl_all_thread.status_update.connect(self.ui.label_2.setText)
        
        self.dl_all_thread.finished.connect(self.on_dl_all_success)
        self.dl_all_thread.error.connect(self.on_dl_all_fail)
        self.dl_all_thread.start()

    # ... (Giữ nguyên on_dl_all_success, on_dl_all_fail) ...

    def clean_filename(self, filename):
        # 1. Thay thế các ký tự cấm trên Windows: \ / : * ? " < > | bằng dấu gạch ngang -
        # Chúng ta dùng regex để tìm và thay thế
        clean_name = re.sub(r'[\\/*?:"<>|]', '-', filename)
        
        # 2. Giới hạn độ dài tên file (Windows tối đa 255 ký tự bao gồm cả đường dẫn)
        return clean_name[:150].strip()


    def handle_find_btn(self):
        self.ui.listWidget.setVisible(False) # Ẩn gợi ý
        url = self.ui.enterPlace.text().strip()
        if not url:
            self.ui.linkName.setText("Not found")
            self.current_video_title = "" # Xóa tên cũ nếu ô trống
            return
            
        # KHÔNG GỌI 2 HÀM CŨ NỮA
        # self.link_name_detect(url)
        # self.show_thumbnail_img(url)

        # MÀ SỬ DỤNG LUỒNG MỚI TẠO Ở ĐÂY:
        # Khóa nút Find và báo trạng thái để người dùng biết app đang làm việc
        self.ui.findBtn.setEnabled(False)
        self.ui.statusbar.showMessage("Đang tìm thông tin...")
        self.ui.videoImg.setText("Đang tải ảnh...")

        # Khởi chạy luồng ngầm FetchInfoThread để lấy thông tin
        self.info_thread = FetchInfoThread(url, self.YDL_OPTIONS)
        self.info_thread.finished.connect(self.on_info_fetched_success)
        self.info_thread.error.connect(self.on_info_fetched_fail)
        self.info_thread.start()

        self.ui.miniSideBarBtn.setEnabled(False)
        if self.ui.sideBarWidget.width() >= 500:
            self.toggle_sidebar() # Tự động đóng nếu đang mở
        return

    def clear_scroll_area(self):
        # Xóa sạch các thẻ video cũ
        while self.scroll_layout.count():
            item = self.scroll_layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()
        
    def toggle_sidebar(self):
        current_side_width = self.ui.sideBarWidget.width()
        current_window_width = self.width()
        current_height = self.height()
        
        if current_side_width >= 500:
            new_side_width = 50 
            new_scroll_width = 50  # Ép vỏ thu nhỏ
            new_content_width = 50 # Ép ruột thu nhỏ
            new_window_width = current_window_width - 450
            
            self.ui.downloadAllBtn.setVisible(False)
            self.ui.comboBoxDownloadAllOpt.setVisible(False)
            self.ui.scrollArea.setVisible(False) 
            self.ui.widget_7.setVisible(False)
            self.ui.miniSideBarBtn.setText("◀") 
        else:
            new_side_width = 500 
            new_scroll_width = 500  # Ép vỏ nở ra 500px
            new_content_width = 500 # Ép ruột nở ra 500px để thanh cuộn dính vách
            new_window_width = current_window_width + 450
            
            self.ui.downloadAllBtn.setVisible(True)
            self.ui.comboBoxDownloadAllOpt.setVisible(True)
            self.ui.scrollArea.setVisible(True)
            self.ui.miniSideBarBtn.setText("▶")

            if self.ui.widget_5.layout():
                self.ui.widget_5.layout().setAlignment(self.ui.miniSideBarBtn, Qt.AlignmentFlag.AlignRight)

        # --- TẠO GROUP ANIMATION ĐỂ CHẠY ĐỒNG BỘ ---
        self.anim_side_min = QPropertyAnimation(self.ui.sideBarWidget, b"minimumWidth")
        self.anim_side_max = QPropertyAnimation(self.ui.sideBarWidget, b"maximumWidth")
        self.anim_window = QPropertyAnimation(self, b"size")
        
        # Ép ScrollArea (Vỏ)
        self.anim_scroll = QPropertyAnimation(self.ui.scrollArea, b"minimumWidth")
        # Ép WidgetContents (Ruột) - ĐÂY LÀ DÒNG QUAN TRỌNG NHẤT
        self.anim_content = QPropertyAnimation(self.ui.scrollAreaWidgetContents, b"minimumWidth")
        
        animations = [self.anim_side_min, self.anim_side_max, self.anim_window, self.anim_scroll, self.anim_content]
        
        for anim in animations:
            anim.setDuration(300)
            anim.setEasingCurve(QEasingCurve.InOutQuart)

        self.anim_side_min.setEndValue(new_side_width)
        self.anim_side_max.setEndValue(new_side_width)
        self.anim_window.setEndValue(QSize(new_window_width, current_height))
        self.anim_scroll.setEndValue(new_scroll_width)
        self.anim_content.setEndValue(new_content_width)

        # Chạy toàn bộ
        for anim in animations:
            anim.start()

    def on_info_fetched_success(self, info_dict):
        # 1. Cập nhật trạng thái giao diện
        self.ui.findBtn.setEnabled(True)
        self.ui.statusbar.showMessage("Đã tìm thấy thông tin", 3000)

        # 2. Cập nhật tên video/playlist
        self.current_video_title = info_dict['title']
        prefix = "Playlist: " if info_dict['is_playlist'] else "Video: "
        self.ui.linkName.setText(f"{prefix}{self.current_video_title}")

        # --- LƯU LỊCH SỬ TÌM KIẾM ---
        self.save_history(info_dict['title'], info_dict['url'], info_dict['is_playlist'])
        
        # 3. Xử lý và hiển thị ảnh bìa chính
        img_data = info_dict.get('img_data')
        if img_data:
            pixmap = QPixmap()
            pixmap.loadFromData(img_data)
            if not pixmap.isNull():
                scaled_pixmap = pixmap.scaled(
                    self.ui.videoImg.size(), 
                    Qt.AspectRatioMode.KeepAspectRatio, 
                    Qt.TransformationMode.SmoothTransformation
                )
                self.ui.videoImg.setPixmap(scaled_pixmap)
                self.ui.videoImg.setAlignment(Qt.AlignmentFlag.AlignCenter)
            else:
                self.ui.videoImg.setText("Lỗi: Dữ liệu ảnh hỏng")
        else:
             self.ui.videoImg.setText("Không tìm thấy Thumbnail")

        # 4. ĐỔ DANH SÁCH PLAYLIST VÀO SCROLL AREA
        self.clear_scroll_area() # Xóa list cũ nếu có
        
        if info_dict['is_playlist']:
            entries = info_dict.get('entries', [])
            for video_info in entries:
                # Tạo một thẻ mini cho mỗi video
                item_widget = VideoItemWidget(
                    title=video_info['title'],
                    url=video_info['url'],
                    thumb_url=video_info['thumbnail']
                )
                # Đưa thẻ mini vào thanh cuộn
                self.scroll_layout.addWidget(item_widget, 0, Qt.AlignmentFlag.AlignHCenter)

        # Cập nhật danh sách chất lượng cho giao diện chính
        self.ui.comboBoxDownloadQuality.clear()
        if info_dict['is_playlist']:
            self.ui.comboBoxDownloadQuality.addItems(["Best Quality", "Worst Quality"])
        else:
            self.ui.comboBoxDownloadQuality.addItems(["Best", "1080p", "720p", "480p", "360p", "Worst"])
            
        # Kiểm tra trạng thái Enabled/Disabled ngay lập tức cho nút Quality chính
        is_mp3 = self.ui.comboBoxDownloadOption.currentText() == "MP3"
        self.ui.comboBoxDownloadQuality.setDisabled(is_mp3)

        # Bật/Tắt nút Toggle Sidebar dựa vào loại link
        if info_dict['is_playlist']:
            self.ui.miniSideBarBtn.setEnabled(True)
            if self.ui.sideBarWidget.width() < 500:
                self.toggle_sidebar()
        else:
            self.ui.miniSideBarBtn.setEnabled(False)
            # Tự động đóng Sidebar nếu trước đó nó đang mở
            if self.ui.sideBarWidget.width() >= 500:
                self.toggle_sidebar()
        
        
        
    
    def on_info_fetched_fail(self, error_msg):
        self.ui.findBtn.setEnabled(True)
        self.ui.statusbar.showMessage("Lỗi tìm kiếm")
        self.ui.linkName.setText("Lỗi kết nối hoặc Link sai")
        self.ui.videoImg.setText("Không thể hiển thị ảnh")
        print(f"Lỗi fetch info: {error_msg}")

    def on_success(self, path):
        self.ui.enterPlace.setEnabled(True)
        self.ui.enterPlace.clear()
        self.ui.linkName.clear()
        QMessageBox.information(self, "Xong!", f"Đã tải về:\n{path}")
        self.ui.statusbar.showMessage("Sẵn sàng", 5000)

    def on_fail(self, msg):
        self.ui.enterPlace.setEnabled(True)
        QMessageBox.critical(self, "Lỗi", f"Thất bại: {msg}")
        self.ui.statusbar.showMessage("Lỗi tải video")
        
    def on_dl_all_success(self, path):
        self.ui.downloadAllBtn.setEnabled(True)
        self.ui.downloadAllBtn.setText("Download ALL") 
        
        # Cập nhật chữ và làm đầy 100%
        self.ui.label_2.setText("Hoàn tất!")
        self.ui.progressBar.setValue(100)
        
        QMessageBox.information(self, "Xong!", f"Đã tải thành công toàn bộ playlist vào:\n{path}")
        self.ui.statusbar.showMessage("Tải playlist xong!", 5000)
        
        # Ẩn Progress bar đi cho gọn
        self.ui.widget_7.setVisible(False)
        
    def on_dl_all_fail(self, msg):
        self.ui.downloadAllBtn.setEnabled(True)
        self.ui.downloadAllBtn.setText("Download ALL")
        self.ui.label_2.setText("Lỗi tải xuống!")
        QMessageBox.critical(self, "Lỗi", f"Thất bại trong quá trình tải:\n{msg}")

# ------------------ PHẦN XỬ LÝ LỊCH SỬ TÌM KIẾM ------------------

    def on_search_text_changed(self, text):
        self.ui.clearBtn.setVisible(bool(text.strip()))

        self.ui.listWidget.clear()
        search_text = text.lower().strip()
        
        matched_items = []
        
        # LOGIC 1: Ô TÌM KIẾM TRỐNG -> HIỆN 5 LỊCH SỬ GẦN NHẤT
        if not search_text:
            matched_items = self.history_data[:5] 
            
        # LOGIC 2: CÓ GÕ CHỮ -> CHỈ TÌM TRONG TIÊU ĐỀ (TITLE), KHÔNG TÌM TRONG LINK
        else:
            for item in self.history_data:
                # Ép tiêu đề về chữ thường và đem so sánh với từ khóa
                if search_text in item['title'].lower():
                    matched_items.append(item)
                
                # HIỂN THỊ TỐI ĐA 8 KẾT QUẢ KHI CÓ TỪ KHÓA
                if len(matched_items) >= 8:
                    break
                    
        # --- Phần hiển thị giao diện ---
        if not matched_items:
            self.ui.listWidget.setVisible(False)
            self.ui.listWidget.setMinimumHeight(0)
            self.ui.listWidget.setMaximumHeight(0)
            return
            
        self.ui.listWidget.setVisible(True)
        for item in matched_items:
            list_item = QListWidgetItem(item['title'])
            # Vẫn giấu URL vào data ngầm để lúc click còn biết đường mà tải
            list_item.setData(Qt.ItemDataRole.UserRole, item['url']) 
            self.ui.listWidget.addItem(list_item)
            
        # Tính toán chiều cao chuẩn
        total_height = len(matched_items) * 38 + 15
        self.ui.listWidget.setMinimumHeight(total_height)
        self.ui.listWidget.setMaximumHeight(total_height)

        # Khóa thanh cuộn
        self.ui.listWidget.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.ui.listWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

    def on_history_item_clicked(self, item):
        url = item.data(Qt.ItemDataRole.UserRole)
        self.ui.enterPlace.setText(url) # Điền tự động URL vào ô nhập
        self.ui.listWidget.setVisible(False) # Ẩn danh sách gợi ý
        self.handle_find_btn() # Tự động kích hoạt nút Find
    # ------------------------------------------------------------------

# ------------------ PHẦN XỬ LÝ LỊCH SỬ TÌM KIẾM ------------------
    def get_history_path(self):
        # Kiểm tra xem App đang chạy bằng Python (.py) hay đã đóng gói thành (.exe)
        if getattr(sys, 'frozen', False):
            # Nếu chạy bằng file .exe -> Lấy thư mục chứa file .exe đó
            base_dir = os.path.dirname(sys.executable)
        else:
            # Nếu chạy code bình thường -> Lấy thư mục chứa file app.py
            base_dir = os.path.dirname(os.path.abspath(__file__))
            
        return os.path.join(base_dir, "history.json")
    
    def load_history(self):
        history_file = self.get_history_path()
        # Nếu file tồn tại đúng ở đường dẫn đó thì mới đọc
        if os.path.exists(history_file):
            try:
                with open(history_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except: pass
        return [] # Nếu chưa có thì trả về list rỗng (chưa từng tìm kiếm)

    def save_history(self, title, url, is_playlist):
        prefix = "[Playlist] " if is_playlist else "[Video] "
        full_title = f"{prefix}{title}"
        
        # Xóa URL trùng lặp (nếu có) để đẩy nó lên đầu danh sách
        self.history_data = [item for item in self.history_data if item['url'] != url]
        
        # Chèn vào đầu danh sách lịch sử
        self.history_data.insert(0, {'title': full_title, 'url': url})
        
        # Lưu tối đa 50 lịch sử gần nhất
        self.history_data = self.history_data[:50]
        
        # CHỈ GHI VÀO ĐÚNG 1 ĐỊA CHỈ DUY NHẤT NÀY
        history_file = self.get_history_path()
        with open(history_file, 'w', encoding='utf-8') as f:
            json.dump(self.history_data, f, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyDownloader()
    window.show()
    sys.exit(app.exec())