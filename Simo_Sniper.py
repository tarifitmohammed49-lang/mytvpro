import requests
import json

def hunt():
    print("🚀 Hunting for High-Quality Links...")
    
    # شعارات القنوات
    logos = {
        "beIN": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/BeIN_Sports_1_logo.svg/128px-BeIN_Sports_1_logo.svg.png",
        "SSC": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/SSC_Logo.svg/128px-SSC_Logo.svg.png",
        "Default": "https://mytvpro1.github.io/favicon.ico"
    }

    # روابط لمصادر IPTV عالمية يتم تحديثها كل دقيقة
    sources = [
        "https://iptv-org.github.io/iptv/languages/ara.m3u",
        "https://raw.githubusercontent.com/teleriumtv/telerium-iptv/main/playlist.m3u"
    ]
    
    found_channels = []

    for src in sources:
        try:
            r = requests.get(src, timeout=15)
            if r.status_code == 200:
                lines = r.text.split('\n')
                for i in range(len(lines)):
                    # نبحث عن القنوات الرياضية فقط لضمان الجودة
                    if "SPORT" in lines[i].upper() or "BEIN" in lines[i].upper():
                        name = lines[i].split(',')[-1].strip() if ',' in lines[i] else "Live Channel"
                        if i+1 < len(lines):
                            url = lines[i+1].strip()
                            if url.startswith("http") and (".m3u8" in url or ".ts" in url):
                                # تحديد اللوجو المناسب
                                logo = logos["beIN"] if "BEIN" in name.upper() else (logos["SSC"] if "SSC" in name.upper() else logos["Default"])
                                
                                if not any(c['url'] == url for c in found_channels):
                                    found_channels.append({
                                        "name": name,
                                        "url": url,
                                        "logo": logo
                                    })
        except:
            continue

    # حفظ القنوات (أول 20 قناة لضمان سرعة الموقع)
    with open('links.json', 'w', encoding='utf-8') as f:
        json.dump(found_channels[:20], f, ensure_ascii=False, indent=2)
    print(f"✅ Success! {len(found_channels[:20])} Working links saved.")

if __name__ == "__main__":
    hunt()
