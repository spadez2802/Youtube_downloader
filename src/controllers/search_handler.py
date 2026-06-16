import json
from PySide6.QtCore import Qt, QSize
from PySide6.QtWidgets import QListWidgetItem, QWidget, QMessageBox
from PySide6.QtGui import QPixmap, QGuiApplication
from models.thread_fetch_info import FetchInfoThread
from views.custom_widgets import VideoItemWidget

# IMPORT GIAO DIỆN LỊCH SỬ CŨ CHO DROPDOWN AUTOCLETE
from views.history_item1_5 import Ui_historyItm

# IMPORT GIAO DIỆN LỊCH SỬ MỚI CHO SIDEBAR TRÁI
from views.ui_history_ver2_0 import Ui_FormHistoryItem

# ==========================================================
# WIDGET CARD LỊCH SỬ SIDEBAR TRÁI (DÙNG UI_HISTORY_VER1_0)
# ==========================================================
class HistoryCard(QWidget):
    def __init__(self, title, url, time_str, parent_handler):
        super().__init__()
        self.ui = Ui_FormHistoryItem()
        self.ui.setupUi(self)
        
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        
        self.url = url
        self.parent_handler = parent_handler
        
        # Dùng fontMetrics để tính toán chiều dài pixel chuẩn xác cho 2 dòng (~270px)
        fm = self.ui.labelName.fontMetrics()
        display_title = fm.elidedText(title, Qt.TextElideMode.ElideRight, 270)
        
        # Điền tiêu đề và thời gian lưu
        self.ui.labelName.setText(display_title)
        self.ui.labelDate.setText(time_str if time_str else "Vừa xong")
        
        # Cho phép labelName tự động xuống dòng và widget thay đổi chiều cao
        self.ui.labelName.setWordWrap(True)
        
        # Đảm bảo labelName chiếm hết không gian trống để nút Option không bị đẩy
        from PySide6.QtWidgets import QSizePolicy
        policy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        self.ui.labelName.setSizePolicy(policy)
        
        # Bỏ giới hạn chiều cao cũ
        self.ui.widget.setMaximumHeight(16777215)
        self.setMaximumHeight(16777215)
        self.ui.labelName.setMinimumHeight(0)
        self.ui.widget.setMinimumHeight(0)
        self.setMinimumHeight(0)

        # Cập nhật style
        self.setStyleSheet("""
            HistoryCard:hover {
                background-color: #3e3e3e;
                border-radius: 4px;
            }
        """)

        # Gán bộ lắng nghe chuột
        self.ui.labelName.setCursor(Qt.CursorShape.PointingHandCursor)
        self.ui.labelDate.setCursor(Qt.CursorShape.PointingHandCursor)
        self.ui.cbbOpt.setCursor(Qt.CursorShape.PointingHandCursor)
        
        # Thiết lập QMenu cho QToolButton
        from PySide6.QtWidgets import QMenu
        from PySide6.QtGui import QAction
        
        self.opt_menu = QMenu(self)
        self.opt_menu.setStyleSheet("""
            QMenu {
                background-color: #212121;
                border: 1px solid #3d3d3d;
                border-radius: 6px;
                padding: 4px 0px;
                color: #e0e0e0;
            }
            QMenu::item {
                padding: 8px 24px 8px 24px;
                font-family: "Segoe UI", sans-serif;
                font-size: 13px;
                background-color: transparent;
            }
            QMenu::item:selected {
                background-color: #3d3d3d;
            }
        """)
        
        # Thêm 2 option hiện có
        self.act_copy = QAction("Copy link", self)
        self.act_delete = QAction("Delete from history", self)
        
        self.opt_menu.addAction(self.act_copy)
        self.opt_menu.addAction(self.act_delete)
        
        self.ui.cbbOpt.setMenu(self.opt_menu)
        
        self.act_copy.triggered.connect(self.copy_url)
        self.act_delete.triggered.connect(self.delete_item)
        
        # Click vào text để tự động tìm kiếm
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
        from PySide6.QtWidgets import QStyleOption, QStyle
        from PySide6.QtGui import QPainter
        opt = QStyleOption()
        opt.initFrom(self)
        p = QPainter(self)
        self.style().drawPrimitive(QStyle.PrimitiveElement.PE_Widget, opt, p, self)

