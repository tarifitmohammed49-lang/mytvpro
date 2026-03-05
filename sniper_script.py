import requests
import json
import re

# مصادر قوية جداً ومتجددة تلقائياً
SOURCES = {
    "ar": "https://raw.githubusercontent.com/mohamed-if/iptv/master/arabic.m3u", # مصدر عربي قوي
    "de": "https://raw.githubusercontent.com/iptv-org/iptv/master/streams/de.m3u",
    "nl": "https://raw.githubusercontent.com/iptv-org/iptv/master/streams/nl.m3u",
    "en": "https://raw.githubusercontent.com/iptv-org/iptv/master/streams/us.m3u",
    "fr": "https://raw.githubusercontent.com/iptv-org/iptv/master/streams/fr.m3u",
    "global_sport": "https://raw.githubusercontent.com/TheBeast-0/Sniping/main/sports_fixed.m3u" # مصدر رياضي عالمي
}

def fetch_channels():
    data = {
        "ar_sport": [], "ar_news": [],
        "fr_sport": [], "fr_news": [],
        "en_sport": [], "en_news": [],
        "de_sport": [], "de_news": [],
        "nl_sport": [], "nl_news": []
    }

    for key_lang, url in SOURCES.items():
        try:
            print(f"📡 جاري قنص قنوات {key_lang}...")
            response = requests.get(url, timeout=20)
            if response.status_code == 200:
                content = response.text
                # تقسيم الملف إلى قنوات
                chunks = content.split('#EXTINF')
                for chunk in chunks[1:]:
                    # استخراج الاسم، اللوجو، والرابط
                    name = re.search(r',(.+)', chunk)
                    logo = re.search(r'tvg-logo="([^"]+)"', chunk)
                    url_stream = re.search(r'(http[^\s]+)', chunk)
                    
                    if name and url_stream:
                        ch_name = name.group(1).strip()
                        ch_url = url_stream.group(1).strip()
                        ch_logo = logo.group(1) if logo else ""
                        
                        channel_obj = {"name": ch_name, "logo": ch_logo, "url": ch_url}
                        
                        # تحديد اللغة والنوع (رياضة أم أخبار)
                        # سنستخدم key_lang لتحديد القسم بدقة
                        lang = key_lang if key_lang in data.keys() else "en"
                        
                        # منطق التوزيع الذكي
                        target_lang = "en"
                        for l in ["ar", "fr", "en", "de", "nl"]:
                            if key_lang.startswith(l): target_lang = l

                        if any(x in ch_name.upper() for x in ['SPORT', 'BEIN', 'KASS', 'AD', 'FOOT', 'COPA']):
                            data[f"{target_lang}_sport"].append(channel_obj)
                        else:
                            data[f"{target_lang}_news"].append(channel_obj)
                            
        except Exception as e:
            print(f"❌ خطأ في {key_lang}: {e}")

    # تنظيف البيانات: حذف المكرر واختيار أفضل 30 قناة لكل قسم
    for section in data:
        data[section] = data[section][:30]

    with open('links.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print("✅ تم تحديث جميع الأقسام بما في ذلك AR و NL بنجاح!")

if __name__ == "__main__":
    fetch_channels()