"""Sprite rendering logic with outlines and shading.

Purpose:
    Convert 2D integer grids into pixel-perfect RGBA PNG images.

Dependencies:
    - numpy
    - pillow (PIL)
"""

import numpy as np
from PIL import Image

class SpriteRenderer:
    """Renders sprite grids into images with artistic effects."""

    def __init__(self, scale: int = 8) -> None:
        """Initializes the renderer with a scaling factor.
        
        Args:
            scale: Pixel multiplier for the final image output.
        """
        self.scale = scale

    def render(self, grid: np.ndarray, palette: list) -> Image.Image:
        """Renders the grid into a PIL Image.
        
        Args:
            grid: 2D integer array.
            palette: Primary, Secondary, and Detail ramps.
            
        Returns:
            A scaled PIL Image object.
        """
        h, w = grid.shape
        # Create an RGBA image
        img_data = np.zeros((h, w, 4), dtype=np.uint8)
        
        # Simple mapping:
        # 0: Transparent
        # 1: Body (Palette[0])
        # 2: Accent (Palette[1])
        # 3: Detail (Palette[2])
        
        for y in range(h):
            for x in range(w):
                val = grid[y, x]
                if val == 0:
                    continue
                
                # Check for "outline" (neighbors are 0)
                is_outline = False
                for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    ny, nx = y + dy, x + dx
                    if 0 <= ny < h and 0 <= nx < w:
                        if grid[ny, nx] == 0:
                            is_outline = True
                            break
                    else:
                        is_outline = True # Edge of image is outline
                        break
                
                if is_outline:
                    # Black outline
                    img_data[y, x] = [20, 20, 25, 255]
                else:
                    # Map to middle shade of the ramp
                    ramp = palette[val - 1]
                    color = ramp[len(ramp)//2]
                    img_data[y, x] = [*color, 255]
                    
        img = Image.fromarray(img_data, "RGBA")
        return img.resize((w * self.scale, h * self.scale), resample=Image.NEAREST)
