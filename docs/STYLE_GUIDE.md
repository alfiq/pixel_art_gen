# PixelForge Style Guide & Standards

This document defines the absolute standards for code, documentation, and asset management within the PixelForge repository. All contributors (human or agent) must adhere to these rules.

## 1. The Zero-Emoji Policy
Non-ASCII characters, symbols, and emojis are strictly forbidden in all text-based assets including:
- Source code comments
- Markdown documentation
- Commit messages
- Configuration files (YAML, TOML)

**Rationale**: To maintain a professional, high-signal environment and ensure maximum compatibility across all terminals and editors.

## 2. Documentation Hierarchy
Every Python file MUST contain a top-level docstring with the following structure:
- **Purpose**: A concise description of the file's architectural role.
- **Dependencies**: A list of key internal and external libraries used.

Every test function MUST document:
- **Rationale**: Why the test exists.
- **Process**: How the test is performed.
- **Inputs/Expectations**: Clear definition of the test contract.

## 3. Coding Standards
### Type Hinting
Mandatory strict type hinting for all:
- Function signatures (arguments and return types).
- Class attributes.
- Complex local variables.

### Linter Compliance
No work is considered complete if `ruff check .` returns errors.

## 4. Integrity Sync
No architectural or feature change is finalized without running the **Verification Pipeline**:
```powershell
.venv\Scripts\python.exe scripts\verify_repo.py
```
This script ensures that the `ARCHITECTURE.md`, `README.md`, and code behaviors are byte-perfect in their alignment. It also enforces the **Zero-Emoji Policy**, **Docstring Standards**, and **Config Integrity**.

## 5. Forbidden Anti-Patterns
Contributors must review **[ANTI_PATTERNS.md](ANTI_PATTERNS.md)** to understand the common failures that block the CI/CD pipeline. Ignorance of these rules is not an excuse for deployment failures.

## 6. Excluded Utilities
One-off tools, "quick-fix" scripts, or maintenance utilities (like emoji strippers) must reside in the `/tools/` directory, which is excluded from Git via `.gitignore`. Core library logic must never depend on files in `/tools/`.
