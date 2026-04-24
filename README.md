# PixelForge

> [!CAUTION]
> **MANDATORY PROTOCOL**: All contributors (Human or AI) MUST read **[docs/ANTI_PATTERNS.md](docs/ANTI_PATTERNS.md)** before touching code. Failure to run **`scripts/verify_repo.py`** before finalization is a breach of repository integrity and will be caught by CI/CD.

A data-free procedural generation engine for high-quality pixel art assets.

## Project Overview
This project produces high-quality, symmetrical pixel art (creatures, icons, items) using mathematical rules and artistic heuristics. For a deep dive into the system design, see the **[Architecture Documentation](docs/ARCHITECTURE.md)**.

### Core Components
- **[Generator](src/pixel_art_gen/generator.py)**: Handles symmetry-masked grid generation.
- **[Palette](src/pixel_art_gen/palette.py)**: Dynamic hue-shifting color theory.
- **[Renderer](src/pixel_art_gen/renderer.py)**: Converts grids to shaded PNGs with outlines.
- [Web Dashboard](main.py): A premium FastAPI interface for real-time asset evolution.

## Mandatory Verification Workflow
To ensure that code, docs, and behavior remain in sync, all developers must run the **[Verification Pipeline](docs/VERIFICATION_PIPELINE.md)** before finalizing changes.
```powershell
.venv\Scripts\python.exe scripts\verify_repo.py
```

## Setup and Environment

### Prerequisites
- **Python 3.12+**
- **uv** (recommended for dependency management)

### Local Development
1. Clone the repository.
2. Initialize the environment: `uv sync`.
3. Run the dashboard: `uv run main.py`.
4. Run tests: `uv run pytest`.

## Coding Standards
- **Type Hinting**: Mandatory for all function signatures.
- **Documentation**: All files must have Purpose/Dependencies docstrings.
- **Linting**: Strict adherence to Ruff standards.

### Enforcement

CAUTION: MANDATORY AGENT PROTOCOL: AI Agents and developers MUST NOT finalize any task or declare a feature complete without a SUCCESSFUL execution of the repository verification script. This script is the ultimate Source of Truth for repository integrity, documentation sync, and behavioral correctness. Failure to run this script before termination is considered a breach of project policy.

- **Linting**: We use ruff (via the verification script) to enforce strict style and documentation standards.
- **Style Rules**: All contributions must adhere to the **[Official Style Guide](docs/STYLE_GUIDE.md)**.
- **Hierarchical Exploration**: Documentation must be explored and maintained recursively as defined in docs/ARCHITECTURE.md.
