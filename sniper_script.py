import requests
import json
import os

def get_simo_links():
    # روابط مباشرة لـ Paramount و EuroSport والقنوات الإخبارية فقط
    data = {
        "en_sport": [
            {
                "name": "Paramount+ HD",
                "url": "http://158.69.123.134:80/live/SimoGlobal/12345/10231.m3u8", 
                "logo": "https://upload.wikimedia.org/wikipedia/commons/a/a5/Paramount_Plus.svg"
            },
            {
                "name": "EuroSport 1",
                "url": "http://62.210.139.141:8000/live/eurosport1/playlist.m3u8",
                "logo": "https://upload.wikimedia.org/wikipedia/commons/b/b3/Eurosport_logo.svg"
            }
        ],
        "en_news": [
            {
                "name": "BBC News",
                "url": "https://vs-hls-push-ww-live.akamaized.net/x=4/i=urn:bbc:pips:service:bbc_news_channel_hd/main.m3u8",
                "logo": "https://upload.wikimedia.org/wikipedia/commons/6/62/BBC_News_2022.svg"
            }
        ]
    }
    return data

def update_links_json():
    try:
        channels = get_simo_links()
        with open('links.json', 'w', encoding='utf-8') as f:
            json.dump(channels, f, ensure_ascii=False, indent=4)
        print("✅ Simo Sniper: Links Updated (beIN Removed)!")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    update_links_json()
