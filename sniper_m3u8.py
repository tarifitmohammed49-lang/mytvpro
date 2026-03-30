import os
import requests
import json
import re

def run_sniper():
    # 1. جلب رابط الاشتراك من GitHub Secrets (الأمان أولاً)
    # تأكد أنك أضفت Secret باسم IPTV_URL في إعدادات المستودع
    source_url = os.getenv("IPTV_URL")
    
    # 2. رابط الـ Cloudflare Worker الخاص بك
    # ملاحظة: إذا قمت بإنشاء Worker جديد، استبدل هذا الرابط بالرابط الجديد
    worker_url = "https://bitter-lab-7724mytv-proxy.mytvpropagesdev.workers.dev/?url="
    
    if not source_url:
        print("❌ Error: IPTV_URL not found in GitHub Secrets!")
        return

    try:
        print("🚀 Starting Sniper: Fetching channels from provider...")
        response = requests.get(source_url, timeout=20)
        
        if response.status_code == 200:
            # سنقوم بتحويل ملف الـ M3U أو الـ JSON إلى صيغة يفهمها موقعك
            raw_content = response.text
            proxied_channels = []

            # محرك بحث لاستخراج القنوات (يدعم صيغ M3U المباشرة)
            # إذا كان اشتراكك يعيد ملف M3U8:
            matches = re.findall(r'#EXTINF:-1.*?,(.*?)\n(http.*)', raw_content)
            
            if matches:
                for name, url in matches:
                    clean_url = url.strip().replace('"', '')
                    # دمج الرابط مع البروكسي
                    final_url = f"{worker_url}{clean_url}"
                    
                    proxied_channels.append({
                        "name": name.strip(),
                        "url": final_url,
                        "logo": "https://mytvpro1.github.io/favicon.ico" # يمكنك تغيير اللوجو لاحقاً
                    })
            else:
                # إذا كان المصدر JSON أصلاً
                try:
                    data = response.json()
                    for item in data:
                        orig_url = item.get("url", "").strip().replace('"', '')
                        proxied_channels.append({
                            "name": item.get("name", "Unknown Channel"),
                            "url": f"{worker_url}{orig_url}",
                            "logo": item.get("logo", "https://mytvpro1.github.io/favicon.ico")
                        })
                except:
                    print("⚠️ Could not parse as M3U or JSON. Check your IPTV_URL.")

            # 3. حفظ النتيجة في ملف channels.json ليقرأه الموقع
            if proxied_channels:
                with open("channels.json", "w", encoding="utf-8") as f:
                    json.dump(proxied_channels, f, ensure_ascii=False, indent=2)
                print(f"✅ Success! {len(proxied_channels)} channels saved to channels.json")
            else:
                print("❌ No channels found in the source.")
        else:
            print(f"❌ Failed to fetch: Provider returned status {response.status_code}")

    except Exception as e:
        print(f"⚠️ Critical Error: {e}")

if __name__ == "__main__":
    run_sniper()
