import os
import requests
import re

def update_html_with_channels():
    # 1. جلب الرابط السري من إعدادات GitHub
    iptv_url = os.getenv('IPTV_URL')
    if not iptv_url:
        print("Error: IPTV_URL secret is not set!")
        return

    try:
        # 2. جلب قائمة القنوات (رابط M3U أو JSON)
        response = requests.get(iptv_url)
        data = response.text
        
        # هنا سنقوم بإنشاء كود الـ HTML لكل قناة
        # ملاحظة: هذا المثال يفترض أننا نستخرج روابط beIN
        # يمكنك تعديل الـ Regex حسب شكل البيانات القادمة من الرابط السري
        channels_html = ""
        
        # مثال لاستخراج القنوات (يجب تعديله ليتناسب مع مصدر روابطك)
        # هذا الكود سيولد بطاقة (Card) لكل قناة بنفس تصميم موقعك
        
        # لنفترض أننا سنضع قنوات beIN Sports كمثال ثابت الآن للتجربة:
        sample_channels = [
            {"name": "beIN SPORTS 1", "url": "رابط_القناة_المتغير", "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/af/BeIN_Sports_1_logo.svg/1200px-BeIN_Sports_1_logo.svg.png"},
            {"name": "beIN SPORTS 2", "url": "رابط_القناة_المتغير", "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/BeIN_Sports_2_logo.svg/1200px-BeIN_Sports_2_logo.svg.png"}
        ]

        for ch in sample_channels:
            channels_html += f"""
            <div class="movie-card" onclick="openLivePlayer('{ch['url']}')">
                <img src="{ch['logo']}" alt="{ch['name']} live" loading="lazy">
                <div class="movie-title">{ch['name']}</div>
            </div>
            """

        # 3. فتح ملف index.html وحقن الكود
        with open('index.html', 'r', encoding='utf-8') as f:
            content = f.read()

        # البحث عن العلامات واستبدال ما بينها
        pattern = r".*?"
        replacement = f"\n{channels_html}\n"
        
        new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)

        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(new_content)
            
        print("Successfully injected channels into index.html!")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    update_html_with_channels()
