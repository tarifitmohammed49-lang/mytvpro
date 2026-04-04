import json
import os
import re
import requests

def sniper_extractor():
    m3u_file = 'playlist.m3u' 
    output_file = 'channels_data.js'
    channels = []
    
    # هذه الرؤوس (Headers) تجعل البائع يظن أن المشاهد يستخدم تطبيقاً رسمياً
    fake_headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 10; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Mobile Safari/537.36',
        'Referer': 'https://google.com', # نوهم البائع أن المصدر هو جوجل وليس موقعك
        'Origin': 'https://google.com'
    }

    if not os.path.exists(m3u_file):
        print(f"❌ Error: {m3u_file} not found!")
        return

    print("🚀 Sniping with Ghost Mode...")
    
    with open(m3u_file, 'r', encoding='utf-8') as f:
        content = f.read()
        
    pattern = re.compile(r'#EXTINF:.*?,(.*?)\n(http.*)', re.MULTILINE)
    matches = pattern.findall(content)
    
    for name, url in matches:
        clean_name = name.strip()
        priority = 99
        name_lower = clean_name.lower()
        
        # ترتيب القنوات
        if 'bein' in name_lower: priority = 1
        elif 'ssc' in name_lower: priority = 2
        elif 'dazn' in name_lower: priority = 3
        elif 'sport' in name_lower: priority = 6

        channels.append({
            "name": clean_name,
            "url": url.strip(),
            "logo": "https://mytvpro1.github.io/favicon.ico",
            "priority": priority
        })

    channels.sort(key=lambda x: (x['priority'], x['name']))

    with open(output_file, 'w', encoding='utf-8') as f:
        final_data = [{"name": c["name"], "url": c["url"], "logo": c["logo"]} for c in channels]
        f.write("const myChannels = " + json.dumps(final_data, ensure_ascii=False) + ";")
    
    print(f"✅ Ghost Update Success! {len(channels)} channels added.")

if __name__ == "__main__":
    sniper_extractor()
