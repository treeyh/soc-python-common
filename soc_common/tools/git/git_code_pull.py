# -*- encoding: utf-8 -*-

import os
import sys

_target_path = '/Users/tree/work/06_wd/07_src'

_max_length = 3


def get_folder_son(path):
  '''
      列举path下一层的所有文件、文件夹
  '''
  paths = os.listdir(path)
  pps = []
  for s in paths:
    p = '%s%s%s' % (path, os.sep, s)
    pps.append(p)
  return pps


def pull_code():
  global _target_path

  paths = get_folder_son(_target_path)

  print(paths)

  for path in paths:
    pull_code_by_path(path, 1)


def pull_code_by_path(path, length):
  global _max_length

  if(_max_length < length):
    return
  if os.path.isfile(path):
    return

  paths = get_folder_son(path)

  gitType = False
  for p in paths:
    if os.path.isfile(p):
      continue
    if '.git' == os.path.basename(p):
      gitType = True
      break
  if gitType == True:
    cmd = '''
                cd %s
                git pull origin
                ''' % (path)
    result = os.popen(cmd).readlines()
    print(path)
    return

  for p in paths:
    pull_code_by_path(p, length + 1)


if __name__ == '__main__':
  pull_code()
