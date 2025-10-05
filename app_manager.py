#coding:utf8

import sys
import threading
from PySide6.QtWidgets import QApplication
from loguru import logger

from scrm_dialog import ScrmDialog


class AppManager:
    """Application Manager for Screen Capture Recorder
    
    Manages the application lifecycle, background tasks, and main dialog.
    """
    
    def __init__(self):
        self.app = None
        self.dialog = None
        self.background_thread = None
        self.shutdown_event = threading.Event()
        logger.info("AppManager initialized")
    
    def setup_application(self):
        """Initialize the QApplication"""
        self.app = QApplication(sys.argv)
        logger.info("QApplication created")
    
    def create_dialog(self):
        """Create and setup the main dialog"""
        self.dialog = ScrmDialog()
        
        # Connect close event to shutdown
        self.dialog.finished.connect(self.shutdown)
        
        logger.info("Main dialog created")
        return self.dialog
    
    def start_background_task(self):
        """Start the background monitoring task"""
        self.background_thread = threading.Thread(
            target=self._background_job, 
            args=(self.shutdown_event,),
            daemon=True
        )
        self.background_thread.start()
        logger.info("Background task started")
    
    def _background_job(self, evt: threading.Event):
        """Background job that runs periodically"""
        logger.info("Background job started")
        
        i = 0
        while not evt.wait(5.0):  # Wait 5 seconds between iterations
            i += 1
            if i > 1000:
                i = 0
            logger.debug(f"Background job running {i}")
        
        logger.info("Background job finished")
    
    def run(self):
        """Run the application"""
        if not self.app:
            raise RuntimeError("Application not setup. Call setup_application() first.")
        
        if not self.dialog:
            raise RuntimeError("Dialog not created. Call create_dialog() first.")
        
        # Start background task
        self.start_background_task()
        
        # Show dialog and run application
        self.dialog.show()
        logger.info("Application started")
        
        # Run the application event loop
        exit_code = self.app.exec()
        
        # Cleanup
        self.shutdown()
        
        return exit_code
    
    def shutdown(self):
        """Shutdown the application gracefully"""
        logger.info("Shutting down application")
        
        # Signal background thread to stop
        self.shutdown_event.set()
        
        # Wait for background thread to finish
        if self.background_thread and self.background_thread.is_alive():
            self.background_thread.join(timeout=2.0)
            logger.info("Background thread stopped")
        
        # Close dialog if still open
        if self.dialog and self.dialog.isVisible():
            self.dialog.close()
        
        logger.info("Application shutdown complete")