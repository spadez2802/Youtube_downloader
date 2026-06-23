# Drag & Drop Download Queue

**Trạng thái:** 📝 Draft  
**Ngày tạo:** 2026-06-17  
**Cần xác nhận thêm:** Vị trí đặt Drop Zone (xem Open Questions)

---

## Mô tả

Thêm tính năng **kéo thả link YouTube** vào app để tạo danh sách tải xuống (queue). Người dùng có thể kéo link từ trình duyệt thả vào khu vực Sidebar phải của app. URL hiển thị ngay lập tức, title + thumbnail được fetch ngầm trong nền. Việc tải chỉ bắt đầu khi người dùng nhấn nút xác nhận.

---

## Quyết định thiết kế đã được xác nhận

| # | Câu hỏi | Quyết định |
|---|---|---|
| 1 | Drag & Drop vs Nhập tay | **Giữ cả hai** — ô `enterPlace` vẫn tồn tại song song |
| 2 | Hiển thị dữ liệu | **Phương án 3**: Hiện URL ngay, lazy-load title + thumbnail ngầm |
| 3 | Khi nào tải? | **Chỉ tải khi nhấn xác nhận** — queue được xây dựng trước, không auto-start |

---

## Open Questions

> **Quyết định cần xác nhận:** Khu vực nhận Drop sẽ được đặt ở đâu?
> - **Phương án A**: Nhúng vào `sideBarWidget` (sidebar phải) — thả link là thanh sidebar mở ra luôn, cùng chỗ với danh sách playlist hiện tại.
> - **Phương án B**: Tạo khu vực Drop riêng biệt ở giữa màn hình (dưới `widget_2`) — trực quan hơn nhưng cần chỉnh layout nhiều hơn.

---

## Tổng quan luồng hoạt động

```
Người dùng kéo link ──► Sidebar nhận Drop ──► Thêm item "đang tải..." vào queue
                                                        │
                                                        ▼
                                              Thread fetch ngầm (title + thumb)
                                                        │
                                                        ▼
                                              Cập nhật UI item → Hiện title + ảnh
                                                        │
                                                        ▼
                                         [Người dùng nhấn "Download" / "Download ALL"]
                                                        │
                                                        ▼
                                              Bắt đầu tải xuống
```

---

## Các file cần tạo / sửa

### [NEW] `src/views/queue_item_widget.py`

Widget hiển thị mỗi item trong queue. Có 3 trạng thái:

| State | Giao diện |
|---|---|
| `LOADING` | Spinner/skeleton animation, hiện raw URL được cắt ngắn |
| `READY` | Hiện thumbnail + title đầy đủ, nút ❌ xóa, checkbox tải |
| `ERROR` | Icon lỗi đỏ, tooltip thông báo nguyên nhân lỗi |

Thành phần chính:
- `QLabel` thumbnail (bo góc)
- `QLabel` title (wrap text, tối đa 2 dòng)
- `QLabel` trạng thái
- `QCheckBox` để chọn khi download hàng loạt
- `QPushButton` ❌ để xóa khỏi queue

> Kế thừa phong cách màu sắc (`#2b2b2b` nền, `#1ED761` accent), tương tự `VideoItemWidget` hiện tại.

---

### [NEW] `src/views/droppable_area.py`

Class `DroppableListArea(QWidget)`:

```python
# Pseudocode
class DroppableListArea(QWidget):
    url_dropped = Signal(str)

    def __init__(self):
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls() or event.mimeData().hasText():
            event.acceptProposedAction()
            self._set_highlight(True)   # Viền xanh #1ED761
        else:
            event.ignore()

    def dragLeaveEvent(self, event):
        self._set_highlight(False)

    def dropEvent(self, event):
        self._set_highlight(False)
        url = self._extract_url(event.mimeData())
        if url:
            self.url_dropped.emit(url)

    def _extract_url(self, mime_data):
        # Ưu tiên 1: Kéo tab trình duyệt
        if mime_data.hasUrls():
            return mime_data.urls()[0].toString()
        # Ưu tiên 2: Bôi đen text URL rồi kéo
        if mime_data.hasText():
            return mime_data.text().strip()
        return None
```

---

### [NEW] `src/controllers/queue_handler.py`

`QueueHandler` chịu trách nhiệm:
1. Nhận URL từ signal `url_dropped`
2. Validate sơ bộ (kiểm tra `youtube.com` / `youtu.be`)
3. Thêm `QueueItemWidget` trạng thái `LOADING` ngay lập tức
4. Spawn `FetchInfoThread` (tái dùng `thread_fetch_info.py`) fetch ngầm
5. Khi thread xong → Cập nhật item sang `READY` hoặc `ERROR`
6. Khi user nhấn xác nhận → Chuyển URL sang `download_handler.py`

> **Quan trọng**: Tái sử dụng `FetchInfoThread` và `YDL_OPTIONS` từ `main_window.py`, mỗi item có thread riêng để fetch song song.

---

### [MODIFY] `src/controllers/main_window.py`

- Khởi tạo `QueueHandler` trong `__init__`
- Kết nối `url_dropped` → `queue_handler.add_to_queue(url)`
- Kết nối nút Download cho Queue

### [MODIFY] `src/controllers/ui_handler.py`

Thêm method `set_drop_zone_highlight(active: bool)`:

```python
# Khi đang kéo lướt vào
border: 2px dashed #1ED761;
background-color: rgba(30, 215, 97, 0.08);

# Bình thường
border: 2px dashed #3e3e3e;
background-color: transparent;
```

---

## Verification Checklist

- [ ] Kéo tab YouTube từ Chrome/Edge → Item xuất hiện với trạng thái Loading
- [ ] Sau vài giây → Item cập nhật sang title thật + thumbnail
- [ ] Kéo link không phải YouTube → Thông báo lỗi nhẹ, không crash
- [ ] Kéo cùng 1 link 2 lần → Logic dedup (không thêm trùng)
- [ ] Nhấn ❌ trên item → Item biến mất khỏi queue
- [ ] Nhấn "Download" → Chỉ tải item được tick checkbox
- [ ] Ô `enterPlace` + nút `findBtn` vẫn hoạt động bình thường
