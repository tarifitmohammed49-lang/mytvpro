import requests

# مصادر قوية تعطي روابط مباشرة لـ beIN وقنوات أخرى
SOURCES = [
    "https://raw.githubusercontent.com/MohamedH96/TV/main/Bein.m3u",
    "https://raw.githubusercontent.com/Stay-S/IPTV/main/free.m3u"
]

def fetch_links():
    content = "#EXTM3U\n"
    print("🚀 جاري صيد الروابط لـ MYTVPRO...")
    for url in SOURCES:
        try:
            r = requests.get(url, timeout=15)
            if r.status_code == 200:
                # نأخذ القنوات التي تحتوي على كلمة Sports أو beIN
                lines = r.text.split('\n')
                for i in range(len(lines)):
                    if "beIN" in lines[i] or "Sports" in lines[i]:
                        if i + 1 < len(lines):
                            content += lines[i] + "\n" + lines[i+1] + "\n"
        except:
            continue
    return content

# حفظ الملف النهائي
with open("playlist.m3u", "w", encoding="utf-8") as f:
    f.write(fetch_links())
