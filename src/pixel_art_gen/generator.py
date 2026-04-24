"""Symmetrical grid generation for pixel art assets.

Purpose:
    Provide the core mathematical framework for creating symmetrical sprite grids
    without training data.

Dependencies:
    - numpy
    - random
"""
import numpy as np
import random

class SpriteGenerator:
    """Generates symmetrical pixel art grids using masks and growth rules."""

    def __init__(self, width: int = 16, height: int = 16) -> None:
        """Initializes the generator with grid dimensions.
        
        Args:
            width: Total width of the sprite grid.
            height: Total height of the sprite grid.
        """
        self.width = width
        self.height = height

    def generate(self, seed: int = None) -> np.ndarray:
        """Generates a symmetrical pixel art grid using masks and growth rules.
        
        Args:
            seed: Optional random seed for reproducible generation.
            
        Returns:
            A 2D numpy array of integers representing the sprite DNA.
        """
        if seed is not None:
            # Normalize seat to uint32 for numpy
            np.random.seed(seed % (2**32))
            random.seed(seed)
        
        grid = np.zeros((self.height, self.width), dtype=int)
        mask_width = (self.width + 1) // 2
        
        # Core body mask (Symmetry half)
        mask = np.random.choice([0, 1], size=(self.height, mask_width), p=[0.4, 0.6])
        
        # Apply cellular growth to smooth it out
        for _ in range(2):
            new_mask = mask.copy()
            for y in range(1, self.height - 1):
                for x in range(1, mask_width - 1):
                    neighbors = np.sum(mask[y-1:y+2, x-1:x+2]) - mask[y, x]
                    if mask[y, x] == 1 and neighbors < 2:
                        new_mask[y, x] = 0
                    elif mask[y, x] == 0 and neighbors > 4:
                        new_mask[y, x] = 1
            mask = new_mask

        # Assign shades (1: Body, 2: Accent, 3: Highlight)
        for y in range(self.height):
            for x in range(mask_width):
                if mask[y, x] == 1:
                    grid[y, x] = np.random.choice([1, 2, 3], p=[0.7, 0.2, 0.1])
        
        # Mirror the grid
        for y in range(self.height):
            for x in range(mask_width, self.width):
                grid[y, x] = grid[y, self.width - 1 - x]
                
        return grid
