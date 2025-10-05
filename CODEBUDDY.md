# CODEBUDDY.md

This file contains essential information for Terminal Assistant Agent instances working in this repository.

## Project Overview

This is a Python GUI application that manages screen-capture-recorder registry information. The project uses PySide6 for the GUI framework, loguru for logging, uv for dependency management, and is designed to be packaged as a Windows executable.

## Development Commands

### Dependencies
```bash
# Install uv (if not already installed)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install all dependencies (including dev dependencies like pyinstaller)
uv sync --group dev

# Install only production dependencies
uv sync
```

### Running the Application
```bash
# Run the main application
uv run python main.py

# Or activate the virtual environment and run directly
uv shell
python main.py
```

### Building
```bash
# Build Windows executable (as done in CI)
uv run pyinstaller --onefile --noconsole main.py

# The executable will be created in dist/main.exe
# Rename to py-scrm.exe for distribution
```

## Code Architecture

### Main Components

- **main.py**: Entry point containing the PySide6 GUI application with a simple window layout, background threading for periodic tasks, and application lifecycle management
- **cfg.py**: Logging configuration module using loguru that sets up both console and rotating file logging with detailed formatting

### Application Structure

The application follows a simple architecture:
1. **GUI Layer**: PySide6-based window with basic layout (QVBoxLayout, QLabel, QPushButton)
2. **Threading**: Background thread runs periodic tasks every 5 seconds with proper event-based shutdown
3. **Logging**: Comprehensive logging using loguru to both console and rotating log files (run.log, max 20MB, 5 backups)

### Key Patterns

- Uses threading.Event for clean thread shutdown coordination
- Logging configuration using loguru is centralized in cfg.py and initialized before main application
- GUI uses lambda functions for event handling
- Application designed for Windows deployment (GitHub Actions uses windows-2022)
- Uses uv for fast and reliable dependency management

## Deployment

The project uses GitHub Actions for automated building on Windows. The workflow:
1. Installs uv package manager
2. Sets up Python 3.10 using uv
3. Installs dependencies using uv sync --dev
4. Uses PyInstaller via uv run to create a single executable
5. Outputs py-scrm.exe as the final artifact

## File Structure

```
/
├── main.py           # Main GUI application entry point
├── cfg.py            # Logging configuration
├── pyproject.toml    # Project configuration and dependencies (pyside6, loguru)
├── README.md         # Project description (Chinese)
└── .github/workflows/package.yml  # CI/CD pipeline
```