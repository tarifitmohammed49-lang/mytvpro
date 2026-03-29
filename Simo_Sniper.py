import requests
import json

def hunt():
    print("🚀 Simo Sniper: Hunting for REAL video streams...")
    
    # قائمة مصادر تعطي روابط m3u8 مباشرة 100%
    sources = [
        "https://raw.githubusercontent.com/moez-bth/my-iptv/main/playlist.m3u",
        "https://iptv-org.github.io/iptv/languages/ara.m3u"
    ]
    
    found_channels = []

    for src in sources:
        try:
            # إضافة User-Agent لكي لا يحظرنا السيرفر
            headers = {'User-Agent': 'Mozilla/5.0'}
            r = requests.get(src, headers=headers, timeout=10)
            if r.status_code == 200:
                lines = r.text.split('\n')
                for i in range(len(lines)):
                    if "#EXTINF" in lines[i] and i+1 < len(lines):
                        # استخراج اسم القناة بشكل نظيف
                        name_part = lines[i].split(',')[-1].strip()
                        url = lines[i+1].strip()
                        
                        # القيد الذهبي: يجب أن يكون الرابط آمن ومباشر
                        if url.startswith("https") and (".m3u8" in url):
                            # تصفية القنوات المهمة فقط (beIN, SSC, MBC, etc.)
                            important_keywords = ["BEIN", "SSC", "AD", "MBC", "AL KASS"]
                            if any(key in name_part.upper() for key in important_keywords):
                                if not any(c['url'] == url for c in found_channels):
                                    found_channels.append({
                                        "name": name_part,
                                        "url": url,
                                        "logo": "https://mytvpro1.github.io/favicon.ico"
                                    })
        except:
            continue

    # إذا كانت القائمة فارغة، نضع روابط بث مباشر رسمية دائمة (مثل قنوات إخبارية) للتأكد من المشغل
    if not found_channels:
        found_channels = [
            {"name": "Al Jazeera (Live)", "url": "https://live-hls-web-aje.akamaized.net/hls/live/2036571/aje/index.m3u8", "logo": "https://mytvpro1.github.io/favicon.ico"},
            {"name": "TRT Arabic", "url": "https://tv-trtarabic.medyahizmetleri.com/live/hls/trtarabic.m3u8", "logo": "https://mytvpro1.github.io/favicon.ico"}
        ]

    with open('links.json', 'w', encoding='utf-8') as f:
        json.dump(found_channels, f, ensure_ascii=False, indent=2)
    print(f"✅ Ready! {len(found_channels)} direct streams found.")

if __name__ == "__main__":
    hunt()
