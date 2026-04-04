import re
import os

def update_from_playlist():
    # هذا هو اسم الملف الذي يظهر في صورتك الأخيرة
    file_path = 'playlist (2).m3u' 
    
    if not os.path.exists(file_path):
        print(f"❌ Error: {file_path} not found in GitHub!")
        return

    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    channels_html = ""
    for i in range(len(lines)):
        if lines[i].startswith('#EXTINF'):
            # استخراج الاسم والشعار
            name = lines[i].split(',')[-1].strip()
            logo_match = re.search('tvg-logo="(.*?)"', lines[i])
            logo = logo_match.group(1) if logo_match else "https://mytvpro1.github.io/favicon.ico"
            
            # الرابط في السطر التالي
            if i + 1 < len(lines):
                url = lines[i+1].strip()
                if url.startswith('http'):
                    # تصميم كارت القناة لموقع Simo Final
                    channels_html += f'''
                    <div class="movie-card" onclick="openLivePlayer('{url}')">
                        <img src="{logo}" alt="{name}" onerror="this.src='https://mytvpro1.github.io/favicon.ico'" loading="lazy">
                        <div class="movie-title">{name}</div>
                    </div>'''

    # حقن الكود في index.html بين العلامات
    try:
        with open('index.html', 'r', encoding='utf-8') as f:
            content = f.read()

        start_tag = ""
        end_tag = ""

        if start_tag in content and end_tag in content:
            parts = content.split(start_tag)
            parts_after = parts[1].split(end_tag)
            new_content = parts[0] + start_tag + "\n" + channels_html + "\n" + end_tag + parts_after[1]
            
            with open('index.html', 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"✅ Successfully added channels from {file_path}!")
        else:
            print("❌ Markers not found in index.html. Add and first.")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    update_from_playlist()
