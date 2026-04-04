import json

def generate_channels_js(m3u_file):
    channels = []
    # هنا نقرأ ملف الروابط الخاص بك
    try:
        with open(m3u_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            
        for i in range(len(lines)):
            if lines[i].startswith('#EXTINF'):
                name = lines[i].split(',')[-1].strip()
                url = lines[i+1].strip()
                if '.ts' in url:
                    # نستخدم شعار موحد أو فارغ حالياً
                    channels.append({
                        "name": name, 
                        "url": url,
                        "logo": "https://mytvpro1.github.io/favicon.ico" 
                    })

        # حفظ البيانات في ملف JS ليقرأه الموقع مباشرة
        with open('channels_data.js', 'w', encoding='utf-8') as f:
            f.write("const myChannels = " + json.dumps(channels, ensure_ascii=False) + ";")
        print(f"✅ تم استخراج {len(channels)} قناة بنجاح!")
    except FileNotFoundError:
        print("❌ لم يتم العثور على ملف list.m3u")

generate_channels_js('list.m3u')
