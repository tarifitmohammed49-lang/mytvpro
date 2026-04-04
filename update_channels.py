import json
import os
import re
import base64

def sniper_extractor():
    m3u_file = 'playlist.m3u' 
    output_file = 'channels_data.js'
    channels = []
    
    if not os.path.exists(m3u_file):
        return

    with open(m3u_file, 'r', encoding='utf-8') as f:
        content = f.read()
        
    pattern = re.compile(r'#EXTINF:.*?,(.*?)\n(http.*)', re.MULTILINE)
    matches = pattern.findall(content)
    
    # قائمة الكلمات المفتاحية للقنوات التي تريدها فقط (لتقليل الحجم)
    important_keywords = ['bein', 'ssc', 'abu dhabi', 'alkass', 'espn', 'sky', 'dazn', 'canal', 'rfi', 'snrt']

    for name, url in matches:
        clean_name = name.strip()
        name_lower = clean_name.lower()
        
        # لن يأخذ إلا القنوات التي تحتوي على الكلمات المهمة
        if any(key in name_lower for key in important_keywords):
            encoded_url = base64.b64encode(url.strip().encode()).decode()
            
            # تحديد الأولوية (beIN أولاً)
            priority = 99
            if 'bein' in name_lower: priority = 1
            elif 'ssc' in name_lower: priority = 2

            channels.append({
                "name": clean_name,
                "url": encoded_url,
                "logo": "https://mytvpro1.github.io/favicon.ico",
                "priority": priority
            })

    # ترتيب القنوات حسب الأولوية
    channels.sort(key=lambda x: (x['priority'], x['name']))

    # حفظ الملف - لن يتجاوز حجمه الآن بضعة كيلوبايتات بدلاً من ميجابايتات
    with open(output_file, 'w', encoding='utf-8') as f:
        final_data = [{"name": c["name"], "url": c["url"], "logo": c["logo"]} for c in channels]
        f.write("const myChannels = " + json.dumps(final_data, ensure_ascii=False) + ";")
    
    print(f"✅ تم استخراج {len(channels)} قناة بنجاح (تم حذف القنوات غير الضرورية).")

if __name__ == "__main__":
    sniper_extractor()
