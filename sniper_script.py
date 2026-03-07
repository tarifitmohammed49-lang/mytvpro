import json
import os

# قاعدة البيانات التي سنعيد بناءها (Simo Final)
SIMO_DATABASE = {
    "Sports": [
        {"name": "Paramount+ HD", "logo": "https://example.com/paramount.png", "url": "رابط_قناة_باراماونت"},
        {"name": "EuroSport 1", "logo": "https://example.com/eurosport.png", "url": "رابط_يوروسبورت"},
        # سنضيف روابط beIN Sports هنا عبر القناص
    ],
    "beIN_Sports": [],
    "News": []
}

def sniper_engine():
    """محرك القناص للبحث عن روابط beIN والروابط الدولية"""
    print("🎯 Sniping International & beIN Links...")
    # هنا نضع المنطق الذي يجلب الروابط الحية
    # حالياً سنضع روابط تجريبية لضمان عمل الملف
    new_bein = [
        {"name": "beIN Sports 1", "url": "https://server.com/live/bein1/index.m3u8", "logo": "https://bit.ly/bein_logo"},
        {"name": "beIN Sports 2", "url": "https://server.com/live/bein2/index.m3u8", "logo": "https://bit.ly/bein_logo"}
    ]
    return new_bein

def save_database():
    bein_links = sniper_engine()
    SIMO_DATABASE["beIN_Sports"] = bein_links
    
    # حفظ الملف بصيغة JSON ليقرأه الموقع
    with open('links.json', 'w', encoding='utf-8') as f:
        json.dump(SIMO_DATABASE, f, ensure_ascii=False, indent=4)
    print("✅ Simo Final Database updated successfully!")

if __name__ == "__main__":
    save_database()
