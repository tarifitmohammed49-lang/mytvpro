import requests
import json
import re
import os

# دالة لجلب الروابط المحدثة (beIN Tokens) من مصادر GitHub نشطة
def fetch_bein_tokens():
    print("Searching for fresh beIN Tokens...")
    # هذه روابط لمصادر مشهورة بتحديث التوكنات يومياً على GitHub
    sources = [
        "https://raw.githubusercontent.com/arab-iptv/arab-iptv/master/bein.m3u",
        "https://raw.githubusercontent.com/mohamed-be/iptv/main/bein_sports.m3u"
    ]
    
    bein_channels = []
    for url in sources:
        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                lines = response.text.split('\n')
                for i in range(len(lines)):
                    if '#EXTINF' in lines[i] and 'beIN' in lines[i]:
                        name = lines[i].split(',')[-1].strip()
                        # البحث عن شعار القناة إذا وجد
                        logo_match = re.search('tvg-logo="(.*?)"', lines[i])
                        logo = logo_match.group(1) if logo_match else "https://mytvpro1.github.io/favicon.ico"
                        if i + 1 < len(lines):
                            link = lines[i+1].strip()
                            if link.startswith('http'):
                                bein_channels.append({"name": name, "url": link, "logo": logo})
                if bein_channels: break # إذا وجدنا روابط لا داعي لإكمال بقية المصادر
        except: continue
    return bein_channels

def update_index_html(channels):
    if not channels:
        print("No channels found.")
        return

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
            parts = content.split(start_tag)
            parts_after = parts[1].split(end_tag)
            new_content = parts[0] + start_tag + "\n" + channels_html + "\n" + end_tag + parts_after[1]
            
            with open('index.html', 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"✅ Updated index.html with {len(channels)} fresh channels!")
        else:
            print("❌ Markers not found in index.html")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    # 1. صيد القنوات المحدثة
    live_bein = fetch_bein_tokens()
    
    # 2. تحديث index.html مباشرة
    update_index_html(live_bein)
