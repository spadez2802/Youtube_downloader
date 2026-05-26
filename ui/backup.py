import sys
import yt_dlp
import re
import yt_dlp
import os
import shutil
from urllib.request import urlopen
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox, QWidget, QProgressBar, QLabel
from PySide6.QtCore import QThread, Signal
from PySide6.QtWidgets import QVBoxLayout # Thêm import này
from urllib.request import urlopen, Request
from backup.old_video_widget.ui_video_ver3_1 import Ui_miniCard as Ui_VideoMini # Import giao diện thẻ mini
from backup.old_ui_main.ui_main_ver4_5 import Ui_MainWindow # Tên file .py bạn đã lưu

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
        self.title = title # Lưu lại title để làm tên file
        
        display_title = title if len(title) < 40 else title[:37] + "..."
        self.ui.labelName.setText(display_title)
        self.ui.labelName.setWordWrap(True) 
        
        # Kết nối nút bấm
        self.ui.downloadVBtn.clicked.connect(self.handle_download_single)

        if thumb_url:
            self.ui.labelImg.setText("Đang tải...")
            self.thumb_thread = ThumbnailThread(thumb_url)
            self.thumb_thread.finished.connect(self.set_image)
            self.thumb_thread.start()
        else:
            self.ui.labelImg.setText("No Image")

    def set_image(self, img_data):
        pixmap = QPixmap()
        pixmap.loadFromData(img_data)
        if not pixmap.isNull():
            scaled_pixmap = pixmap.scaled(self.ui.labelImg.size(), Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
            self.ui.labelImg.setPixmap(scaled_pixmap)
            self.ui.labelImg.setAlignment(Qt.AlignmentFlag.AlignCenter)

    def handle_download_single(self):
        try:
            # Đảm bảo đọc đúng tên ComboBox trong ui_video_ver3_1.py
            selected_option = self.ui.comboBoxDownloadOpt.currentText()
            
            # Làm sạch tên file và thêm sẵn đuôi mở rộng mặc định
            clean_name = re.sub(r'[\\/*?:"<>|]', '-', self.title)[:150].strip()
            default_name = f"{clean_name}.mp4" if selected_option == "MP4" else f"{clean_name}.mp3"
            
            # Hỏi chỗ lưu
            if selected_option == "MP4":
                file_path, _ = QFileDialog.getSaveFileName(self, "Lưu Video", default_name, "Video Files (*.mp4)")
            else:
                file_path, _ = QFileDialog.getSaveFileName(self, "Lưu Nhạc", default_name, "Audio Files (*.mp3)")
                
            if not file_path: return
            
            self.ui.downloadVBtn.setEnabled(False)
            self.ui.downloadVBtn.setText("Đang tải...")

            self.thread = DownloadThread(self.url, file_path, selected_option)
            self.thread.finished.connect(self.on_dl_success)
            self.thread.error.connect(self.on_dl_fail)
            self.thread.start()
            
        except Exception as e:
            # Bắt lỗi và hiển thị thẳng lên màn hình để dễ bắt bệnh
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

    def __init__(self, url, save_path,selected_option):
        super().__init__()
        self.url = url
        self.save_path = save_path
        self.selected_option = selected_option

    def run(self): # Không để tham số ở đây
        node_path = shutil.which("node")
        ffmpeg_path = shutil.which("ffmpeg")
        try:
            # Đường dẫn ffmpeg bạn đã tìm thấy lúc trước
            #ffmpeg_path = self.ffmpeg_path
            #node_path = self.node_path
            if self.selected_option == "MP4":
                ydl_opts = {
                    'js_runtimes': {
                        'node': {
                            'path': node_path
                        }
                    },
                    'allow_remote_scripts': True,
                    'remote_components': ['ejs:github'],
                    'outtmpl': self.save_path,
                    'format': 'bestvideo+bestaudio/best',
                    'merge_output_format': 'mp4',
                    'ffmpeg_location': ffmpeg_path,
                }
            else:  # MP3
                ydl_opts = {
                    'js_runtimes': {
                        'node': {
                            'path': node_path
                        }
                    },
                    'allow_remote_scripts': True,
                    'remote_components': ['ejs:github'],
                    'outtmpl': self.save_path.replace('.mp3', ''), # yt-dlp tự thêm đuôi
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
    # Thêm 2 tín hiệu (Signal) mới để báo cáo về giao diện
    progress_update = Signal(int)
    status_update = Signal(str)

    def __init__(self, playlist_url, folder_path, selected_option):
        super().__init__()
        self.playlist_url = playlist_url
        self.folder_path = folder_path
        self.selected_option = selected_option

    def run(self):
        node_path = shutil.which("node")
        ffmpeg_path = shutil.which("ffmpeg")
        
        # Hàm theo dõi tiến trình của yt-dlp
        def progress_hook(d):
            if d['status'] == 'downloading':
                info = d.get('info_dict', {})
                title = info.get('title', 'Unknown')
                p_index = info.get('playlist_index', '?')
                p_count = info.get('playlist_count', '?')

                # Gửi tên video và vị trí (VD: [1/10] Tên video...) về UI
                self.status_update.emit(f"Đang tải [{p_index}/{p_count}]: {title}")

                # Gửi phần trăm về UI (Lọc bỏ các ký tự màu sắc ẩn của terminal)
                p_str = d.get('_percent_str', '0%')
                clean_p = re.sub(r'\x1b\[[0-9;]*m', '', p_str).replace('%', '').strip()
                try:
                    self.progress_update.emit(int(float(clean_p)))
                except ValueError:
                    pass

        try:
            outtmpl = os.path.join(self.folder_path, '%(title)s.%(ext)s')
            
            base_opts = {
                'noplaylist': False, 
                'ignoreerrors': True, 
                'js_runtimes': {'node': {'path': node_path}},
                'allow_remote_scripts': True,
                'remote_components': ['ejs:github'],
                'outtmpl': outtmpl,
                'ffmpeg_location': ffmpeg_path,
                'progress_hooks': [progress_hook], # Gắn hàm theo dõi vào đây
            }

            if self.selected_option == "MP4":
                base_opts.update({'format': 'bestvideo+bestaudio/best', 'merge_output_format': 'mp4'})
            else:
                base_opts.update({
                    'format': 'bestaudio/best',
                    'postprocessors': [{'key': 'FFmpegExtractAudio', 'preferredcodec': 'mp3', 'preferredquality': '192'}],
                })

            with yt_dlp.YoutubeDL(base_opts) as ydl:
                ydl.download([self.playlist_url])
            
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
                            'thumbnail': self.get_thumb_url(item) # Lấy URL an toàn
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
                'entries': entries_data 
            }
            self.finished.emit(result)

        except Exception as e:
            self.error.emit(str(e))


# 2. Lớp điều khiển giao diện
class MyDownloader(QMainWindow):
    node_path = shutil.which("node")
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
        self.ui.downloadAllBtn.clicked.connect(self.handle_download_all)
        # KẾT NỐI SỰ KIỆN NÚT BẤM
        self.ui.downloadBtn.clicked.connect(self.handle_download_video_request)
        self.ui.findBtn.clicked.connect(self.handle_find_btn)

        # --- SỬA LỖI CON TRỎ CHUỘT XOAY VÒNG ---
        self.ui.centralwidget.setCursor(Qt.CursorShape.ArrowCursor)

        # --- CÀI ĐẶT THANH TIẾN TRÌNH TỪ QT DESIGNER ---
        self.ui.widget_7.setVisible(False) # Ẩn toàn bộ cụm progress bar đi khi chưa tải
        self.ui.progressBar.setValue(0)
        self.ui.label_2.setText("")
        self.ui.label_2.setWordWrap(True) # Cho phép tên video rớt dòng nếu quá dài
        self.ui.label_2.setStyleSheet("color: white;") # Chỉnh chữ màu trắng cho dễ nhìn

        self.dl_progress_bar = QProgressBar()
        self.dl_progress_bar.setStyleSheet("""
            QProgressBar {
                border: 2px solid #555;
                border-radius: 10px;
                text-align: center;
                color: white;
            }
            QProgressBar::chunk {
                background-color: rgb(255, 85, 0);
                border-radius: 8px;
            }
        """)
        self.dl_progress_bar.setVisible(False) # Ẩn đi lúc bình thường

        # --- KHỞI TẠO LAYOUT CHO SCROLL AREA (CHỈ LÀM 1 LẦN DUY NHẤT) ---
        
        # 1. Gỡ bỏ giới hạn chiều cao tĩnh (Quan trọng nhất để không bị chồng)
        self.ui.scrollAreaWidgetContents.setMaximumHeight(16777215) 

        # 2. Cài đặt Layout cho Scroll Area
        self.scroll_layout = QVBoxLayout(self.ui.scrollAreaWidgetContents)
        self.scroll_layout.setSpacing(10) # Thêm khoảng cách 10px giữa các video
        self.scroll_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

    def clean_filename(self, filename):
        # 1. Thay thế các ký tự cấm trên Windows: \ / : * ? " < > | bằng dấu gạch ngang -
        # Chúng ta dùng regex để tìm và thay thế
        clean_name = re.sub(r'[\\/*?:"<>|]', '-', filename)
        
        # 2. Giới hạn độ dài tên file (Windows tối đa 255 ký tự bao gồm cả đường dẫn)
        return clean_name[:150].strip()


    def handle_find_btn(self):
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



    def clear_scroll_area(self):
        # Xóa sạch các thẻ video cũ
        while self.scroll_layout.count():
            item = self.scroll_layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()

    def on_info_fetched_success(self, info_dict):
        # 1. Cập nhật trạng thái giao diện
        self.ui.findBtn.setEnabled(True)
        self.ui.statusbar.showMessage("Đã tìm thấy thông tin", 3000)

        # 2. Cập nhật tên video/playlist
        self.current_video_title = info_dict['title']
        prefix = "Playlist: " if info_dict['is_playlist'] else "Video: "
        self.ui.linkName.setText(f"{prefix}{self.current_video_title}")

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
    
    

    def on_info_fetched_fail(self, error_msg):
        self.ui.findBtn.setEnabled(True)
        self.ui.statusbar.showMessage("Lỗi tìm kiếm")
        self.ui.linkName.setText("Lỗi kết nối hoặc Link sai")
        self.ui.videoImg.setText("Không thể hiển thị ảnh")
        print(f"Lỗi fetch info: {error_msg}")

    def handle_download_video_request(self):
        url = self.ui.enterPlace.text().strip()
        # Đã xóa phần lặp chữ dư thừa
        selected_option = self.ui.comboBoxDownloadOption.currentText()
        if not url:
            return
        safe_title = self.clean_filename(self.current_video_title)
        
        # Chọn nơi lưu
        if selected_option == "MP4":
            file_path, _ = QFileDialog.getSaveFileName(self, "Lưu Video", f"{safe_title}", "Video Files (*.mp4)")
            if not file_path:
                return
        if selected_option == "MP3":
            # Đã sửa "Video Files (*.mp3)" thành "Audio Files (*.mp3)" cho chuẩn xác
            file_path, _ = QFileDialog.getSaveFileName(self, "Lưu Nhạc", f"{safe_title}", "Audio Files (*.mp3)")
            if not file_path:
                return    

        # Khóa giao diện và bắt đầu tải
        self.ui.enterPlace.setEnabled(False)
        self.ui.statusbar.showMessage("Đang tải video...")

        self.thread = DownloadThread(url, file_path, selected_option)
        self.thread.finished.connect(self.on_success)
        self.thread.error.connect(self.on_fail)
        self.thread.start()

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

    def handle_download_all(self):
        url = self.ui.enterPlace.text().strip()
        if not url or ("list=" not in url):
            QMessageBox.warning(self, "Cảnh báo", "Vui lòng nhập link của một Playlist!")
            return
            
        selected_option = self.ui.comboBoxDownloadAllOpt.currentText()
            
        dir_path = QFileDialog.getExistingDirectory(self, "Chọn thư mục lưu Playlist")
        if not dir_path: return
            
        safe_title = self.clean_filename(self.current_video_title)
        if not safe_title: safe_title = "Downloaded_Playlist"
        
        playlist_folder = os.path.join(dir_path, safe_title)
        os.makedirs(playlist_folder, exist_ok=True) 
        
        # Đổi trạng thái giao diện và HIỆN Progress Bar đã vẽ
        self.ui.downloadAllBtn.setEnabled(False)
        self.ui.downloadAllBtn.setText("Đang tải...") 
        
        self.ui.widget_7.setVisible(True) # Hiện cụm chứa Progress bar + Label
        self.ui.label_2.setText("Đang chuẩn bị dữ liệu...")
        self.ui.progressBar.setValue(0)
        
        self.dl_all_thread = PlaylistDownloadThread(url, playlist_folder, selected_option)
        
        # Kết nối tín hiệu với UI của Qt Designer
        self.dl_all_thread.progress_update.connect(self.ui.progressBar.setValue)
        self.dl_all_thread.status_update.connect(self.ui.label_2.setText)
        
        self.dl_all_thread.finished.connect(self.on_dl_all_success)
        self.dl_all_thread.error.connect(self.on_dl_all_fail)
        self.dl_all_thread.start()
        
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

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyDownloader()
    window.show()
    sys.exit(app.exec())