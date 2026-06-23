import os
from utils.helpers import get_asset_path

class ThemeManager:
    DEFAULT_ACCENT = "#1ED761"
    QSS_PATH = "ui/global_style.qss"

    def __init__(self):
        self._raw_qss = ""
        self._load_qss()

    def _load_qss(self):
        path = get_asset_path(self.QSS_PATH)
        if not os.path.exists(path):
            print(f"Warning: ThemeManager could not find qss at {path}")
            return
            
        with open(path, "r", encoding="utf-8") as f:
            self._raw_qss = f.read()
            
        arrow_path = get_asset_path("img/icon/down_arrow.png").replace("\\", "/")
        self._raw_qss = self._raw_qss.replace("ARROW_ICON_PATH", arrow_path)

    def apply(self, app, accent_color: str = None):
        color = accent_color or self.DEFAULT_ACCENT
        if not self._raw_qss:
            return
            
        qss = self._raw_qss.replace("ACCENT_COLOR", color)
        app.setStyleSheet(qss)
