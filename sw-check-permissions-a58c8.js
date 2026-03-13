// محتوى ملف sw.js
function getYmid() { try { return new URL(location.href).searchParams.get('ymid'); } catch (e) { console.warn(e); } return null; } 
function getVar() { try { return new URL(location.href).searchParams.get('var'); } catch (e) { console.warn(e); } return null; } 
self.options = { 
    "domain": "kmnts.com", 
    "resubscribeOnInstall": true, 
    "zoneId": 10722972, 
    "ymid": getYmid(), 
    "var": getVar() 
} 
self.lary = ""; 
importScripts('https://kmnts.com/act/files/sw.perm.check.min.js?r=sw');
