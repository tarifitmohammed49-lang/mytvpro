<?php
// الرابط الذي قنصته أنت يا بطل
$remoteUrl = "http://185.114.146.35:53480/live/4563cedc/UzFZUENMLzFCMU10Qmh5TEV1NkfGdM5XVUZSckZtc01ZNHl6V293N1ZSVUpvS05CaDQrV0ZzR3BwTVpIQUxlSXVhUlpZCaDQ9/1.ts";

// هوية التلفاز التي استخرجناها من Wireshark
$userAgent = "Mozilla/5.0 (WebOS; Linux/SmartTV) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 WebAppManager";

$opts = [
    "http" => [
        "method" => "GET",
        "header" => "User-Agent: " . $userAgent . "\r\n"
    ]
];

$context = stream_context_create($opts);

// إخبار المتصفح أن هذا فيديو
header("Content-Type: video/mp2t");

// جلب البث وتمريره للمتصفح
readfile($remoteUrl, false, $context);
