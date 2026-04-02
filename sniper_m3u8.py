import os
import requests
import re

# 1. جلب رابط الملف من إعدادات GitHub (Secrets)
m3u_url = os.getenv('IPTV_URL')

def fetch_channels():
    if not m3u_url:
        print("Error: IPTV_URL secret is not set!")
        return ""

    try:
        response = requests.get(m3u_url, timeout=15)
        response.raise_for_status()
        m3u_content = response.text
    except Exception as e:
        print(f"Error fetching M3U: {e}")
        return ""

    # استخراج القنوات باستخدام Regex (الاسم، اللوجو، والرابط)
    # نبحث عن #EXTINF مع tvg-logo و اسم القناة، ثم الرابط في السطر التالي
    pattern = re.compile(r'#EXTINF:-1.*?tvg-logo="(.*?)".*?,(.*?)\n(http.*)', re.MULTILINE)
    matches = pattern.findall(m3u_content)

    channels_html = ""
    
    for logo, name, url in matches:
        # تنظيف الرابط والاسم من أي مسافات زائدة
        url = url.strip()
        name = name.strip()
        
        # إنشاء الكارت بتنسيق MYTVPRO
        # نستخدم دالة openLivePlayer التي أضفناها في index.html
        card = f'''
        <div class="movie-card" onclick="openLivePlayer('{url}')">
            <img src="{logo}" alt="{name}" onerror="this.src='https://mytvpro1.github.io/favicon.ico'" loading="lazy">
            <div class="movie-title">{name}</div>
        </div>
        '''
        channels_html += card

    return channels_html

def update_index_html(content):
    file_path = 'index.html'
    if not os.path.exists(file_path):
        print("Error: index.html not found!")
        return

    with open(file_path, 'r', encoding='utf-8') as f:
        html_data = f.read()

    # تحديد علامات الحقن (يجب أن تتطابق تماماً مع الموجود في index.html)
    start_tag = ""
    end_tag = ""

    if start_tag in html_data and end_tag in html_data:
        # تقسيم الملف وحقن القنوات الجديدة
        before = html_data.split(start_tag)[0]
        after = html_data.split(end_tag)[1]
        
        new_html = before + start_tag + "\n" + content + "\n" + end_tag + after
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_html)
        print(f"Successfully injected {content.count('movie-card')} channels into index.html")
    else:
        print("Error: Could not find injection tags (CHANNELS_START/END) in index.html")

if __name__ == "__main__":
    print("Starting Sniper Update...")
    # 1. توليد كود الـ HTML الخاص بالقنوات
    new_content = fetch_channels() 
    
    if new_content:
        # 2. تحديث ملف الموقع مباشرة
        update_index_html(new_content)
    else:
        print("No channels found to update.")
