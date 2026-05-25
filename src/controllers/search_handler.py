import json
from PySide6.QtCore import Qt, QSize
from PySide6.QtWidgets import QListWidgetItem, QWidget
from PySide6.QtGui import QPixmap
from models.thread_fetch_info import FetchInfoThread
from views.custom_widgets import VideoItemWidget

# IMPORT GIAO DIỆN BẠN VỪA TẠO (Giả sử file tên là history_item.py nằm trong views)
from views.history_item1_5 import Ui_historyItm

# ==========================================================
# WIDGET LỊCH SỬ DÙNG FILE UI CỦA BẠN
# ==========================================================
class HistoryItemWidget(QWidget):
    def __init__(self, title, url, parent_handler):
        super().__init__()
        # Khởi tạo giao diện từ file của bạn
        self.ui = Ui_historyItm()
        self.ui.setupUi(self)
        
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setStyleSheet("background: transparent;")

        self.url = url
        self.parent_handler = parent_handler
        
        # 1. Điền tên bài hát vào label bạn đã tạo
        self.ui.label.setText(title)
        
        # Cực kỳ quan trọng: Cho phép click chuột xuyên qua chữ để ListWidget nhận diện được hành động chọn bài
        self.ui.label.setAttribute(Qt.WidgetAttribute.WA_TransparentForMouseEvents) 
        
        # 2. Kết nối nút Xóa (deleteHistoryBtn) bạn đã tạo với hàm xóa
        self.ui.deleteHistoryBtn.setCursor(Qt.CursorShape.PointingHandCursor)
        self.ui.deleteHistoryBtn.clicked.connect(self.delete_item)

    def delete_item(self):
        # Gọi lệnh xóa
        self.parent_handler.delete_history_item(self.url)


