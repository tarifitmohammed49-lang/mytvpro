function playChannel(url) {
    const video = document.getElementById('liveVideoPlayer');
    
    // إظهار المشغل
    video.style.display = "block";

    // ملاحظة: الرابط القادم في المتغير url هو بالفعل يحتوي على رابط الووركر + التشفير
    // مثال: https://noisy-frog-a85dmytv-proxy.workers.dev/RzBNdWppNmVy...
    const finalUrl = url; 

    if (Hls.isSupported()) {
        // تنظيف أي نسخة سابقة من HLS لتجنب تعليق البث
        if (window.hls) {
            window.hls.destroy();
        }

        const hls = new Hls({
            xhrSetup: function (xhr, url) {
                // إعدادات إضافية لضمان عمل البث عبر Cloudflare
                xhr.withCredentials = false;
            }
        });

        window.hls = hls; // حفظ النسخة الحالية
        hls.loadSource(finalUrl); 
        hls.attachMedia(video);

        hls.on(Hls.Events.MANIFEST_PARSED, function() {
            video.muted = false; 
            video.play().catch(e => {
                console.log("Auto-play prevented, needs user interaction");
                // في بعض المتصفحات يجب أن يضغط المستخدم أولاً
            });
        });

        // مراقبة الأخطاء
        hls.on(Hls.Events.ERROR, function (event, data) {
            if (data.fatal) {
                switch (data.type) {
                    case Hls.ErrorTypes.NETWORK_ERROR:
                        console.error("خطأ في الشبكة: تأكد من رابط الووركر");
                        hls.startLoad();
                        break;
                    case Hls.ErrorTypes.MEDIA_ERROR:
                        console.error("خطأ في الميديا: محاولة الإصلاح...");
                        hls.recoverMediaError();
                        break;
                    default:
                        hls.destroy();
                        break;
                }
            }
        });

    } else if (video.canPlayType('application/vnd.apple.mpegurl')) {
        // دعم متصفح Safari
        video.src = finalUrl;
        video.addEventListener('loadedmetadata', function() {
            video.play();
        });
    }
}
