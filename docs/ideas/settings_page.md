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
    └── [Nhóm 4] Tải xuống nâng cao
```

---

## Nội dung từng nhóm

### Nhóm 1 — Thư mục lưu file

| Widget | Mô tả |
|---|---|
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
| `QPushButton` Xóa lịch sử | Xóa toàn bộ history.json |

### Nhóm 4 — Tải xuống nâng cao (Tab Nâng cao)

| Widget | Mô tả |
|---|---|
| `QCheckBox` | Sử dụng đường dẫn mặc định (Không hỏi lại đường dẫn khi tải xuống). Khi tick vào ô này thì các ô bên dưới mới được enable. |
| `QLineEdit` (read-only) + `QPushButton` Change | Hiển thị và chọn đường dẫn mặc định. Mặc định bị disable, chỉ enable khi tick ô trên. Nếu tick ô trên mà đường dẫn trống, hiện thông báo lỗi. |
| `QCheckBox` | Tải xuống với tên gốc. Mặc định bị disable, chỉ enable khi tick ô trên. (Nếu tick: tải tên gốc; nếu không tick: hiện 1 ô nhập tên file khi tải) |

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
  "use_default_path": false,
  "use_original_name": true,
  "default_format": "MP4",
  "default_quality": "1080p",
  "default_bitrate": "192kbps",
  "max_concurrent_downloads": 2,
  "accent_color": "#1ED761"
}
```

### [NEW] `ui/settings_dialog.ui`

`QDialog` với `QTabWidget` 2 tab. Style theo bảng màu app (nền `#2b2b2b`, accent `#1ED761`).

### [NEW] `src/controllers/settings_dialog_controller.py`

`SettingsDialogController`:
- Nạp giá trị từ `SettingsManager` khi mở dialog
- Nút Change (chọn thư mục) → `QFileDialog.getExistingDirectory()`
- Thay đổi `default_format` → ẩn/hiện quality combobox
- Logic `use_default_path`:
  - Bắt sự kiện `toggled` để bật/tắt (enable/disable) ô chọn đường dẫn và ô "Tải xuống với tên gốc" bên dưới.
  - Cảnh báo khi tick `use_default_path` mà đường dẫn trống.
- Nút Save → validate → `settings_manager.save()` → apply accent → `accept()`
- Nút Cancel → `reject()`
- Nút Xóa lịch sử → `search_handler.clear_all_history()`

### [MODIFY] `src/controllers/main_window.py`

- Khởi tạo `SettingsManager` trong `__init__`
- Kết nối `actionSetting` → mở `SettingsDialogController`
- Truyền `settings_manager` vào các handler cần dùng

### [MODIFY] `src/controllers/download_handler.py`

- Đọc `download_path`, `use_default_path` và `use_original_name` từ settings khi bắt đầu tải.
- Nếu `use_default_path` = True: Không hỏi thư mục. Nếu `use_original_name` = False, hiện 1 ô nhập để hỏi tên file/playlist trước khi tải.
- Nếu `use_default_path` = False: Hỏi người dùng chọn đường dẫn tải xuống.

### [MODIFY] `src/models/history_manager.py`

- Thêm method `clear_all()` nếu chưa có
- Lưu lịch sử không giới hạn (bỏ giới hạn max_history_entries)

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
