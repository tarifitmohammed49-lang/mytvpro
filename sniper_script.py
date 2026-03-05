import requests
import json
import re

# استعادة كافة المصادر العالمية لضمان عدم مسح أي قناة كانت تعمل
SOURCES = {
    "de": "https://raw.githubusercontent.com/iptv-org/iptv/master/streams/de.m3u",
    "nl": "https://raw.githubusercontent.com/iptv-org/iptv/master/streams/nl.m3u",
    "en": "https://raw.githubusercontent.com/iptv-org/iptv/master/streams/us.m3u",
    "fr": "https://raw.githubusercontent.com/iptv-org/iptv/master/streams/fr.m3u",
    "ar_news": "https://raw.githubusercontent.com/teleriumtv/iptv/main/iptv.m3u"
}

# روابط إخبارية عربية إضافية "مباشرة" لضمان الامتلاء
EXTRA_AR = [
    {"name": "الجزيرة مباشر", "logo": "https://upload.wikimedia.org/wikipedia/commons/0/00/Al_Jazeera_Mubasher_logo.png", "url": "https://live-hls-web-ajm.getaj.net/ajm/index.m3u8"},
    {"name": "سكاي نيوز", "logo": "https://upload.wikimedia.org/wikipedia/ar/b/bb/Sky_News_Arabia_logo.svg", "url": "https://snatv.akamaized.net/hls/live/2034871/snatv/snatv_main_1.m3u8"},
    {"name": "العربية", "logo": "https://upload.wikimedia.org/wikipedia/commons/4/4c/Al_Arabiya_Logo.svg", "url": "https://vcl-v-m-u.alarabiya.net/alarabiya/alarabiya.smil/playlist.m3u8"}
]

def fetch_channels():
    data = {
        "ar_sport": [], "ar_news": EXTRA_AR.copy(),
        "fr_sport": [], "fr_news": [],
        "en_sport": [], "en_news": [],
        "de_sport": [], "de_news": [],
        "nl_sport": [], "nl_news": []
    }

    for key_lang, url in SOURCES.items():
        try:
            print(f"📡 جاري جلب قنوات {key_lang}...")
            response = requests.get(url, timeout=15)
            if response.status_code == 200:
                chunks = response.text.split('#EXTINF')
                for chunk in chunks[1:]:
                    name = re.search(r',(.+)', chunk)
                    logo = re.search(r'tvg-logo="([^"]+)"', chunk)
                    url_stream = re.search(r'(http[^\s]+)', chunk)
                    
                    if name and url_stream:
                        ch_name = name.group(1).strip()
                        ch_url = url_stream.group(1).strip()
                        ch_logo = logo.group(1) if logo else ""
                        channel_obj = {"name": ch_name, "logo": ch_logo, "url": ch_url}
                        
                        # توزيع اللغات (نظام الحماية لعدم مسح القنوات)
                        if key_lang in ["de", "nl", "en", "fr"]:
                            target = key_lang
                            if any(x in ch_name.upper() for x in ['SPORT', 'FOOT']):
                                data[f"{target}_sport"].append(channel_obj)
                            else:
                                data[f"{target}_news"].append(channel_obj)
                        elif key_lang == "ar_news":
                            # تصفية الأخبار العربية فقط
                            if not any(x in ch_name.upper() for x in ['SPORT', 'BEIN']):
                                data["ar_news"].append(channel_obj)
                            
        except Exception as e:
            print(f"❌ خطأ في {key_lang}: {e}")

    # تحديد العدد للحفاظ على السرعة
    for section in data:
        data[section] = data[section][:50]

    with open('links.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print("✅ تم التحديث بنجاح! جميع القنوات الأوروبية محفوظة وقسم الأخبار العربية ممتلئ.")

if __name__ == "__main__":
    fetch_channels()