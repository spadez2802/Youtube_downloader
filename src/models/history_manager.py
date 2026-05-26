import os
import json
import sys

class HistoryManager:
    def __init__(self):
        self.history_data = []

    def get_history_path(self):
        # Kiểm tra môi trường .exe hay .py
        if getattr(sys, 'frozen', False):
            base_dir = os.path.dirname(sys.executable)
        else:
            # Vì file này nằm trong src/models/, nên lùi ra 2 cấp để ra gốc project
            base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        return os.path.join(base_dir, "history.json")

    def load_history(self):
        path = self.get_history_path()
        if os.path.exists(path):
            try:
                with open(path, 'r', encoding='utf-8') as f:
                    self.history_data = json.load(f)
                    return self.history_data
            except:
                pass
        return []

    def save_history(self, title, url, is_playlist):
        prefix = "[Playlist] " if is_playlist else "[Video] "
        full_title = f"{prefix}{title}"
        
        # Làm sạch list: Xóa bài trùng để đưa bài mới nhất lên đầu
        self.history_data = [item for item in self.history_data if item['url'] != url]
        self.history_data.insert(0, {'title': full_title, 'url': url})
        
        # Giới hạn 100 bài gần nhất
        self.history_data = self.history_data[:100]
        
        try:
            with open(self.get_history_path(), 'w', encoding='utf-8') as f:
                json.dump(self.history_data, f, ensure_ascii=False, indent=4)
        except Exception as e:
            print(f"Lỗi lưu lịch sử: {e}")
            
        return self.history_data