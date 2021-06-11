# -*- encoding: utf-8 -*-

from utils import str_utils, file_utils
import os
import sys
import re


path = os.path.split(os.path.realpath(__file__))[0]
sys.path.append(path + os.sep + '..' + os.sep + '..')


target_domain_path = 'D:\\06_wd\\07_src\\08_task_manager\\task-dispatch-platform\\task-dispatch-service\\src\\main\\java\\com\\ffan\\task\\dispatch\\domain\\TaskServer.java'
source_domain_path = 'D:\\06_wd\\07_src\\08_task_manager\\task-dispatch-platform\\task-dispatch-service\\src\\main\\java\\com\\ffan\\task\\dispatch\\service\\domain\\req\\TaskServerReq.java'

is_to_none_prop = True

# source_domain_path = 'D:\\06_wd\\07_src\\03_spider\\TXWTaskMangerService\\taskmanager-api\\src\\main\\java\\com\\ffan\\txw\\crawler\\taskmanager\\domain\\TaskServer.java'
# target_domain_path = 'D:\\06_wd\\07_src\\03_spider\\TXWTaskMangerService\\taskmanager-api\\src\\main\\java\\com\\ffan\\txw\\crawler\\taskmanager\\domain\\req\\TaskServerReq.java'


def get_props(file_path, name):
  lines = file_utils.read_all_lines_file(file_path)
  props = {
      'map': {},
      'list': [],
      'name': name,
  }
  for line in lines:
    l = line.strip()
    ls = l.replace(';', '').split()
    if 3 != len(ls) or 'private' != ls[0]:
      continue
    props['map'][ls[2]] = ls[1]
    props['list'].append(ls[2])
  return props


def get_name(file_path):
  sname = os.path.basename(file_path).split('.')[0]
  return str_utils.lowerFirstWord(sname)


def get_default_val(ptype):
  if 'String' == ptype:
    return '""'
  elif 'Integer' == ptype or 'int' == ptype:
    return '0'
  elif 'Double' == ptype or 'double' == ptype:
    return '0D'
  elif 'Long' == ptype or 'long' == ptype:
    return '0L'
  elif 'Date' == ptype:
    return 'new Date(System.currentTimeMillis())'


def build_to_domain_code(sprops, tprops):
  global is_to_none_prop
  content = ''
  for tpk in tprops['list']:
    if None == sprops['map'].get(tpk, None):
      if True == is_to_none_prop:
        content = '%s%s%s.set%s(%s);' % (content, os.linesep, tprops['name'],
                                         str_utils.upperFirstWord(tpk), get_default_val(tprops['map'][tpk]))
      continue

    content = '%s%s%s.set%s(%s.get%s());' % (content, os.linesep, tprops['name'],
                                             str_utils.upperFirstWord(tpk), sprops['name'], str_utils.upperFirstWord(tpk))

  return content + os.linesep + os.linesep


def main():
  global source_domain_path, target_domain_path
  sname = get_name(source_domain_path)
  tname = get_name(target_domain_path)

  sprops = get_props(source_domain_path, sname)
  tprops = get_props(target_domain_path, tname)

  print(sprops)

  return build_to_domain_code(sprops, tprops)


if __name__ == '__main__':
  print(main())
