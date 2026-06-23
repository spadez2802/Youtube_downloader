# Tiêu chuẩn Code & Quản Lý Phiên Bản UI (Coding Standard)

Tài liệu này quy định cách thức hoạt động và quy tắc dành cho AI / Lập trình viên khi làm việc trong dự án **Youtube Playlist Downloader**.

## 1. Nguyên Tắc Cơ Bản về UI
Tất cả các phiên bản của giao diện (ví dụ: `ver1_0`, `ver2_0`, v.v.) **PHẢI** được điều khiển tập trung duy nhất tại file cấu hình:
**`src/views/ui_config.py`**

**TUYỆT ĐỐI KHÔNG** import trực tiếp các file UI có chứa hậu tố version (như `from views.ui_history_ver2_0 import ...`) tại bất kỳ file logic/controller nào khác (ví dụ: `search_handler.py`, `app.py`).

### Cách Import Đúng (tại Controller):
```python
# ĐÚNG:
from views.ui_config import Ui_HistorySidebar, Ui_HistoryDropdown

class HistoryCard(QWidget):
    def __init__(self):
        self.ui = Ui_HistorySidebar()
        self.ui.setupUi(self)
```
```python
# SAI (Tuyệt đối không làm):
from views.ui_history_ver2_0 import Ui_FormHistoryItem
```

## 2. Quy Trình Làm Việc với Qt Designer (Wrapper Pattern)

> **TUYỆT ĐỐI KHÔNG chỉnh sửa tay các file `ui_*.py` trong thư mục `views/`.**
> Các file này được generate tự động từ Qt Designer và sẽ bị ghi đè mỗi khi regenerate.

### Bảng phân công trách nhiệm
| Muốn làm gì | Chỉnh ở đâu |
|---|---|
| Thêm widget, đổi layout, kéo thả | File `.ui` trong `ui/` bằng Qt Designer |
| Set text / data động vào widget | Class Wrapper trong thư mục `controllers/` |
| Style theo trạng thái (hover, active)| Class Wrapper trong thư mục `controllers/` |
| Kết nối signal/slot, gắn menu | Class Wrapper trong thư mục `controllers/` |
| Đổi phiên bản UI đang dùng | `src/views/ui_config.py` |
| **Tuyệt đối không** | Chỉnh trực tiếp file `ui_*.py` |

### Lệnh regenerate file Python từ `.ui`
Chạy từ thư mục gốc dự án:
```python
python -c "import sys; sys.argv=['pyside6-uic','ui/<file.ui>','-o','src/views/<file.py>']; from PySide6.scripts.pyside_tool import uic; uic()"
```

## 3. Dành cho Lập Trình Viên & AI
Khi cần chỉnh sửa, cập nhật chức năng hoặc UI:
1. Đọc và hiểu kiến trúc Controller - Model - View (tham khảo `architecture.md`).
2. Mọi logic bất đồng bộ và tác vụ nặng bắt buộc phải chạy trên **Thread** (trong thư mục `models/`) để tránh đóng băng UI.
3. Liên kết giữa View và Model chỉ thông qua **Signals & Slots**. Không truyền trực tiếp đối tượng View vào trong Thread.
4. Tuân thủ việc dùng `ui_config.py` khi khai báo một component mới.

---
*(Được tổng hợp từ tài liệu UI_VERSIONING_GUIDE.md)*
