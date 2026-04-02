import requests
import re

# رابط المصدر
M3U_URL = "https://iptv-org.github.io/iptv/languages/ara.m3u"

def build():
    try:
        # 1. جلب القنوات
        print("جاري جلب القنوات من المصدر...")
        r = requests.get(M3U_URL, timeout=15)
        r.raise_for_status()
        lines = r.text.split('\n')
        
        channels_html = ""
        for i in range(len(lines)):
            if lines[i].startswith('#EXTINF'):
                # استخراج الاسم
                name = lines[i].split(',')[-1].strip()
                # الرابط يكون عادة في السطر التالي
                if i + 1 < len(lines):
                    url = lines[i+1].strip()
                    
                    if url.startswith('http'):
                        # تصميم الكارد ليتناسب مع تصميم MYTVPRO
                        channels_html += f'''
            <div class="movie-card" onclick="openLivePlayer('{url}')">
                <img src="https://mytvpro1.github.io/favicon.ico" style="object-fit: contain; padding: 20px; background: #111;">
                <div class="movie-title">{name}</div>
            </div>'''

        # 2. قراءة ملف index.html
        with open("index.html", "r", encoding="utf-8") as f:
            content = f.read()

        # 3. حقن القنوات بين العلامات المخصصة
        # النمط الصحيح للبحث عن ما بين العلامات واستبداله
        start_tag = ""
        end_tag = ""
        
        pattern = f"{start_tag}.*?{end_tag}"
        replacement = f"{start_tag}\n{channels_html}\n{end_tag}"
        
        # التأكد من وجود العلامات في الملف قبل الاستبدال
        if start_tag in content and end_tag in content:
            new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)
            
            # 4. حفظ الملف المحدث
            with open("index.html", "w", encoding="utf-8") as f:
                f.write(new_content)
            print(f"تم بنجاح حقن القنوات داخل index.html!")
        else:
            print("خطأ: لم يتم العثور على علامات CHANNELS_START و CHANNELS_END في ملف index.html")

    except Exception as e:
        print(f"حدث خطأ أثناء التحديث: {e}")

if __name__ == "__main__":
    build()
