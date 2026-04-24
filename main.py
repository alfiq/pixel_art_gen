"""FastAPI application for the PixelForge dashboard.

Purpose:
    Provide a web interface and API for real-time asset generation.

Dependencies:
    - fastapi
    - uvicorn
    - pixel_art_gen (internal)
"""

import os
import uuid
from typing import Any
from fastapi import FastAPI, Query
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from src.pixel_art_gen.generator import SpriteGenerator
from src.pixel_art_gen.palette import PaletteGenerator
from src.pixel_art_gen.renderer import SpriteRenderer

app = FastAPI(title="PixelForge API")

# Ensure output directory exists
os.makedirs("output", exist_ok=True)

# Mount static files
app.mount("/static", StaticFiles(directory="src/pixel_art_gen/web"), name="static")
app.mount("/output", StaticFiles(directory="output"), name="output")

@app.get("/")
async def read_root() -> FileResponse:
    """Serves the main web dashboard interface.
    
    Returns:
        FileResponse of the index.html.
    """
    return FileResponse("src/pixel_art_gen/web/index.html")

@app.get("/generate")
async def generate_sprite(
    width: int = Query(16, ge=8, le=64),
    height: int = Query(16, ge=8, le=64),
    scale: int = Query(16, ge=1, le=64),
    seed: int = None
) -> dict[str, Any]:
    """API endpoint to generate and save a procedural sprite.
    
    Args:
        width: Sprite width (8-64).
        height: Sprite height (8-64).
        scale: Final image scale.
        seed: Optional generation seed.
        
    Returns:
        JSON with the image_url, palette, and seed.
    """
    gen = SpriteGenerator(width=width, height=height)
    grid = gen.generate(seed=seed)
    
    palette = PaletteGenerator.get_random_palette()
    
    renderer = SpriteRenderer(scale=scale)
    img = renderer.render(grid, palette)
    
    filename = f"sprite_{uuid.uuid4().hex}.png"
    filepath = os.path.join("output", filename)
    img.save(filepath)
    
    return {
        "image_url": f"/output/{filename}",
        "palette": palette,
        "seed": seed
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
