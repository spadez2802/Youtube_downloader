# Hướng Dẫn Quản Lý Phiên Bản UI (UI Versioning Guide)

Tài liệu này quy định cách thức hoạt động và quy tắc dành cho AI / Lập trình viên khi làm việc với các thành phần giao diện (UI) trong dự án.

## 1. Nguyên Tắc Cơ Bản
Tất cả các phiên bản của giao diện (ví dụ: `ver1_0`, `ver2_0`, v.v.) **PHẢI** được điều khiển tập trung duy nhất tại file cấu hình:
**`src/views/ui_config.py`**

**TUYỆT ĐỐI KHÔNG** import trực tiếp các file UI có chứa hậu tố version (như `from views.ui_history_ver2_0 import ...`) tại bất kỳ file logic/controller nào khác (ví dụ: `search_handler.py`, `app.py`).

## 2. Cách Thực Hiện Đúng

### Tại `ui_config.py`:
File này định nghĩa phiên bản và nạp class tương ứng. Ví dụ:

```python
# 3. History Sidebar UI Version
HISTORY_SIDEBAR_VERSION = "ver2_0"

# 4. History Dropdown UI Version
HISTORY_DROPDOWN_VERSION = "1_5"

...
# Tự động import dựa trên version config
sidebar_module = importlib.import_module(f"views.ui_history_{HISTORY_SIDEBAR_VERSION}")
Ui_HistorySidebar = sidebar_module.Ui_FormHistoryItem

dropdown_module = importlib.import_module(f"views.history_item{HISTORY_DROPDOWN_VERSION}")
Ui_HistoryDropdown = dropdown_module.Ui_historyItm
```

### Tại các file Controller (ví dụ `search_handler.py`):
Luôn import các class UI thông qua `views.ui_config`:

```python
# ĐÚNG:
from views.ui_config import Ui_HistorySidebar, Ui_HistoryDropdown

class HistoryCard(QWidget):
    def __init__(...):
        self.ui = Ui_HistorySidebar()
        self.ui.setupUi(self)
```

```python
# SAI (Tuyệt đối không làm):
from views.ui_history_ver2_0 import Ui_FormHistoryItem
```

## 3. Lý Do
- Việc fix cứng version vào code gây khó khăn trong việc bảo trì và thay đổi/nâng cấp UI.
- Thống nhất một điểm cấu hình (`ui_config.py`) giúp cho việc chuyển đổi giao diện an toàn, tránh lỗi mismatch phiên bản giữa các file.

## 4. Dành cho AI
Khi cần chỉnh sửa, cập nhật hoặc sử dụng một thành phần UI mới:
1. Tạo file UI mới trong thư mục `views`.
2. Đảm bảo cấu trúc class được export từ UI mới tương thích với hệ thống hiện tại.
3. Cập nhật biến cấu hình version tương ứng tại `ui_config.py` nếu muốn apply UI đó.
4. Không được sửa đổi import cứng ở các file Controllers.

---

## 5. Quy Trình Làm Việc với Qt Designer (Wrapper Pattern)

### Nguyên tắc vàng

> **TUYỆT ĐỐI KHÔNG chỉnh sửa tay các file `ui_*.py` trong thư mục `views/`.**
> Các file này được generate tự động từ Qt Designer và sẽ bị ghi đè mỗi khi regenerate.
> Mọi cảnh báo đã có sẵn ở dòng đầu file: `WARNING! All changes made in this file will be lost when recompiling UI file!`

### Kiến trúc đúng

```
ui/history_item2.ui           ← Chỉnh giao diện TẠI ĐÂY (Qt Designer)
        │
        │  pyside6-uic (auto-generate)
        ▼
src/views/ui_history_ver2_0.py  ← KHÔNG CHỈNH TAY — chỉ import
        │
        │  import Ui_FormHistoryItem
        ▼
src/controllers/search_handler.py
└── class HistoryCard(QWidget)   ← Mọi custom logic viết TẠI ĐÂY
        ├── self.ui = Ui_HistorySidebar()
        ├── self.ui.setupUi(self)
        ├── self.ui.labelName.setText(...)   ← Set dữ liệu động
        ├── self.ui.cbbOpt.setMenu(...)      ← Gắn menu, signal
        └── self.ui.labelDate.setStyleSheet(...)  ← Style động
```

### Khi muốn thay đổi giao diện

**Thay đổi layout / widget mới → Dùng Qt Designer:**

1. Mở Qt Designer:
   ```
   d:\design\ytb_playlist_downloader\.conda\Scripts\pyside6-designer.exe
   ```
2. Mở file `.ui` tương ứng trong thư mục `ui/`
3. Chỉnh sửa trong Designer (kéo thả, thêm widget, v.v.)
4. Lưu file `.ui`
5. Regenerate file Python (xem lệnh bên dưới)

**Thay đổi logic / style / text động → Chỉnh file Controller:**

- Chỉnh trong class Wrapper tương ứng (ví dụ: `HistoryCard` trong `search_handler.py`)
- Không cần regenerate gì cả

### Lệnh regenerate file Python từ `.ui`

Chạy từ thư mục gốc dự án (`d:\design\ytb_playlist_downloader`):

```python
# Regenerate ui_history_ver2_0.py từ history_item2.ui
python -c "import sys; sys.argv=['pyside6-uic','ui/history_item2.ui','-o','src/views/ui_history_ver2_0.py']; from PySide6.scripts.pyside_tool import uic; uic()"
```

> **Lưu ý:** Không dùng `pyside6-uic.exe` trong `.conda/Scripts/` vì nó bị lỗi trên môi trường này.
> Dùng `python -c "... from PySide6.scripts.pyside_tool import uic; uic()"` thay thế.

### Bảng phân công trách nhiệm

| Muốn làm gì | Chỉnh ở đâu |
|---|---|
| Thêm widget, đổi layout, kéo thả | File `.ui` trong Qt Designer |
| Set text / data động vào widget | Class Wrapper trong Controller |
| Style theo trạng thái (hover, active) | Class Wrapper trong Controller |
| Kết nối signal/slot, gắn menu | Class Wrapper trong Controller |
| Đổi phiên bản UI đang dùng | `ui_config.py` |
| **Tuyệt đối không** | Chỉnh trực tiếp file `ui_*.py` |
