# PixelForge Anti-Patterns: The Wall of Forbidden Errors

This document serves as a mandatory guide for all contributors (human or autonomous) to prevent the recurrence of critical repository failures discovered during the project's hardening phase.

## 1. The Carbon-Copy Sync Rule
> **Mistake**: `docs/index.md` and `README.md` drifting apart.
> **Enforcement**: `scripts/verify_repo.py` performs a byte-by-byte comparison.
> **Fix**: Always copy `README.md` to `docs/index.md` after changes.

## 2. The Ghost Config Syndrome
> **Mistake**: An empty or missing `pyproject.toml`.
> **Enforcement**: The verification script checks for the existence and basic schema of the project file.
> **Fix**: Use `uv init` or maintain the `[project]` section with all dependencies properly versioned.

## 3. The Shadow Tool Leak
> **Mistake**: Typos in `.gitignore` (e.g., `t o o l s /`) allowing maintenance scripts into version control.
> **Enforcement**: Manual review and automated `.gitignore` presence check for the `tools/` entry.
> **Fix**: Verify `.gitignore` syntax after every modification.

## 4. The "Trust Me" Documentation Gap
> **Mistake**: Adding functions or methods without `Args:` and `Returns:` documentation.
> **Enforcement**: Enhanced docstring parser in `verify_repo.py` and Ruff `D100/D101/D102/D103` rules.
> **Fix**: Every method, including `__init__`, must document its signature and return type.

## 5. Non-ASCII Character Contamination
> **Mistake**: Including curly quotes " ", emojis, or other non-ASCII symbols in text assets.
> **Enforcement**: `scripts/verify_repo.py` ASCII-only validation across the entire tree.
> **Fix**: Use standard ASCII characters only. Use tools to strip non-ASCII if needed.

## 6. Placeholder Navigation
> **Mistake**: Adding files to `mkdocs.yml` that are empty or contain only boilerplate.
> **Enforcement**: Verification script now flags files with 0 or near-zero byte counts that are referenced in documentation.
> **Fix**: Fill all documentation files before declaring a task complete.

---
**FAILURE TO ADHERE TO THESE GUIDELINES WILL RESULT IN A BLOCKED CI/CD PIPELINE.**
