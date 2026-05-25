from PySide6.QtCore import QThread, Signal
import yt_dlp
from urllib.request import urlopen, Request

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
        if thumbs and isinstance(thumbs, list):
            return thumbs[-1].get('url') 
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
            
            # --- TÍNH NĂNG MỚI: QUÉT ĐỘ PHÂN GIẢI THỰC TẾ ---
            resolutions = ["Best"] # Luôn có tùy chọn Best mặc định
            if not is_playlist:
                formats = info.get('formats', [])
                heights = set()
                for f in formats:
                    h = f.get('height')
                    # Lọc lấy những định dạng có hình ảnh (vcodec != 'none') và có chiều cao
                    if h and isinstance(h, int) and f.get('vcodec') != 'none':
                        heights.add(h)
                
                # Sắp xếp chiều cao từ lớn đến bé (Ví dụ: 1080, 720, 480...)
                sorted_heights = sorted(list(heights), reverse=True)
                for h in sorted_heights:
                    resolutions.append(f"{h}p")
            else:
                # Nếu là Playlist, ta vẫn để list cố định vì không thể đoán chung cho cả list
                resolutions = ["Best", "1080p", "720p", "480p", "360p"]
            # ------------------------------------------------

            if is_playlist:
                raw_entries = list(info.get('entries', []))
                
                if not thumbnail_url and len(raw_entries) > 0:
                    thumbnail_url = self.get_thumb_url(raw_entries[0])
                
                for item in raw_entries:
                    if item: 
                        entries_data.append({
                            'title': item.get('title', 'Unknown'),
                            'url': item.get('url', ''),
                            'thumbnail': self.get_thumb_url(item), 
                            
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
                'entries': entries_data,
                'url': self.url,
                'resolutions': resolutions # <--- FIX: ĐÃ THÊM CHÌA KHÓA NÀY ĐỂ TRẢ VỀ GIAO DIỆN
            }
            self.finished.emit(result)

        except Exception as e:
            self.error.emit(str(e))