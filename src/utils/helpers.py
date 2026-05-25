import os
import sys

def get_asset_path(relative_path):
    """ Tự động dò đường dẫn ảnh/bin dù là chạy code hay chạy .exe """
    if getattr(sys, 'frozen', False):
        base_path = sys._MEIPASS
    else:
        # File này nằm trong src/utils/, lùi ra 2 cấp để thấy thư mục img/bin ở gốc project
        base_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    
    return os.path.join(base_path, relative_path).replace("\\", "/")

def get_format_string(quality_text):
    """ Chuyển đổi text giao diện sang lệnh format của yt-dlp """
    if quality_text in ["Best", "Best Quality"]:
        return 'bestvideo+bestaudio/best'
    elif quality_text in ["Worst", "Worst Quality"]:
        return 'worstvideo+worstaudio/worst'
    
    # Các mốc chất lượng cụ thể
    quality_map = {
        "1080p": 'bestvideo[height<=1080]+bestaudio/best',
        "720p":  'bestvideo[height<=720]+bestaudio/best',
        "480p":  'bestvideo[height<=480]+bestaudio/best',
        "360p":  'bestvideo[height<=360]+bestaudio/best'
    }
    return quality_map.get(quality_text, 'bestvideo+bestaudio/best')