import requests

# رابط القائمة التي نجحت معك في PotPlayer
M3U_URL = "https://iptv-org.github.io/iptv/languages/ara.m3u"

def build():
    r = requests.get(M3U_URL)
    lines = r.text.split('\n')
    
    # بداية كود الصفحة لموقع MYTVPRO
    html = "<html><body style='background:#111; color:white; font-family:sans-serif;'><h1>MYTVPRO Channels</h1><div style='display:grid; grid-template-columns: repeat(auto-fill, minmax(200px, 1fr)); gap:10px;'>"
    
    for i in range(len(lines)):
        if lines[i].startswith('#EXTINF'):
            name = lines[i].split(',')[-1]
            url = lines[i+1]
            # صنع زر لكل قناة يفتحها في المشغل
            html += f"<div style='padding:15px; background:#222; border-radius:10px; text-align:center;'><h3>{name}</h3><a href='{url}' style='color:cyan;'>Play Channel</a></div>"
            
    html += "</div></body></html>"
    
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html)

if __name__ == "__main__":
    build()
