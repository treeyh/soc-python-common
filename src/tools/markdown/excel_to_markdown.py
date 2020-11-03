#-*- encoding: utf-8 -*-

import pyperclip


def clipboard_to_markdown():
  info = pyperclip.paste()
  content = ''
  index = 0
  for line in info.split('\r\n'):
    if line.strip() == '':
      continue
    ls = line.replace('\n', '<br />').split('\t')
    for l in ls:
      content += '| ' + l+' '
    content += '|\n'

    if index == 0:
      # 补头
      for l in ls:
        content += '|:--'
      content += '|\n'
    index += 1
  pyperclip.copy(content)

if __name__ == "__main__":
    clipboard_to_markdown()