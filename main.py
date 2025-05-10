#coding:utf8

import sys
import os

import logging

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QLabel

from cfg import cfgLogging
                                                     

def main():
    app = QApplication(sys.argv)
    label = QLabel("Hello World", alignment=Qt.Alignment.AlignCenter)
    label.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    cfgLogging()
    main()
