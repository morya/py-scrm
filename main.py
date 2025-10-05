#coding:utf8

import sys
import os
import threading
import queue

from loguru import logger
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton

from cfg import cfgLogging


def job(evt: threading.Event):
    logger.info("Thread job started")

    i = 0

    while not evt.wait(5000):
        i += 1
        if i > 1000:
            i = 0
        logger.info(f"Thread job running {i}")
    logger.info("Thread job finished")


def main():
    app = QApplication(sys.argv)

    evt = threading.Event()
    t = threading.Thread(target=job, args=(evt,)).start()
    
    win = QWidget("Title")
    win.setGeometry(100, 100, 300, 200)

    lay = QVBoxLayout()
    win.setLayout(lay)
    
    lay.addWidget(QLabel("Hello World", alignment=Qt.Alignment.AlignCenter))
    btn = QPushButton("Exit")
    btn.clicked.connect(lambda: evt.set())
    lay.addSpacing(20)
    lay.addWidget(btn, alignment=Qt.Alignment.AlignCenter)

    win.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    cfgLogging()
    main()
