#coding:utf8

import sys
from loguru import logger


def cfgLogging():
    # 移除默认的 handler
    logger.remove()
    
    # 添加控制台输出
    logger.add(
        sys.stderr,
        level="DEBUG",
        format="[{time:YYYY-MM-DD HH:mm:ss.SSS}] [{elapsed}] {name} pid:{process} {level} | {message}",
        colorize=True
    )
    
    # 添加文件输出，带轮转
    logger.add(
        "run.log",
        level="DEBUG",
        format="[{time:YYYY-MM-DD HH:mm:ss.SSS}] [{elapsed}] {name} pid:{process} {level} | {message}",
        rotation="20 MB",
        retention=5,
        encoding="utf-8"
    )