# ==========================================================
# BỘ XỬ LÝ TÌM KIẾM CHÍNH
# ==========================================================
class SearchHandler:
    def __init__(self, main_window):
        self.main = main_window
        self.ui = main_window.ui

    def on_text_changed(self, text):
        self.ui.clearBtn.setVisible(bool(text.strip()))
        self.ui.listWidget.clear()
        search_text = text.lower().strip()
        
        matched = [i for i in self.main.history_data if not search_text or search_text in i['title'].lower()][:8 if search_text else 5]
        
        if not matched:
            self.ui.listWidget.setVisible(False)
            self.ui.listWidget.setMinimumHeight(0)
            self.ui.listWidget.setMaximumHeight(0)
            return

        self.ui.listWidget.setVisible(True)
        for item in matched:
            li = QListWidgetItem()
            # Giấu URL ngầm vào item để click biết đường mà load
            li.setData(Qt.ItemDataRole.UserRole, item['url'])
            
            # File UI của bạn set max_height=48, min=40. Mình set cứng dòng là 45px cho đẹp
            li.setSizeHint(QSize(0, 40)) 
            
            # Gắn cái giao diện Ui_historyItm của bạn vào dòng
            custom_widget = HistoryItemWidget(item['title'], item['url'], self)
            self.ui.listWidget.addItem(li)
            self.ui.listWidget.setItemWidget(li, custom_widget)
        
        # Nới chiều cao dựa vào số lượng lịch sử đang hiển thị (mỗi dòng 45px)
        h = len(matched) * 40 + 15
        self.ui.listWidget.setMinimumHeight(h)
        self.ui.listWidget.setMaximumHeight(h)

    def delete_history_item(self, url):
        # 1. Xóa khỏi RAM tạm thời
        self.main.history_data = [item for item in self.main.history_data if item['url'] != url]
        
        # 2. Xóa vĩnh viễn khỏi file history.json
        try:
            with open(self.main.history_manager.get_history_path(), 'w', encoding='utf-8') as f:
                json.dump(self.main.history_data, f, ensure_ascii=False, indent=4)
        except Exception as e:
            print(f"Lỗi xóa lịch sử: {e}")
            
        # 3. F5 cập nhật lại giao diện danh sách ngay lập tức
        self.on_text_changed(self.ui.enterPlace.text())

    def handle_find(self):
        url = self.ui.enterPlace.text().strip()
        if not url: return
        
        self.ui.findBtn.setEnabled(False)
        self.ui.downloadBtn.setEnabled(False)
        self.ui.comboBoxDownloadOption.setEnabled(False) 
        self.ui.comboBoxDownloadQuality.setEnabled(False) 
        self.ui.videoImg.setText("Loading...")
        
        self.main.fetch_thread = FetchInfoThread(url, self.main.YDL_OPTIONS)
        self.main.fetch_thread.finished.connect(self.on_fetch_success)
        self.main.fetch_thread.error.connect(self.on_fetch_fail)
        self.main.fetch_thread.start()

    def on_fetch_success(self, data):
        self.ui.findBtn.setEnabled(True)
        self.ui.downloadBtn.setEnabled(True)
        self.ui.comboBoxDownloadOption.setEnabled(True)
        
        # --- FIX: LƯU TRẠNG THÁI PLAYLIST VÀO MAIN ĐỂ DÙNG CHUNG ---
        self.main.current_is_playlist = data['is_playlist']
        
        # --- FIX: BƠM DỮ LIỆU VÀ XỬ LÝ BẬT/TẮT NÚT CHẤT LƯỢNG ---
        self.ui.comboBoxDownloadQuality.clear()
        if not data['is_playlist']:
            # Nếu là Video lẻ -> Bơm các độ phân giải quét được vào
            self.ui.comboBoxDownloadQuality.addItems(data['resolutions'])
        else:
            # Nếu là Playlist -> Chỉ để chữ Best
            self.ui.comboBoxDownloadQuality.addItem("Best")
            
        # Kiểm tra xem có đang chọn MP4 hay không
        is_mp4 = self.ui.comboBoxDownloadOption.currentText() == "MP4"
        
        # CHỈ BẬT NÚT KHI: Đang chọn MP4 VÀ không phải là Playlist
        if is_mp4 and not data['is_playlist']:
            self.ui.comboBoxDownloadQuality.setEnabled(True)
        else:
            self.ui.comboBoxDownloadQuality.setEnabled(False)
        # -----------------------------------------------------------

        self.main.current_video_title = data['title']
        self.ui.linkName.setText(data['title'])
        
        # Lưu lịch sử
        self.main.history_data = self.main.history_manager.save_history(data['title'], data['url'], data['is_playlist'])
        
        # Hiển thị ảnh
        if data['img_data']:
            px = QPixmap()
            px.loadFromData(data['img_data'])
            self.ui.videoImg.setPixmap(px.scaled(self.ui.videoImg.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))

        # Đổ dữ liệu vào Sidebar
        self.main.clear_scroll_area()
        if data['is_playlist']:
            for entry in data['entries']:
                item_widget = VideoItemWidget(entry['title'], entry['url'], entry['thumbnail'])
                self.main.scroll_layout.addWidget(item_widget, 0, Qt.AlignmentFlag.AlignHCenter)
                
            if self.ui.sideBarWidget.width() < 500: 
                self.main.ui_handler.toggle_sidebar()
        else:
            if self.ui.sideBarWidget.width() >= 500:
                self.main.ui_handler.toggle_sidebar()
        
        self.ui.miniSideBarBtn.setEnabled(data['is_playlist'])

    def on_fetch_fail(self, err):
        self.ui.findBtn.setEnabled(True)
        self.ui.downloadBtn.setEnabled(False) 
        self.ui.comboBoxDownloadOption.setEnabled(False)
        self.ui.comboBoxDownloadQuality.setEnabled(False)
        self.ui.linkName.setText("Error: Link không hợp lệ")

    def on_history_item_clicked(self, item):
        url = item.data(Qt.ItemDataRole.UserRole)
        self.ui.enterPlace.setText(url) 
        self.ui.listWidget.setVisible(False) 
        self.handle_find()