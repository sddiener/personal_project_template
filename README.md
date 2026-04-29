# Personal Project Template

A minimal Python project template using `uv` for dependency management and `ruff` for code formatting and linting.

## Quickstart

### Prerequisites
- Python >= 3.14
- [`uv`](https://github.com/astral-sh/uv)

### Setup

1. **Rename the Template:**
   Before working on the code, rename the boilerplate `my_package` to your actual project name in the following places:
   - Rename the physical folder `src/my_package/`
   - In `pyproject.toml`, update `name = "personal_project_template"` under `[project]`
   - In `pyproject.toml`, update `packages = ["src/my_package"]` under `[tool.hatch.build.targets.wheel]`
   - In this `README.md`, update the `uv run python` command below to match

2. **Install Dependencies:**
   Create a virtual environment and install dependencies:
   ```bash
   uv sync
   ```

3. **Pre-commit Hooks:**
   Ensure code style consistency by setting up `pre-commit`:
   ```bash
   uv run pre-commit install
   ```

## Development

- **Running Code:**
  ```bash
  uv run python src/my_package/main.py
  ```

- **Formatting & Linting:** 
  The project is configured to use `ruff`.
  ```bash
  uv run ruff check --fix .
  uv run ruff format .
  ```

- **Testing:**
  Run tests using `pytest`:
  ```bash
  uv run pytest
  ```

## Folder Structure

- `data/`: Data files used by the application.
- `docs/`: Documentation and notes.
- `logs/`: Application logs.
- `notebooks/`: Experimental scripts and Jupyter notebooks.
- `src/`: Source code.
- `tests/`: Test scripts.
