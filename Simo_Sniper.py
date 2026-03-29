import requests, json, base64

def hunt():
    print("🚀 Simo Sniper: Safe Mode Activated...")
    
    # 1. رابط اشتراكك (تم وضعه هنا مباشرة)
    # سنضيف له 'User-Agent' وهمي في ملف الـ JSON لكي يقرأه المشغل في المتصفح
    my_premium_url = "http://s1219.x.smline.xyz:2082/get.php?username=287466745324941&password=44754351&type=m3u&output=mpegts"
    
    found_channels = []

    # إضافة اشتراكك الشخصي مع "هوية مزيفة" (User-Agent) لإيهام السيرفر أنه تطبيق VLC أو Smart TV
    found_channels.append({
        "name": "⭐ MY PREMIUM SERVER (Simo)",
        "url": my_premium_url,
        "logo": "https://mytvpro1.github.io/favicon.ico",
        "headers": {
            "User-Agent": "VLC/3.0.18 LibVLC/3.0.18" 
        }
    })

    # 2. جلب القنوات العامة كتمويه
    sources = ["https://iptv-org.github.io/iptv/languages/ara.m3u"]
    
    # هوية مزيفة لعملية البحث (Scraping)
    fake_headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
    }

    for src in sources:
        try:
            r = requests.get(src, headers=fake_headers, timeout=15)
            if r.status_code == 200:
                lines = r.text.split('\n')
                for i in range(len(lines)):
                    if "#EXTINF" in lines[i] and i+1 < len(lines):
                        name = lines[i].split(',')[-1].strip()
                        url = lines[i+1].strip()
                        
                        # تمويه القائمة بقنوات إخبارية ورياضية
                        if any(w in name.upper() for w in ["AL GHAD", "AL JAZEERA", "BEIN", "SSC", "SPORT"]):
                            found_channels.append({
                                "name": name,
                                "url": url,
                                "logo": "https://mytvpro1.github.io/favicon.ico"
                            })
                    if len(found_channels) >= 60: break
        except: continue

    # حفظ الملف بصيغة JSON
    with open('links.json', 'w', encoding='utf-8') as f:
        json.dump(found_channels, f, ensure_ascii=False, indent=2)
    
    print(f"✅ Mission Accomplished Safely! {len(found_channels)} channels.")

if __name__ == "__main__":
    hunt()
