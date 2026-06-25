import json
import datetime
from PySide6.QtCore import Qt, QSize
from PySide6.QtWidgets import QListWidgetItem, QWidget, QMessageBox, QLabel, QSizePolicy
from PySide6.QtGui import QPixmap, QGuiApplication
from models.thread_fetch_info import FetchInfoThread

# --- IMPORT WIDGETS TỪ VIEWS (ĐÚNG THEO MVC) ---
# HistoryCard và HistoryItemWidget là View components → thuộc views/custom_widgets.py
from views.custom_widgets import VideoItemWidget, HistoryCard, HistoryItemWidget

# IMPORT GIAO DIỆN LỊCH SỬ TỪ CẤU HÌNH UI_CONFIG.PY ĐỂ KHÔNG BỊ FIX CỨNG PHIÊN BẢN
from views.ui_config import Ui_HistorySidebar, Ui_HistoryDropdown


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
            
            # Thêm prefix [Video]/[Playlist] vào tiêu đề hiển thị trong dropdown
            item_type = item.get('type', 'video')
            prefix = "[Playlist] " if item_type == 'playlist' else "[Video] "
            display_title = prefix + item['title']
            
            # Gắn cái giao diện Ui_historyItm của bạn vào dòng
            custom_widget = HistoryItemWidget(display_title, item['url'], self)
            self.ui.listWidget.addItem(li)
            self.ui.listWidget.setItemWidget(li, custom_widget)
        
        # Nới chiều cao dựa vào số lượng lịch sử đang hiển thị (mỗi dòng 45px)
        h = len(matched) * 40 + 15
        self.ui.listWidget.setMinimumHeight(h)
        self.ui.listWidget.setMaximumHeight(h)

    def delete_history_item(self, url):
        # Ủy quyền xóa cho HistoryManager (Model) thay vì tự thào tác file
        self.main.history_data = self.main.history_manager.delete_items([url])
        # Cập nhật giao diện
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
                    
            # 2. Nhóm item theo ngày, tạo header ngày + các card bên dưới
            today = datetime.date.today()
            yesterday = today - datetime.timedelta(days=1)
            last_date_str = None

            for item in self.main.history_data:
                title = item.get('title', '')
                url = item.get('url', '')
                time_str = item.get('time', '')
                item_type = item.get('type', 'video')
                
                # Xác định ngày của item
                item_date_str = ""
                if time_str:
                    parts = time_str.strip().split(' ')
                    if len(parts) >= 1:
                        item_date_str = parts[0]  # "YYYY-MM-DD"
                
                # Tạo header ngày nếu ngày mới
                if item_date_str and item_date_str != last_date_str:
                    last_date_str = item_date_str
                    try:
                        item_date = datetime.date.fromisoformat(item_date_str)
                        if item_date == today:
                            prefix = "Today"
                        elif item_date == yesterday:
                            prefix = "Yesterday"
                        else:
                            prefix = item_date.strftime("%d/%m/%Y")
                        # Format: "Today - Tuesday, June 16, 2026"
                        day_name = item_date.strftime("%A, %B %d, %Y")
                        header_text = f"{prefix} - {day_name}"
                    except Exception:
                        header_text = item_date_str
                    
                    header_label = QLabel(header_text)
                    header_label.setStyleSheet(
                        "color: #cccccc; font-weight: bold; font-size: 11px; "
                        "padding: 8px 6px 4px 6px; background: transparent;"
                    )
                    header_label.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
                    self.main.history_layout.addWidget(header_label)
                
                card = HistoryCard(title, url, time_str, self, item_type=item_type)
                # Kết nối sự kiện checkbox
                card.ui.checkBox.stateChanged.connect(self.update_history_delete_btn_state)
                self.main.history_layout.addWidget(card)

        # 3. Cập nhật trạng thái nút Delete
        self.update_history_delete_btn_state()

    def update_history_delete_btn_state(self):
        total = 0
        checked = 0
        if hasattr(self.main, 'history_layout') and self.main.history_layout:
            for i in range(self.main.history_layout.count()):
                item = self.main.history_layout.itemAt(i)
                if item and item.widget() and isinstance(item.widget(), HistoryCard):
                    total += 1
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
                if item and item.widget() and isinstance(item.widget(), HistoryCard):
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
                if item and item.widget() and isinstance(item.widget(), HistoryCard):
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


        if msg_box.exec() != QMessageBox.StandardButton.Yes:
            return

        # Ủy quyền xóa cho HistoryManager (Model)
        self.main.history_data = self.main.history_manager.delete_items(urls_to_delete)
        self.on_text_changed(self.ui.enterPlace.text())
        self.refresh_left_history_sidebar()

    def clear_all_history(self):
        # Ủy quyền xóa cho HistoryManager (Model)
        self.main.history_data = self.main.history_manager.clear_all()
        self.refresh_left_history_sidebar()