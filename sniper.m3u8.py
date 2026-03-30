import requests # تأكد أن الحرف الأول صغير (import) وليس (Import)

# بيانات السيرفر
HOST = "http://s1219.x.smline.xyz:2082"
USER = "287466745324941"
PASS = "44754351"

# الرابط السحري - بصيغة m3u8
url = f"{HOST}/get.php?username={USER}&password={PASS}&type=m3u_plus&output=m3u8"

headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Mobile Safari/537.36'
}

try:
    response = requests.get(url, headers=headers, timeout=20)
    if response.status_code == 200:
        # حفظ الملف في المجلد الرئيسي
        with open("playlist.m3u", "w", encoding="utf-8") as f:
            f.write(response.text)
        print("✅ تم بنجاح! القنوات الآن بصيغة m3u8 وجاهزة لموقعك.")
    else:
        print(f"❌ فشل الاتصال بالسيرفر. الكود: {response.status_code}")
        exit(1) # لإخبار GitHub أن هناك مشكلة في الرد
except Exception as e:
    print(f"⚠️ خطأ تقني: {e}")
    exit(1)
