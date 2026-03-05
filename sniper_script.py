import requests
import json
import re

# مصادر محدثة لضمان NL Sport و AR News
SOURCES = {
    "de": "https://raw.githubusercontent.com/iptv-org/iptv/master/streams/de.m3u",
    "nl": "https://raw.githubusercontent.com/iptv-org/iptv/master/streams/nl.m3u",
    "nl_extra": "https://raw.githubusercontent.com/iptv-org/iptv/master/streams/nl_ext.m3u", # مصدر إضافي لهولندا
    "en": "https://raw.githubusercontent.com/iptv-org/iptv/master/streams/us.m3u",
    "fr": "https://raw.githubusercontent.com/iptv-org/iptv/master/streams/fr.m3u",
    "ar_news": "https://raw.githubusercontent.com/teleriumtv/iptv/main/iptv.m3u"
}

# روابط عربية "خفيفة" جداً للتشغيل السريع
FAST_AR = [
    {"name": "الجزيرة مباشر (سريع)", "logo": "https://upload.wikimedia.org/wikipedia/commons/0/00/Al_Jazeera_Mubasher_logo.png", "url": "https://live-hls-web-ajm.getaj.net/ajm/index.m3u8"},
    {"name": "فرانس 24 عربي", "logo": "https://upload.wikimedia.org/wikipedia/commons/8/82/France_24_logo.svg", "url": "https://static.france24.com/live/F24_AR_HI_HLS/live_hi.m3u8"}
]

def fetch_channels():
    data = {
        "ar_sport": [], "ar_news": FAST_AR,
        "fr_sport": [], "fr_news": [],
        "en_sport": [], "en_news": [],
        "de_sport": [], "de_news": [],
        "nl_sport": [], "nl_news": []
    }

    for key_lang, url in SOURCES.items():
        try:
            print(f"📡 جلب {key_lang}...")
            response = requests.get(url, timeout=15)
            if response.status_code == 200:
                chunks = response.text.split('#EXTINF')
                for chunk in chunks[1:]:
                    name = re.search(r',(.+)', chunk)
                    url_stream = re.search(r'(http[^\s]+)', chunk)
                    if name and url_stream:
                        ch_name = name.group(1).strip()
                        ch_url = url_stream.group(1).strip()
                        # توزيع ذكي
                        target = key_lang.split('_')[0]
                        if any(x in ch_name.upper() for x in ['SPORT', 'ZIGGO', 'ESPN', 'FOOT']):
                            data[f"{target}_sport"].append({"name": ch_name, "url": ch_url, "logo": ""})
                        else:
                            data[f"{target}_news"].append({"name": ch_name, "url": ch_url, "logo": ""})
        except: pass

    for s in data: data[s] = data[s][:50]
    with open('links.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print("✅ تحديث القناص اكتمل!")

if __name__ == "__main__": fetch_channels()