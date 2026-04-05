import requests
import json

# 1. رابط الـ Worker الجديد (الدرع الخاص بك)
PROXY_PREFIX = "https://misty-silence-e830.mytvpropagesdev.workers.dev/?target="

# 2. ضع هنا الروابط الـ 1000 أو المصادر التي تجلب منها
SOURCES = [
    "https://raw.githubusercontent.com/example/source1.txt",
    # أضف هنا كل المصادر التي تملكها...
]

def fetch_links():
    channels = []
    # ملاحظة: إذا كان لديك قائمة روابط جاهزة بمتغير، ضعها هنا مباشرة
    for i, source in enumerate(SOURCES, 1):
        try:
            response = requests.get(source, timeout=15)
            if response.status_code == 200:
                original_link = response.text.strip()
                
                if original_link and (original_link.startswith("http") or original_link.startswith("https")):
                    # تغليف الرابط بالبروكسي لحماية سيرفر البائع وإخفاء الـ IP
                    final_link = PROXY_PREFIX + original_link
                    
                    channels.append({
                        "name": f"BEIN SPORTS {i}",
                        "url": final_link,
                        "logo": "https://mytvpro1.github.io/favicon.ico" # يمكنك وضع رابط شعار موحد أو خاص
                    })
                    print(f"✅ تم إضافة القناة {i}")
        except Exception as e:
            print(f"❌ خطأ في المصدر {i}: {e}")
            
    return channels

def save_all_data(channels):
    # حفظ الملف الأول: channels_data.js (للموقع)
    with open("channels_data.js", "w", encoding="utf-8") as f:
        f.write("var channels = ") # تأكد أن اسم المتغير 'channels' يطابق ما في الموقع
        json.dump(channels, f, indent=2, ensure_ascii=False)
        f.write(";")
    
    # حفظ الملف الثاني: playlist.m3u8 (الرابط الواحد للـ 1000 قناة)
    with open("playlist.m3u8", "w", encoding="utf-8") as f:
        f.write("#EXTM3U\n")
        for ch in channels:
            f.write(f'#EXTINF:-1 tvg-logo="{ch["logo"]}", {ch["name"]}\n')
            f.write(f'{ch["url"]}\n')
            
    print(f"🚀 اكتمل العمل! تم حفظ {len(channels)} قناة في JS و M3U8.")

if __name__ == "__main__":
    links = fetch_links()
    
    # إذا لم يجد روابط (للتجربة فقط)
    if not links:
        test_url = "http://s1219.x.smline.xyz:2082/plays/SFpZalQ5U0czZ292ZG1ZdXkvVmpwZ25Ec1htbG4xSkp3Ym1TRDVjMk1MdHo5SUozK2hCL3E1cFRZanYzTXlmeXFpRVhQcDMvMXZKMWQ2WlhHS0VSTUE9PQ==.ts"
        links = [{
            "name": "AL JAZEERA (PROTECTED)", 
            "url": PROXY_PREFIX + test_url,
            "logo": "https://mytvpro1.github.io/favicon.ico"
        }]
    
    save_all_data(links)
