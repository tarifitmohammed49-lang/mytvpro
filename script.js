import requests
import re
import json
import os

def get_live_links():
    # قائمة المصادر (يمكنك إضافة روابط Raw لملفات m3u مشهورة هنا)
    sources = [
        "https://raw.githubusercontent.com/Iptv-Full/Free-Iptv/main/iptv.m3u",
        "https://raw.githubusercontent.com/moez-bth/my-iptv/main/playlist.m3u"
    ]
    
    channels_found = []
    # الكلمات المفتاحية التي نبحث عنها
    target_channels = ["beIN SPORTS 1", "beIN SPORTS 2", "beIN SPORTS 3", "beIN SPORTS 4"]

    for source in sources:
        try:
            response = requests.get(source, timeout=10)
            if response.status_status == 200:
                lines = response.text.split('\n')
                for i in range(len(lines)):
                    for target in target_channels:
                        if target.lower() in lines[i].lower() and i+1 < len(lines):
                            url = lines[i+1].strip()
                            if url.startswith("http"):
                                # إضافة القناة للقائمة
                                channels_found.append({
                                    "name": target + " HD",
                                    "url": url,
                                    "logo": "https://mytvpro1.github.io/favicon.ico"
                                })
                                break
        except:
            continue
            
    # إزالة التكرار
    unique_channels = {v['name']: v for v in channels_found}.values()
    return list(unique_channels)

def save_to_json(data):
    with open('links.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    print("جاري اصطياد القنوات...")
    links = get_live_links()
    save_to_json(links)
    print(f"تم العثور على {len(links)} قنوات وحفظها في links.json")
