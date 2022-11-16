# -*- encoding: utf-8 -*-

import os

from soc_common.utils import str_utils, file_utils, log_utils

_source_path = 'D:\\01_product\\24_soc-toolkit\\01_src\\soc-toolkit-app\\lib\\common\\langs'

_file_name = 'en_US.dart'

_line = '\n'


def run():
  global _source_path, _file_name, _line
  file_path = os.path.join(_source_path, _file_name)

  lines = file_utils.read_all_lines_file(file_path)

  content = ''
  nextFlag = False
  for line in lines:
    l = line.strip()
    if l == '':
      content += _line
      continue
    if l.startswith('//'):
      content += l + _line
      continue
    ls = l.split('\': \'')
    if nextFlag:
      nextFlag = False
      content += ls[0] + _line
      continue
    if len(ls) == 1:
      if 'tool.' in l:
        nextFlag = True
        content += ls[0].replace('.', '_')
      continue

    if len(ls) == 2:
      content += ls[0].replace('.', '_') + '\' : \'' + ls[1] + _line
      continue
  file_utils.write_file('d:\\t.log', content)


if __name__ == '__main__':
  # sys.setdefaultencoding('utf-8')

  pass
