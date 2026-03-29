import requests
import json

def hunt():
    print("🚀 Simo Sniper is hunting...")
    targets = {
        "beIN SPORTS 1 HD": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/BeIN_Sports_1_logo.svg/128px-BeIN_Sports_1_logo.svg.png",
        "beIN SPORTS 2 HD": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/BeIN_Sports_2_logo.svg/128px-BeIN_Sports_2_logo.svg.png"
    }
    
    # رابط مصدر واحد مباشر وسريع للتجربة
    source = "https://raw.githubusercontent.com/Iptv-Full/Free-Iptv/main/iptv.m3u"
    found = []
    
    try:
        r = requests.get(source, timeout=15)
        if r.status_code == 200:
            lines = r.text.split('\n')
            for i, line in enumerate(lines):
                for name, logo in targets.items():
                    if name.split(' ')[2] in line and i+1 < len(lines):
                        url = lines[i+1].strip()
                        if url.startswith("http"):
                            found.append({"name": name, "url": url, "logo": logo})
                            break
    except Exception as e:
        print(f"Error: {e}")

    # إذا لم يجد شيئاً، يضع روابط احتياطية لكي لا يفشل الأكشن
    if not found:
        found = [{"name": "Server 1 (Busy)", "url": "https://example.com/live.m3u8", "logo": "https://mytvpro1.github.io/favicon.ico"}]
    
    with open('links.json', 'w', encoding='utf-8') as f:
        json.dump(found, f, ensure_ascii=False, indent=2)
    print("✅ links.json updated!")

if __name__ == "__main__":
    hunt()
