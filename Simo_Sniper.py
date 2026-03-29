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

    # تم تغيير المخرجات إلى m3u8 لضمان التوافق مع المتصفح
    m3u_url = f"{HOST}/get.php?username={USER}&password={PASS}&type=m3u_plus&output=m3u8"
    
    try:
        print("🚀 جاري فحص القائمة العظيمة وتحويلها لـ m3u8...")
        response = requests.get(m3u_url, timeout=30)
        lines = response.text.split('\n')
        
        channels = []
        for i in range(len(lines)):
            if "#EXTINF" in lines[i]:
                line_upper = lines[i].upper()
                # فلترة القنوات الرياضية
                if any(x in line_upper for x in ["BEIN", "SSC", "AD SPORTS", "ARRIADIA", "RMC"]):
                    name = lines[i].split(',')[-1].strip()
                    
                    if i + 1 < len(lines) and "http" in lines[i+1]:
                        original_link = lines[i+1].strip()
                        
                        # استخراج الـ ID وتحويله لـ m3u8
                        stream_id = original_link.split('/')[-1].replace(".ts", ".m3u8")
                        if ".m3u8" not in stream_id:
                            stream_id += ".m3u8"
                        
                        # تشفير الرابط لزيادة الحماية (Base64) ليقرأه الووركر
                        encoded_id = base64.b64encode(stream_id.encode()).decode()
                        protected_link = f"{WORKER_URL}/{encoded_id}"
                        
                        channels.append({
                            "name": name,
                            "url": protected_link
                        })
        
        with open('links.json', 'w', encoding='utf-8') as f:
            json.dump(channels, f, ensure_ascii=False, indent=4)
            
        print(f"✅ تم صيد {len(channels)} قناة بصيغة m3u8 بنجاح!")
        
    except Exception as e:
        print(f"❌ خطأ في الصيد: {e}")

if __name__ == "__main__":
    update_links()
