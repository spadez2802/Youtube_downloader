# QSS Theming — Tập trung StyleSheet

**Trạng thái:** 🔍 In Review  
**Ngày tạo:** 2026-06-17  
**Liên quan:** [settings_page.md](./settings_page.md) — cần hoàn thành trước khi làm accent color changer  
**Backup stylesheet:** [`ui/style_backup.qss`](../../ui/style_backup.qss)

---

## Mô tả

Migrate toàn bộ inline stylesheet đang phân tán trong các file `.ui` và controller code sang **một file `style.qss` duy nhất**. Dùng placeholder `ACCENT_COLOR` thay cho màu hardcode `#1ED761`, resolve tại runtime qua class `ThemeManager`. Kết quả: đổi màu accent toàn bộ app chỉ cần **1 dòng code**.

---

## Vấn đề hiện tại

Màu `#1ED761` đang bị hardcode **rải rác** ở nhiều nơi:

| File | Số chỗ hardcode | Loại |
|---|---|---|
| `src/views/ui_main_ver9_6.py` | ~30 dòng | Generated từ `newui.ui` |
| `src/views/ui_video_ver6_2.py` | 9 dòng | Generated từ `mini.ui` |
| `src/views/ui_download_dialog_ver1_0.py` | 6 dòng | Generated từ `download_dialog.ui` |
| `src/controllers/ui_handler.py` | 4 dòng | setStyleSheet() trong code |
| `src/controllers/search_handler.py` | 5 dòng | setStyleSheet() trong code |
| `src/controllers/download_dialog_controller.py` | 3 dòng | setStyleSheet() trong code |
| `src/controllers/main_window.py` | 1 dòng | setStyleSheet() trong code |

> **Nguyên nhân**: Qt stylesheet specificity — inline style trong `.ui` ghi đè `QApplication.setStyleSheet()`, nên không thể dùng global style nếu còn inline style.

---

## Giải pháp (Hướng B)

```
Xóa toàn bộ inline styles trong .ui files
            ↓
Tạo file ui/style.qss với ACCENT_COLOR placeholder
            ↓
ThemeManager load .qss → replace ACCENT_COLOR → QApplication.setStyleSheet()
            ↓
Đổi màu accent = chỉ cần gọi theme_manager.apply(app, new_color)
```

---

## Bản sao Stylesheet đã tạo

> File [`ui/style_backup.qss`](../../ui/style_backup.qss) chứa **28 sections** stylesheet đầy đủ, extract từ tất cả file active. Dùng làm reference khi xóa inline styles trong Qt Designer.

---

## Các file cần tạo / sửa

### [NEW] `ui/style.qss`

Copy từ `style_backup.qss`. Sử dụng placeholder:
- `ACCENT_COLOR` — thay thế `#1ED761`
- `ARROW_ICON_PATH` — thay thế đường dẫn icon cứng (resolve tại runtime)

**28 sections bao gồm:**

| Sections | Widgets |
|---|---|
| 1–2 | QMainWindow, #centralwidget, #sideBarWidget |
| 3–5 | #widget, #widget_2, #enterWidget, #enterPlace |
| 6–7 | #clearBtn, #findBtn |
| 8–10 | #linkName, #linkContentWidget, #videoImg |
| 11–13 | #downloadBtn, #comboBoxDownloadOption, #comboBoxDownloadQuality |
| 14–16 | #downloadAllBtn, #comboBoxDownloadAllOpt, #btnClearAll, #btnChooseAll |
| 17–18 | #miniSideBarBtn, #listWidget |
| 19–20 | QMenuBar, QMenu |
| 21–24 | HistoryCard, context menu, delete button, header labels |
| 25–26 | QDialog, QProgressBar, #btnPauseContinue, #btnCancel |
| 27 | #miniCard, #downloadVBtn, #comboBoxDownloadOpt, #comboBoxDQuality |
| 28 | QMessageBox |

### [NEW] `src/utils/theme_manager.py`

