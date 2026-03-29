import requests
import re
import json

def fetch_tokens_and_links():
    # المصادر التي يبحث فيها السنايبر عن روابط beIN المحدثة
    sources = [
        "https://raw.githubusercontent.com/Iptv-Full/Free-Iptv/main/iptv.m3u",
        "https://raw.githubusercontent.com/moez-bth/my-iptv/main/playlist.m3u",
        "https://raw.githubusercontent.com/iptv-org/iptv/master/streams/ar.m3u"
    ]
    
    channels_list = []
    # القنوات المستهدفة
    targets = {
        "beIN SPORTS 1": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/BeIN_Sports_1_logo.svg/1024px-BeIN_Sports_1_logo.svg.png",
        "beIN SPORTS 2": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/BeIN_Sports_2_logo.svg/1024px-BeIN_Sports_2_logo.svg.png",
        "beIN SPORTS 3": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a2/BeIN_Sports_3_logo.svg/1024px-BeIN_Sports_3_logo.svg.png",
        "beIN SPORTS Premium 1": "https://mytvpro1.github.io/favicon.ico"
    }

    print("--- Simo Sniper Started ---")

    for source in sources:
        try:
            response = requests.get(source, timeout=15)
            if response.status_code == 200:
                content = response.text
                lines = content.split('\n')
                
                for i in range(len(lines)):
                    for name, logo in targets.items():
                        if name.lower() in lines[i].lower() and i+1 < len(lines):
                            link = lines[i+1].strip()
                            if link.startswith("http") and ".m3u8" in link:
                                # حماية من التكرار
                                if not any(c['name'] == name for c in channels_list):
                                    channels_list.append({
                                        "name": name,
                                        "url": link,
                                        "logo": logo
                                    })
                                    print(f"Captured: {name}")
        except Exception as e:
            print(f"Error fetching from {source}: {e}")

    return channels_list

def save_links(data):
    # حفظ الملف بصيغة JSON لكي يقرأه الموقع تلقائياً
    with open('links.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"Done! Saved {len(data)} channels to links.json")

if __name__ == "__main__":
    found_channels = fetch_tokens_and_links()
    if found_channels:
        save_links(found_channels)
    else:
        # إذا لم يجد روابط، يضع رسالة تجريبية لكي لا يظهر الموقع فارغاً
        test_data = [{
            "name": "beIN SPORTS (Offline)",
            "url": "https://example.com/stream.m3u8",
            "logo": "https://mytvpro1.github.io/favicon.ico"
        }]
        save_links(test_data)
