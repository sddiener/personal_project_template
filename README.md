# Personal Project Template

A minimal Python project template using `uv` for dependency management and `ruff` for code formatting and linting.

## Quickstart

### Prerequisites
- Python >= 3.11
- [`uv`](https://github.com/astral-sh/uv)

### Setup

1. **Install Dependencies:**
   Create a virtual environment and install dependencies:
   ```bash
   uv sync
   ```

2. **Pre-commit Hooks:**
   Ensure code style consistency by setting up `pre-commit`:
   ```bash
   uv run pre-commit install
   ```

## Development

- **Running Code:**
  ```bash
  uv run python src/main.py
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
