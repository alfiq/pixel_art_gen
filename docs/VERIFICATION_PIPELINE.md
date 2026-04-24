# Repository Verification Pipeline

To maintain the integrity of the PixelForge Generator, every change MUST be followed by a verification pass. This ensures that the documentation remains a faithful representation of the code structure and behavior.

## Mandatory Workflow
Before finalizing any feature or bugfix, the following verification pipeline must be executed:

### 1. Automated Verification
Run the following command from the root directory:
```bash
uv run scripts/verify_repo.py
```

This script automatically validates:
- **Linting**: Code quality and style (Ruff).
- **Behavior**: Functional correctness (Pytest suite).
- **Hierarchy**: Presence of mandatory docstrings (Purpose/Dependencies).
- **Sync**: Link integrity between README.md and docs/.

### 2. Manual Verification (Artifacts & UI)
If the change affects the User Interface or the Art Algorithm:
1. Start the web server: `uv run main.py`.
2. Generate at least 5 sprites to check for visual artifacts.

## Failure Policy
If any step in the pipeline fails, the repository is considered out-of-sync. No changes should be finalized until the verification script returns a SUCCESSFUL status.

---

## Agent Mandatory Protocol (AMP-01)
To ensure long-term maintenance by AI assistants, the following protocol is enforced:

1.  **Run Pipeline**: Before reporting completion to the USER, the agent MUST execute scripts/verify_repo.py.
2.  **Self-Correction**: If the script returns any errors, the agent MUST resolve them and re-run the script until it succeeds.
3.  **Audit Trail**: The output of the verification script should be included in the agent's final progress summary to provide proof of integrity.
