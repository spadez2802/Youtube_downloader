import socket
from PySide6.QtCore import QThread, Signal

class NetworkChecker(QThread):
    connection_changed = Signal(bool)

    def __init__(self):
        super().__init__()
        self.is_running = True
        self.last_status = None

    def run(self):
        while self.is_running:
            status = self.check_internet()
            if status != self.last_status:
                self.connection_changed.emit(status)
                self.last_status = status
            
            # Check every 2 seconds. Sleep in 100ms intervals so thread exits quickly when stopped
            for _ in range(20):
                if not self.is_running:
                    break
                self.msleep(100)

    def check_internet(self):
        try:
            socket.setdefaulttimeout(1.5)
            # Standard DNS check to Google Public DNS (fast, non-blocking)
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect(("8.8.8.8", 53))
            sock.close()
            return True
        except Exception:
            return False

    def stop(self):
        self.is_running = False
        self.wait()
