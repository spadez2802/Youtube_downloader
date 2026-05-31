import re
import yt_dlp
from PySide6.QtCore import QThread, Signal
from utils.helpers import get_asset_path, get_format_string, get_node_path, get_ffmpeg_path

class DownloadThread(QThread):
    finished = Signal(str)
    error = Signal(str)
    progress_update = Signal(int)
    status_update = Signal(str)

    def __init__(self, url, save_path, selected_option, quality="Best"):
        super().__init__()
        self.url = url
        self.save_path = save_path
        self.selected_option = selected_option
        self.quality = quality
        self._is_paused = False
        self._is_cancelled = False

    def pause(self):
        self._is_paused = True
        self.status_update.emit("Paused")

    def resume(self):
        self._is_paused = False
        self.status_update.emit("Downloading...")

    def cancel(self):
        self._is_cancelled = True
        self._is_paused = False # break pause wait loop
        self.status_update.emit("Cancelling...")

    def run(self): 
        node_path = get_node_path()
        ffmpeg_path = get_ffmpeg_path()
        
        def progress_hook(d):
            if self._is_cancelled:
                raise Exception("CANCELLED")
            while self._is_paused:
                if self._is_cancelled:
                    raise Exception("CANCELLED")
                self.msleep(100)
                
            if d['status'] == 'downloading':
                p_str = d.get('_percent_str', '0%')
                clean_p = re.sub(r'\x1b\[[0-9;]*m', '', p_str).replace('%', '').strip()
                try:
                    self.progress_update.emit(int(float(clean_p)))
                except:
                    pass
            elif d['status'] == 'finished':
                self.progress_update.emit(100)

        try:
            ydl_opts = {
                'noplaylist': True, # TRÓI TAY YTB LẠI
                'allow_remote_scripts': True,
                'remote_components': ['ejs:github'],
                'progress_hooks': [progress_hook],
            }
            if node_path:
                ydl_opts['js_runtimes'] = {'node': {'path': node_path}}
            if ffmpeg_path:
                ydl_opts['ffmpeg_location'] = ffmpeg_path

            if self.selected_option == "MP4":
                ydl_opts.update({
                    'outtmpl': self.save_path,
                    'format': get_format_string(self.quality),
                    'merge_output_format': 'mp4',
                })
            else:  
                ydl_opts.update({
                    'outtmpl': self.save_path.replace('.mp3', ''),
                    'format': 'bestaudio/best',
                    'postprocessors': [{
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': 'mp3',
                        'preferredquality': '192',
                    }],
                })

            self.status_update.emit("Downloading...")
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([self.url])
            
            if self._is_cancelled:
                raise Exception("CANCELLED")
                
            self.finished.emit(self.save_path)
        except Exception as e:
            if "CANCELLED" in str(e):
                self.error.emit("CANCELLED")
            else:
                self.error.emit(str(e))