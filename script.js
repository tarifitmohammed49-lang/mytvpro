function playChannel(url) {
    const video = document.getElementById('liveVideoPlayer');
    
    // سطر إظهار الفيديو
    video.style.display = "block";

    if (Hls.isSupported()) {
        const hls = new Hls();
        hls.loadSource(url);
        hls.attachMedia(video);
        hls.on(Hls.Events.MANIFEST_PARSED, function() {
            video.muted = true; 
            video.play();
        });
    } else if (video.canPlayType('application/vnd.apple.mpegurl')) {
        video.src = url;
        video.play();
    }
}
