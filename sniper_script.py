import requests
import re

# مصادر "الكنز" لروابط beIN Sports المحدثة تلقائياً
SOURCES = [
    "https://raw.githubusercontent.com/MohamedH96/TV/main/Bein.m3u",
    "https://raw.githubusercontent.com/Mocro-Player/Mocro/main/Mocro.m3u",
    "https://raw.githubusercontent.com/Stay-S/IPTV/main/free.m3u"
]

def fetch_links():
    channels_content = "#EXTM3U\n"
    print("🚀 جاري قنص روابط beIN Sports الجديدة لـ MYTVPRO...")
    
    for url in SOURCES:
        try:
            response = requests.get(url, timeout=15)
            if response.status_code == 200:
                # البحث عن قنوات beIN Sports تحديداً
                lines = response.text.split('\n')
                for i in range(len(lines)):
                    if "BEIN" in lines[i].upper() and "SPORTS" in lines[i].upper():
                        # إضافة سطر المعلومات وسطر الرابط الذي يليه
                        if i + 1 < len(lines):
                            channels_content += lines[i] + "\n" + lines[i+1] + "\n"
        except Exception as e:
            print(f"⚠️ خطأ في المصدر {url}: {e}")
            continue
            
    return channels_content

# تنفيذ القنص وحفظ النتائج في ملف playlist.m3u
final_playlist = fetch_links()
with open("playlist.m3u", "w", encoding="utf-8") as f:
    f.write(final_playlist)

print("✅ تم بنجاح تحديث قائمة القنوات!")
