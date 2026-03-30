import os
import requests
import json

def run_sniper():
    # هنا نضع الروابط التي تجلب التوكينات (أو السيرفر الخاص بك)
    # ملاحظة: يمكنك تعديل الرابط أدناه ليتوافق مع مصدر روابطك
    source_url = "https://raw.githubusercontent.com/mytvpro1/sniped-links/main/bein_tokens.json" 
    
    try:
        print("Searching for fresh beIN Sports tokens...")
        response = requests.get(source_url, timeout=15)
        
        if response.status_code == 200:
            channels_data = response.json()
            
            # حفظ البيانات في ملف channels.json
            with open("channels.json", "w", encoding="utf-8") as f:
                json.dump(channels_data, f, ensure_ascii=False, indent=2)
            
            print(f"Successfully sniped {len(channels_data)} channels and saved to channels.json")
        else:
            print("Failed to fetch tokens from source.")

    except Exception as e:
        print(f"Error during sniping: {e}")

if __name__ == "__main__":
    run_sniper()
