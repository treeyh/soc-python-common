# -*- encoding: utf-8 -*-


import os
import sys
import time

import json
from soc_common.utils import file_utils, excel_utils, str_utils


# _excel_file = 'd:\\data\\note\\notes\\知识记录\\10_项目资料\\toolkit\\货币.xlsx'
# _excel_file = 'd:\\data\\note\\notes\\知识记录\\10_项目资料\\toolkit\\单位.xlsx'
_excel_file = 'd:\\data\\note\\notes\\知识记录\\10_项目资料\\toolkit\\单位.xlsx'
_config_zh_file = 'D:\\convert_tool_zh.json'
_config_en_file = 'D:\\convert_tool_en.json'
_config_map_file = 'D:\\convert_config.json'
_config_item_column = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                       'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T']


def load_type_info(ws, lang='zh'):
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
      'name': str(ws['B1'].value) if 'zh' == lang else str(ws['B2'].value),
      'code': str(ws['B3'].value),
      'source': str(ws['B4'].value),
      'target': str(ws['B5'].value),
      'baseline': str(ws['B6'].value),
      'ratioFlag': int(ws['B7'].value),
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


def load_config_item_info(ws, titleList, lang='zh'):
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
    index = -1
    info = {}
    for c in _config_item_column:
      index += 1
      if index >= len(titleList):
        break
      key = c+str(i)
      val = ws[key].value
      if str_utils.is_null_or_empty(val) and index == 0:
        overFlag = True
        break

      if titleList[index] == 'namezh':
        if lang == 'zh':
          info['name'] = val
        continue
      if titleList[index] == 'nameen':
        if lang == 'en':
          info['name'] = val
        continue

      if titleList[index] == 'typezh':
        if lang == 'zh':
          info['type'] = val
        continue
      if titleList[index] == 'typeen':
        if lang == 'en':
          info['type'] = val
        continue

      if titleList[index] == 'unit' and val == None:
        val = ''
      if titleList[index] == 'code':
        val = str(val)

      info[titleList[index]] = val
    if overFlag:
      break
    items.append(info)
  return items


def build_config():
  global _excel_file, _config_zh_file, _config_en_file, _config_map_file

  wb = excel_utils.open_excel(_excel_file)
  sheetnames = wb.get_sheet_names()

  configZhList = []
  configEnList = []
  configMap = {}
  configZhListObj = {}
  configEnListObj = {}

  for name in sheetnames:
    ws = wb.get_sheet_by_name(name)
    info = load_type_info(ws, 'zh')
    info2 = load_type_info(ws, 'en')
    titleList = load_config_item_title(ws)
    items = load_config_item_info(ws, titleList, 'zh')
    items2 = load_config_item_info(ws, titleList, 'en')

    if len(items) > 0:
      info['items'] = items
      info2['items'] = items2
      configZhList.append(info)
      configEnList.append(info2)
      configMap[info['code']] = info

  configZhListObj['version'] = int(time.time())
  configZhListObj['default'] = configZhList[0]['code']
  configZhListObj['items'] = configZhList

  configEnListObj['version'] = int(time.time())
  configEnListObj['default'] = configEnList[0]['code']
  configEnListObj['items'] = configEnList

  file_utils.write_file(_config_zh_file, json.dumps(configZhListObj, ensure_ascii=False))
  file_utils.write_file(_config_en_file, json.dumps(configEnListObj, ensure_ascii=False))
  file_utils.write_file(_config_map_file, json.dumps(configMap, ensure_ascii=False))

  return configZhList
