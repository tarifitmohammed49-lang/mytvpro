import os
import requests
import json

def run_sniper():
    # 1. رابط الـ Worker الخاص بك (تأكد أنه ينتهي بـ ?url=)
    worker_url = "https://bitter-lab-7724mytv-proxy.mytvpropagesdev.workers.dev/?url="
    
    # 2. رابط المصدر الذي تجلب منه البيانات (سواء كان M3U أو JSON)
    # ملاحظة: إذا كان لديك رابط الاشتراك المباشر، يفضل وضعه هنا
    source_url = "https://raw.githubusercontent.com/mytvpro1/sniped-links/main/bein_tokens.json" 
    
    try:
        print("Searching for fresh beIN Sports tokens...")
        response = requests.get(source_url, timeout=15)
        
        if response.status_code == 200:
            raw_data = response.json()
            proxied_channels = []

            for channel in raw_data:
                # استخراج الرابط الأصلي
                original_url = channel.get("url", "")
                
                # دمج الرابط مع البروكسي لفك الحظر
                clean_url = original_url.strip().replace('"', '')
                new_url = f"{worker_url}{clean_url}"
                
                # بناء بيانات القناة الجديدة
                proxied_channels.append({
                    "name": channel.get("name", "Unknown Channel"),
                    "url": new_url,
                    "logo": channel.get("logo", "https://mytvpro1.github.io/favicon.ico"),
                    "headers": {
                        "User-Agent": "IPTVSmartersPlayer"
                    }
                })
            
            # حفظ البيانات النهائية في ملف channels.json
            with open("channels.json", "w", encoding="utf-8") as f:
                json.dump(proxied_channels, f, ensure_ascii=False, indent=2)
            
            print(f"✅ Done! {len(proxied_channels)} channels are now routed through your Worker.")
        else:
            print(f"❌ Failed: Source returned status {response.status_code}")

    except Exception as e:
        print(f"⚠️ Error: {e}")

if __name__ == "__main__":
    run_sniper()
