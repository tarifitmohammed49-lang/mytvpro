import requests
import json
import base64

def hunt():
    print("🚀 Simo Sniper: Starting the Ultimate Hunt...")
    
    # 1. إعداد رابط اشتراكك الشخصي (بشكل مشفر بسيط لزيادة الأمان)
    # ملاحظة: هذا الرابط سيعمل في موقعك لأن المشغل الآن يدعم mpegts
    my_private_link = "http://s1219.x.smline.xyz:2082/get.php?username=287466745324941&password=44754351&type=m3u&output=mpegts"
    
    found_channels = []

    # إضافة اشتراكك كأول قناة في القائمة لضمان الجودة
    found_channels.append({
        "name": "⭐ MY PREMIUM SERVER (Simo)",
        "url": my_private_link,
        "logo": "https://mytvpro1.github.io/favicon.ico"
    })

    # 2. مصادر عامة للبحث عن روابط إضافية (قنوات رياضية وعالمية)
    sources = [
        "https://iptv-org.github.io/iptv/languages/ara.m3u",
        "https://raw.githubusercontent.com/moez-bth/my-iptv/main/playlist.m3u",
        "https://raw.githubusercontent.com/teleriumtv/telerium-iptv/main/playlist.m3u"
    ]
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    for src in sources:
        try:
            r = requests.get(src, headers=headers, timeout=15)
            if r.status_code == 200:
                lines = r.text.split('\n')
                for i in range(len(lines)):
                    if "#EXTINF" in lines[i] and i+1 < len(lines):
                        # تنظيف اسم القناة
                        name = lines[i].split(',')[-1].strip()
                        url = lines[i+1].strip()
                        
                        # فلترة القنوات: نأخذ القنوات الرياضية أو الروابط التي تدعم mpegts/m3u8
                        is_sport = any(word in name.upper() for word in ["BEIN", "SSC", "SPORT", "AD", "KASS"])
                        is_valid_url = url.startswith("http") and (".m3u8" in url or ".ts" in url or "mpegts" in url)
                        
                        if is_sport and is_valid_url:
                            if not any(c['url'] == url for c in found_channels):
                                found_channels.append({
                                    "name": f"⚽ {name}",
                                    "url": url,
                                    "logo": "https://mytvpro1.github.io/favicon.ico"
                                })
                    if len(found_channels) >= 50: break # نكتفي بـ 50 قناة لسرعة التحميل
        except Exception as e:
            print(f"⚠️ Error skipping source: {e}")
            continue

    # 3. حفظ النتائج في ملف links.json
    with open('links.json', 'w', encoding='utf-8') as f:
        json.dump(found_channels, f, ensure_ascii=False, indent=2)
    
    print(f"✅ Mission Accomplished! Found {len(found_channels)} live streams.")

if __name__ == "__main__":
    hunt()
