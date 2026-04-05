import requests
import json

# رابط البروكسي الخاص بك في Cloudflare
PROXY_PREFIX = "https://broad-cake-463d.mytvpropagesdev.workers.dev/?target="

# ضع هنا الروابط الحقيقية التي تجلب منها القنوات (مثل روابط GitHub الخام)
SOURCES = [
    "https://raw.githubusercontent.com/example/source1.txt",
    "https://raw.githubusercontent.com/example/source2.txt",
    "https://raw.githubusercontent.com/example/source3.txt"
]

def fetch_links():
    channels = []
    for i, source in enumerate(SOURCES, 1):
        try:
            response = requests.get(source, timeout=15)
            if response.status_code == 200:
                original_link = response.text.strip()
                
                if original_link and original_link.startswith("http"):
                    # دمج الرابط الأصلي مع البروكسي لضمان العمل على المتصفح
                    final_link = PROXY_PREFIX + original_link
                    
                    channels.append({
                        "name": f"BEIN SPORTS {i}", # يمكنك تغيير الاسم هنا
                        "url": final_link
                    })
                    print(f"Successfully added source {i}")
        except Exception as e:
            print(f"Error fetching source {i}: {e}")
    return channels

def save_to_js(channels):
    filename = "channel_data.js"
    # تحويل البيانات إلى تنسيق جافا سكريبت
    with open(filename, "w", encoding="utf-8") as f:
        f.write("var live_channels = ")
        json.dump(channels, f, indent=2, ensure_ascii=False)
        f.write(";")
    print(f"Done! Saved {len(channels)} channels with Proxy integration.")

if __name__ == "__main__":
    links = fetch_links()
    # إذا لم يجد السكريبت روابط، سنضع رابط تجريبي (مثل الجزيرة) للتأكد من عمل الموقع
    if not links:
        test_link = "http://s1219.x.smline.xyz:2082/plays/SFpZalQ5U0czZ292ZG1ZdXkvVmpwZ25Ec1htbG4xSkp3Ym1TRDVjMk1MdHo5SUozK2hCL3E1cFRZanYzTXlmeXFpRVhQcDMvMXZKMWQ2WlhHS0VSTUE9PQ==.ts"
        links = [{"name": "AL JAZEERA (AUTO-PROXY)", "url": PROXY_PREFIX + test_link}]
    
    save_to_js(links)
