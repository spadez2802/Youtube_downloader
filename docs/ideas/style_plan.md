# Kế hoạch: Chuẩn hóa Stylesheet

## Hiện trạng

### Điểm tốt ✅
- Các file `.ui` **không có stylesheet** bên trong — đúng chuẩn
- `ThemeManager` + `ui/global_style.qss` đã tồn tại — là backbone đúng hướng
- `global_style.qss` dùng token `ACCENT_COLOR` và `ARROW_ICON_PATH` (dynamic)

### Vi phạm cần sửa ❌

| Vị trí | Nội dung hardcode |
|--------|-------------------|
| `settings_dialog_controller.py` L167 | `self.setStyleSheet("""...""")` — toàn bộ Settings Dialog |
| `settings_dialog_controller.py` L111 | `btnAccentPreview.setStyleSheet(...)` — dynamic (OK giữ lại) |
| `custom_widgets.py` L66, 70 | `setStyleSheet(style_opt/style_qual)` — ComboBox widget |
| `custom_widgets.py` L171, 181 | `labelDate/labelType.setStyleSheet(...)` — HistoryCard |
| `custom_widgets.py` L196 | `HistoryCard.setStyleSheet(...)` — hover effect |
| `custom_widgets.py` L250 | `HistoryItemWidget.setStyleSheet("background: transparent")` |
| `ui_handler.py` L61 | `historyList.setStyleSheet(...)` — scroll area |
| `ui_handler.py` L106 | `historyList.setStyleSheet(...)` — sau toggle |
| `main_window.py` L171, 180 | `statusbar.setStyleSheet(...)` — network status |
| `search_handler.py` L197 | `header_label.setStyleSheet(...)` — date header |

> **Lưu ý:** `btnAccentPreview.setStyleSheet(...)` là **dynamic** (thay đổi theo màu do user chọn), không thể đưa vào QSS tĩnh → giữ nguyên trong Controller.

---

## Quyết định kiến trúc: 1 file QSS hay nhiều file?

### Phương án A — 1 file QSS duy nhất (hiện tại)
- ✅ Đơn giản, `ThemeManager` chỉ load 1 file
- ✅ Token replacement (`ACCENT_COLOR`) áp dụng toàn bộ 1 lần
- ⚠️ File sẽ dài (~1000+ dòng)

### Phương án B — Nhiều file QSS phân theo component
```
ui/styles/
  ├── main_window.qss
  ├── history_sidebar.qss
  ├── settings_dialog.qss
  ├── custom_widgets.qss
  └── global.qss
```
- ✅ Dễ tìm style của từng component
- ⚠️ ThemeManager phải load nhiều file, merge trước khi replace token

### Lựa chọn: **Phương án A** (1 file) với cấu trúc SECTION rõ ràng
Lý do: `ThemeManager` đơn giản, token replacement nhất quán, và file đã có comment section. Chỉ cần **thêm section mới** vào `global_style.qss`.

---

## Kế hoạch thực hiện

1. **Thêm tiêu chuẩn vào `my_new_rules.md`**:
   - `.ui` files không được chứa stylesheet
   - Mọi style đều vào `ui/global_style.qss`
   - Chỉ giữ `setStyleSheet()` trong code nếu style là **dynamic** (thay đổi theo runtime)

2. **Thêm sections vào `global_style.qss`**:
   - `SECTION 9: SETTINGS DIALOG` — từ `settings_dialog_controller.py`
   - `SECTION 10: HISTORY SIDEBAR WIDGETS` — từ `custom_widgets.py`

3. **Sửa các file Python**:
   - `settings_dialog_controller.py`: xóa `_apply_style()`, xóa `setStyleSheet()`
   - `custom_widgets.py`: xóa hardcoded styles, dùng objectName + QSS
   - `ui_handler.py` + `main_window.py` + `search_handler.py`: xóa `setStyleSheet()` inline

4. **Giữ nguyên (dynamic)**:
   - `btnAccentPreview.setStyleSheet(...)` — màu thay đổi theo user pick
   - `statusbar.setStyleSheet(...)` — màu thay đổi theo network status

---

## Câu hỏi mở

> **Q:** Một số style như `labelType` badge color (`#1ED761` vs `#4A90D9`) thay đổi tùy `item_type` (video/playlist). Đây là dynamic → giữ `setStyleSheet()` trong code, hay chuyển sang dùng CSS class property?

**Đề xuất:** Dùng `setProperty("item_type", "video")` kết hợp với QSS selector `[item_type="video"]` → hoàn toàn không cần `setStyleSheet()` trong code.
