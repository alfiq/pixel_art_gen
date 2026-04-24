"""Unit tests for the SpriteGenerator.

Purpose:
    Ensure that the core grid generation logic maintains physical invariants 
    like symmetry and valid pixel values.

Dependencies:
    - numpy
    - src.pixel_art_gen.generator
"""
import numpy as np
from src.pixel_art_gen.generator import SpriteGenerator

def test_generator_symmetry() -> None:
    """Verify that generated sprites are symmetrical.
    
    Rationale:
        Symmetry is the core artistic invariant of the PixelForge engine.
    Process:
        Instantiate a generator with a fixed seed and check if the left 
        side matches the reflected right side.
    Inputs:
        Width=16, Height=16, Seed=42.
    Expectations:
        Each pixel (y, x) must equal (y, width-1-x).
    """
    width, height = 16, 16
    gen = SpriteGenerator(width=width, height=height)
    grid = gen.generate(seed=42)
    
    assert grid.shape == (height, width)
    
    for y in range(height):
        for x in range(width // 2):
            assert grid[y, x] == grid[y, width - 1 - x]

def test_generator_values() -> None:
    """Verify that grid contains expected values (0-3).
    
    Rationale:
        The renderer depends on specific integer constants for color mapping.
    Process:
        Generate a random grid and iterate through unique values.
    Inputs:
        12x12 grid with default probabilities.
    Expectations:
        All values must be in the set {0, 1, 2, 3}.
    """
    gen = SpriteGenerator(12, 12)
    grid = gen.generate()
    
    unique_vals = np.unique(grid)
    for val in unique_vals:
        assert val in [0, 1, 2, 3]
