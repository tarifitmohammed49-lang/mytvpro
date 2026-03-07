import json

def get_international_database():
    return {
        "en_sport": [
            {"name": "Sky Sports News", "url": "https://skysports.com/live.m3u8", "logo": "https://flagcdn.com/w160/gb.png"},
            {"name": "ABC News USA", "url": "https://content.uplynk.com/channel/3324f2467c414329b3b0cc5cd98d7712.m3u8", "logo": "https://flagcdn.com/w160/us.png"}
        ],
        "fr_sport": [
            {"name": "France 24 FR", "url": "https://static.france24.com/live/f24_fr.m3u8", "logo": "https://flagcdn.com/w160/fr.png"},
            {"name": "20 Minutes TV", "url": "https://live-20minutestv.digiteka.com/1961167769/index.m3u8", "logo": "https://flagcdn.com/w160/fr.png"}
        ],
        "de_sport": [
            {"name": "DW Deutsch", "url": "https://dw-amd-live.akamaized.net/hls/live/2014190/dwstreamae/index.m3u8", "logo": "https://flagcdn.com/w160/de.png"},
            {"name": "Welt TV News", "url": "https://welt-live.akamaized.net/hls/live/2012345/welt/index.m3u8", "logo": "https://flagcdn.com/w160/de.png"}
        ],
        "nl_sport": [
            {"name": "NOS Sport NL", "url": "https://nos-live.akamaized.net/hls/live/201234/nos/index.m3u8", "logo": "https://flagcdn.com/w160/nl.png"}
        ]
    }

def main():
    data = get_international_database()
    with open('links.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print("✅ Done! International list updated.")

if __name__ == "__main__":
    main()
