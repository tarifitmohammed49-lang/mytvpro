import json

def update_links():
    links_data = {
        "ar_sport": [{"name": "beIN NEWS", "logo": "https://upload.wikimedia.org/wikipedia/commons/5/5b/BeIN_Sports_News_logo.svg", "url": "https://all-sports.onrender.com/beinn.m3u8"}],
        "ar_news": [],
        "en_sport": [{"name": "RED BULL TV", "logo": "https://via.placeholder.com/60", "url": "https://rbmn-live.akamaized.net/hls/live/590964/relentless/master.m3u8"}],
        "en_news": []
    }
    try:
        with open('links.json', 'w', encoding='utf-8') as f:
            json.dump(links_data, f, ensure_ascii=False, indent=2)
        print("✅ تم تحديث الروابط بنجاح!")
    except Exception as e:
        print(f"❌ خطأ: {e}")

if __name__ == "__main__":
    update_links()