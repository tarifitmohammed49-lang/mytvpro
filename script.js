// وظيفة جلب القنوات من ملف links.json المحدث بواسطة القناص
async function loadCategory(cat) {
    const grid = document.getElementById('channelsGrid');
    if (!grid) return;

    // إظهار رسالة تحميل
    grid.innerHTML = '<div style="color:#ff3b5c; grid-column:1/-1;">جاري قنص القنوات... 🚀</div>';

    try {
        // جلب البيانات مع منع التخزين المؤقت (Cache)
        const response = await fetch(`links.json?t=${new Date().getTime()}`);
        const data = await response.json();
        
        // مسح الشبكة لعرض القنوات الجديدة
        grid.innerHTML = '';

        // تحديد القسم المطلوب (رياضة، أخبار، أو دولة معينة)
        const channels = data[cat] || [];

        if (channels.length > 0) {
            channels.forEach(channel => {
                const card = document.createElement('div');
                card.className = 'channel-card';
                card.innerHTML = `
                    <img src="${channel.logo}" onerror="this.src='https://via.placeholder.com/60/0b0e11/ff3b5c?text=TV'">
                    <span>${channel.name}</span>
                `;
                // تشغيل القناة عند الضغط
                card.onclick = () => startStream(channel.url);
                grid.appendChild(card);
            });
        } else {
            grid.innerHTML = '<div style="grid-column:1/-1;">لا توجد قنوات في قسم ' + cat.toUpperCase() + '</div>';
        }

        // تحديث شكل الأزرار (Active)
        document.querySelectorAll('.cat-btn').forEach(btn => btn.classList.remove('active'));
        if(document.getElementById('cat-' + cat)) document.getElementById('cat-' + cat).classList.add('active');

    } catch (error) {
        console.error("خطأ:", error);
        grid.innerHTML = '<div style="color:red; grid-column:1/-1;">تأكد من تشغيل python sniper_script.py</div>';
    }
}

// وظيفة تشغيل البث المباشر في المشغل (Player)
function startStream(url) {
    closeChannelsModal(); // إغلاق قائمة القنوات
    document.getElementById('mainPlayer').style.display = 'none';
    const video = document.getElementById('liveVideoPlayer');
    video.style.display = 'block';
    document.getElementById('videoPlayerContainer').style.display = 'flex';
    
    if (Hls.isSupported()) {
        const hls = new Hls();
        hls.loadSource(url);
        hls.attachMedia(video);
        hls.on(Hls.Events.MANIFEST_PARSED, () => video.play());
    } else {
        video.src = url;
        video.play();
    }
}