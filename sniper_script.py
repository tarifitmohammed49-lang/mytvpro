import requests

# مصادر عالمية مفتوحة وشغالة 100% للتجربة
SOURCES = [
    "https://raw.githubusercontent.com/Free-TV/IPTV/master/playlist.m3u8"
]

def fetch_links():
    channels_content = "#EXTM3U\n"
    print("🚀 جاري صيد القنوات العالمية المفتوحة...")
    try:
        response = requests.get(SOURCES[0], timeout=15)
        if response.status_code == 200:
            # سنأخذ أول 20 قناة فقط للتجربة
            lines = response.text.split('\n')
            channels_content += "\n".join(lines[1:40]) 
    except:
        pass
    return channels_content

with open("playlist.m3u", "w", encoding="utf-8") as f:
    f.write(fetch_links())
