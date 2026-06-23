# Kiến trúc dự án (Architecture) — Youtube Playlist Downloader

Tài liệu này mô tả chi tiết toàn bộ kiến trúc và luồng hoạt động của ứng dụng, từ khởi động đến hoàn tất tải xuống. Kiến trúc dự án theo mô hình **MVC** (Model–View–Controller), sử dụng **PySide6** cho giao diện và **yt-dlp** để xử lý video.

---

## 1. Kiến trúc tổng quan

```text
src/
├── app.py                          # Entry point
├── controllers/
│   ├── main_window.py              # MyDownloader — controller chính
│   ├── ui_handler.py               # Xử lý hiệu ứng & trạng thái UI
│   ├── search_handler.py           # Xử lý tìm kiếm & trích xuất metadata
│   ├── download_handler.py         # Điều phối tải xuống
│   └── download_dialog_controller.py  # Controller cho dialog tải
├── models/
│   ├── history_manager.py          # Quản lý lịch sử
│   ├── thread_fetch_info.py        # Thread: lấy metadata yt-dlp
│   ├── thread_thumbnail.py         # Thread: tải thumbnail
│   ├── thread_download_single.py   # Thread: tải video đơn
│   ├── thread_download_playlist.py # Thread: tải toàn bộ playlist
│   └── thread_network_checker.py   # Thread: kiểm tra mạng
├── views/
│   ├── ui_main_ver9_6.py           # Giao diện chính
│   ├── ui_video_ver6_2.py          # Widget hiển thị từng video
│   ├── ui_history_ver2_0.py        # Giao diện lịch sử
│   ├── ui_download_dialog_ver1_0.py# Giao diện dialog tải
│   ├── custom_widgets.py           # Các widget tùy chỉnh
│   ├── history_item1_5.py          # Widget item lịch sử
│   └── ui_config.py                # Cấu hình giao diện
└── utils/
    └── helpers.py                  # Các hàm tiện ích dùng chung
```

---

## 2. Luồng hoạt động

### 2.1 Luồng khởi động ứng dụng
1. Người dùng chạy `app.py`. Khởi tạo `QApplication` và `MyDownloader` (controller chính).
2. Load View `ui_main_ver9_6.py` và khởi tạo các thiết lập cơ bản cho yt-dlp.
3. Khởi tạo Models: `HistoryManager` và `NetworkChecker`.
4. Khởi tạo Sub-Controllers: `UIHandler`, `SearchHandler`, `DownloadHandler`.
5. Kết nối các Signals & Slots, sau đó load lịch sử từ file vào UI.

### 2.2 Luồng tìm kiếm & trích xuất thông tin
1. Người dùng nhập URL / từ khóa, `SearchHandler` bắt đầu xử lý.
2. Kiểm tra URL và kết nối mạng. Nếu hợp lệ, tạo thread `FetchInfoThread` (`thread_fetch_info.py`).
3. Dùng `yt-dlp` trích xuất metadata và chia luồng theo loại nội dung (Video đơn, Playlist, hoặc Lỗi).
4. Tạo giao diện/thumbnail tương ứng thông qua View và kích hoạt các nút tải.

### 2.3 Luồng tải xuống
1. Người dùng nhấn Download/Download All, `DownloadHandler` xử lý.
2. Mở dialog chọn chất lượng, hoặc định dạng.
3. Tạo các thread tải tương ứng (`thread_download_single.py` hoặc `thread_download_playlist.py`).
4. yt-dlp thực thi tải xuống, liên tục emit progress signal (%, tốc độ, tên file).
5. Khi hoàn tất, ghi vào lịch sử thông qua `HistoryManager`.

### 2.4 Luồng tương tác MVC đầy đủ
- **View**: Chỉ hiển thị giao diện và phát các Signals (nhấn nút, nhập URL).
- **Controller**: Nhận Signals, gọi Model để xử lý nghiệp vụ, gọi View để cập nhật hiển thị.
- **Model**: Xử lý logic nặng trên Threads (kéo thông tin, tải file, đọc/ghi lịch sử) và trả về dữ liệu cho Controller.

---
*(Được tổng hợp từ tài liệu workflow.md)*
