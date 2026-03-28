function playChannel(url) {
    const video = document.getElementById('liveVideoPlayer');
    video.style.display = "block";

    // ربط الرابط بالـ Worker الخاص بك لتخطي الحماية وتجنب الشاشة السوداء
    const proxyUrl = "https://mytvpro.mytvpropagesdev.workers.dev/?url=" + encodeURIComponent(url);

    if (Hls.isSupported()) {
        const hls = new Hls({
            xhrSetup: function (xhr, url) {
                xhr.withCredentials = false; 
            }
        });
        hls.loadSource(proxyUrl); 
        hls.attachMedia(video);
        hls.on(Hls.Events.MANIFEST_PARSED, function() {
            video.muted = false; 
            video.play().catch(e => console.log("Auto-play prevented"));
        });

        // مراقبة الأخطاء لمعرفة سبب توقف الصورة
        hls.on(Hls.Events.ERROR, function (event, data) {
            if (data.fatal) {
                console.error("HLS Fatal Error:", data.type);
            }
        });

    } else if (video.canPlayType('application/vnd.apple.mpegurl')) {
        video.src = proxyUrl;
        video.play();
    }
}
