import os
import sys
import json

class SettingsManager:
    """
    Model quản lý toàn bộ cài đặt người dùng.
    Đọc/ghi settings.json ở thư mục gốc dự án.
    Controller đọc cài đặt qua get(key) và ghi qua set(key, value) + save().
    """

    DEFAULT_SETTINGS = {
        "download_path": "",
        "create_subfolder_for_playlist": True,
        "open_folder_after_download": False,
        "use_default_path": False,
        "use_original_name": True,
        "default_format": "MP4",
        "default_quality": "1080p",
        "default_bitrate": "192kbps",
        "max_concurrent_downloads": 2,
        "accent_color": "#1ED761"
    }

    def __init__(self):
        self._data = {}
        self.load()

    def get_settings_path(self) -> str:
        """Trả về đường dẫn tuyệt đối đến settings.json."""
        if getattr(sys, 'frozen', False):
            base_dir = os.path.dirname(sys.executable)
        else:
            # File này nằm trong src/models/ → lùi 2 cấp ra gốc project
            base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        return os.path.join(base_dir, "settings.json")

    def load(self) -> dict:
        """Đọc settings từ file, fallback về DEFAULT_SETTINGS nếu file chưa tồn tại hoặc lỗi."""
        self._data = dict(self.DEFAULT_SETTINGS)
        path = self.get_settings_path()
        if os.path.exists(path):
            try:
                with open(path, 'r', encoding='utf-8') as f:
                    saved = json.load(f)
                # Merge: chỉ ghi đè những key đã lưu, giữ default cho key mới
                self._data.update(saved)
            except Exception as e:
                print(f"Lỗi đọc settings.json: {e}")
        return self._data

    def save(self) -> None:
        """Ghi toàn bộ settings hiện tại ra file settings.json."""
        try:
            with open(self.get_settings_path(), 'w', encoding='utf-8') as f:
                json.dump(self._data, f, ensure_ascii=False, indent=4)
        except Exception as e:
            print(f"Lỗi ghi settings.json: {e}")

    def get(self, key: str, default=None):
        """Lấy giá trị setting theo key. Trả về default nếu key chưa tồn tại."""
        return self._data.get(key, default if default is not None else self.DEFAULT_SETTINGS.get(key))

    def set(self, key: str, value) -> None:
        """Cập nhật giá trị setting trong RAM (chưa ghi file). Gọi save() để lưu."""
        self._data[key] = value
