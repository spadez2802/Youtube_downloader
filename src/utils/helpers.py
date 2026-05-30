import os
import sys
import shutil

def get_asset_path(relative_path):
    """ Tự động dò đường dẫn ảnh/bin dù là chạy code hay chạy .exe """
    if getattr(sys, 'frozen', False):
        base_path = sys._MEIPASS
    else:
        # File này nằm trong src/utils/, lùi ra 2 cấp để thấy thư mục img/bin ở gốc project
        base_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    
    return os.path.join(base_path, relative_path).replace("\\", "/")

_cached_node_path = None
_cached_ffmpeg_path = None

def get_node_path():
    """ Trả về đường dẫn của node.exe nếu có (trong bin/ hoặc trong PATH hệ thống) """
    global _cached_node_path
    if _cached_node_path is not None:
        return _cached_node_path if _cached_node_path != "" else None
        
    local_path = get_asset_path("bin/node.exe")
    if os.path.exists(local_path):
        _cached_node_path = local_path
        return local_path
    
    # Check system PATH
    sys_path = shutil.which("node")
    if sys_path:
        _cached_node_path = sys_path
        return sys_path
        
    _cached_node_path = ""
    return None

def get_ffmpeg_path():
    """ Trả về đường dẫn của ffmpeg.exe nếu có (trong bin/ hoặc trong PATH hệ thống) """
    global _cached_ffmpeg_path
    if _cached_ffmpeg_path is not None:
        return _cached_ffmpeg_path if _cached_ffmpeg_path != "" else None
        
    local_path = get_asset_path("bin/ffmpeg.exe")
    if os.path.exists(local_path):
        _cached_ffmpeg_path = local_path
        return local_path
    
    # Try static-ffmpeg
    try:
        import static_ffmpeg
        static_ffmpeg.add_paths()
    except Exception as e:
        print(f"Không thể load static-ffmpeg: {e}")
        
    # Check system PATH
    sys_path = shutil.which("ffmpeg")
    if sys_path:
        _cached_ffmpeg_path = sys_path
        return sys_path
        
    _cached_ffmpeg_path = ""
    return None



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