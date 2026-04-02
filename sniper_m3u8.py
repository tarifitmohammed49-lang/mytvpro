import os
import requests

# جلب الرابط من Secrets
m3u_url = os.getenv('IPTV_URL')

def fetch_channels():
    # هنا نضع الكود الخاص بك لجلب القنوات (هذا مثال)
    # تأكد أن السكريبت الخاص بك يولد متغير HTML يحتوي على كروت القنوات
    
    channels_html = ""
    # مثال لشكل الكارت الذي سيتم حقنه:
    # channels_html += '<div class="movie-card" onclick="openLivePlayer(\'URL\')">...</div>'
    
    return channels_html

def update_index_html(content):
    file_path = 'index.html'
    if not os.path.exists(file_path):
        print("Error: index.html not found!")
        return

    with open(file_path, 'r', encoding='utf-8') as f:
        html_data = f.read()

    # تحديد مكان الحقن
    start_tag = ""
    end_tag = ""

    if start_tag in html_data and end_tag in html_data:
        # استبدال ما بين العلامات بالمحتوى الجديد
        before = html_data.split(start_tag)[0]
        after = html_data.split(end_tag)[1]
        new_html = before + start_tag + "\n" + content + "\n" + end_tag + after
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_html)
        print("Successfully updated index.html with new channels!")
    else:
        print("Error: Injection tags not found in index.html")

if __name__ == "__main__":
    # 1. جلب البيانات
    new_content = fetch_channels() 
    # 2. تحديث ملف الموقع مباشرة
    update_index_html(new_content)
