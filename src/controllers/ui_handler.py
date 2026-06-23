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

        # --- LÀM TO 3 DẤU CHẤM (...) BẰNG KÝ TỰ TRÒN UNICODE HẢI-FI (● ● ●) ---
        # Thay thế dấu "." truyền thống thành dấu chấm tròn đặc sắc nét và to lớn hơn
        self.ui.menuAAA.setTitle("● ● ●") 
        


        self.ui.actionHistory.setCheckable(True)



        # --- FIX 2: THÊM LOGO APP (GÓC TRÁI MÀN HÌNH & TASKBAR) ---
        # Zun hãy kiểm tra xem trong thư mục img/icon/ đã có file logo chưa nhé.
        # Mình giả định file logo tên là 'app_logo.png' nằm trong img/icon/.
        # Nếu tên file khác, bạn hãy sửa lại dòng dưới đây cho khớp.
        app_icon_path = get_asset_path("img/icon/app_logo.png")
        self.main.setWindowIcon(QIcon(app_icon_path))



        # (Giữ nguyên các phần styling khác...)
        self.main.setCursor(Qt.CursorShape.ArrowCursor)
        self.ui.centralwidget.setCursor(Qt.CursorShape.ArrowCursor)
        self.ui.scrollArea.setWidgetResizable(True)
        self.ui.scrollArea.setFrameShape(QFrame.NoFrame)
        
        self.ui.clearBtn.setText("✕") 
        self.ui.clearBtn.setVisible(False) 

        # Mở khóa chiều cao và chiều rộng để tránh bị chèn khi cả 2 sidebar cùng mở
        self.main.setMaximumHeight(16777215)
        self.main.setMaximumWidth(16777215)
        self.ui.centralwidget.setMaximumHeight(16777215)
        self.ui.centralwidget.setMaximumWidth(16777215)
        self.ui.widget_3.setMaximumHeight(16777215) 
        self.ui.sideBarWidget.setMaximumHeight(16777215)
        self.ui.widget.setMaximumHeight(16777215)
        self.ui.widget_9.setMaximumHeight(16777215)
        self.ui.widget_6.setMaximumHeight(16777215)
        # --- FIX LỖI TÀNG HÌNH WIDGET CON (BỔ SUNG 2 DÒNG NÀY) ---
        self.ui.scrollArea.setMaximumSize(16777215, 16777215)
        self.ui.scrollAreaWidgetContents.setMaximumSize(16777215, 16777215)

        # --- CẤU HÌNH GIAO DIỆN SIDEBAR BÊN TRÁI (historyList) ---
        self.ui.historyList.setMinimumWidth(250)
        self.ui.historyList.setMaximumWidth(250)
        self.ui.historyList.setStyleSheet("""
            QScrollArea {
                border: none;
                background-color: #2b2b2b;
                border-right: 1px solid #3e3e3e;
            }
        """)
        
        # Sửa lỗi căn lề tuyệt đối (absolute positioning) của Qt Designer trên sidebar trái
        from PySide6.QtWidgets import QVBoxLayout
        if not self.ui.scrollAreaWidgetContents_2.layout():
            layout_left = QVBoxLayout(self.ui.scrollAreaWidgetContents_2)
            layout_left.setContentsMargins(10, 10, 10, 10)
            layout_left.setSpacing(0)
            layout_left.addWidget(self.ui.widget_12)
            layout_left.setAlignment(Qt.AlignmentFlag.AlignTop)
            
        self.ui.verticalLayout_8.setAlignment(Qt.AlignmentFlag.AlignTop)

        # Ẩn plainTextEdit (chữ nhật xám placeholder) để dọn đường nạp danh sách card động
        self.ui.plainTextEdit.setVisible(False)
        
        # Tạo widget container và layout để chứa các card lịch sử động
        from PySide6.QtWidgets import QWidget
        self.main.history_container = QWidget(self.ui.widget_12)
        self.main.history_layout = QVBoxLayout(self.main.history_container)
        self.main.history_layout.setContentsMargins(0, 0, 0, 0)
        self.main.history_layout.setSpacing(10)
        self.main.history_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        
        # Thêm container vào verticalLayout_8 của widget_12 (dưới widget_7 chứa nút bấm)
        self.ui.verticalLayout_8.addWidget(self.main.history_container)

        self.ui.horizontalLayout_2.setAlignment(self.ui.sideBarWidget, Qt.AlignmentFlag(0))
        self.ui.sideBarWidget.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        self.ui.horizontalLayout_2.setSpacing(0)
        self.ui.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        
        # Cập nhật chỉ số chèn stretch sang 2 (giữa widget_3 và sideBarWidget) để widget_3 ở trung tâm
        self.ui.horizontalLayout_2.insertStretch(2, 1)

        self.ui.verticalLayout_4.setAlignment(self.ui.scrollArea, Qt.AlignmentFlag(0))
        self.ui.scrollArea.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.ui.verticalLayout_4.setStretchFactor(self.ui.scrollArea, 1)

    def init_state(self):
        # --- THIẾT LẬP HISTORY SIDEBAR GỐC ---
        self.ui.historyList.setStyleSheet("QScrollArea { border-right: 2px solid #1ED761; background-color: #2b2b2b; }")
        self.ui.historyList.setMaximumWidth(0)
        self.ui.historyList.setMinimumWidth(0)
        self.ui.historyList.setVisible(False)
        self.ui.scrollAreaWidgetContents_2.setMinimumWidth(250)
        self.ui.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)

        self.ui.downloadAllBtn.setVisible(False)
        self.ui.comboBoxDownloadAllOpt.setVisible(False)
        self.ui.scrollArea.setVisible(False)
        self.ui.widget_11.setVisible(False)
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
        
        # Căn giữa màn hình và dịch sang trái một chút (100px) để không bị che khi mở full các pane
        from PySide6.QtGui import QGuiApplication
        screen = QGuiApplication.primaryScreen()
        if screen:
            screen_geo = screen.availableGeometry()
            x = screen_geo.center().x() - (730 // 2) - 100
            # Đảm bảo x không bị âm (không bị lọt ra ngoài mép trái)
            if x < 0:
                x = 0
            y = screen_geo.center().y() - (650 // 2)
            self.main.move(x, y)
        
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
        self.ui.widget_11.setVisible(is_opening)
        
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

    def toggle_history_sidebar(self):
        from PySide6.QtCore import QSize
        is_visible = self.ui.historyList.isVisible() and self.ui.historyList.width() > 0
        
        if not is_visible:
            self.ui.actionHistory.setChecked(True)
            self.ui.historyList.setVisible(True)
            
            current_geo = self.main.geometry()
            from PySide6.QtCore import QRect
            self.anim_win = QPropertyAnimation(self.main, b"geometry")
            self.anim_win.setDuration(250)
            self.anim_win.setEasingCurve(QEasingCurve.OutQuart)
            self.anim_win.setEndValue(QRect(current_geo.x() - 250, current_geo.y(), current_geo.width() + 250, current_geo.height()))
            self.anim_win.start()
            
            self.anim_history_min = QPropertyAnimation(self.ui.historyList, b"minimumWidth")
            self.anim_history_min.setDuration(250)
            self.anim_history_min.setEasingCurve(QEasingCurve.OutQuart)
            self.anim_history_min.setEndValue(250)
            self.anim_history_min.start()
            
            self.anim_history_max = QPropertyAnimation(self.ui.historyList, b"maximumWidth")
            self.anim_history_max.setDuration(250)
            self.anim_history_max.setEasingCurve(QEasingCurve.OutQuart)
            self.anim_history_max.setEndValue(250)
            self.anim_history_max.start()
        else:
            self.ui.actionHistory.setChecked(False)
            current_geo = self.main.geometry()
            from PySide6.QtCore import QRect
            self.anim_win = QPropertyAnimation(self.main, b"geometry")
            self.anim_win.setDuration(250)
            self.anim_win.setEasingCurve(QEasingCurve.InQuart)
            self.anim_win.setEndValue(QRect(current_geo.x() + 250, current_geo.y(), current_geo.width() - 250, current_geo.height()))
            self.anim_win.start()
            
            self.anim_history_min = QPropertyAnimation(self.ui.historyList, b"minimumWidth")
            self.anim_history_min.setDuration(250)
            self.anim_history_min.setEasingCurve(QEasingCurve.InQuart)
            self.anim_history_min.setEndValue(0)
            self.anim_history_min.finished.connect(self.ui.historyList.hide)
            self.anim_history_min.start()
            
            self.anim_history_max = QPropertyAnimation(self.ui.historyList, b"maximumWidth")
            self.anim_history_max.setDuration(250)
            self.anim_history_max.setEasingCurve(QEasingCurve.InQuart)
            self.anim_history_max.setEndValue(0)
            self.anim_history_max.start()