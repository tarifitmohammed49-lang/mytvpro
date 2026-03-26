import requests

# مصادر قوية ومباشرة
SOURCES = [
    "https://iptv-org.github.io/iptv/countries/mo.m3u", # قنوات المغرب
    "https://raw.githubusercontent.com/Stay-S/IPTV/main/free.m3u" # قنوات رياضية متنوعة
]

def fetch_links():
    channels_content = "#EXTM3U\n"
    print("🚀 جاري محاولة صيد قنوات جديدة...")
    for url in SOURCES:
        try:
            response = requests.get(url, timeout=15)
            if response.status_code == 200:
                lines = response.text.split('\n')
                for i in range(len(lines)):
                    if "beIN" in lines[i] or "Sports" in lines[i]:
                        channels_content += lines[i] + "\n" + lines[i+1] + "\n"
        except:
            continue
    return channels_content

# حفظ النتائج
with open("playlist.m3u", "w", encoding="utf-8") as f:
    f.write(fetch_links())
