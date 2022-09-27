# -*- encoding: utf-8 -*-

import os
import json
import traceback

ts = {}


def read_line_file(filePath, method='r', callBack=None, encoding='utf-8'):
  '''
      读取所有文件，一次性读取所有内容， 文件不存在返回None
      filePath：文件路径
      method：读取方式，'r'读取，'rb' 二进制方式读取
      callBack：每行读取的回调函数，有两个传入参数，行索引和行内容
  '''
  if callBack == None:
    return
  fh = open(filePath, method, encoding=encoding)
  try:
    limit = 100000
    lineIndex = 0
    while True:
      lines = fh.readlines(limit)
      if not lines:
        break
      for line in lines:
        callBack(lineIndex, line)
        lineIndex += 1
  finally:
    fh.close()


def write_file(filePath, content, method='w', encoding='utf-8'):
  '''
      写文件
      filePath：文件路径
      content：文件内容
      method：写入方式，'w'覆盖写，'a' 续写，'wb' 二进制覆盖写
  '''
  fh = open(filePath, method, encoding=encoding)

  try:
    fh.write(content)
  except:
    print(traceback.format_exc())
  finally:
    fh.close()


def line_fenxi(lineIndex, line):
  global ts
  print(lineIndex)
  l = line.strip()
  if l == '' or '2022-09-24T10:4' not in l:
    return
  ls = json.loads(line.strip())
  content = ls['content']
  # if content == '' or 'processOrderPayStatusNotify' not in content:
  if content == '':
    return
  if content[0] != '{':
    print(content)
    return
  ls2 = json.loads(ls['content'])
  ip = ls['_container_ip_']
  t = ls2['thread']
  if ts.get(ip, None) == None:
    ts[ip] = {}

  ts[ip][t] = ts[ip].get(t, 0) + 1


if __name__ == '__main__':
  # file_path = 'e5ac79bb-936f-438a-92b1-7c6c0637f6c7.json'
  file_path = '87604919-0afc-408c-bda5-21e812f80ef7.json'
  read_line_file(filePath=file_path, callBack=line_fenxi)
  print(ts)
  write_file(filePath='a3.json', content=json.dumps(ts))
