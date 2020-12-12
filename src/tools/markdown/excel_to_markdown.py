#-*- encoding: utf-8 -*-

import pyperclip


def format_clipboard_content(c):
  if len(c) >= 6:
    if c[:3] == '"""' and c[-3:] == '"""':
      return c[3:-3]
  if len(c) >= 3:
    if c[:1] == '"' and c[-1:] == '"':
      return c[1:-1]
  return c

def clipboard_to_markdown():
  info = pyperclip.paste()
  content = ''
  index = 0
  for line in info.split('\r\n'):
    if line.strip() == '':
      continue
    ls = line.replace('\n', '<br />').split('\t')
    for l in ls:
      content += '| ' + format_clipboard_content(l) +' '
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

    # str = '1234567890'
    # print(str[:3])
    # print(str[-3:])
    # print(str[3:-3])
