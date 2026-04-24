# PixelForge Test Suite

This directory contains the automated verification suite for the PixelForge procedural engine.

## 1. Structure
- `test_generator.py`: Invariants for symmetrical grid generation.
- `test_palette.py`: Color theory and hue-shifting verification.
- `test_renderer.py`: Scaling and pixel-perfect rendering tests.
- `test_properties.py`: Hypothesis-based property testing for robustness.
- `test_api.py`: FastAPI endpoint integration tests.

## 2. Mandatory Documentation Standards
All test functions MUST adhere to the following docstring structure:
- **Rationale**: Why the test exists and what invariant it protects.
- **Process**: Step-by-step description of the execution.
- **Inputs/Expectations**: Defined contract for the test.

## 3. Running Tests
```powershell
uv run pytest
```
For coverage reports:
```powershell
uv run pytest --cov=src
```
