"""Unit tests for the SpriteRenderer.

Purpose:
    Verify that sprite grids are correctly rendered into scaled PNG images 
    with proper transparency and dimensions.

Dependencies:
    - numpy
    - pillow (PIL)
    - src.pixel_art_gen.renderer
"""
import numpy as np
from PIL import Image
from src.pixel_art_gen.renderer import SpriteRenderer

def test_renderer_output_size() -> None:
    """Verify that the output image has the correct scaled dimensions.
    
    Rationale:
        Scaling must be pixel-perfect for the art to look sharp.
    Process:
        Render a 10x10 grid with 8x scale and check the resulting PIL object.
    Inputs:
        Width=10, Height=10, Scale=8.
    Expectations:
        PIL Image with size (80, 80).
    """
    width, height = 10, 10
    scale = 8
    renderer = SpriteRenderer(scale=scale)
    
    grid = np.ones((height, width), dtype=int)
    ramps = [[(0, 0, 0)] * 4] * 3
    
    img = renderer.render(grid, ramps)
    
    assert isinstance(img, Image.Image)
    assert img.size == (width * scale, height * scale)
