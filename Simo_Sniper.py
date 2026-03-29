import requests, json

def hunt():
    print("🚀 Simo Sniper: Extracting BeIN Sports from your subscription...")
    
    # رابط اشتراكك الشخصي (الملف الكامل)
    m3u_url = "http://s1219.x.smline.xyz:2082/get.php?username=287466745324941&password=44754351&type=m3u&output=mpegts"
    
    found_channels = []
    fake_headers = {"User-Agent": "VLC/3.0.18 LibVLC/3.0.18"}

    try:
        # جلب محتوى الاشتراك
        response = requests.get(m3u_url, headers=fake_headers, timeout=20)
        if response.status_code == 200:
            lines = response.text.split('\n')
            for i in range(len(lines)):
                # البحث عن كلمة BEIN في أسماء القنوات داخل ملفك
                if "#EXTINF" in lines[i] and "BEIN" in lines[i].upper():
                    name = lines[i].split(',')[-1].strip()
                    # التأكد من وجود رابط تحت الاسم
                    if i + 1 < len(lines) and lines[i+1].startswith('http'):
                        url = lines[i+1].strip()
                        found_channels.append({
                            "name": f"⭐ {name}",
                            "url": url,
                            "logo": "https://mytvpro1.github.io/favicon.ico",
                            "headers": fake_headers # حماية إضافية لكل قناة
                        })
            print(f"✅ Found {len(found_channels)} BeIN channels in your account.")
    except Exception as e:
        print(f"❌ Error accessing your subscription: {e}")

    # إضافة قنوات تمويه (إخبارية) في نهاية القائمة
    sources = ["https://iptv-org.github.io/iptv/languages/ara.m3u"]
    try:
        r = requests.get(sources[0], timeout=10)
        if r.status_code == 200:
            extra_lines = r.text.split('\n')
            for j in range(len(extra_lines)):
                if "#EXTINF" in extra_lines[j] and any(w in extra_lines[j].upper() for w in ["AL GHAD", "AL JAZEERA"]):
                    name = extra_lines[j].split(',')[-1].strip()
                    if j + 1 < len(extra_lines) and extra_lines[j+1].startswith('http'):
                        found_channels.append({
                            "name": name,
                            "url": extra_lines[j+1].strip(),
                            "logo": "https://mytvpro1.github.io/favicon.ico"
                        })
                if len(found_channels) >= 80: break
    except: pass

    # حفظ النتيجة النهائية
    with open('links.json', 'w', encoding='utf-8') as f:
        json.dump(found_channels, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    hunt()