# ==========================================================
# WIDGET LỊCH SỬ DÙNG FILE UI CỦA BẠN (CŨ CHO AUTOCLETE DROPDOWN)
# ==========================================================
class HistoryItemWidget(QWidget):
    def __init__(self, title, url, parent_handler):
        super().__init__()
        self.ui = Ui_historyItm()
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
        self.refresh_left_history_sidebar()

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
        self.refresh_left_history_sidebar()
        
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
                # Kết nối sự kiện checkbox thay đổi để cập nhật chữ trên nút Download All / Download
                item_widget.ui.checkBoxDownload.stateChanged.connect(self.main.update_download_all_btn_text)
                self.main.scroll_layout.addWidget(item_widget, 0, Qt.AlignmentFlag.AlignHCenter)
            
            # Cập nhật chữ nút Download All khi vừa nạp xong
            self.main.update_download_all_btn_text()
                
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

    def refresh_left_history_sidebar(self):
        # 1. Dọn dẹp các card cũ trong container
        if hasattr(self.main, 'history_layout') and self.main.history_layout:
            while self.main.history_layout.count():
                item = self.main.history_layout.takeAt(0)
                if item.widget():
                    item.widget().deleteLater()
                    
            # 2. Tạo card mới cho từng lịch sử từ dữ liệu RAM
            for item in self.main.history_data:
                title = item.get('title', '')
                url = item.get('url', '')
                time_str = item.get('time', 'Đã lưu')
                
                card = HistoryCard(title, url, time_str, self)
                # Kết nối sự kiện checkbox
                card.ui.checkBox.stateChanged.connect(self.update_history_delete_btn_state)
                self.main.history_layout.addWidget(card)

        # 3. Cập nhật trạng thái nút Delete
        self.update_history_delete_btn_state()

    def update_history_delete_btn_state(self):
        total = 0
        checked = 0
        if hasattr(self.main, 'history_layout') and self.main.history_layout:
            total = self.main.history_layout.count()
            for i in range(total):
                item = self.main.history_layout.itemAt(i)
                if item and item.widget():
                    if item.widget().ui.checkBox.isChecked():
                        checked += 1

        # Cập nhật Checkbox tổng
        self.main.ui.checkBox.blockSignals(True)
        if total == 0:
            self.main.ui.checkBox.setEnabled(False)
            self.main.ui.checkBox.setChecked(False)
        else:
            self.main.ui.checkBox.setEnabled(True)
            self.main.ui.checkBox.setChecked(checked == total and total > 0)
        self.main.ui.checkBox.blockSignals(False)

        # Cập nhật nút Delete
        btn = self.main.ui.pushButton
        
        btn.setStyleSheet("""
            QPushButton {
                border: 2px solid;
                border-color: #1ED761;
                border-radius:12px;
                background-color: rgb(67, 67, 67);
                color : white;
                padding: 2px 10px;
                font-family: "Segoe UI", sans-serif;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color:#1ED761;
                color : black;
            }
            QPushButton:disabled {
                border-color: rgb(136, 136, 136);
                background-color:rgb(67, 67, 67);
                color : #888888;
            }
        """)

        if checked == 0:
            btn.setEnabled(False)
            btn.setText("Delete")
        else:
            btn.setEnabled(True)
            if checked == total:
                btn.setText("Delete All")
            else:
                btn.setText("Delete")

    def toggle_all_history_ticks(self, state):
        is_checked = (state == 2) # Qt.CheckState.Checked
        if hasattr(self.main, 'history_layout') and self.main.history_layout:
            for i in range(self.main.history_layout.count()):
                item = self.main.history_layout.itemAt(i)
                if item and item.widget():
                    item.widget().ui.checkBox.setChecked(is_checked)
        self.update_history_delete_btn_state()

    def load_history_url(self, url):
        self.ui.enterPlace.setText(url)
        self.handle_find()
        # Tự động đóng sidebar lịch sử sau khi click để giao diện gọn gàng
        if self.main.ui.historyList.isVisible():
            self.main.ui_handler.toggle_history_sidebar()

    def delete_selected_history_items(self):
        urls_to_delete = []
        if hasattr(self.main, 'history_layout') and self.main.history_layout:
            for i in range(self.main.history_layout.count()):
                item = self.main.history_layout.itemAt(i)
                if item and item.widget():
                    if item.widget().ui.checkBox.isChecked():
                        urls_to_delete.append(item.widget().url)
                        
        if not urls_to_delete:
            return

        # Hiển thị hộp thoại xác nhận (Confirm Dialog)
        msg_box = QMessageBox(self.main)
        msg_box.setWindowTitle("Xác nhận xóa")
        if len(urls_to_delete) == len(self.main.history_data):
            msg_box.setText("Bạn có chắc chắn muốn xóa toàn bộ lịch sử không?")
        else:
            msg_box.setText(f"Bạn có chắc chắn muốn xóa {len(urls_to_delete)} mục đã chọn không?")
        msg_box.setIcon(QMessageBox.Icon.Question)
        msg_box.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        msg_box.setDefaultButton(QMessageBox.StandardButton.No)
        
        # Style cho QMessageBox phù hợp với giao diện tối
        msg_box.setStyleSheet("""
            QMessageBox {
                background-color: #2b2b2b;
            }
            QLabel {
                color: white;
                font-family: "Segoe UI", sans-serif;
                font-size: 11pt;
            }
            QPushButton {
                border: 2px solid #1ED761;
                border-radius: 12px;
                background-color: rgb(67, 67, 67);
                color: white;
                padding: 4px 15px;
                font-family: "Segoe UI", sans-serif;
                font-weight: bold;
                min-width: 60px;
            }
            QPushButton:hover {
                background-color: #1ED761;
                color: black;
            }
        """)

        if msg_box.exec() != QMessageBox.StandardButton.Yes:
            return

        self.main.history_data = [item for item in self.main.history_data if item['url'] not in urls_to_delete]
        
        try:
            with open(self.main.history_manager.get_history_path(), 'w', encoding='utf-8') as f:
                json.dump(self.main.history_data, f, ensure_ascii=False, indent=4)
        except Exception as e:
            print(f"Lỗi xóa lịch sử: {e}")
            
        self.on_text_changed(self.ui.enterPlace.text())
        self.refresh_left_history_sidebar()

    def clear_all_history(self):
        self.main.history_data = []
        try:
            with open(self.main.history_manager.get_history_path(), 'w', encoding='utf-8') as f:
                json.dump([], f, ensure_ascii=False, indent=4)
        except Exception as e:
            print(f"Lỗi xóa toàn bộ lịch sử: {e}")
        self.refresh_left_history_sidebar()