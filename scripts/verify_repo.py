"""Repository Integrity & Verification Script.

Purpose:
    Ultimate **Source of Truth** for the Pixel Forge Generator. This script
    guarantees that code, documentation, and the architectural model are 
    perfectly in sync and follow the mandatory repository policies.

Role:
    All development agents and contributors are FORCED by policy to use 
    this script as a final gatekeeper before finishing any task.

Dependencies:
    - os
    - subprocess
    - sys
"""

import os
import subprocess
import sys

def run_command(cmd: str) -> bool:
    """Runs a shell command and returns success."""
    print(f"Executing: {cmd}")
    result = subprocess.run(cmd, shell=True)
    return result.returncode == 0

def check_ascii_only(filepath: str) -> bool:
    """Checks if a file contains only ASCII characters (Zero-Emoji Policy)."""
    with open(filepath, 'rb') as f:
        content = f.read()
        try:
            content.decode('ascii')
            return True
        except UnicodeDecodeError:
            return False

def check_docstring_header(filepath: str) -> bool:
    """Checks if a file contains the mandatory Purpose/Dependencies headers."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        has_purpose = "Purpose:" in content
        has_deps = "Dependencies:" in content
        return has_purpose and has_deps

def check_docstring_sections(filepath: str) -> bool:
    """Checks if a file's functions/classes contain Args: and Returns: headers.
    
    This is only applied to core library files in src/.
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        # Very simple heuristic: check if at least one Args: and Returns: section exists
        # in files that define classes or functions.
        if "class " in content or "def " in content:
            # We allow skips for some files if needed, but not core src
            has_args = "Args:" in content
            has_returns = "Returns:" in content
            return has_args and has_returns
        return True

def main() -> None:
    """Performs full repo verification."""
    errors = []

    print("--- 1. Static Analysis (Ruff) ---")
    if not run_command(f"{sys.executable} -m ruff check ."):
        errors.append("Linter (Ruff) failed.")

    print("\n--- 2. Behavioral Tests (Pytest) ---")
    if not run_command(f"{sys.executable} -m pytest"):
        errors.append("Tests (Pytest) failed.")

    print("\n--- 3. Project Configuration Integrity ---")
    if not os.path.exists("pyproject.toml"):
        errors.append("Missing pyproject.toml")
    else:
        if os.path.getsize("pyproject.toml") < 100:
            errors.append("pyproject.toml is suspicious (too small/empty)")

    print("\n--- 4. Zero-Emoji / Non-ASCII Policy ---")
    text_extensions = {".py", ".md", ".txt", ".yml", ".yaml", ".toml", "LICENSE"}
    for root, _, files in os.walk("."):
        if ".git" in root or ".venv" in root or "__pycache__" in root:
            continue
        for f in files:
            ext = os.path.splitext(f)[1]
            if ext in text_extensions or f == "LICENSE":
                fpath = os.path.join(root, f)
                if not check_ascii_only(fpath):
                    errors.append(f"Non-ASCII characters found in: {fpath}")

    print("\n--- 5. Documentation Integrity ---")
    py_files = []
    for root, _, files in os.walk("src"):
        for f in files:
            if f.endswith(".py") and not f.startswith("__"):
                py_files.append(os.path.join(root, f))
    
    for pf in py_files:
        if not check_docstring_header(pf):
            errors.append(f"Documentation missing Purpose/Dependencies in: {pf}")
        
        if not check_docstring_sections(pf):
            errors.append(f"Documentation missing Args/Returns sections in: {pf}")

    print("\n--- 6. Architectural & Navigation Sync ---")
    if not os.path.exists("docs/ARCHITECTURE.md"):
        errors.append("Missing docs/ARCHITECTURE.md")
    
    if os.path.exists("README.md"):
        with open("README.md", "r", encoding='utf-8') as f:
            readme_content = f.read()
            if "ARCHITECTURE.md" not in readme_content:
                errors.append("README.md does not link to ARCHITECTURE.md")
            
            if os.path.exists("docs/index.md"):
                with open("docs/index.md", "r", encoding='utf-8') as f_idx:
                    if f_idx.read() != readme_content:
                        err = "docs/index.md is out of sync with README.md"
                        errors.append(err)

    # MkDocs Navigation and Empty File Check
    if os.path.exists("mkdocs.yml"):
        with open("mkdocs.yml", "r", encoding='utf-8') as f:
            mkdocs_content = f.read()
            for pf in py_files:
                basename = os.path.basename(pf).replace(".py", "")
                md_path = f"docs/api/{basename}.md"
                if not os.path.exists(md_path):
                    errors.append(f"Missing API doc file: {md_path}")
                elif os.path.getsize(md_path) < 10:
                    errors.append(f"API doc file is empty: {md_path}")
                
                if f"{basename}.md" not in mkdocs_content:
                    err = f"API doc {basename}.md is not in mkdocs.yml navigation"
                    errors.append(err)

    print("\n" + "="*30)
    if errors:
        print("VERIFICATION FAILED")
        for err in errors:
            print(f" ERROR: {err}")
        sys.exit(1)
    else:
        msg = "VERIFICATION SUCCESSFUL: Repo and Docs are in sync."
        print(msg)
        sys.exit(0)

if __name__ == "__main__":
    main()
