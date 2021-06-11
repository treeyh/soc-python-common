# -*- encoding: utf-8 -*-

import os


base_git = 'git@gitlab.snowballtech.com:fp/android-transit-job.git'


def run_sys_cmd_result(cmd):
  '''
      系统命令，返回输出，返回file对象，可以使用read()或readlines()读取信息
  '''
  return os.popen(cmd)


def run():
  pass


if __name__ == "__main__":
  run()
