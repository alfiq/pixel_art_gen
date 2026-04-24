const spriteImg = document.getElementById('sprite-image');
const generateBtn = document.getElementById('generate-btn');
const downloadBtn = document.getElementById('download-btn');
const loader = document.getElementById('loader');
const historyGrid = document.getElementById('history');
const palettePreview = document.getElementById('palette-preview');
const scaleButtons = document.querySelectorAll('.scale-buttons button');

let currentScale = 16;
let currentSpriteData = null;

async function generateSprite() {
    loader.classList.remove('hidden');
    spriteImg.style.opacity = '0.3';
    
    try {
        const response = await fetch(`/generate?scale=${currentScale}`);
        const data = await response.json();
        
        currentSpriteData = data;
        renderSprite(data.image_url, data.palette);
        addToHistory(data.image_url);
        
    } catch (error) {
        console.error("Faliure in the evolution process:", error);
    } finally {
        loader.classList.add('hidden');
        spriteImg.style.opacity = '1';
    }
}

function renderSprite(url, palette) {
    spriteImg.src = url;
    
    // Render palette preview
    palettePreview.innerHTML = '';
    palette.forEach(ramp => {
        ramp.forEach(color => {
            const swatch = document.createElement('div');
            swatch.className = 'palette-swatch';
            swatch.style.backgroundColor = `rgb(${color[0]}, ${color[1]}, ${color[2]})`;
            palettePreview.appendChild(swatch);
        });
    });
}

function addToHistory(url) {
    const div = document.createElement('div');
    div.className = 'history-item';
    div.innerHTML = `<img src="${url}" class="pixelated">`;
    div.onclick = () => { spriteImg.src = url; };
    
    if (historyGrid.firstChild) {
        historyGrid.insertBefore(div, historyGrid.firstChild);
    } else {
        historyGrid.appendChild(div);
    }
}

scaleButtons.forEach(btn => {
    btn.onclick = () => {
        scaleButtons.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        currentScale = parseInt(btn.dataset.val);
        document.getElementById('res-label').innerText = `${currentScale}x Scaled`;
    };
});

generateBtn.onclick = generateSprite;

downloadBtn.onclick = () => {
    if (spriteImg.src) {
        const link = document.createElement('a');
        link.href = spriteImg.src;
        link.download = `pixel_asset_${Date.now()}.png`;
        link.click();
    }
};

// Initial generation
generateSprite();
