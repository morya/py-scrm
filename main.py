#coding:utf8

import sys
from loguru import logger

from cfg import cfgLogging
from app_manager import AppManager


def main():
    """Main entry point for the Screen Capture Recorder application"""
    # Initialize logging
    cfgLogging()
    logger.info("Starting Screen Capture Recorder application")
    
    try:
        # Create and setup application manager
        app_manager = AppManager()
        app_manager.setup_application()
        
        # Create main dialog
        dialog = app_manager.create_dialog()
        
        # Run the application
        exit_code = app_manager.run()
        
        logger.info(f"Application exited with code: {exit_code}")
        sys.exit(exit_code)
        
    except Exception as e:
        logger.error(f"Application failed to start: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
