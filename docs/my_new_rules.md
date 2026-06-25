# My New Rules — Youtube Playlist Downloader

Tài liệu này chứa các quy tắc bổ sung, cập nhật theo quá trình phát triển dự án.

---

## 1. Vị trí đặt Widget Class

- Tất cả các **custom widget class** (kế thừa QWidget, QDialog) **phải** được đặt trong `src/views/custom_widgets.py`.
- **Tuyệt đối không** định nghĩa widget class bên trong Controller (`controllers/`).
- Controller chỉ **import và sử dụng** widget từ `views/custom_widgets.py`.

## 2. Không dùng Inline Imports

- Toàn bộ câu lệnh `import` và `from ... import ...` **phải** được đặt ở đầu file.
- **Tuyệt đối không** viết `from PySide6.QtWidgets import ...` bên trong body của method/function.

## 3. Lịch sử Không Giới Hạn

- Lịch sử tải xuống **không bị giới hạn số lượng** (unlimited).
- Không áp dụng bất kỳ `[:N]` slice nào lên `history_data` khi lưu.

## 4. Tập Trung Logic Xóa Lịch Sử

- Mọi thao tác đọc/ghi/xóa lịch sử **phải** thông qua `HistoryManager` (Model).
- Controller không được mở file `history.json` trực tiếp để xóa — phải gọi method của `HistoryManager`.

## 5. Settings Manager

- Mọi cài đặt người dùng được quản lý tập trung qua `SettingsManager` (`src/models/settings_manager.py`).
- Các Handler (`DownloadHandler`, v.v.) đọc settings thông qua `self.main.settings_manager.get(key)`.
