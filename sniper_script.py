import requests

# مصادر قوية جداً وتعمل بنظام التحديث الآلي
SOURCES = [
    "https://raw.githubusercontent.com/MohamedH96/TV/main/Bein.m3u",
    "https://raw.githubusercontent.com/Mocro-Player/Mocro/main/Mocro.m3u"
]

def fetch_links():
    channels_content = "#EXTM3U\n"
    print("🚀 جاري صيد أقوى روابط beIN Sports...")
    for url in SOURCES:
        try:
            response = requests.get(url, timeout=15)
            if response.status_code == 200:
                # سنأخذ القنوات الرياضية فقط لضمان الجودة
                content = response.text
                if "#EXTM3U" in content:
                    # تصفية المحتوى لجلب قنوات beIN فقط
                    lines = content.split('\n')
                    for i in range(len(lines)):
                        if "beIN SPORTS" in lines[i].upper():
                            channels_content += lines[i] + "\n" + lines[i+1] + "\n"
        except:
            continue
    return channels_content

with open("playlist.m3u", "w", encoding="utf-8") as f:
    f.write(fetch_links())
