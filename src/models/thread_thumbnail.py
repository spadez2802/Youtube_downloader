from PySide6.QtCore import QThread, Signal
from urllib.request import urlopen, Request


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