# Luồng hoạt động (Workflow) - Youtube Playlist Downloader

Tài liệu này mô tả chi tiết luồng hoạt động của ứng dụng tải video và playlist từ Youtube. Ứng dụng được xây dựng trên nền tảng Python, sử dụng thư viện PySide6 (Qt) cho giao diện người dùng và áp dụng mô hình kiến trúc phân chia thành các Controller, Model và View rõ ràng.

## 1. Khởi động ứng dụng
- Entry point của ứng dụng là `app.py`. Khi chạy, ứng dụng sẽ khởi tạo class `MyDownloader` (được định nghĩa trong `src/controllers/main_window.py`).
- Quá trình khởi tạo bao gồm:
  - Tải giao diện từ View (`ui_main_ver8_5.py`).
  - Khởi tạo các cấu hình yt-dlp cơ bản.
  - Khởi tạo Models: `HistoryManager` (quản lý lịch sử tìm kiếm/tải xuống).
  - Khởi tạo Handlers (Controllers phụ): `UIHandler` (quản lý giao diện, hiệu ứng), `SearchHandler` (xử lý tìm kiếm), `DownloadHandler` (xử lý tải xuống).
  - Kết nối các tín hiệu (Signals/Slots) giữa các thành phần giao diện (UI) và các hàm xử lý tương ứng.

## 2. Tìm kiếm và Trích xuất thông tin
- Người dùng nhập URL (của một Video hoặc một Playlist Youtube) hoặc từ khóa tìm kiếm vào thanh tìm kiếm (`enterPlace`).
- Khi người dùng tương tác, ứng dụng có thể hiển thị lịch sử các lần tìm kiếm trước đó (quản lý bởi `HistoryManager`).
- Khi nhấn nút Tìm kiếm (`findBtn`):
  - Sự kiện được chuyển tới `SearchHandler`.
  - Một luồng nền (thread) được tạo ra từ `thread_fetch_info.py` (nằm trong `models`) để gọi yt-dlp lấy thông tin siêu dữ liệu (metadata) của video hoặc playlist mà không làm đơ giao diện chính.
  - Sau khi lấy được dữ liệu, tín hiệu sẽ trả về Controller:
    - **Nếu là Video đơn:** Cập nhật thông tin tiêu đề, hình thu nhỏ (thông qua `thread_thumbnail.py`) và kích hoạt các tùy chọn tải.
    - **Nếu là Playlist:** Giao diện sẽ hiển thị danh sách các video bên trong bằng cách tạo các `VideoItemWidget` (custom widget) và thêm vào vùng cuộn (`scrollArea`).

## 3. Cấu hình Tùy chọn Tải xuống
- Người dùng có thể chọn định dạng tải về (MP4 hoặc MP3) qua ComboBox.
- Nếu chọn MP4 cho video đơn, nút chọn chất lượng (Quality) sẽ được kích hoạt. Các logic này được liên kết trực tiếp trong `main_window.py` và đồng bộ tới toàn bộ các item nếu là playlist.
- Giao diện cung cấp nút để "Download" cho từng video riêng lẻ hoặc "Download All" cho toàn bộ playlist.

## 4. Thực thi Tải xuống
- Khi nhấn nút Tải xuống:
  - Sự kiện được chuyển tới `DownloadHandler`.
  - Tùy thuộc vào bối cảnh, hệ thống sẽ khởi tạo luồng nền tương ứng:
    - `thread_download_single.py`: Xử lý tải một video riêng biệt.
    - `thread_download_playlist.py`: Xử lý tải toàn bộ video trong playlist hiện tại.
  - Các luồng nền này gọi yt-dlp thực hiện quá trình tải thực tế.
  - Trong quá trình tải, luồng nền liên tục phát tín hiệu (emit signals) về phần trăm tiến độ, tốc độ tải. UI (Progress bar) sẽ nhận tín hiệu và cập nhật trực quan cho người dùng.

## 5. Hoàn tất và Lưu lịch sử
- Khi quá trình tải hoàn tất, ứng dụng sẽ thông báo trên giao diện và lưu trữ thông tin về tệp vừa tải vào lịch sử.
- Dữ liệu lịch sử được ghi vào file cục bộ để có thể phục hồi (load) lại vào các lần mở ứng dụng tiếp theo thông qua `HistoryManager`.
