import requests
import json
import os
import base64

HOST = os.getenv('IPTV_HOST')
USER = os.getenv('IPTV_USER')
PASS = os.getenv('IPTV_PASS')
# تأكد أن هذا الرابط هو رابط الـ Worker الخاص بك
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
                # نركز على أهم القنوات الرياضية
                if any(x in line_upper for x in ["BEIN", "SSC", "AD SPORTS", "ARRIADIA"]):
                    name = lines[i].split(',')[-1].strip()
                    if i + 1 < len(lines) and "http" in lines[i+1]:
                        original_link = lines[i+1].strip()
                        # استخراج المعرف وتحويله لـ m3u8
                        stream_id = original_link.split('/')[-1].replace(".ts", ".m3u8")
                        if not stream_id.endswith(".m3u8"): stream_id += ".m3u8"
                        
                        # تشفير المعرف ليرسله للووركر بشكل نظيف
                        encoded_id = base64.b64encode(stream_id.encode()).decode()
                        channels.append({"name": name, "url": f"{WORKER_URL}/{encoded_id}"})
        
        with open('links.json', 'w', encoding='utf-8') as f:
            json.dump(channels, f, ensure_ascii=False, indent=4)
        print("✅ Done!")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    update_links()
