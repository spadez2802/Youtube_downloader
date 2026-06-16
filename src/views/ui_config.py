import importlib

# --- UI VERSION CONFIGURATION ---
# Thay đổi phiên bản UI tại đây khi cần thiết:
# Khi bạn thêm file UI mới vào thư mục views, chỉ cần cập nhật tên phiên bản tương ứng ở dưới.

# 1. Main Window UI Version (Ví dụ: "ver9_4" sẽ tự nạp file views.ui_main_ver9_4)
MAIN_WINDOW_VERSION = "ver9_6"

# 2. Video Mini Card UI Version (Ví dụ: "ver6_2" sẽ tự nạp file views.ui_video_ver6_2)
VIDEO_MINI_VERSION = "ver6_2"

# 3. History Item UI Version (Ví dụ: "ver1_0" sẽ tự nạp file views.ui_history_ver1_0)
HISTORY_ITEM_VERSION = "ver1_0"

# 4. Download Dialog UI Version (Ví dụ: "ver1_0" sẽ tự nạp file views.ui_download_dialog_ver1_0)
DOWNLOAD_DIALOG_VERSION = "ver1_0"


# --- AUTOMATIC DYNAMIC IMPORTS ---
# Phần này tự động tìm và nạp Class giao diện tương ứng theo chuỗi phiên bản cấu hình ở trên.

try:
    # 1. Tự động nạp Main Window UI
    main_module = importlib.import_module(f"views.ui_main_{MAIN_WINDOW_VERSION}")
    Ui_MainWindow = main_module.Ui_MainWindow

    # 2. Tự động nạp Video Mini UI
    video_module = importlib.import_module(f"views.ui_video_{VIDEO_MINI_VERSION}")
    Ui_VideoMini = video_module.Ui_miniCard

    # 3. Tự động nạp History Item UI (Hỗ trợ định dạng cũ và mới)
    if HISTORY_ITEM_VERSION.startswith("ver"):
        history_module = importlib.import_module(f"views.ui_history_{HISTORY_ITEM_VERSION}")
        Ui_historyItm = history_module.Ui_Form
    else:
        history_module = importlib.import_module(f"views.history_item{HISTORY_ITEM_VERSION}")
        Ui_historyItm = history_module.Ui_historyItm

    # 4. Tự động nạp Download Dialog UI
    dialog_module = importlib.import_module(f"views.ui_download_dialog_{DOWNLOAD_DIALOG_VERSION}")
    Ui_Dialog = dialog_module.Ui_Dialog

except ImportError as e:
    raise ImportError(
        f"Lỗi: Không tìm thấy file UI tương ứng với cấu hình phiên bản hiện tại!\n"
        f"Chi tiết lỗi hệ thống: {e}"
    )
