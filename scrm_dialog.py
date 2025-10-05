#coding:utf8

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QDialog
from PySide6.QtGui import QPainter, QPen
from loguru import logger


class ScrmDialog(QDialog):
    """Screen Capture Recorder Main Dialog
    
    A red-bordered dialog that stays on top without standard title bar.
    """
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setup_ui()
        logger.info("ScrmDialog initialized")
    
    def setup_ui(self):
        """Setup the dialog UI properties"""
        # Remove standard title bar and set window flags
        self.setWindowFlags(
            Qt.WindowType.Dialog |
            Qt.WindowType.FramelessWindowHint |
            Qt.WindowType.WindowStaysOnTopHint
        )
        
        # Set dialog size and position
        self.setGeometry(100, 100, 300, 200)
        
        # Set transparent background so we can draw custom border
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        
        logger.info("ScrmDialog UI setup completed")
    
    def paintEvent(self, event):
        """Custom paint event to draw red border"""
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        
        # Create red pen with 2 pixel width
        pen = QPen()
        pen.setColor(Qt.GlobalColor.red)  # #FF0000
        pen.setWidth(2)
        painter.setPen(pen)
        
        # Draw border rectangle
        rect = self.rect()
        # Adjust rect to account for pen width
        rect.adjust(1, 1, -1, -1)
        painter.drawRect(rect)
        
        super().paintEvent(event)
    
    def mousePressEvent(self, event):
        """Handle mouse press for window dragging"""
        if event.button() == Qt.MouseButton.LeftButton:
            self.drag_start_position = event.globalPosition().toPoint()
    
    def mouseMoveEvent(self, event):
        """Handle mouse move for window dragging"""
        if hasattr(self, 'drag_start_position') and event.buttons() == Qt.MouseButton.LeftButton:
            self.move(self.pos() + event.globalPosition().toPoint() - self.drag_start_position)
            self.drag_start_position = event.globalPosition().toPoint()