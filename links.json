import json

def get_simo_international_list():
    return {
        "en_sport": [
            {"name": "Sky Sports News", "url": "https://skysports.com/live.m3u8", "logo": "https://flagcdn.com/w160/gb.png"},
            {"name": "Eurosport 1 UK", "url": "https://index.iptv.ovh/eurosport1.m3u8", "logo": "https://flagcdn.com/w160/gb.png"},
            {"name": "Paramount+ Sport", "url": "https://pplus-ch-us.akamaized.net/hls/live/2097312/primary/index.m3u8", "logo": "https://flagcdn.com/w160/us.png"},
            {"name": "ABC News News", "url": "https://content.uplynk.com/channel/3324f2467c414329b3b0cc5cd98d7712.m3u8", "logo": "https://flagcdn.com/w160/us.png"}
        ],
        "fr_sport": [
            {"name": "France 24 FR", "url": "https://static.france24.com/live/f24_fr.m3u8", "logo": "https://flagcdn.com/w160/fr.png"},
            {"name": "20 Minutes TV", "url": "https://live-20minutestv.digiteka.com/1961167769/index.m3u8", "logo": "https://flagcdn.com/w160/fr.png"},
            {"name": "Africa 24 Sport", "url": "https://africa24.vedge.infomaniak.com/livecast/ik:africa24sport/manifest.m3u8", "logo": "https://flagcdn.com/w160/fr.png"}
        ],
        "de_sport": [
            {"name": "DW Deutsch", "url": "https://dw-amd-live.akamaized.net/hls/live/2014190/dwstreamae/index.m3u8", "logo": "https://flagcdn.com/w160/de.png"},
            {"name": "Welt TV Live", "url": "https://welt-live.akamaized.net/hls/live/2012345/welt/index.m3u8", "logo": "https://flagcdn.com/w160/de.png"}
        ],
        "nl_sport": [
            {"name": "NOS Sport", "url": "https://nos-live.akamaized.net/hls/live/201234/nos/index.m3u8", "logo": "https://flagcdn.com/w160/nl.png"}
        ]
    }

def main():
    data = get_simo_international_list()
    with open('links.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print("✅ تم استعادة القنوات الدولية الأصلية بنجاح!")

if __name__ == "__main__":
    main()
