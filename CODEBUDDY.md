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
uv run pyinstaller main.spec

# The executable will be created in dist/main.exe
# Rename to py-scrm.exe for distribution
```

## Code Architecture

### Main Components

- **main.py**: Entry point that initializes logging and creates the application manager
- **app_manager.py**: Application lifecycle management, handles QApplication setup, background tasks, and graceful shutdown
- **scrm_dialog.py**: Custom QDialog with red border (2px, #FF0000), frameless window that stays on top
- **cfg.py**: Logging configuration module using loguru that sets up both console and rotating file logging with detailed formatting

### Application Structure

The application follows a modular architecture:
1. **GUI Layer**: Custom QDialog (ScrmDialog) with red border, no title bar, stays on top, supports mouse dragging
2. **Application Management**: AppManager handles application lifecycle, threading, and cleanup
3. **Threading**: Background thread runs periodic monitoring tasks every 5 seconds with proper event-based shutdown
4. **Logging**: Comprehensive logging using loguru to both console and rotating log files (run.log, max 20MB, 5 backups)

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
├── main.py           # Application entry point and initialization
├── app_manager.py    # Application lifecycle and background task management
├── scrm_dialog.py    # Custom red-bordered dialog (main UI)
├── cfg.py            # Logging configuration using loguru
├── main.spec         # PyInstaller specification file for building
├── pyproject.toml    # Project configuration and dependencies (pyside6, loguru)
├── README.md         # Project description (Chinese)
└── .github/workflows/package.yml  # CI/CD pipeline
```