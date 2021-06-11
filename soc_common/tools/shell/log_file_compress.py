# -*- encoding: utf-8 -*-


import os
import sys

from datetime import date, datetime, timedelta
import time

from utils import log_utils


def get_logger():
  global _log_path, _logger, _log_file_name

  if _logger is not None:
    return _logger
  _logger = log_utils.get_logger(os.path.join(_log_path, _log_file_name))
  return _logger


def add_datetime_by_datetime(dt=datetime.now(), days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0,
                             weeks=0):
  return dt + timedelta(days=days, seconds=seconds, microseconds=microseconds,
                        milliseconds=milliseconds, minutes=minutes, hours=hours, weeks=weeks)


def get_add_date(days):
  ''' 获取隔当前日期几天的日期 '''
  return add_datetime_by_datetime(days=days).strftime('%Y%m%d')


def run_cmd(cmd):
  ''' 执行系统命令返回输出 '''
  results = os.popen(cmd).readlines()
  return results


def compress_log_file(path, fileName, date):

  filePath = os.path.join(path, fileName+'.'+date)

  if not os.path.isfile(filePath):
    # get_logger().info('filePath: %s now exist.' % filePath )
    return

  cmd = 'cd %(path)s && gzip %(file)s.%(date)s' % {'path': path, 'file': fileName, 'date': date}
  get_logger().info('cmd : %s' % cmd)
  run_cmd(cmd)
  time.sleep(0.1)


def remove_log_file(path, fileName, date):
  filePath = os.path.join(path, fileName + '.' + date)

  if os.path.isfile(filePath):
    cmd = 'cd %(path)s && rm %(file)s.%(date)s' % {'path': path, 'file': fileName, 'date': date}
    run_cmd(cmd)
    time.sleep(0.1)

  filePath = os.path.join(path, fileName + '.' + date + '.gz')

  if os.path.isfile(filePath):
    cmd = 'cd %(path)s && rm %(file)s.%(date)s.gz' % {'path': path, 'file': fileName, 'date': date}
    run_cmd(cmd)
    time.sleep(0.1)


def run_log_file(logInfo):
  ''' 压缩日志文件 '''

  for fileName in logInfo['fileNames']:
    # 压缩日志
    for i in range(1, logInfo['saveMaxCount'] + 1):
      date = get_add_date(-1 * i)
      get_logger().info('compress date: %s, path: %s, file: %s' % (date, logInfo['path'], fileName))

      compress_log_file(logInfo['path'], fileName, date)

    # 删除旧文件
    for i in range(logInfo['saveMaxCount'] + 1, (logInfo['saveMaxCount'] + 1) * 2):
      date = get_add_date(-1 * i)
      get_logger().info('remove date: %s, path: %s, file: %s' % (date, logInfo['path'], fileName))

      remove_log_file(logInfo['path'], fileName, date)


def run():
  global _log_infos

  get_logger().info(' compress log file start ....')

  for logInfo in _log_infos:
    run_log_file(logInfo)

  get_logger().info(' compress log file end.')


# 日志文件路径
_log_path = '/data0/script/log-file-compress/log'
_log_file_name = 'run.log'

_logger = None


# 日志根路径
_log_base_path = '/data0/logs/logpath'
# 需压缩日志配置
_log_infos = [
    {
        'path': os.path.join(_log_base_path, 'default'),
        'fileNames': ['common-default.log'],
        'saveMaxCount': 90,
    },
    {
        'path': os.path.join(_log_base_path, 'error'),
        'fileNames': ['common-error.log', 'common-mq-send-fail.log'],
        'saveMaxCount': 90,
    },
    {
        'path': os.path.join(_log_base_path, 'rr'),
        'fileNames': ['request-response.log'],
        'saveMaxCount': 90,
    }
]


if __name__ == '__main__':
  run()
