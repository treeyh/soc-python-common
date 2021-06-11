# -*- encoding: utf-8 -*-

import logging
import logging.handlers

_loggers = {}


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
