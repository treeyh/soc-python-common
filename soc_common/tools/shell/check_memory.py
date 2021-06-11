# -*- encoding: utf-8 -*-


import os
import sys

import time

from utils import log_utils


def get_logger():
  global _log_path, _logger, _log_file_name

  if _logger is not None:
    return _logger
  _logger = log_utils.get_logger(os.path.join(_log_path, _log_file_name))
  return _logger


def get_process_memory(processName):
  ''' 获取进程内存 '''
  cmd = 'pgrep -f %s' % (processName)
  pids = os.popen(cmd).readlines()
  for pid in pids:
    l = pid.strip()
    if l is None or l == '':
      return None
    return int(l)


def get_os_memory():
  ''' 获取系统内存 '''
  cmd = 'free '
  memorys = os.popen(cmd).readlines()
  i = 0
  mem = {
      'mem': {},
      'swap': {}
  }
  for memory in memorys:
    if 0 == i:
      i = + 1
      continue
    ms = memory.strip().split()
    if len(ms) < 2:
      continue
    if 'mem' in ms[0].lower():
      mem['mem'] = {
          'total': int(ms[1]),
          'used': int(ms[2]),
          'free': int(ms[3]),
          'shared': int(ms[4]),
          'buff': int(ms[5]),
          'available': int(ms[6]),
      }
      continue
    if 'swap' in ms[0].lower():
      mem['swap'] = {
          'total': int(ms[1]),
          'used': int(ms[2]),
          'free': int(ms[3]),
      }
  return mem


def run_cmd(cmd):
  ''' 执行系统命令返回输出 '''
  results = os.popen(cmd).readlines()
  return results


def get_os_memory_ratio():
  ''' 获得系统可用内存比例 '''
  mem = get_os_memory()
  if len(mem['mem'].keys()) < 2:
    return None

  total = mem['mem'].get('total', 0)
  if total <= 0:
    return None
  active_mem = mem['mem'].get('used', 0) - mem['mem'].get('buff', 0)
  ratio = active_mem / total
  return ratio


def save_java_process_status():
  global _os_memory_ratio, _process_name, _log_path

  # 获取应用进程PID
  pid = get_process_memory(_process_name)
  if pid is None or pid <= 1:
    return

  ti = str(time.time())

  dumpCmd = 'jmap -dump:live,format=b,file=%s %s' % (
      os.path.join(_log_path, 'jmap_' + ti + '.bin'), str(pid))
  get_logger().info(dumpCmd)
  run_cmd(dumpCmd)

  stactCmd = 'jstack  %s > %s' % (str(pid), str(os.path.join(_log_path, 'jstack_' + ti + '.log')))
  get_logger().info(stactCmd)
  run_cmd(stactCmd)


def check_memory():
  global _os_memory_ratio, _process_name, _log_path
  ratio = get_os_memory_ratio()

  get_logger().info('now memory ratio: %s' % (str(ratio)))

  if ratio is None or ratio < _os_memory_ratio:
    return False

  # 获取内存占用前三的进程
  cmd = 'ps -aux | sort -k4nr | head -3'
  results = run_cmd(cmd)
  for r in results:
    get_logger().info('process memory top: %s' % (r))

  return True


def run():
  global _time_interval
  get_logger().info('check_memory start...')

  save_time = 0

  while(True):
    if not check_memory():
      time.sleep(65)
      continue
    now_time = time.time()
    if (save_time + _time_interval) < now_time:
      save_time = now_time
      save_java_process_status()


# 日志文件路径
_log_path = '/data0/script/check-memory/logs'
_log_file_name = 'run.log'

_logger = None
# 内存占用比例
_os_memory_ratio = 0.8
# 进程名
_process_name = 'process-name'

# 每次dump时间间隔
_time_interval = 60 * 60 * 24


if __name__ == '__main__':
  run()
