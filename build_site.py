import requests

# رابط المصدر الذي يعمل في PotPlayer
M3U_URL = "https://iptv-org.github.io/iptv/languages/ara.m3u"

def build():
    # 1. جلب القنوات
    r = requests.get(M3U_URL)
    lines = r.text.split('\n')
    
    channels_html = ""
    for i in range(len(lines)):
        if lines[i].startswith('#EXTINF'):
            # استخراج الاسم والشعار (إذا وجد) والرابط
            name = lines[i].split(',')[-1].strip()
            url = lines[i+1].strip()
            
            if url.startswith('http'):
                # تصميم الكارد ليتناسب مع تصميم موقعك MYTVPRO
                channels_html += f'''
                <div class="movie-card" onclick="openLivePlayer('{url}')">
                    <img src="https://mytvpro1.github.io/favicon.ico" style="object-fit: contain; padding: 20px; background: #111;">
                    <div class="movie-title">{name}</div>
                </div>'''

    # 2. قراءة ملف index.html الأساسي
    with open("index.html", "r", encoding="utf-8") as f:
        content = f.read()

    # 3. حقن القنوات في المكان المخصص (بين العلامات)
    import re
    pattern = r".*?"
    replacement = f"{channels_html} "
    
    new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)

    # 4. حفظ الملف المحدث
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(new_content)
    print("تم تحديث قسم Live Foot بنجاح داخل index.html!")

if __name__ == "__main__":
    build()
