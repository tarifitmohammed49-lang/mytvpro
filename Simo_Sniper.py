import requests
import json
import os

# جلب البيانات من الخزنة السرية لـ GitHub التي أنشأتها (IPTV_HOST, IPTV_USER, IPTV_PASS)
HOST = os.getenv('IPTV_HOST')
USER = os.getenv('IPTV_USER')
PASS = os.getenv('IPTV_PASS')

# رابط الدرع (الـ Worker) الخاص بك في Cloudflare
WORKER_URL = "https://noisy-frog-a85dmytv-proxy.mytvpropagesdev.workers.dev" 

def update_links():
    # التأكد أن البيانات وصلت من الخزنة بنجاح
    if not all([HOST, USER, PASS]):
        print("❌ خطأ: لم نجد البيانات في الخزنة! تأكد من الأسماء في Settings > Secrets.")
        return

    # رابط الـ M3U لجلب قائمة القنوات الأصلية
    m3u_url = f"{HOST}/get.php?username={USER}&password={PASS}&type=m3u_plus&output=ts"
    
    try:
        print("🚀 جاري قنص قنوات beIN Sports عبر الدرع الآمن...")
        response = requests.get(m3u_url, timeout=20)
        lines = response.text.split('\n')
        
        channels = []
        for i in range(len(lines)):
            # سنركز على قنوات beIN Sports العربية لضمان الجودة
            if "#EXTINF" in lines[i] and "beIN SPORTS" in lines[i].upper():
                name = lines[i].split(',')[-1].strip()
                original_link = lines[i+1].strip()
                
                # استخراج معرف القناة (مثل 8842.ts) لتمويهه خلف الـ Worker
                if '/' in original_link:
                    stream_id = original_link.split('/')[-1]
                    # صنع الرابط المحمي الذي سيظهر للجمهور (البائع لن يراه)
                    protected_link = f"{WORKER_URL}/{stream_id}"
                    
                    channels.append({
                        "name": name,
                        "url": protected_link
                    })
        
        # حفظ القنوات المحمية في ملف JSON ليقرأه موقعك
        with open('links.json', 'w', encoding='utf-8') as f:
            json.dump(channels, f, ensure_ascii=False, indent=4)
            
        print(f"✅ مبروك يا سيمو! تم تحديث {len(channels)} قناة والبيانات مشفرة.")
        
    except Exception as e:
        print(f"❌ حدث خطأ تقني: {e}")

if __name__ == "__main__":
    update_links()
