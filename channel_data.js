/* النسخة الاحترافية لمنع التشنج - سيمو فاينل */
async function loadLiveFoot() {
    isFeatured = false; 
    currentGenre = null; 
    currentPage = 1;
    
    document.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
    document.getElementById('btnLiveFoot').classList.add('active');
    
    const grid = document.getElementById('moviesGrid');
    grid.innerHTML = "<p style='text-align:center; width:100%; padding:20px; color:var(--main-red);'>🔄 جاري تحديث القنوات الحية بدون تشنج...</p>"; 

    try {
        // إضافة Timestamp لمنع التخزين المؤقت (Cache)
        const response = await fetch('https://raw.githubusercontent.com/mytvpro1/mytvpro1.github.io/main/channels_data.js?t=' + new Date().getTime());
        const text = await response.text();
        
        // استخراج المصفوفة بدقة من النص
        const startIndex = text.indexOf('[');
        const endIndex = text.lastIndexOf(']') + 1;
        const dataString = text.substring(startIndex, endIndex);
        
        let channels = JSON.parse(dataString);
        grid.innerHTML = ""; 

        if (channels.length > 0) {
            // تحميل أول 50 قناة فوراً لسرعة الاستجابة
            renderChannelBatch(channels.slice(0, 50));
            
            // تحميل البقية بعد 100 ملي ثانية لتجنب تجميد الواجهة
            if (channels.length > 50) {
                setTimeout(() => {
                    renderChannelBatch(channels.slice(50));
                }, 100);
            }
        } else {
            grid.innerHTML = "<p style='text-align:center; width:100%; padding:20px;'>⚠️ لا توجد قنوات متاحة حالياً.</p>";
        }
    } catch (error) {
        console.error("Error:", error);
        grid.innerHTML = "<p style='text-align:center; width:100%; padding:20px;'>❌ حدث خطأ أثناء تحميل القنوات.</p>";
    }
    document.getElementById('loadMoreSection').style.display = 'none';
}

// دالة مساعدة لرسم القنوات
function renderChannelBatch(batch) {
    const grid = document.getElementById('moviesGrid');
    const html = batch.map(ch => `
        <div class="movie-card" onclick="openLivePlayer('${ch.url}')">
            <img src="${ch.logo}" alt="${ch.name}" onerror="this.src='https://mytvpro1.github.io/favicon.ico'" loading="lazy" style="object-fit: contain; background: #000; padding: 10px;">
            <div class="movie-title">${ch.name}</div>
        </div>
    `).join('');
    grid.insertAdjacentHTML('beforeend', html);
}
