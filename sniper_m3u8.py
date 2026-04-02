import requests
import json
import re
import os

# دالة لجلب القنوات من ملفك المحلي channels.json
def fetch_local_channels():
    file_path = 'channels.json'
    if os.path.exists(file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            print(f"Error reading channels.json: {e}")
    return []

# دالة جلب قنوات iptv-org (كاحتياط لضمان عدم بقاء الصفحة فارغة)
def fetch_iptv_org():
    url = "https://iptv-org.github.io/iptv/languages/ara.m3u"
    try:
        response = requests.get(url, timeout=15)
        if response.status_code == 200:
            lines = response.text.split('\n')
            channels = []
            for i in range(len(lines)):
                if lines[i].startswith('#EXTINF'):
                    name_match = re.search('tvg-name="(.*?)"', lines[i])
                    logo_match = re.search('tvg-logo="(.*?)"', lines[i])
                    name = name_match.group(1) if name_match else lines[i].split(',')[-1].strip()
                    logo = logo_match.group(1) if logo_match else "https://mytvpro1.github.io/favicon.ico"
                    if i + 1 < len(lines):
                        link = lines[i+1].strip()
                        if link.startswith('http'):
                            channels.append({"name": name, "url": link, "logo": logo})
            return channels
    except: return []
    return []

def update_index_html(channels):
    """حقن القنوات في ملف index.html"""
    if not channels:
        print("No channels found to inject.")
        return

    channels_html = "\n"
    for ch in channels:
        channels_html += f'''
            <div class="movie-card" onclick="openLivePlayer('{ch['url']}')">
                <img src="{ch['logo']}" alt="{ch['name']}" onerror="this.src='https://mytvpro1.github.io/favicon.ico'" loading="lazy">
                <div class="movie-title">{ch['name']}</div>
            </div>'''
    channels_html += "\n"

    try:
        with open('index.html', 'r', encoding='utf-8') as f:
            content = f.read()

        start_tag = ""
        end_tag = ""

        if start_tag in content and end_tag in content:
            parts_before = content.split(start_tag)
            parts_after = parts_before[1].split(end_tag)
            new_content = parts_before[0] + start_tag + channels_html + end_tag + parts_after[1]
            
            with open('index.html', 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Successfully injected {len(channels)} channels into index.html")
        else:
            print("Error: Markers not found in index.html")
    except Exception as e:
        print(f"Error updating HTML: {e}")

if __name__ == "__main__":
    print("Starting Sniper Update...")
    
    # 1. جلب قنوات beIN من ملفك (حتى لو لم تعمل، لنتأكد من ظهورها أولاً)
    local_channels = fetch_local_channels()
    
    # 2. جلب قنوات إضافية لضمان أن القسم ليس فارغاً
    public_channels = fetch_iptv_org()
    
    # 3. دمج القنوات (وضع قنواتك في البداية)
    final_list = local_channels + public_channels[:50]
    
    # 4. التحديث
    update_index_html(final_list)
