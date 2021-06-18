# -*- encoding: utf-8 -*-

import logging
import logging.handlers

from soc_common.utils import str_utils


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
_default_format = logging.Formatter(
    fmt='%(asctime)s %(levelname)s [%(process)d %(threadName)s %(module)s %(funcName)s:%(lineno)d] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S')

_loggers = {}

__logger = False


def init_logging(logFile: str = './log.log', level: int = logging.INFO, formatter: str = _default_format, isAddStreamHandler: bool = True):
  global __logger
  if True == __logger:
    return
  __logger = True

  handlers = []
  if isAddStreamHandler or str_utils.is_null_or_empty(logFile):
    consoleLog = logging.StreamHandler()
    consoleLog.setFormatter(formatter)
    consoleLog.setLevel(level)
    handlers.append(consoleLog)

  if not str_utils.is_null_or_empty(logFile):
    fileLog = logging.handlers.TimedRotatingFileHandler(
        filename=logFile, when='d', interval=1, backupCount=0, encoding='utf-8', delay=False, utc=False)
    fileLog.setFormatter(formatter)
    fileLog.setLevel(level)
  logging.basicConfig(handlers=handlers, level=level, format=formatter)


def get_logger(logFile: str = './log.log', level: int = logging.INFO, formatter: str = _default_format, isAddStreamHandler: bool = True):
  global _loggers
  if None != _loggers.get(logFile, None):
    return _loggers[logFile]
  logger = logging.getLogger(logFile)
  logger.setLevel(level)
  handler = logging.handlers.TimedRotatingFileHandler(filename=logFile, when='d', interval=1, backupCount=0,
                                                      encoding='utf-8', delay=False, utc=False)
  handler.setFormatter(formatter)
  logger.addHandler(handler)

  if isAddStreamHandler:
    sh = logging.StreamHandler()
    sh.setFormatter(formatter)
    logger.addHandler(sh)

  _loggers[logFile] = logger
  return logger


if __name__ == '__main__':
  logger = get_logger()
  logger.info('asdfasdsasdf')