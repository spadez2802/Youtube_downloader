import yt_dlp
from PySide6.QtCore import QThread, Signal
from utils.helpers import get_asset_path, get_format_string

class DownloadThread(QThread):
    finished = Signal(str)
    error = Signal(str)

    def __init__(self, url, save_path, selected_option, quality="Best"):
        super().__init__()
        self.url = url
        self.save_path = save_path
        self.selected_option = selected_option
        self.quality = quality

    def run(self): 
        node_path = get_asset_path("bin/node.exe")
        ffmpeg_path = get_asset_path("bin/ffmpeg.exe")
        try:
            ydl_opts = {
                'noplaylist': True, # TRÓI TAY YTB LẠI
                'js_runtimes': {'node': {'path': node_path}},
                'allow_remote_scripts': True,
                'remote_components': ['ejs:github'],
                'ffmpeg_location': ffmpeg_path,
            }

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

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([self.url])
            
            self.finished.emit(self.save_path)
        except Exception as e:
            self.error.emit(str(e))