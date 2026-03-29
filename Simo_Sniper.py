import json

def hunt():
    print("🚀 Simo Sniper: Injecting Premium BeIN Channels into Live Foot...")
    
    # هذه هي القائمة التي أرسلتها أنت (قنواتك الشغالة)
    premium_channels = [
        {"name": "⭐ BeIn 1 FHD", "url": "http://s1219.x.smline.xyz:2082/plays/b1U0TXBPYU85TXRwWTlUYVVKNkNhdWtxcEdnR2tkcHZOUmZzekNNOWMwWWxka1BPNlNKTHlzKzd5Vys4eWo0Wg==.ts"},
        {"name": "⭐ BeIn 2 FHD", "url": "http://s1219.x.smline.xyz:2082/plays/NEQ5cGhpQWlSTm9kNkFDeGFMWlFpTXdWY0Y0bmUycUlXUnVMb0VwbFhIa0pLWUlEK0pqZEJMRUMwMFhJN3hHMw==.ts"},
        {"name": "⭐ BeIn 3 FHD", "url": "http://s1219.x.smline.xyz:2082/plays/c0xvTG84ellzWVBaQ3M3eDJ0MCs4bG5tTEJTU2RYN01hNldzUlAvanVlbThoRFFJaDVvRUpFYzBlQkxWWTlJeg==.ts"},
        {"name": "⭐ BeIn 4 FHD", "url": "http://s1219.x.smline.xyz:2082/plays/amZId09XT3ZmQ3BBUXVUS2dpbFZOV2hSOWFjNjU4V1F0bWVxMG1hSjdwTDhhMHJWTlRvUDZXclRuRThWYmhvTQ==.ts"},
        {"name": "⭐ BeIn 5 FHD", "url": "http://s1219.x.smline.xyz:2082/plays/dUJxOEoyZWFISWZ4eXEzS3IwTVYxbERGbnNMN3l1RXkrSW9FRDN1UUdXWEtVbTNxS1A2aHcva2lBVFpuT0Rpcg==.ts"},
        {"name": "⭐ BeIn 6 FHD", "url": "http://s1219.x.smline.xyz:2082/plays/SGVMY0RkUW9NY2NQc2VzelFHMk8wTm1FcUlyYWoxMUVZTnZaeVJsMnVVL3NBU1dnLzhUTWl6SjZGNExOci9NVQ==.ts"},
        {"name": "⭐ BeIn 7 FHD", "url": "http://s1219.x.smline.xyz:2082/plays/TWxxMGxHclcyRnVGbkhGdW9NTXZzZlZtVEVVV1VmUHBnSnlIb3lKMFNBY2NKS0RLYU9SM3I2bXlRUVc4NjZkWg==.ts"},
        {"name": "⭐ BeIn 8 FHD", "url": "http://s1219.x.smline.xyz:2082/plays/RjFQckNxWXIwdHJ2bDhSRGZKKzFJME9HaWwwSk9oN2N6TlFQamJqNCszS0J2Q3ZuSmpJZkMrZXFGaitYYmU5WA==.ts"},
        {"name": "⭐ BeIn 9 FHD", "url": "http://s1219.x.smline.xyz:2082/plays/ZlEyN2E0dlliNVdNektUZDJvS3RHSjFUdVhVc1I4anE0QjR1bVk0Y1k5Wk9ZbmJhVGFqRVFPTlkySHdoZ3lWLw==.ts"},
        {"name": "⭐ BeIn Sports News FHD", "url": "http://s1219.x.smline.xyz:2082/plays/b0daUHozNUpiQitGL25FN3d4MzdmYWVGQy8zVDMyTVJHdysxNzF3dmVuSXk4b3ROMjFrVnRnemNEK0ZETURIQw==.ts"},
        {"name": "⭐ beIN Sports 1 HD", "url": "http://s1219.x.smline.xyz:2082/plays/ZDBWbHJBZmM0a3lZRk10NmpIKzZ6a2xCNFV2dzZTUUJSWmY1SWQ0L1NPbWRTWUx1aFFMbVkrL2FFV0ZleUtELzUxOEhmSkQ5ell6cGZBczc5UDJ0Z3c9PQ==.ts"},
        {"name": "⭐ BeIn 1 FR FHD", "url": "http://s1219.x.smline.xyz:2082/plays/UnZOcG5kT2kzbnU4VDFkNC9lNjhyQVdwSXdwNWczbEtMdjhUcVIxVzErRFcra2l4TzNDbHdlMDRHOTRxUHdEdw==.ts"}
        # ملاحظة: يمكنك إضافة باقي القنوات بنفس الطريقة هنا
    ]

    final_list = []
    
    for ch in premium_channels:
        final_list.append({
            "name": ch["name"],
            "url": ch["url"],
            "logo": "https://mytvpro1.github.io/favicon.ico",
            "headers": {"User-Agent": "VLC/3.0.18 LibVLC/3.0.18"}
        })

    # حفظ الملف ليقرأه الموقع فوراً
    with open('links.json', 'w', encoding='utf-8') as f:
        json.dump(final_list, f, ensure_ascii=False, indent=2)
    
    print(f"✅ Success! {len(final_list)} BeIN channels are now ready for your website.")

if __name__ == "__main__":
    hunt()
