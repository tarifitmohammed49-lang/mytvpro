import requests
import json
import os

HOST = os.getenv('IPTV_HOST')
USER = os.getenv('IPTV_USER')
PASS = os.getenv('IPTV_PASS')
WORKER_URL = "https://noisy-frog-a85dmytv-proxy.mytvpropagesdev.workers.dev" 

def update_links():
    if not all([HOST, USER, PASS]):
        print("❌ Secrets missing!")
        return

    # جلب القنوات بصيغة m3u_plus لضمان جلب الأسماء كاملة
    m3u_url = f"{HOST}/get.php?username={USER}&password={PASS}&type=m3u_plus&output=ts"
    
    try:
        print("🚀 جاري فحص القائمة العظيمة...")
        # زيادة وقت الانتظار لـ 30 ثانية لأن القائمة كبيرة
        response = requests.get(m3u_url, timeout=30)
        lines = response.text.split('\n')
        
        channels = []
        for i in range(len(lines)):
            if "#EXTINF" in lines[i]:
                # سيبحث عن beIN أو SSC أو أي قناة رياضية مغربية
                # لجعل القائمة مليئة وممتعة
                line_upper = lines[i].upper()
                if "BEIN" in line_upper or "SSC" in line_upper or "AD SPORTS" in line_upper:
                    name = lines[i].split(',')[-1].strip()
                    
                    # التأكد من وجود السطر التالي الذي يحتوي على الرابط
                    if i + 1 < len(lines) and "http" in lines[i+1]:
                        original_link = lines[i+1].strip()
                        stream_id = original_link.split('/')[-1]
                        protected_link = f"{WORKER_URL}/{stream_id}"
                        
                        channels.append({
                            "name": name,
                            "url": protected_link
                        })
        
        with open('links.json', 'w', encoding='utf-8') as f:
            json.dump(channels, f, ensure_ascii=False, indent=4)
            
        print(f"✅ تم صيد {len(channels)} قناة بنجاح!")
        
    except Exception as e:
        print(f"❌ خطأ في الصيد: {e}")

if __name__ == "__main__":
    update_links()
