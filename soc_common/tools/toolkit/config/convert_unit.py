# -*- encoding: utf-8 -*-


import os
import sys
import time

import json
from soc_common.utils import file_utils, excel_utils, str_utils


_excel_file = 'D:\\data\\note\\知识记录\\10_项目资料\\toolkit\\单位.xlsx'
_config_file = 'D:\\convert_tool.json'
_config_map_file = 'D:\\convert_config.json'
_config_item_column = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                       'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T']


def load_type_info(ws):
  """获取配置类型信息

  Args:
      ws ([type]): [description]

  Returns:
      [type]: [description]
  """
  b1 = ws['B1'].value
  if str_utils.is_null_or_empty(b1):
    return None

  info = {
      'namezh': ws['B1'].value,
      'nameen': ws['B2'].value,
      'code': ws['B3'].value,
      'sourceId': ws['B4'].value,
      'targetId': ws['B5'].value,
      'baselineId': ws['B6'].value,
  }
  return info


def load_config_item_title(ws):
  """加载配置title

  Args:
      ws ([type]): [description]

  Returns:
      [type]: [description]
  """
  titleList = []
  for c in _config_item_column:
    title = ws[c+'15'].value
    if str_utils.is_null_or_empty(title):
      return titleList
    titleList.append(title)


def load_config_item_info(ws, titleList):
  """加载配置项目信息

  Args:
      ws ([type]): [description]
      titleList ([type]): [description]

  Returns:
      [type]: [description]
  """
  items = []

  if len(titleList) <= 0:
    return items

  overFlag = False
  for i in range(16, 500):
    index = 0
    info = {}
    for c in _config_item_column:
      if index >= len(titleList):
        break
      key = c+str(i)
      val = ws[key].value
      if str_utils.is_null_or_empty(val) and index == 0:
        overFlag = True
        break
      if titleList[index] == 'code' and val == None:
        val = ''
      info[titleList[index]] = val
      index += 1
    if overFlag:
      break
    items.append(info)
  return items


def build_config():
  global _excel_file, _config_file, _config_map_file

  wb = excel_utils.open_excel(_excel_file)
  sheetnames = wb.get_sheet_names()

  configList = []
  configMap = {}
  configListObj = {}

  for name in sheetnames:
    ws = wb.get_sheet_by_name(name)
    info = load_type_info(ws)
    titleList = load_config_item_title(ws)
    items = load_config_item_info(ws, titleList)

    if len(items) > 0:
      info['items'] = items
      configList.append(info)
      configMap[info['code']] = info

  configListObj['version'] = int(time.time())
  configListObj['items'] = configList
  file_utils.write_file(_config_file, json.dumps(configListObj, ensure_ascii=False))
  file_utils.write_file(_config_map_file, json.dumps(configMap, ensure_ascii=False))

  return configList
