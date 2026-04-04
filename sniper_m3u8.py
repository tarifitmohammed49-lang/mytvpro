def update_index_html(channels):
    """حقن القنوات في ملف index.html"""
    if not channels:
        print("No channels found to inject.")
        return

    # بناء كود الـ HTML للقنوات
    channels_html = ""
    for ch in channels:
        # التأكد من تنظيف الرابط والاسم
        url = ch.get('url', '').strip()
        name = ch.get('name', 'Channel').strip()
        logo = ch.get('logo', 'https://mytvpro1.github.io/favicon.ico').strip()
        
        channels_html += f'''
        <div class="movie-card" onclick="openLivePlayer('{url}')">
            <img src="{logo}" alt="{name}" onerror="this.src='https://mytvpro1.github.io/favicon.ico'" loading="lazy">
            <div class="movie-title">{name}</div>
        </div>'''

    try:
        with open('index.html', 'r', encoding='utf-8') as f:
            content = f.read()

        # العلامات التي وضعناها في ملف الـ HTML
        start_tag = ""
        end_tag = ""

        if start_tag in content and end_tag in content:
            # تقسيم الملف وإعادة تجميعه بالمحتوى الجديد
            parts_before = content.split(start_tag)
            parts_after = parts_before[1].split(end_tag)
            
            new_content = parts_before[0] + start_tag + "\n" + channels_html + "\n" + end_tag + parts_after[1]
            
            with open('index.html', 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"✅ Successfully injected {len(channels)} channels into index.html")
        else:
            print("❌ Error: Markers (SNIPER_START/END) not found in index.html")
    except Exception as e:
        print(f"❌ Error updating HTML: {e}")
