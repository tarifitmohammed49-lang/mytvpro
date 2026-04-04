import json
import os
import re

def sniper_extractor():
    m3u_file = 'playlist.m3u' 
    output_file = 'channels_data.js'
    channels = []
    
    if not os.path.exists(m3u_file):
        print(f"❌ Error: {m3u_file} not found!")
        return

    print("🚀 Sniping and Sorting channels...")
    
    with open(m3u_file, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # استخراج الاسم والرابط وشعار القناة
    pattern = re.compile(r'#EXTINF:.*?,(.*?)\n(http.*)', re.MULTILINE)
    matches = pattern.findall(content)
    
    for name, url in matches:
        clean_name = name.strip()
        # تحديد الأولوية (Priority) لترتيب القنوات
        priority = 99
        name_lower = clean_name.lower()
        
        if 'bein' in name_lower: priority = 1
        elif 'ssc' in name_lower: priority = 2
        elif 'dazn' in name_lower: priority = 3
        elif 'abu dhabi' in name_lower or 'adsports' in name_lower: priority = 4
        elif 'alkass' in name_lower: priority = 5
        elif 'sport' in name_lower: priority = 6

        channels.append({
            "name": clean_name,
            "url": url.strip(),
            "logo": "https://mytvpro1.github.io/favicon.ico",
            "priority": priority
        })

    # فرز القنوات بناءً على الأولوية ثم الاسم
    channels.sort(key=lambda x: (x['priority'], x['name']))

    # تحويل البيانات إلى تنسيق JS للموقع
    with open(output_file, 'w', encoding='utf-8') as f:
        # نحذف خاصية الأولوية من ملف النهاية ليبقى خفيفاً
        final_data = [{"name": c["name"], "url": c["url"], "logo": c["logo"]} for c in channels]
        f.write("const myChannels = " + json.dumps(final_data, ensure_ascii=False) + ";")
    
    print(f"✅ Success! {len(channels)} channels sorted and added.")

if __name__ == "__main__":
    sniper_extractor()
