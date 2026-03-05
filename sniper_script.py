import json
import requests

def sniper_engine():
    # 1. القنوات الثابتة التي تعمل دائماً (الجزيرة، سكاي، الرياضية)
    channels_data = {
        "ar_news": [
            {
                "name": "الجزيرة مباشر",
                "url": "https://live-hls-web-aje.akamaized.net/hls/live/2036303/aje/index.m3u8",
                "logo": "https://upload.wikimedia.org/wikipedia/commons/f/f2/Aljazeera_eng.svg"
            },
            {
                "name": "سكاي نيوز عربية",
                "url": "https://live.skynewsarabia.com/hls/sna.m3u8",
                "logo": "https://upload.wikimedia.org/wikipedia/commons/b/b8/Sky_News_Arabia_logo.svg"
            }
        ],
        "ar_sport": [
            {
                "name": "الرياضية المغربية",
                "url": "https://snrtlive-hls-ch3-apple-delivery.akamaized.net/adbe018f_1/index.m3u8",
                "logo": "https://www.snrt.ma/sites/default/files/styles/logo_chaine/public/2021-12/arryadia.png"
            }
        ]
    }

    # 2. محاولة قنص قنوات رياضية إضافية (beIN)
    try:
        source = "https://raw.githubusercontent.com/iptv-org/iptv/master/streams/ar.m3u"
        r = requests.get(source, timeout=10)
        if r.status_code == 200:
            lines = r.text.splitlines()
            for i, line in enumerate(lines):
                if "beIN SPORTS" in line and i+1 < len(lines):
                    stream_url = lines[i+1].strip()
                    if stream_url.startswith("http"):
                        channels_data["ar_sport"].append({
                            "name": "beIN Sports (Sniper)",
                            "url": stream_url,
                            "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6b/BeIN_Sports_logo.svg/1024px-BeIN_Sports_logo.svg.png"
                        })
    except:
        pass

    # 3. حفظ كل القنوات في الملف
    with open('links.json', 'w', encoding='utf-8') as f:
        json.dump(channels_data, f, ensure_ascii=False, indent=4)
    print("✅ تم تحديث الروابط بنجاح مع الحفاظ على القنوات الأساسية")

if __name__ == "__main__":
    sniper_engine()