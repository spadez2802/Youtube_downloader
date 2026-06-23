# Luồng Hoạt Động (Workflow) — Youtube Playlist Downloader

> Tài liệu này mô tả chi tiết toàn bộ luồng hoạt động của ứng dụng, từ khởi động đến hoàn tất tải xuống. Kiến trúc dự án theo mô hình **MVC** (Model–View–Controller), sử dụng **PySide6** cho giao diện và **yt-dlp** để xử lý video.

---

## Mục lục

1. [Kiến trúc tổng quan](#1-kiến-trúc-tổng-quan)
2. [Luồng khởi động ứng dụng](#2-luồng-khởi-động-ứng-dụng)
3. [Luồng tìm kiếm & trích xuất thông tin](#3-luồng-tìm-kiếm--trích-xuất-thông-tin)
4. [Luồng tải xuống](#4-luồng-tải-xuống)
5. [Luồng quản lý lịch sử](#5-luồng-quản-lý-lịch-sử)
6. [Sơ đồ tương tác đầy đủ](#6-sơ-đồ-tương-tác-đầy-đủ)
7. [Cấu trúc file dự án](#7-cấu-trúc-file-dự-án)

---

## 1. Kiến trúc tổng quan

```
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

## 2. Luồng khởi động ứng dụng

```mermaid
flowchart TD
    A(["`**Người dùng chạy**
    app.py`"]) --> B["Khởi tạo QApplication"]
    B --> C["Khởi tạo MyDownloader\n(main_window.py)"]
    C --> D["Load View\nui_main_ver9_6.py"]
    D --> E["Khởi tạo yt-dlp\ncấu hình cơ bản"]
    E --> F["Khởi tạo Models"]
    F --> F1["HistoryManager\n(history_manager.py)"]
    F --> F2["NetworkChecker\n(thread_network_checker.py)"]
    F1 & F2 --> G["Khởi tạo Sub-Controllers"]
    G --> G1["UIHandler\n(ui_handler.py)"]
    G --> G2["SearchHandler\n(search_handler.py)"]
    G --> G3["DownloadHandler\n(download_handler.py)"]
    G1 & G2 & G3 --> H["Kết nối Signals & Slots"]
    H --> I["Load lịch sử từ file\nvào UI"]
    I --> J(["`**Ứng dụng sẵn sàng**`"])

    style A fill:#4A90D9,color:#fff,stroke:none
    style J fill:#27AE60,color:#fff,stroke:none
```

---

## 3. Luồng tìm kiếm & trích xuất thông tin

```mermaid
flowchart TD
    U(["Người dùng nhập URL / từ khóa"]) --> SH["SearchHandler\nbắt đầu xử lý"]
    SH --> VAL{"Validate\nURL?"}
    VAL -- Không hợp lệ --> ERR["Hiển thị thông báo lỗi\ntrên UI"]
    VAL -- Hợp lệ --> NET{"Có kết nối\nmạng?"}
    NET -- Không --> NETERR["Thông báo lỗi mạng"]
    NET -- Có --> TH["Tạo thread:\nthread_fetch_info.py"]
    TH --> UI1["UI: Hiển thị\nloading spinner"]
    TH --> YTDLP["yt-dlp trích xuất\nmetadata"]
    YTDLP --> TYPE{"Loại nội dung?"}

    TYPE -- Video đơn --> V1["Cập nhật tiêu đề\n& thông tin video"]
    V1 --> V2["Tạo thread:\nthread_thumbnail.py"]
    V2 --> V3["Hiển thị thumbnail\ntrên UI"]
    V3 --> V4["Kích hoạt nút\nDownload"]

    TYPE -- Playlist --> P1["Lấy danh sách\ntất cả video"]
    P1 --> P2["Tạo VideoItemWidget\ncho từng video"]
    P2 --> P3["Thêm vào scrollArea\nvới animation"]
    P3 --> P4["Kích hoạt nút\nDownload All"]

    TYPE -- Lỗi --> FETCHERR["Hiển thị thông báo\ntrích xuất thất bại"]

    style U fill:#4A90D9,color:#fff,stroke:none
    style ERR fill:#E74C3C,color:#fff,stroke:none
    style NETERR fill:#E74C3C,color:#fff,stroke:none
    style FETCHERR fill:#E74C3C,color:#fff,stroke:none
```

---

## 4. Luồng tải xuống

```mermaid
flowchart TD
    A(["Người dùng nhấn Download\n/ Download All"]) --> B["DownloadHandler\nbắt đầu xử lý"]
    B --> C{"Chọn định dạng\nMP4 hay MP3?"}

    C -- MP4 --> D{"Người dùng chọn\nChất lượng?"}
    D -- Chưa chọn --> D1["Mở Quality Picker\nDialog"]
    D1 --> D2["Người dùng xác nhận\nchất lượng"]
    D2 --> E
    D -- Đã chọn --> E

    C -- MP3 --> E

    E{"Download đơn\nhay Playlist?"}
    E -- Video đơn --> F1["Tạo thread:\nthread_download_single.py"]
    E -- Playlist --> F2["Tạo thread:\nthread_download_playlist.py"]

    F1 --> G["yt-dlp thực thi\ntải xuống"]
    F2 --> G

    G --> H["Emit signals:\n• progress %\n• tốc độ tải\n• tên file"]
    H --> I["UI cập nhật\nProgress Bar & Label"]

    I --> J{"Tải xong?"}
    J -- Thất bại --> K["Emit error signal\nHiển thị lỗi"]
    J -- Thành công --> L["Thông báo hoàn tất\ntrên UI"]
    L --> M["Lưu vào HistoryManager"]
    M --> N["Ghi lịch sử\nra file JSON"]

    style A fill:#4A90D9,color:#fff,stroke:none
    style K fill:#E74C3C,color:#fff,stroke:none
    style L fill:#27AE60,color:#fff,stroke:none
```

---

## 5. Luồng quản lý lịch sử

```mermaid
flowchart LR
    A["Hoàn tất tải xuống"] --> B["HistoryManager\n.add_entry()"]
    B --> C["Ghi vào\nhistory.json"]
    C --> D["Cập nhật UI\nHistory Tab"]

    E["Mở ứng dụng\nlần tiếp theo"] --> F["HistoryManager\n.load_history()"]
    F --> G["Đọc history.json"]
    G --> H["Tạo HistoryItemWidget\ncho từng entry"]
    H --> I["Hiển thị trong\nui_history_ver2_0.py"]

    J["Người dùng xóa\n1 item lịch sử"] --> K["HistoryManager\n.remove_entry()"]
    K --> L["Cập nhật file JSON\n& refresh UI"]

    style A fill:#27AE60,color:#fff,stroke:none
    style E fill:#4A90D9,color:#fff,stroke:none
```

---

## 6. Sơ đồ tương tác đầy đủ

Sơ đồ dưới đây thể hiện mối liên hệ giữa các tầng kiến trúc (View → Controller → Model).

```mermaid
sequenceDiagram
    actor User as 👤 Người dùng
    participant View as 🖥️ View<br/>(ui_main_ver9_6)
    participant MainCtrl as ⚙️ MainWindow<br/>(main_window.py)
    participant SearchH as 🔍 SearchHandler
    participant DownloadH as ⬇️ DownloadHandler
    participant UIH as 🎨 UIHandler
    participant Model as 🧵 Models<br/>(Threads)
    participant Hist as 📋 HistoryManager

    User->>View: Nhập URL & nhấn Find
    View->>MainCtrl: Signal: findBtn.clicked
    MainCtrl->>SearchH: handle_search(url)
    SearchH->>UIH: show_loading()
    SearchH->>Model: FetchInfoThread.start()
    Model-->>SearchH: Signal: info_fetched(data)
    SearchH->>View: Cập nhật UI (thumbnail, title, items)
    SearchH->>UIH: hide_loading()

    User->>View: Nhấn Download
    View->>MainCtrl: Signal: downloadBtn.clicked
    MainCtrl->>DownloadH: handle_download(info)
    DownloadH->>Model: DownloadThread.start()
    Model-->>View: Signal: progress(percent, speed)
    View->>User: Cập nhật Progress Bar

    Model-->>DownloadH: Signal: download_finished(file_path)
    DownloadH->>Hist: add_entry(file_path)
    Hist->>Hist: Ghi history.json
    DownloadH->>UIH: show_success_notification()
    UIH->>View: Hiển thị thông báo hoàn tất
```

---

## 7. Cấu trúc file dự án

```
ytb_playlist_downloader/
├── app.py                          # 🚀 Entry point
├── requirements.txt                # 📦 Dependencies
├── docs/
│   ├── workflow.md                 # 📄 File này — tài liệu luồng hoạt động
│   ├── UI_VERSIONING_GUIDE.md      # 📄 Hướng dẫn versioning UI
│   └── ideas/                      # 💡 Ý tưởng tính năng mới
│       └── drag_drop_queue.md
├── src/
│   ├── app.py
│   ├── controllers/
│   │   ├── main_window.py
│   │   ├── ui_handler.py
│   │   ├── search_handler.py
│   │   ├── download_handler.py
│   │   └── download_dialog_controller.py
│   ├── models/
│   │   ├── history_manager.py
│   │   ├── thread_fetch_info.py
│   │   ├── thread_thumbnail.py
│   │   ├── thread_download_single.py
│   │   ├── thread_download_playlist.py
│   │   └── thread_network_checker.py
│   ├── views/
│   │   ├── ui_main_ver9_6.py
│   │   ├── ui_video_ver6_2.py
│   │   ├── ui_history_ver2_0.py
│   │   ├── ui_download_dialog_ver1_0.py
│   │   ├── custom_widgets.py
│   │   ├── history_item1_5.py
│   │   └── ui_config.py
│   └── utils/
│       └── helpers.py
├── ui/                             # 🎨 File .ui và .qss gốc (Qt Designer)
├── img/                            # 🖼️ Tài nguyên hình ảnh
└── bin/                            # 🔧 File thực thi / build output
```

---

*Cập nhật lần cuối: 2026-06-18*
