import os
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QDialog, QFileDialog, QColorDialog, QMessageBox, QApplication
from PySide6.QtGui import QColor, QIcon

from views.ui_config import Ui_SettingsDialog
from utils.helpers import get_asset_path
from utils.theme_manager import ThemeManager


class SettingsDialog(QDialog):
    """
    Controller cho dialog Cài Đặt — theo kiến trúc MVC.
    - View:  Ui_SettingsDialog (được generate từ ui/settings_dialog.ui)
    - Model: SettingsManager
    - Controller: class này — chỉ điều phối tín hiệu UI ↔ Model, không chứa code tạo widget.
    """

    def __init__(self, parent, settings_manager, search_handler=None):
        super().__init__(parent)
        self.settings_manager = settings_manager
        self.search_handler = search_handler

        # --- Nạp View từ ui_config (đúng theo Wrapper Pattern) ---
        self.ui = Ui_SettingsDialog()
        self.ui.setupUi(self)

        self.setModal(True)

        app_icon_path = get_asset_path("img/icon/app_logo.png")
        self.setWindowIcon(QIcon(app_icon_path))

        # Màu accent đang được preview (trước khi lưu)
        self._accent_preview = self.settings_manager.get("accent_color", "#1ED761")

        # Đặt objectName để CSS selector #btnSave hoạt động
        self.ui.btnSave.setObjectName("btnSave")

        self._setup_connections()
        self._apply_style()
        self._load_values()

    # ------------------------------------------------------------------
    # KẾT NỐI SIGNALS & SLOTS
    # ------------------------------------------------------------------
    def _setup_connections(self):
        self.ui.btnAccentPreview.clicked.connect(self._pick_accent_color)
        self.ui.cmbFormat.currentTextChanged.connect(self._on_format_changed)
        self.ui.chkDefaultPath.toggled.connect(self._on_default_path_toggled)
        self.ui.btnChangePath.clicked.connect(self._pick_download_path)
        self.ui.btnClearHistory.clicked.connect(self._clear_history)
        self.ui.btnCancel.clicked.connect(self.reject)
        self.ui.btnSave.clicked.connect(self._save_and_close)

        # Con trỏ chuột
        self.ui.btnAccentPreview.setCursor(Qt.CursorShape.PointingHandCursor)
        self.ui.cmbFormat.setCursor(Qt.CursorShape.PointingHandCursor)
        self.ui.cmbQuality.setCursor(Qt.CursorShape.PointingHandCursor)
        self.ui.cmbBitrate.setCursor(Qt.CursorShape.PointingHandCursor)
        self.ui.btnChangePath.setCursor(Qt.CursorShape.PointingHandCursor)
        self.ui.btnClearHistory.setCursor(Qt.CursorShape.PointingHandCursor)
        self.ui.btnCancel.setCursor(Qt.CursorShape.PointingHandCursor)
        self.ui.btnSave.setCursor(Qt.CursorShape.PointingHandCursor)

    # ------------------------------------------------------------------
    # NẠP GIÁ TRỊ TỪ MODEL (SettingsManager)
    # ------------------------------------------------------------------
    def _load_values(self):
        sm = self.settings_manager
        # Tab General
        self._update_accent_btn(sm.get("accent_color", "#1ED761"))
        self.ui.chkSubfolder.setChecked(sm.get("create_subfolder_for_playlist", True))
        self.ui.chkOpenAfter.setChecked(sm.get("open_folder_after_download", False))
        self.ui.cmbFormat.setCurrentText(sm.get("default_format", "MP4"))
        self.ui.cmbQuality.setCurrentText(sm.get("default_quality", "1080p"))
        self.ui.cmbBitrate.setCurrentText(sm.get("default_bitrate", "192kbps"))
        # Tab Advanced
        use_default = sm.get("use_default_path", False)
        self.ui.chkDefaultPath.setChecked(use_default)
        self.ui.txtPath.setText(sm.get("download_path", ""))
        self.ui.chkOriginalName.setChecked(sm.get("use_original_name", True))
        # Khởi tạo trạng thái enable/disable
        self._on_default_path_toggled(use_default)
        self._on_format_changed(sm.get("default_format", "MP4"))

    # ------------------------------------------------------------------
    # EVENT HANDLERS
    # ------------------------------------------------------------------
    def _on_format_changed(self, text):
        is_mp4 = (text == "MP4")
        self.ui.lblQuality.setEnabled(is_mp4)
        self.ui.cmbQuality.setEnabled(is_mp4)
        self.ui.lblBitrate.setEnabled(not is_mp4)
        self.ui.cmbBitrate.setEnabled(not is_mp4)

    def _on_default_path_toggled(self, checked):
        self.ui.txtPath.setEnabled(checked)
        self.ui.btnChangePath.setEnabled(checked)
        self.ui.chkOriginalName.setEnabled(checked)

    def _pick_accent_color(self):
        color = QColorDialog.getColor(
            QColor(self._accent_preview), self, "Chọn màu Accent"
        )
        if color.isValid():
            self._accent_preview = color.name()
            self._update_accent_btn(self._accent_preview)

    def _update_accent_btn(self, hex_color: str):
        self._accent_preview = hex_color
        self.ui.btnAccentPreview.setStyleSheet(
            f"QPushButton {{ background-color: {hex_color}; border: 2px solid #555; border-radius: 4px; }}"
            f"QPushButton:hover {{ border: 2px solid #fff; }}"
        )

    def _pick_download_path(self):
        folder = QFileDialog.getExistingDirectory(self, "Chọn thư mục tải xuống mặc định")
        if folder:
            self.ui.txtPath.setText(folder)

    def _clear_history(self):
        if not self.search_handler:
            return
        reply = QMessageBox.question(
            self, "Xác nhận",
            "Bạn có chắc muốn xóa toàn bộ lịch sử không?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No
        )
        if reply == QMessageBox.StandardButton.Yes:
            self.search_handler.clear_all_history()
            QMessageBox.information(self, "Thành công", "Đã xóa toàn bộ lịch sử.")

    def _save_and_close(self):
        # Validate: nếu use_default_path mà đường dẫn trống thì cảnh báo
        if self.ui.chkDefaultPath.isChecked() and not self.ui.txtPath.text().strip():
            QMessageBox.warning(
                self, "Thiếu thông tin",
                "Bạn đã bật 'Sử dụng đường dẫn mặc định' nhưng chưa chọn thư mục.\n"
                "Vui lòng chọn thư mục trước khi lưu."
            )
            self.ui.tabWidget.setCurrentIndex(1)  # chuyển sang tab Advanced
            return

        sm = self.settings_manager
        sm.set("accent_color", self._accent_preview)
        sm.set("create_subfolder_for_playlist", self.ui.chkSubfolder.isChecked())
        sm.set("open_folder_after_download", self.ui.chkOpenAfter.isChecked())
        sm.set("default_format", self.ui.cmbFormat.currentText())
        sm.set("default_quality", self.ui.cmbQuality.currentText())
        sm.set("default_bitrate", self.ui.cmbBitrate.currentText())
        sm.set("use_default_path", self.ui.chkDefaultPath.isChecked())
        sm.set("download_path", self.ui.txtPath.text().strip())
        sm.set("use_original_name", self.ui.chkOriginalName.isChecked())
        sm.save()

        # Apply accent color ngay lập tức
        tm = ThemeManager()
        tm.apply(QApplication.instance(), self._accent_preview)

        self.accept()

    # ------------------------------------------------------------------
    # STYLE (áp dụng qua stylesheet — không tạo widget ở đây)
    # ------------------------------------------------------------------
    def _apply_style(self):
        self.setStyleSheet("""
            QDialog {
                background-color: #1a1a1a;
                color: #ffffff;
                font-family: 'Segoe UI', Helvetica, Arial, sans-serif;
                font-size: 13px;
            }
            QTabWidget::pane {
                border: none;
                background-color: #1a1a1a;
            }
            QTabBar::tab {
                background: #2b2b2b;
                color: #aaaaaa;
                padding: 8px 20px;
                border: none;
                font-size: 13px;
            }
            QTabBar::tab:selected {
                background: #1a1a1a;
                color: #ffffff;
                border-bottom: 2px solid #1ED761;
            }
            QTabBar::tab:hover:!selected {
                background: #333333;
                color: #ffffff;
            }
            QGroupBox {
                border: 1px solid #3e3e3e;
                border-radius: 6px;
                margin-top: 10px;
                padding: 12px 10px 10px 10px;
                color: #cccccc;
                font-weight: bold;
                font-size: 12px;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 6px;
                color: #aaaaaa;
            }
            QCheckBox {
                color: #dddddd;
                spacing: 8px;
            }
            QCheckBox::indicator {
                width: 16px;
                height: 16px;
                border-radius: 3px;
                border: 1px solid #555555;
                background: #2b2b2b;
            }
            QCheckBox::indicator:checked {
                background: #1ED761;
                border: 1px solid #1ED761;
            }
            QCheckBox:disabled {
                color: #555555;
            }
            QCheckBox::indicator:disabled {
                border: 1px solid #444444;
                background: #222222;
            }
            QLabel {
                color: #dddddd;
            }
            QLabel:disabled {
                color: #555555;
            }
            QComboBox {
                background: #2b2b2b;
                color: #ffffff;
                border: 1px solid #3e3e3e;
                border-radius: 4px;
                padding: 4px 8px;
                min-width: 120px;
            }
            QComboBox:hover {
                border: 1px solid #1ED761;
            }
            QComboBox:disabled {
                color: #555555;
                border: 1px solid #333333;
            }
            QComboBox::drop-down {
                border: none;
            }
            QComboBox QAbstractItemView {
                background: #2b2b2b;
                color: #ffffff;
                selection-background-color: #1ED761;
                selection-color: #000000;
            }
            QLineEdit {
                background: #2b2b2b;
                color: #ffffff;
                border: 1px solid #3e3e3e;
                border-radius: 4px;
                padding: 5px 8px;
            }
            QLineEdit:disabled {
                color: #555555;
                border: 1px solid #333333;
                background: #1e1e1e;
            }
            QPushButton {
                background: #434343;
                color: #ffffff;
                border: 1px solid #555555;
                border-radius: 4px;
                padding: 6px 14px;
                font-size: 13px;
            }
            QPushButton:hover {
                background: #1ED761;
                color: #000000;
                border: 1px solid #1ED761;
            }
            QPushButton:disabled {
                background: #222222;
                color: #555555;
                border: 1px solid #333333;
            }
            QPushButton#btnSave {
                background: #1ED761;
                color: #000000;
                font-weight: bold;
                border: none;
            }
            QPushButton#btnSave:hover {
                background: #25f070;
            }
            QFrame[frameShape="4"] {
                color: #3e3e3e;
                max-height: 1px;
            }
        """)
