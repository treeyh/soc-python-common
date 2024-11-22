# -*- encoding: utf-8 -*-

import sys
import os
import time

import inspect

import subprocess

import platform
from functools import wraps


# appname = 'tree'
# version = __import__('tree').__version__
# psutil_version = __import__('tree').__psutil_version

# PY3?

PY3 = sys.version_info >= (3,)
if PY3:
  xrange = range

if PY3:
  unicode_type = str
  basestring_type = str
else:
  # The names unicode and basestring don't exist in py3 so silence flake8.
  unicode_type = unicode  # noqa
  basestring_type = basestring  # noqa


# Operating system flag
# Note: Somes libs depends of OS
is_bsd = sys.platform.find('bsd') != -1
is_linux = sys.platform.startswith('linux')
is_mac = sys.platform.startswith('darwin')
is_windows = sys.platform.startswith('win')

# Path definitions
work_path = os.path.realpath(os.path.dirname(__file__))
appname_path = os.path.split(sys.argv[0])[0]
sys_prefix = os.path.realpath(os.path.dirname(appname_path))


def get_current_function_name(level=0):
  """获取当前方法名或调用链上的方法名
  Args:
      level (int): 0 表示当前方法，1 表示上一级调用方法，依次类推。
  Returns:
      str: 方法名
  """
  return inspect.stack()[level + 1].function

def add_path(path):
  '''
      将path追加入系统PATH
  '''
  sys.path.append(path)


def run_sys_cmd(cmd):
  '''
    系统命令，返回输出
    将字符串转化成命令在服务器上运行
    其返回值是指令运行后返回的状态码，0表示指令成功执行，1表示失败，256表示没有返回结果，该方法适用于系统命令不需要输出内容的场景。
  '''
  return os.system(cmd)


def run_sys_cmd_result(cmd):
  '''
      系统命令，返回输出，返回file对象，可以使用read()或readlines()读取信息
  '''
  return os.popen(cmd)


def run_sys_cmd_status_output(cmd):
  '''
      系统命令，返回输出，获得到返回值和输出，输出为(status, output)。
  '''
  result, value = subprocess.getstatusoutput(cmd)
  return (result, value)


Windows = 'Windows'
Linux = 'Linux'


def get_os_platform():
  global Windows
  global Linux
  if Windows in platform.platform():
    return Windows

  if Linux in platform.platform():
    return Linux
  return None


def get_local_ip():
  global Linux
  if Linux == get_os_platform():
    return os.popen("ifconfig | grep 'inet '|grep -v '127.0'|xargs|awk -F '[ :]' '{print($3}'").readline().rstrip()
  return None


def print(msg):
  print(msg)


# 计时器
def timer(function):
  @wraps(function)
  def function_timer(*args, **kwargs):
    t0 = time.time()
    result = function(*args, **kwargs)
    t1 = time.time()
    print("Total time running %s: %s seconds" % (function.func_name, str(t1-t0)))
    return result
  return function_timer


@timer
def my_sum(n, m):
  return sum([i for i in range(n, m)])


if __name__ == '__main__':
  # print(platform.architecture()
  # print(platform.platform()

  pass
