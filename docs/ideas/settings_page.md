# Settings Page

**Trạng thái:** 🔍 In Review  
**Ngày tạo:** 2026-06-17  
**Liên quan:** [qss_theming.md](./qss_theming.md) — cần hoàn thành QSS migration trước khi implement accent color

---

## Mô tả

Tạo trang **Settings** hoàn chỉnh mở từ menu `● ● ●` → "Setting". Giao diện dạng `QDialog` gồm **2 tab**: Cài đặt chung (Basic) và Nâng cao (Advanced). Toàn bộ cài đặt lưu vào `settings.json` local, đọc lại khi khởi động app.

---

## Bảng màu hiện tại của app (tham khảo)

| Vai trò | Màu | Ghi chú |
|---|---|---|
| Accent / Primary | `#1ED761` | Viền nút, hover fill, highlight |
| Background | `#000000` | Nền centralwidget |
| Surface / Panel | `#2b2b2b` | Sidebar, card, menu |
| Button normal | `#434343` | Nền nút chưa hover |
| Border phụ | `#3e3e3e` | Đường ngăn cách |
| Disabled border | `#888888` | Viền nút disabled |
| Text chính | `white` | Label, button text |
| Text trên accent | `black` | Khi hover vào nút |
| Font | `Segoe UI`, Helvetica, Arial | Toàn bộ app |

---

## Cấu trúc trang Settings

```
SettingsDialog (QDialog)
├── Tab 1: Cài đặt chung
│   ├── [Nhóm 1] Thư mục lưu file
│   ├── [Nhóm 2] Tải xuống mặc định
│   └── [Nhóm 3] Lịch sử
└── Tab 2: Nâng cao
    └── [Nhóm 4] Mạng & Proxy
```

---

## Nội dung từng nhóm

### Nhóm 1 — Thư mục lưu file

| Widget | Mô tả |
|---|---|
| `QLineEdit` + `QPushButton` Browse | Đường dẫn thư mục lưu mặc định |
| `QCheckBox` | Tự động tạo subfolder tên playlist |
| `QCheckBox` | Mở thư mục sau khi tải xong |

### Nhóm 2 — Tải xuống mặc định

| Widget | Mô tả |
|---|---|
| `QComboBox` | Định dạng mặc định: MP3 / MP4 |
| `QComboBox` | Chất lượng mặc định: 1080p / 720p / 480p / Best |
| `QComboBox` | Bitrate mặc định (MP3): 320 / 192 / 128 kbps |
| `QSpinBox` | Số luồng tải đồng thời (1–5) |

### Nhóm 3 — Lịch sử

| Widget | Mô tả |
|---|---|
| `QCheckBox` | Bật/tắt lưu lịch sử tải |
| `QSpinBox` | Số mục lịch sử tối đa (50 / 100 / không giới hạn) |
| `QPushButton` Xóa lịch sử | Xóa toàn bộ history.json |

### Nhóm 4 — Mạng & Proxy (Tab Nâng cao)

| Widget | Mô tả |
|---|---|
| `QLineEdit` | Địa chỉ proxy (để trống = không dùng) |
| `QLineEdit` | Rate limit (VD: `5M` = 5 MB/s) |
| `QSpinBox` | Số lần retry khi lỗi (1–5) |

---

## Màu giao diện (Accent Color Picker)

Trong Tab **Cài đặt chung**, thêm:
- `QPushButton` hình vuông nhỏ hiển thị màu accent hiện tại (preview swatch)
- Click → mở `QColorDialog` chọn màu
- Lưu vào `settings.json["accent_color"]`
- Apply ngay hoặc sau khi nhấn Lưu (cần xác nhận — xem Open Questions)

> Cơ chế apply phụ thuộc vào [qss_theming.md](./qss_theming.md) đã hoàn thành chưa.

---

## Các file cần tạo / sửa

### [NEW] `src/models/settings_manager.py`

Class `SettingsManager`:
- `load()` — đọc `settings.json`, fallback về default nếu file không tồn tại
- `save()` — ghi toàn bộ dict xuống file
- `get(key, default)` / `set(key, value)`

**Default schema:**
```json
{
  "download_path": "",
  "create_subfolder_for_playlist": true,
  "open_folder_after_download": false,
  "default_format": "MP4",
  "default_quality": "1080p",
  "default_bitrate": "192kbps",
  "max_concurrent_downloads": 2,
  "save_history": true,
  "max_history_entries": 100,
  "proxy": "",
  "rate_limit": "",
  "retry_count": 3,
  "accent_color": "#1ED761"
}
```

### [NEW] `ui/settings_dialog.ui`

`QDialog` với `QTabWidget` 2 tab. Style theo bảng màu app (nền `#2b2b2b`, accent `#1ED761`).

### [NEW] `src/controllers/settings_dialog_controller.py`

`SettingsDialogController`:
- Nạp giá trị từ `SettingsManager` khi mở dialog
- Nút Browse → `QFileDialog.getExistingDirectory()`
- Thay đổi `default_format` → ẩn/hiện quality combobox
- Nút Save → validate → `settings_manager.save()` → apply accent → `accept()`
- Nút Cancel → `reject()`
- Nút Xóa lịch sử → `search_handler.clear_all_history()`

### [MODIFY] `src/controllers/main_window.py`

- Khởi tạo `SettingsManager` trong `__init__`
- Kết nối `actionSetting` → mở `SettingsDialogController`
- Truyền `settings_manager` vào các handler cần dùng

### [MODIFY] `src/controllers/download_handler.py`

- Đọc `download_path`, `proxy`, `rate_limit`, `retry_count` từ settings khi bắt đầu tải

### [MODIFY] `src/models/history_manager.py`

- Thêm method `clear_all()` nếu chưa có
- Đọc `max_history_entries` từ settings khi append

---

## Open Questions

> **Q1**: Settings mở dạng **QDialog popup** hay **Single Page** (thay nội dung trong cùng 1 cửa sổ)?
> Hiện tại đang plan dùng QDialog vì đơn giản hơn.

> **Q2**: Accent color — apply **ngay lập tức** (live preview) khi chọn màu, hay chỉ apply sau khi nhấn Lưu?

> **Q3**: `settings.json` đặt cùng thư mục gốc (giống `history.json`) hay trong `AppData`?

---

## Verification Checklist

- [ ] Mở Settings từ menu `● ● ●` → Dialog mở đúng style
- [ ] Thay đổi thư mục lưu → Tải video → File lưu đúng vị trí
- [ ] Thay đổi định dạng mặc định → Mở lại app → Vẫn giữ cài đặt
- [ ] Xóa lịch sử → Sidebar lịch sử trống
- [ ] Đổi accent color → Tất cả nút, combobox, border đổi màu
- [ ] Nhập proxy sai → App vẫn chạy bình thường (không crash)
