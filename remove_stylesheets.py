import os, re

ui_dir = r"d:\design\ytb_playlist_downloader\ui"
pattern = re.compile(r'[ \t]*<property name="styleSheet">[\s\S]*?</property>\n?')

ui_files = [f for f in os.listdir(ui_dir) if f.endswith(".ui")]
for filename in ui_files:
    filepath = os.path.join(ui_dir, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content, count = pattern.subn('', content)
    if count > 0:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Removed {count} stylesheets from {filename}")
