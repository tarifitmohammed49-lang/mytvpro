import json
import os
import re
import base64

def sniper_extractor():
    m3u_file = 'playlist.m3u' 
    output_file = 'channels_data.js'
    channels = []
    
    if not os.path.exists(m3u_file):
        print("M3U file not found!")
        return

    with open(m3u_file, 'r', encoding='utf-8') as f:
        content = f.read()
        
    pattern = re.compile(r'#EXTINF:.*?,(.*?)\n(http.*)', re.MULTILINE)
    matches = pattern.findall(content)
    
    # أهم خطوة: سنأخذ فقط القنوات الرياضية لكي لا يشنج الموقع
    important_keywords = ['bein', 'ssc', 'abu dhabi', 'alkass', 'espn', 'sky', 'dazn', 'canal', 'eurosport', 'rmc']

    for name, url in matches:
        clean_name = name.strip()
        name_lower = clean_name.lower()
        
        if any(key in name_lower for key in important_keywords):
            encoded_url = base64.b64encode(url.strip().encode()).decode()
            channels.append({
                "name": clean_name,
                "url": encoded_url,
                "logo": "https://mytvpro1.github.io/favicon.ico"
            })

    with open(output_file, 'w', encoding='utf-8') as f:
        # كتابة الملف بتنسيق صغير جداً
        f.write("const myChannels = " + json.dumps(channels, ensure_ascii=False) + ";")
    
    print(f"✅ تم استخراج {len(channels)} قناة رياضية فقط. الحجم الآن مثالي!")

if __name__ == "__main__":
    sniper_extractor()
