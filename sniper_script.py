import requests
import json
import re

# المصادر الأصلية التي تعبنا عليها (مضمونة 100%)
SOURCES = {
    "de": "https://raw.githubusercontent.com/iptv-org/iptv/master/streams/de.m3u",
    "nl": "https://raw.githubusercontent.com/iptv-org/iptv/master/streams/nl.m3u",
    "nl_ext": "https://raw.githubusercontent.com/iptv-org/iptv/master/streams/nl_ext.m3u",
    "en": "https://raw.githubusercontent.com/iptv-org/iptv/master/streams/us.m3u",
    "fr": "https://raw.githubusercontent.com/iptv-org/iptv/master/streams/fr.m3u",
    "ar_news": "https://raw.githubusercontent.com/teleriumtv/iptv/main/iptv.m3u"
}

# روابط الأعلام الثابتة (لا تتغير ولا تسبب اهتزاز)
FLAGS = {
    "nl": "https://flagcdn.com/w160/nl.png", # علم هولندا
    "fr": "https://flagcdn.com/w160/fr.png", # علم فرنسا
    "de": "https://flagcdn.com/w160/de.png", # علم ألمانيا
    "en": "https://flagcdn.com/w160/us.png", # علم أمريكا (للقنوات الإنجليزية)
    "ar": "https://flagcdn.com/w160/ma.png"  # علم المغرب (للقنوات العربية)
}

def fetch_channels():
    # استعادة الهيكل الأصلي
    data = {
        "ar_sport": [], "ar_news": [],
        "fr_sport": [], "fr_news": [],
        "en_sport": [], "en_news": [],
        "de_sport": [], "de_news": [],
        "nl_sport": [], "nl_news": []
    }

    for key_lang, url in SOURCES.items():
        try:
            print(f"📡 جاري استعادة قنوات {key_lang} مع وضع الأعلام...")
            response = requests.get(url, timeout=15)
            if response.status_code == 200:
                chunks = response.text.split('#EXTINF')
                for chunk in chunks[1:]:
                    # حماية ضد beIN كما طلبت
                    if "BEIN" in chunk.upper(): continue
                    
                    name_match = re.search(r',(.+)', chunk)
                    url_match = re.search(r'(http[^\s]+)', chunk)
                    
                    if name_match and url_match:
                        ch_name = name_match.group(1).strip()
                        ch_url = url_match.group(1).strip()
                        
                        # تحديد كود اللغة (nl, fr, etc.)
                        lang_code = key_lang.split('_')[0]
                        # وضع العلم المناسب بدل اللوجو المكسور
                        ch_logo = FLAGS.get(lang_code, "")
                        
                        channel_obj = {"name": ch_name, "logo": ch_logo, "url": ch_url}
                        
                        # التوزيع الرياضي/الإخباري الأصلي
                        if any(x in ch_name.upper() for x in ['SPORT', 'ESPN', 'ZIGGO', 'FOOT', 'TV']):
                            data[f"{lang_code}_sport"].append(channel_obj)
                        else:
                            data[f"{lang_code}_news"].append(channel_obj)
                            
        except Exception as e:
            print(f"❌ خطأ في {key_lang}: {e}")

    # موازنة الأعداد لضمان السرعة
    for section in data:
        data[section] = data[section][:60]

    with open('links.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print("✅ تم الاسترجاع بنجاح! جميع القنوات عادت بنظام الأعلام المستقر.")

if __name__ == "__main__":
    fetch_channels()