```python
from utils.helpers import get_asset_path

class ThemeManager:
    DEFAULT_ACCENT = "#1ED761"
    QSS_PATH = "ui/style.qss"

    def __init__(self):
        self._raw_qss = ""
        self._load_qss()

    def _load_qss(self):
        path = get_asset_path(self.QSS_PATH)
        with open(path, "r", encoding="utf-8") as f:
            self._raw_qss = f.read()
        arrow_path = get_asset_path("img/icon/down_arrow.png").replace("\\", "/")
        self._raw_qss = self._raw_qss.replace("ARROW_ICON_PATH", arrow_path)

    def apply(self, app, accent_color: str = None):
        color = accent_color or self.DEFAULT_ACCENT
        qss = self._raw_qss.replace("ACCENT_COLOR", color)
        app.setStyleSheet(qss)
```

---

## Bước thực hiện

### Bước 1 — Do người dùng thực hiện trong Qt Designer

Xóa `styleSheet` property của các widget sau:

| File .ui | Widgets cần xóa stylesheet |
|---|---|
| **newui.ui** | QMainWindow, #centralwidget, #widget, #widget_2, #widget_3, #enterWidget, #enterPlace, #clearBtn, #findBtn, #linkName, #linkContentWidget, #videoImg, #downloadBtn, #comboBoxDownloadOption, #comboBoxDownloadQuality, #downloadAllBtn, #comboBoxDownloadAllOpt, #btnClearAll, #btnChooseAll, #miniSideBarBtn, #listWidget, #sideBarWidget |
| **download_dialog.ui** | #btnPauseContinue, #btnCancel |
| **mini.ui** | #miniCard, #widgetDownloadOpt, #downloadVBtn, #comboBoxDownloadOpt, #comboBoxDQuality |

Sau khi xóa → Save → chạy `pyside6-uic` regenerate file `.py`.

### Bước 2–6 — Do code thực hiện

| Bước | Việc |
|---|---|
| 2 | Tạo `ui/style.qss` từ `style_backup.qss` |
| 3 | Tạo `src/utils/theme_manager.py` |
| 4 | Xóa `setStyleSheet()` trong `ui_handler.py`, `search_handler.py`, `download_dialog_controller.py`, `main_window.py` |
| 5 | Tích hợp `ThemeManager` vào `main_window.py` |
| 6 | Kết nối với accent color changer trong Settings |

---

## setStyleSheet() cần xóa trong controllers

### `ui_handler.py`
- Xóa: `self.ui.menubar.setStyleSheet(...)`
- Xóa: `self.ui.menuAAA.setStyleSheet(...)`
- Xóa: `self.ui.miniSideBarBtn.setStyleSheet(...)`
- Xóa: `self.ui.clearBtn.setStyleSheet(...)`
- **Giữ**: `self.ui.historyList.setStyleSheet(...)` (border dynamic khi mở/đóng)

### `search_handler.py`
- Xóa: `btn.setStyleSheet(...)` trong `update_history_delete_btn_state`
- Xóa: `msg_box.setStyleSheet(...)`
- **Giữ**: badge_color logic cho `labelType` (dynamic theo type)

### `download_dialog_controller.py`
- Xóa: `self.setStyleSheet(...)` block

### `main_window.py`
- Xóa: `self.setStyleSheet("QMainWindow { background-color: ... }")`

---

## Open Questions

> **Q1**: `#historyList` border thay đổi khi mở/đóng (border-right: 2px solid ACCENT_COLOR vs không border). Giữ `setStyleSheet()` dynamic hay dùng cách khác?

> **Q2**: Đặt `style.qss` ở `ui/style.qss` hay `src/resources/style.qss`?

---

## Verification Checklist

- [ ] Chạy app sau migrate → giao diện giống hệt trước (màu `#1ED761` đúng)
- [ ] Đổi `accent_color` trong `settings.json` thành `#FF5733` → restart → tất cả widget đổi màu
- [ ] Download Dialog, History sidebar, Video cards, MenuBar, QMessageBox đều đúng màu
- [ ] Accent color changer trong Settings → apply ngay không cần restart
