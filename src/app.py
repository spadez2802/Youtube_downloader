import sys
from PySide6.QtWidgets import QApplication
from controllers.main_window import MyDownloader

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyDownloader()
    window.show()
    sys.exit(app.exec())