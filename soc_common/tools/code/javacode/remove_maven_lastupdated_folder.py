# -*- encoding: utf-8 -*-

from soc_common.utils import str_utils, file_utils, mail_utils, date_utils, log_utils
import os
import sys
import time

import sys
import re


path = os.path.split(os.path.realpath(__file__))[0]
sys.path.append(path + os.sep + '..')


_maven_path = '/Users/tree/.m2/repository'


def run():
  global _maven_path

  paths = file_utils.walk2(_maven_path)

  for p in paths:
    folder = p[0]
    filename = p[1]
    if '.lastUpdated' in filename and os.path.exists(folder):
      print('remove:' + folder)
      file_utils.remove_folder(folder)


def run_dns_error():
  global _maven_path

  paths = file_utils.walk2(_maven_path)

  for p in paths:
    path = os.path.join(p[0], p[1])

    if os.path.exists(path) and 1024 < file_utils.get_filesize(path):
      continue

    content = file_utils.read_all_file(path)
    if None == content:
      print('None:' + path)
      continue
    if 'DNS解析失败' in content or 'text/javascript' in content:
      print('removefile:' + p[0])
      print('remove:' + p[0])
      file_utils.remove_folder(p[0])


if __name__ == '__main__':
  run()
  run_dns_error()
