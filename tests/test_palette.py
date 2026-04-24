"""Unit tests for the PaletteGenerator.

Purpose:
    Verify artistic logic like hue-shifting, color wrapping, and ramp generation.

Dependencies:
    - pytest
    - src.pixel_art_gen.palette
"""
import pytest
from src.pixel_art_gen.palette import PaletteGenerator

def test_hue_shift_wrapping() -> None:
    """Verify that hue shifting wraps correctly around 0-1.
    
    Rationale:
        Colors should not 'clip' at 360 degrees; they must wrap to ensure 
        infinite color range.
    Process:
        Perform shift and check approximation to handle float precision.
    Inputs:
        0.9 + 0.2 and 0.1 - 0.2.
    Expectations:
        Returns 0.1 and 0.9 respectively.
    """
    assert PaletteGenerator.hue_shift(0.9, 0.2) == pytest.approx(0.1)
    assert PaletteGenerator.hue_shift(0.1, -0.2) == pytest.approx(0.9)

def test_generate_ramp() -> None:
    """Verify that a color ramp has the correct number of steps.
    
    Rationale:
        Lighting depth depends on the distinct number of shades available.
    Process:
        Generate a ramp from a base RGB and validate array properties.
    Inputs:
        RGB(100, 150, 200), Steps=5.
    Expectations:
        List of 5 RGB tuples, all values in range [0, 255].
    """
    base = (100, 150, 200)
    steps = 5
    ramp = PaletteGenerator.generate_ramp(base, steps=steps)
    
    assert len(ramp) == steps
    for color in ramp:
        assert len(color) == 3
        assert all(0 <= c <= 255 for c in color)
