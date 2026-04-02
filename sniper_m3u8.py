import requests
import json
import re

def fetch_iptv_org():
    """سحب القنوات العربية من iptv-org"""
    url = "https://iptv-org.github.io/iptv/languages/ara.m3u"
    try:
        response = requests.get(url, timeout=15)
        if response.status_code == 200:
            lines = response.text.split('\n')
            channels = []
            for i in range(len(lines)):
                if lines[i].startswith('#EXTINF'):
                    # استخراج الاسم واللوغو باستخدام Regex
                    name_match = re.search('tvg-name="(.*?)"', lines[i])
                    logo_match = re.search('tvg-logo="(.*?)"', lines[i])
                    name = name_match.group(1) if name_match else "Unknown Channel"
                    logo = logo_match.group(1) if logo_match else "https://mytvpro1.github.io/favicon.ico"
                    
                    # الرابط يكون في السطر التالي مباشرة
                    if i + 1 < len(lines):
                        link = lines[i+1].strip()
                        if link.startswith('http'):
                            channels.append({
                                "name": name,
                                "url": link,
                                "logo": logo
                            })
            return channels
    except Exception as e:
        print(f"Error fetching iptv-org: {e}")
    return []

def update_index_html(channels):
    """حقن القنوات في ملف index.html"""
    channels_html = ""
    for ch in channels:
        channels_html += f'''
    <div class="movie-card" onclick="openLivePlayer('{ch['url']}')">
        <img src="{ch['logo']}" alt="{ch['name']}" onerror="this.src='https://mytvpro1.github.io/favicon.ico'" loading="lazy">
        <div class="movie-title">{ch['name']}</div>
    </div>'''

    try:
        with open('index.html', 'r', encoding='utf-8') as f:
            content = f.read()

        start_tag = ""
        end_tag = ""

        if start_tag in content and end_tag in content:
            new_content = content.split(start_tag)[0] + start_tag + channels_html + end_tag + content.split(end_tag)[1]
            with open('index.html', 'w', encoding='utf-8') as f:
                f.write(new_content)
            print("Successfully updated index.html with new channels!")
    except Exception as e:
        print(f"Error updating HTML: {e}")

# التشغيل الرئيسي
if __name__ == "__main__":
    print("Starting Sniper Update...")
    
    # 1. جلب القنوات
    all_channels = fetch_iptv_org()
    
    # 2. حفظها في links.json كنسخة احتياطية
    with open('links.json', 'w', encoding='utf-8') as f:
        json.dump(all_channels, f, ensure_ascii=False, indent=2)
    
    # 3. تحديث الموقع مباشرة
    if all_channels:
        update_index_html(all_channels)
    else:
        print("No channels found to update.")
