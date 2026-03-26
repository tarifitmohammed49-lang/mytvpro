import requests
import re

# مصادر روابط beIN Sports - قناص سيمو
SOURCES = [
    "https://raw.githubusercontent.com/MohamedH96/TV/main/Bein.m3u",
    "https://raw.githubusercontent.com/Mocro-Player/Mocro/main/Mocro.m3u"
]

def fetch_links():
    channels_content = "#EXTM3U\n"
    print("🚀 جاري قنص روابط beIN Sports الجديدة...")
    for url in SOURCES:
        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                # البحث عن قنوات beIN بذكاء
                matches = re.findall(r'(#EXTINF.*?,beIN SPORTS.*?\n(http.*?))', response.text, re.IGNORECASE)
                for match in matches:
                    info, link = match
                    channels_content += f"{info}\n{link}\n"
        except:
            continue
    return channels_content

playlist_data = fetch_links()
with open("playlist.m3u", "w", encoding="utf-8") as f:
    f.write(playlist_data)
print("✅ تم تحديث playlist.m3u بنجاح!")
