import os
import requests

# جلب البيانات من Secrets
HOST = os.getenv("IPTV_HOST")
USER = os.getenv("IPTV_USER")
PASS = os.getenv("IPTV_PASS")

url = f"{HOST}/get.php?username={USER}&password={PASS}&type=m3u_plus&output=m3u8"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

try:
    response = requests.get(url, headers=headers, timeout=30)
    if response.status_code == 200:
        with open("playlist.m3u", "w", encoding="utf-8") as f:
            f.write(response.text)
        print("✅ Success: playlist.m3u updated!")
    else:
        print(f"❌ Error: {response.status_code}")
        exit(1)
except Exception as e:
    print(f"⚠️ Exception: {e}")
    exit(1)
