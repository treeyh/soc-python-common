# -*- encoding: utf-8 -*-

import os
import sys

from soc_common.utils import file_utils, sys_utils

_parent_path = ''


def pull_code():
  pass


def main():
  # rta
  # _parent_path = 'D:\\01_work\\05_rta\\01_src'
  # 国内公交
  # _parent_path = 'D:\\01_work\\06_internal_transit\\01_src'
  # tag
  # _parent_path = 'D:\\01_work\\07_creation\\01_src'
  # ITSO
  # _parent_path = 'D:\\01_work\\08_itso\\01_src'
  # dk
  _parent_path = 'D:\\01_work\\10_dk\\01_src'

  paths = file_utils.get_folder_son(_parent_path)

  print(paths)

  for path in paths:
    if not os.path.isdir(path):
      continue
    cmd = 'cd %s && git checkout master && git pull ' % path
    result, value = sys_utils.run_sys_cmd_status_output(cmd)
    print(value)
    print('%s over.' % path)


if __name__ == '__main__':
  main(path)
