import requests
import json
import os

# إعدادات لضمان عدم حظر السنايبر أثناء البحث
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

def hunt_for_links():
    print("🚀 Simo Sniper Started Hunting...")
    
    # مصادر موثوقة للروابط المحدثة (M3U Raw)
    sources = [
        "https://raw.githubusercontent.com/Iptv-Full/Free-Iptv/main/iptv.m3u",
        "https://raw.githubusercontent.com/iptv-org/iptv/master/streams/ar.m3u"
    ]
    
    # القنوات المستهدفة وشعاراتها
    targets = {
        "beIN SPORTS 1 HD": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/BeIN_Sports_1_logo.svg/128px-BeIN_Sports_1_logo.svg.png",
        "beIN SPORTS 2 HD": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/BeIN_Sports_2_logo.svg/128px-BeIN_Sports_2_logo.svg.png",
        "SSC NEWS HD": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/SSC_Logo.svg/128px-SSC_Logo.svg.png"
    }
    
    found_channels = []

    for source in sources:
        try:
            print(f"📡 Checking source: {source}")
            response = requests.get(source, headers=HEADERS, timeout=15)
            if response.status_code == 200:
                lines = response.text.split('\n')
                
                for i in range(len(lines)):
                    # البحث عن اسم القناة في السطر
                    line_upper = lines[i].upper()
                    
                    for channel_name, logo_url in targets.items():
                        # التحقق من تطابق الاسم وتوفر سطر للرابط بعده
                        if channel_name.upper().split(' HD')[0] in line_upper and i + 1 < len(lines):
                            link = lines[i+1].strip()
                            
                            # التأكد من أن الرابط صالح (يبدأ بـ http وفيه .m3u8)
                            if link.startswith("http") and ".m3u8" in link:
                                # حماية من تكرار القناة
                                if not any(c['name'] == channel_name for c in found_channels):
                                    found_channels.append({
                                        "name": channel_name,
                                        "url": link,
                                        "logo": logo_url
                                    })
                                    print(f"✅ Captured: {channel_name}")
                                    break
        except Exception as e:
            print(f"⚠️ Error fetching {source}: {e}")

    return found_channels

def save_to_json(data):
    # حفظ الملف بصيغة JSON لكي يقرأه الموقع فوراً
    print(f"💾 Saving {len(data)} channels to links.json...")
    with open('links.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print("✨ Links.json updated successfully!")

if __name__ == "__main__":
    links = hunt_for_links()
    
    if links:
        save_to_json(links)
    else:
        print("❌ No links found. Using temporary data to avoid empty site.")
        # بيانات مؤقتة لكي لا يظهر الموقع فارغاً إذا فشل البحث
        backup_data = [{
            "name": "beIN SPORTS (Offline)",
            "url": "https://example.com/stream.m3u8",
            "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/30/BeIN_Sports_logo.svg/128px-BeIN_Sports_logo.svg.png"
        }]
        save_to_json(backup_data)
