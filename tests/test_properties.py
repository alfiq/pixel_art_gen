"""Property-based testing for pixel art generation invariants.

Purpose:
    Exhaustively test the generation algorithm with random parameters to 
    ensure it never crashes and always maintains physical properties (symmetry).

Dependencies:
    - hypothesis
    - src.pixel_art_gen.generator
"""
from hypothesis import given, strategies as st
from src.pixel_art_gen.generator import SpriteGenerator

@given(
    w=st.integers(min_value=2, max_value=64),
    h=st.integers(min_value=2, max_value=64)
)
def test_generator_invariants(w: int, h: int) -> None:
    """Verify that symmetry always holds for any size and random state.
    
    Rationale:
        Fuzzing catches edge cases that hardcoded widths might miss.
    Process:
        Use Hypothesis to generate ranges and check symmetry logic.
    Inputs:
        w in [2, 64], h in [2, 64].
    Expectations:
        Symmetry invariant holds for every generated case.
    """
    gen = SpriteGenerator(width=w, height=h)
    grid = gen.generate()
    
    assert grid.shape == (h, w)
    
    for y in range(h):
        for x in range(w // 2):
            left_val = grid[y, x]
            right_val = grid[y, w - 1 - x]
            msg = f"Symmetry broken at ({y}, {x}) for size {w}x{h}"
            assert left_val == right_val, msg
