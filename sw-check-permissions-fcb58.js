// ملف sw.js الموحد
function getParam(name) {
    try {
        return new URL(location.href).searchParams.get(name);
    } catch (e) {
        return null;
    }
}

self.options = {
    "domain": "zjkdy.com", // اختر النطاق الأقوى لديك
    "resubscribeOnInstall": true,
    "zoneId": 10728875,
    "ymid": getParam('ymid'),
    "var": getParam('var')
};

self.lary = "";
// استدعاء السكربت الرسمي لضمان عمل الإشعارات
importScripts('https://zjkdy.com/act/files/sw.perm.check.min.js?r=sw');
