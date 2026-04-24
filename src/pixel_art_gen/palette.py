"""Procedural color palette generation with hue-shifting.

Purpose:
    Provide harmonious color ramps using artistic lighting heuristics.

Dependencies:
    - colorsys (standard library)
"""

import colorsys
from typing import List, Tuple

# Type alias for RGB color (0-255)
RGB = Tuple[int, int, int]

class PaletteGenerator:
    """Generates harmonious color ramps using hue-shifting logic."""

    @staticmethod
    def hue_shift(h: float, amount: float) -> float:
        """Shifts the hue within the 0-1 range.
        
        Args:
            h: Current hue (0-1).
            amount: Amount to shift.
            
        Returns:
            Shifted hue.
        """
        return (h + amount) % 1.0

    @classmethod
    def generate_ramp(
        cls, 
        base_color: RGB, 
        steps: int = 4, 
        hue_shift_amount: float = 0.05
    ) -> List[RGB]:
        """Generates a color ramp from a base color with hue shifting.
        
        Args:
            base_color: The starting RGB color.
            steps: Number of shades to generate.
            hue_shift_amount: How much to shift hue per step.
            
        Returns:
            A list of RGB tuples representing the ramp from darkest to lightest.
        """
        # Convert RGB to HLS (Hue, Lightness, Saturation)
        r, g, b = [x / 255.0 for x in base_color]
        h, l_light, s = colorsys.rgb_to_hls(r, g, b)

        ramp: List[RGB] = []
        
        for i in range(steps):
            target_l = 0.15 + (i / (steps - 1)) * 0.75
            shift = (target_l - 0.5) * hue_shift_amount
            new_h = cls.hue_shift(h, shift)
            new_s = max(0.1, min(1.0, s + (0.5 - target_l) * 0.2))
            
            new_r, new_g, new_b = colorsys.hls_to_rgb(new_h, target_l, new_s)
            ramp.append((int(new_r * 255), int(new_g * 255), int(new_b * 255)))
            
        return ramp

    @classmethod
    def get_random_palette(cls) -> List[List[RGB]]:
        """Generates a random multi-ramp palette (Main, Accent, Detail).
        
        Returns:
            List of ramps.
        """
        import random
        
        base_h = random.random()
        accent_h = (base_h + 0.5) % 1.0
        detail_h = (base_h + 0.3) % 1.0
        
        palettes = []
        for val_h in [base_h, accent_h, detail_h]:
            r_val, g_val, b_val = colorsys.hls_to_rgb(val_h, 0.5, 0.7)
            rgb_base = (int(r_val * 255), int(g_val * 255), int(b_val * 255))
            palettes.append(cls.generate_ramp(rgb_base))
            
        return palettes
