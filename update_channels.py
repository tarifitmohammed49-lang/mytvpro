import requests
import json
import os

# قائمة الروابط التي تريد جلبها (ضع هنا روابط البحث أو الملفات التي تحتوي التوكينات)
SOURCES = [
    "https://raw.githubusercontent.com/example/dazn1_token.txt",
    "https://raw.githubusercontent.com/example/dazn2_token.txt",
    "https://raw.githubusercontent.com/example/dazn3_token.txt"
]

def fetch_links():
    channels = []
    # هنا نقوم بتسمية القنوات وتحديد الروابط
    # سأضع لك مثالاً لثلاث قنوات DAZN
    for i, source in enumerate(SOURCES, 1):
        try:
            # محاولة جلب الرابط المباشر من المصدر
            response = requests.get(source, timeout=10)
            if response.status_code == 200:
                link = response.text.strip()
                if link:
                    channels.append({
                        "name": f"DAZN DE {i+7}", # سيبدأ من DAZN 8 و 9 و 10
                        "url": link
                    })
        except Exception as e:
            print(f"Error fetching source {i}: {e}")
    
    return channels

def save_to_js(channels):
    # هذا هو الجزء الأهم الذي كان ينقصك يا سيمو
    # نقوم بكتابة المتغير البرمجي قبل البيانات
    filename = "channel_data.js"
    
    with open(filename, "w", encoding="utf-8") as f:
        f.write("var live_channels = ")
        json.dump(channels, f, indent=2, ensure_ascii=False)
        f.write(";")
    
    print(f"Successfully saved {len(channels)} channels to {filename}")

if __name__ == "__main__":
    print("Starting Sniper Update...")
    live_data = fetch_links()
    
    if live_data:
        save_to_js(live_data)
    else:
        # في حال فشل السحب، نضع مصفوفة فارغة لكي لا يتوقف الموقع
        save_to_js([])
        print("No links found, saved empty list.")
