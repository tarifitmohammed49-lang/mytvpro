import requests
import json

# ضع هنا روابط المصادر الحقيقية التي تجلب منها التوكينات أو الروابط
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
                link = response.text.strip()
                if link and link.startswith("http"):
                    channels.append({
                        "name": f"DAZN DE {i+7}",
                        "url": link
                    })
        except Exception as e:
            print(f"Error fetching source {i}: {e}")
    return channels

def save_to_js(channels):
    # تحويل البيانات إلى تنسيق جافا سكريبت لكي يقرأها الموقع
    filename = "channel_data.js"
    with open(filename, "w", encoding="utf-8") as f:
        f.write("var live_channels = ")
        json.dump(channels, f, indent=2, ensure_ascii=False)
        f.write(";")
    print(f"Done! Saved {len(channels)} channels.")

if __name__ == "__main__":
    links = fetch_links()
    save_to_js(links)
