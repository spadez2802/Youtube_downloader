import os
import re
import yt_dlp
from PySide6.QtCore import QThread, Signal
from utils.helpers import get_asset_path, get_format_string, get_node_path, get_ffmpeg_path

class PlaylistDownloadThread(QThread):
    finished = Signal(str)
    error = Signal(str)
    progress_update = Signal(int)
    status_update = Signal(str)

    def __init__(self, download_list, folder_path):
        super().__init__()
        self.download_list = download_list 
        self.folder_path = folder_path

    def run(self): 
        node_path = get_node_path()
        ffmpeg_path = get_ffmpeg_path()
        total = len(self.download_list)
        
        def progress_hook(d):
            if d['status'] == 'downloading':
                p_str = d.get('_percent_str', '0%')
                clean_p = re.sub(r'\x1b\[[0-9;]*m', '', p_str).replace('%', '').strip()
                try: self.progress_update.emit(int(float(clean_p)))
                except: pass

        try:
            for i, item in enumerate(self.download_list):
                self.status_update.emit(f"Đang tải [{i+1}/{total}]: {item['title']}")
                self.progress_update.emit(0)

                # CHỐT CHẶT ĐƯỜNG DẪN: Thư mục Playlist / Tên Bài Hát . đuôi file
                outtmpl = os.path.join(self.folder_path, f"{item['clean_name']}.%(ext)s")
                
                base_opts = {
                    'noplaylist': True, # TRÓI TAY YTB: Bắt buộc chỉ tải 1 bài, không kéo cả chùm!
                    'ignoreerrors': True, 
                    'allow_remote_scripts': True,
                    'remote_components': ['ejs:github'],
                    'outtmpl': outtmpl, # Lưu đúng tên từng bài
                    'progress_hooks': [progress_hook], 
                }
                
                if node_path:
                    base_opts['js_runtimes'] = {'node': {'path': node_path}}
                if ffmpeg_path:
                    base_opts['ffmpeg_location'] = ffmpeg_path


                if item['type'] == "MP4":
                    base_opts.update({'format': get_format_string(item['quality']), 'merge_output_format': 'mp4'})
                else:
                    base_opts.update({
                        'format': 'bestaudio/best',
                        'postprocessors': [{'key': 'FFmpegExtractAudio', 'preferredcodec': 'mp3', 'preferredquality': '192'}],
                    })

                try:
                    with yt_dlp.YoutubeDL(base_opts) as ydl:
                        ydl.download([item['url']])
                except Exception as ex:
                    print(f"Bỏ qua lỗi video {item['title']}: {ex}")
                    continue 
            
            self.finished.emit(self.folder_path)
        except Exception as e:
            self.error.emit(str(e))