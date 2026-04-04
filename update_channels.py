import json
import os
import re

def sniper_extractor():
    # تأكد أن هذا الاسم يطابق ملفك المرفوع بالضبط
    m3u_file = 'playlist.m3u' 
    output_file = 'channels_data.js'
    channels = []
    
    if not os.path.exists(m3u_file):
        print(f"❌ Error: {m3u_file} not found!")
        return

    print(f"🚀 Sniping from {m3u_file}...")
    
    with open(m3u_file, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # نظام استخراج ذكي يتوافق مع الروابط الطويلة و ==.ts
    pattern = re.compile(r'#EXTINF:.*?,(.*?)\n(http.*)', re.MULTILINE)
    matches = pattern.findall(content)
    
    for name, url in matches:
        channels.append({
            "name": name.strip(),
            "url": url.strip(),
            "logo": "https://mytvpro1.github.io/favicon.ico"
        })

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("const myChannels = " + json.dumps(channels, ensure_ascii=False) + ";")
    
    print(f"✅ Success! {len(channels)} channels added.")

if __name__ == "__main__":
    sniper_extractor()
