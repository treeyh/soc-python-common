# -*- encoding: utf-8 -*-

import os
import logging
import json
import sys
import logging.handlers

from loguru import logger

from soc_common.config import config
from soc_common.utils import file_utils


############################
# %(levelno)s	打印日志级别的数值
# %(levelname)s	打印日志级别名称
# %(pathname)s	打印当前执行程序的路径
# %(filename)s	打印当前执行程序名称
# %(funcName)s	打印日志的当前函数
# %(lineno)d	打印日志的当前行号
# %(asctime)s	打印日志的时间
# %(thread)d	打印线程 id
# %(threadName)s	打印线程名称
# %(process)d	打印进程 ID
# %(message)s	打印日志信息
############################
# _default_format = logging.Formatter(
#     fmt='%(asctime)s - %(levelname)s - [%(process)d %(threadName)s %(module)s %(filename)s %(funcName)s:%(lineno)d] - %(message)s',
#     datefmt='%Y-%m-%d %H:%M:%S')
__default_format = '%(asctime)s - %(levelname)s - [%(process)d %(threadName)s %(module)s %(filename)s %(funcName)s:%(lineno)d] - %(message)s'

_loggers = {}

__logger = False

__default_logger = None

__folder_path = ''

# https://github.com/Delgan/loguru
# https://www.cnblogs.com/struggleMan/p/17510494.html
__default_format1 = '{time} - {level} - {message}'



def init(path: str, level: int = logging.INFO):
  global __logger, __folder_path, __default_format, __default_logger

  if True == __logger:
    return
  __logger = True

  consoleLog = logging.StreamHandler()
  consoleLog.setLevel(level)
  logging.basicConfig(handlers=[consoleLog], level=level, format=__default_format)

  if path != None and path != '':
    __folder_path = os.path.dirname(path)
    if not file_utils.exists_file(__folder_path):
      file_utils.make_folders(__folder_path)

    logger = logging.getLogger(path)
    logger.setLevel(level)
    handler = logging.handlers.TimedRotatingFileHandler(filename=path, when='d', interval=1, backupCount=0,
                                                        encoding='utf-8', delay=False, utc=False)
    handler.setFormatter(logging.Formatter(__default_format))
    logger.addHandler(handler)
    _loggers[os.path.basename(path)] = logger
    __default_logger = logger


def get_logger(logFile: str = '', level: int = logging.INFO, formatter: str = __default_format):
  global _loggers, __folder_path
  if '' == logFile:
    return __default_logger
  if None != _loggers.get(logFile, None):
    return _loggers[logFile]
  log_path = os.path.join(__folder_path, logFile)
  logger = logging.getLogger(log_path)
  logger.setLevel(level)
  handler = logging.handlers.TimedRotatingFileHandler(filename=log_path, when='d', interval=1, backupCount=0,
                                                      encoding='utf-8', delay=False, utc=False)
  handler.setFormatter(logging.Formatter(formatter))
  logger.addHandler(handler)

  _loggers[logFile] = logger
  return logger





log = None


# <cyan>{module}</cyan>:
LOG_STD_FORMAT = '<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>'
LOG_FILE_FORMAT = '{time:YYYY-MM-DD HH:mm:ss.SSS} - {level} - {name}:{function}:{line} - {message}'


# 定义 JSON 格式的日志
def log_json_format(record):
  return json.dumps({
      "time": record["time"].strftime("%Y-%m-%dT%H:%M:%S.%f%Z"),
      "pid": record["process"].id,
      "file": record["file"].name,
      "thread": record["thread"].id,
      "class": record["name"],
      "line": record["line"],
      "level": record["level"].name,
      "log": record["message"]
  })

def log_formatter(record):
    # Note this function returns the string to be formatted, not the actual message to be logged
    record["extra"]["serialized"] = log_json_format(record)
    return "{extra[serialized]}\n"

def init_log():
  global log
  # 日志配置
  LOG_CONFIG = {
      "handlers": [
          {"sink": sys.stdout, "level": "INFO", "format": LOG_STD_FORMAT},
          # LOG_FILE_FORMAT   "serialize": True, 
          {"sink": config.LogPath, "level": "INFO", "format": log_formatter, "rotation": "1 hour", "retention": "3 day"},
      ],
  }
  logger.configure(**LOG_CONFIG)
  log = logger



if __name__ == '__main__':
  logger = get_logger()
  logger.info('asdfasdsasdf')
