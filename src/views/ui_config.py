import importlib

# --- UI VERSION CONFIGURATION ---
# Thay đổi phiên bản UI tại đây khi cần thiết:
# Khi bạn thêm file UI mới vào thư mục views, chỉ cần cập nhật tên phiên bản tương ứng ở dưới.

# 1. Main Window UI Version (Ví dụ: "ver9_4" sẽ tự nạp file views.ui_main_ver9_4)
MAIN_WINDOW_VERSION = "ver10_0"

# 2. Video Mini Card UI Version (Ví dụ: "ver6_2" sẽ tự nạp file views.ui_video_ver6_2)
VIDEO_MINI_VERSION = "ver7_0"

# 3. History Sidebar UI Version (Ví dụ: "ver2_0" sẽ tự nạp file views.ui_history_ver2_0)
HISTORY_SIDEBAR_VERSION = "ver3_0"

# 4. History Dropdown UI Version (Ví dụ: "1_5" sẽ tự nạp file views.history_item1_5)
HISTORY_DROPDOWN_VERSION = "2_0"

# 5. Download Dialog UI Version (Ví dụ: "ver1_0" sẽ tự nạp file views.ui_download_dialog_ver1_0)
DOWNLOAD_DIALOG_VERSION = "ver2_0"


# --- AUTOMATIC DYNAMIC IMPORTS ---
# Phần này tự động tìm và nạp Class giao diện tương ứng theo chuỗi phiên bản cấu hình ở trên.

try:
    # 1. Tự động nạp Main Window UI
    main_module = importlib.import_module(f"views.ui_main_{MAIN_WINDOW_VERSION}")
    Ui_MainWindow = main_module.Ui_MainWindow

    # 2. Tự động nạp Video Mini UI
    video_module = importlib.import_module(f"views.ui_video_{VIDEO_MINI_VERSION}")
    Ui_VideoMini = video_module.Ui_miniCard

    # 3. Tự động nạp History Sidebar UI
    sidebar_module = importlib.import_module(f"views.ui_history_{HISTORY_SIDEBAR_VERSION}")
    if hasattr(sidebar_module, 'Ui_FormHistoryItem'):
        Ui_HistorySidebar = sidebar_module.Ui_FormHistoryItem
    else:
        Ui_HistorySidebar = sidebar_module.Ui_Form

    # 4. Tự động nạp History Dropdown UI
    dropdown_module = importlib.import_module(f"views.history_item{HISTORY_DROPDOWN_VERSION}")
    Ui_HistoryDropdown = dropdown_module.Ui_historyItm

    # 5. Tự động nạp Download Dialog UI
    dialog_module = importlib.import_module(f"views.ui_download_dialog_{DOWNLOAD_DIALOG_VERSION}")
    Ui_Dialog = dialog_module.Ui_Dialog

except ImportError as e:
    raise ImportError(
        f"Lỗi: Không tìm thấy file UI tương ứng với cấu hình phiên bản hiện tại!\n"
        f"Chi tiết lỗi hệ thống: {e}"
    )
