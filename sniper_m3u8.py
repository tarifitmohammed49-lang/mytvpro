import re
import os

def update_from_playlist():
    # اسم ملف التشغيل الخاص بك
    file_path = 'playlist (2).m3u' 
    
    if not os.path.exists(file_path):
        print(f"❌ Error: {file_path} not found in GitHub!")
        return

    # قراءة محتوى ملف m3u
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except Exception as e:
        print(f"❌ Error reading playlist: {e}")
        return

    channels_html = ""
    for i in range(len(lines)):
        # البحث عن سطر المعلومات الذي يبدأ بـ #EXTINF
        if lines[i].startswith('#EXTINF'):
            # استخراج اسم القناة (يكون بعد الفاصلة الأخيرة)
            name = lines[i].split(',')[-1].strip()
            
            # استخراج شعار القناة إذا وجد
            logo_match = re.search('tvg-logo="(.*?)"', lines[i])
            logo = logo_match.group(1) if logo_match else "https://mytvpro1.github.io/favicon.ico"
            
            # الرابط يكون عادة في السطر الذي يلي #EXTINF مباشرة
            next_line_index = i + 1
            while next_line_index < len(lines):
                url = lines[next_line_index].strip()
                if url and not url.startswith('#'):
                    # بناء كود HTML متوافق مع تصميم "Simo Final"
                    channels_html += f'''
            <div class="movie-card" onclick="openLivePlayer('{url}')">
                <img src="{logo}" alt="{name}" onerror="this.src='https://mytvpro1.github.io/favicon.ico'" loading="lazy">
                <div class="movie-title">{name}</div>
            </div>'''
                    break
                next_line_index += 1

    # تحديث ملف index.html
    try:
        if not os.path.exists('index.html'):
            print("❌ Error: index.html not found!")
            return

        with open('index.html', 'r', encoding='utf-8') as f:
            content = f.read()

        # هذه هي العلامات التي وضعتها لك في كود الـ HTML
        start_tag = ""
        end_tag = ""

        if start_tag in content and end_tag in content:
            # تقسيم النص واستبدال ما بين العلامات بالقنوات الجديدة
            parts = content.split(start_tag)
            parts_after = parts[1].split(end_tag)
            
            new_content = parts[0] + start_tag + "\n" + channels_html + "\n            " + end_tag + parts_after[1]
            
            with open('index.html', 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"✅ Successfully updated index.html with channels from {file_path}!")
        else:
            print("❌ Error: Sniper markers not found in index.html. Please ensure and exist.")
    except Exception as e:
        print(f"❌ Error during HTML update: {e}")

if __name__ == "__main__":
    update_from_playlist()
