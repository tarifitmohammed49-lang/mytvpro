import requests
import json
import os
import base64

HOST = os.getenv('IPTV_HOST')
USER = os.getenv('IPTV_USER')
PASS = os.getenv('IPTV_PASS')
WORKER_URL = "https://noisy-frog-a85dmytv-proxy.mytvpropagesdev.workers.dev" 

def update_links():
    if not all([HOST, USER, PASS]):
        print("❌ Secrets missing!")
        return

    m3u_url = f"{HOST}/get.php?username={USER}&password={PASS}&type=m3u_plus&output=m3u8"
    
    try:
        response = requests.get(m3u_url, timeout=30)
        lines = response.text.split('\n')
        channels = []
        for i in range(len(lines)):
            if "#EXTINF" in lines[i]:
                line_upper = lines[i].upper()
                if any(x in line_upper for x in ["BEIN", "SSC", "AD SPORTS", "ARRIADIA", "RMC"]):
                    name = lines[i].split(',')[-1].strip()
                    if i + 1 < len(lines) and "http" in lines[i+1]:
                        original_link = lines[i+1].strip()
                        # نأخذ الـ ID فقط ونحوله لـ m3u8
                        stream_id = original_link.split('/')[-1].replace(".ts", ".m3u8")
                        if not stream_id.endswith(".m3u8"): stream_id += ".m3u8"
                        
                        # التشفير الصافي
                        encoded_id = base64.b64encode(stream_id.encode()).decode()
                        protected_link = f"{WORKER_URL}/{encoded_id}"
                        
                        channels.append({"name": name, "url": protected_link})
        
        with open('links.json', 'w', encoding='utf-8') as f:
            json.dump(channels, f, ensure_ascii=False, indent=4)
        print(f"✅ تم بنجاح صيد {len(channels)} قناة")
    except Exception as e:
        print(f"❌ خطأ: {e}")

if __name__ == "__main__":
    update_links()
