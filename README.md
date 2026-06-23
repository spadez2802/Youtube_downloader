# TheDownloader (YouTube Playlist Downloader)

Một ứng dụng Desktop tải video và playlist từ YouTube với giao diện trực quan, được xây dựng bằng Python và PySide6.

## 🚀 Tính năng chính

- **Tải Video & Playlist:** Hỗ trợ tải một video lẻ hoặc toàn bộ playlist từ YouTube một cách dễ dàng.
- **Giao diện hiện đại (GUI):** Xây dựng bằng PySide6, mang lại trải nghiệm mượt mà và trực quan.
- **Tốc độ cao & Đáng tin cậy:** Sử dụng core `yt-dlp` mạnh mẽ để get link và tải xuống với chất lượng cao nhất.
- **Xử lý Audio/Video:** Tích hợp `static-ffmpeg` giúp tự động gộp âm thanh và hình ảnh (muxing) hoặc chuyển đổi định dạng.
- **Theo dõi tiến trình:** Xem trực tiếp phần trăm tải xuống, tốc độ tải và lịch sử các video đã tải.

*(Bạn có thể xem thêm các tính năng đang lên ý tưởng tại [docs/ideas/README.md](docs/ideas/README.md))*

## 🛠 Thư viện cần cài đặt (Prerequisites)

Dự án yêu cầu Python 3.8+ và sử dụng các thư viện chính sau:
- `PySide6` (>= 6.5.0): Framework giao diện người dùng.
- `yt-dlp` (>= 2023.0.0): Thư viện core dùng để bóc tách và tải video/audio.
- `static-ffmpeg` (>= 2.5.0): Cung cấp FFmpeg tĩnh (không cần cài FFmpeg vào biến môi trường hệ thống) để xử lý file media.

## 📦 Hướng dẫn cài đặt

1. **Clone dự án về máy:**
   ```bash
   git clone https://github.com/spadez2802/Youtube_downloader.git
   cd Youtube_downloader
   ```

2. **Tạo môi trường ảo (Khuyến nghị):**
   ```bash
   python -m venv .venv
   
   # Kích hoạt môi trường ảo:
   # - Trên Windows:
   .venv\Scripts\activate
   # - Trên macOS/Linux:
   source .venv/bin/activate
   ```

3. **Cài đặt các thư viện yêu cầu:**
   ```bash
   pip install -r requirements.txt
   ```

## 🎮 Cách sử dụng

Để khởi động ứng dụng, bạn chạy lệnh sau từ thư mục gốc của dự án:

```bash
python src/app.py
```
Sau đó, dán link YouTube (Video hoặc Playlist) vào thanh tìm kiếm trên giao diện ứng dụng và nhấn tải.

---
**License:** [Thêm thông tin License nếu có]
