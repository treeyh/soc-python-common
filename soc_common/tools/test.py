# -*- encoding: utf-8 -*-

import os
import sys
import json

from soc_common.utils import file_utils, str_utils, mysql_utils


def format_langs():
  langMap = {

      'tool.calcDogAge.dogAge': 'Dog age',
      'tool.calcDogAge.dogModel': 'Dog type',
      'tool.calcDogAge.age': 'age',
      'tool.calcDogAge.month': 'month',
      'tool.calcDogAge.humanAge': 'Human age',

      'tool.calcCatAge.catAge': 'Cat age',

  }

  content = ''
  for k, v in langMap.items():
    ks = k.split('.')
    key = ks[0] + ''.join([str_utils.upperFirstWord(i) for i in ks[1:]])
    content += '  static String get %s =>\'%s\'.tr;\n' % (key, k)
  print(content)


def load_user_id():

  lines = file_utils.read_all_lines_file('D:\\app_account_v2-account_id-20230315.txt')
  work_ids = {}
  data_center_ids = {}
  for l in lines:
    b2 = bin(int(l.strip()))
    # print(len(b2))
    # print(b2)
    seq = b2[-12:]
    # print(seq)
    work_id = b2[-17:-12]
    if None == work_ids.get(work_id, None):
      print(work_id)
      print(int(work_id, 2))
      work_ids[work_id] = 1
    data_center_id = b2[-22:-17]
    if None == data_center_ids.get(data_center_id, None):
      # print(data_center_id)
      # print(data_center_id, 2)
      data_center_ids[data_center_id] = 1
  pass


def run():
  # export_permission()
  # print('\n' * 3)
  # export_role()
  # print('\n' * 3)
  # export_role_permission()

  format_langs()
  # load_user_id()


if __name__ == '__main__':
  run()
