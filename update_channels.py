import json

# رابط الـ Worker الخاص بك
PROXY = "https://misty-silence-e830.mytvpropagesdev.workers.dev/?target="

# القائمة الذهبية التي أرسلتها
RAW_CHANNELS = [
    {"n": "beIN SPORTS 1 AR", "u": "http://s1219.x.smline.xyz:2082/plays/eFRkU3FSM3hhQ0FBWFRkV2NKMERNYjZqVGtoUDVZMW1HODB2M3BQdnFKOHphN2h5VEphL05FbjR4MGFKbGxORTVJbmZsdUU5dFRRVnBvaklGcnJSR3c9PQ==.ts"},
    {"n": "beIN SPORTS 2 AR", "u": "http://s1219.x.smline.xyz:2082/plays/WmY5VVJSUmpidHNNWG5ZME9CT2dPajJrQ0FaZkFmWkdyUUl6dmJ4U2tpRlRDZnpWSHMvL2tPUDcwZzF4eDg5dFNmekNVNnJTaEJSYjUxSVQ4c3M5L1E9PQ==.ts"},
    {"n": "beIN SPORTS 3 AR", "u": "http://s1219.x.smline.xyz:2082/plays/bXh2SnFxQnQyRWdHWndsWDMyV05ycWxyaFJCdDZMUy9Tb1EwczdPVHU4aWpZWldyRkhsY2dHQjNzemVyaTFEZTdsRzBYL2RYeXNFWitCcFVUc04yL0E9PQ==.ts"},
    {"n": "beIN SPORTS 4 AR", "u": "http://s1219.x.smline.xyz:2082/plays/Z1JzYTRmOFphRW4zRXFpT3JxTUpmNGV0b1ZWZHVLYldPZEdWTTViT01wOEU5WVBFNFduU3pOU0xxUmU3dk96UmNCY0R0MHE5LzA4TjhJZDM0QWl4d1E9PQ==.ts"},
    {"n": "beIN SPORTS 5 AR", "u": "http://s1219.x.smline.xyz:2082/plays/VzB3T2tNSjRBTUNyUk5XNTNjK0wySlBxMVdnNkMyQi9FZy85Zi9FV3UyeGRMakFLSFJsb1E3M0JqUk1uT1RnOXNYVVROQkdZc2JBNkgvbDV0MWZiWVE9PQ==.ts"},
    {"n": "beIN SPORTS 6 AR", "u": "http://s1219.x.smline.xyz:2082/plays/VzB3T2tNSjRBTUNyUk5XNTNjK0wySlBxMVdnNkMyQi9FZy85Zi9FV3UyeGRMakFLSFJsb1E3M0JqUk1uT1RnOXNYVVROQkdZc2JBNkgvbDV0MWZiWVE9PQ==.ts"},
    {"n": "beIN SPORTS 7 AR", "u": "http://s1219.x.smline.xyz:2082/plays/VFdIbWdjbzZ3alV5dE9UTE5CMUNtclhHZ09sbS95bjU0YUpScDR0U0x3by8wTmgvbXR0OW5JSGxXUTdZbENnRmN4MlgvanlEek9mRFh3L1hhZHlOOFE9PQ==.ts"},
    {"n": "beIN SPORTS 8 AR", "u": "http://s1219.x.smline.xyz:2082/plays/eTBIZzRKMG1rUmJXeGx2ek9yT1BCNi82VndGVjBTa29WWVg0cUdYSjlUMnRKdTN1bFI3Ykd5NVAya045bW9SUCtMZDJNSnVuZXM1SmVxeDZqbENYTXc9PQ==.ts"},
    {"n": "beIN SPORTS 9 AR", "u": "http://s1219.x.smline.xyz:2082/plays/TEI4KzBpdzZMY2dIT3pFRlYxcnliZE9SWEpLUXNtTnkwanVpOC9nRUM4YXllQW9ORW5jeXk5UWo1cFdsUzlscEpEcWw2N043bXNLMEE3TksrUlkrN3c9PQ==.ts"}
]

def build():
    final_list = []
    for item in RAW_CHANNELS:
        final_list.append({
            "name": item['n'],
            "url": PROXY + item['u'],
            "logo": "https://mytvpro1.github.io/favicon.ico"
        })

    # 1. ملف الـ JS لموقعك (مع اسم متغير مختلف لزيادة التعمية)
    with open("channels_data.js", "w", encoding="utf-8") as f:
        f.write("var _0xSimoData = " + json.dumps(final_list, ensure_ascii=False) + ";")

    # 2. ملف الـ M3U8 (الرابط الواحد)
    with open("playlist.m3u8", "w", encoding="utf-8") as f:
        f.write("#EXTM3U\n")
        for ch in final_list:
            f.write(f'#EXTINF:-1 tvg-logo="{ch["logo"]}", {ch["name"]}\n')
            f.write(f'{ch["url"]}\n')

if __name__ == "__main__":
    build()
    print("🚀 All secured and generated!")
