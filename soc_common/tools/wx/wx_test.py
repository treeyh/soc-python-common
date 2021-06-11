# -*- encoding: utf-8 -*-

from helper import str_helper, file_helper, pymysql_helper, http_helper
import os
import sys
import re
import time
import random

import itchat

path = os.path.split(os.path.realpath(__file__))[0]
sys.path.append(path + os.sep + '..' + os.sep + '..')


# TEXT, MAP, CARD, NOTE, SHARING, PICTURE, RECORDING, ATTACHMENT, VIDEO, FRIENDS


@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
  print(msg.text)
  return msg.text


@itchat.msg_register(itchat.content.TEXT)
def _(msg):
  # equals to print(msg['FromUserName'])
  print(msg.fromUserName)


def run():
  itchat.auto_login(enableCmdQR=True, hotReload=True)
  itchat.send('Hello, filehelper', toUserName='filehelper')
  author = itchat.search_friends(nickName='filehelper')[0]
  author.send('greeting, filehelper!')
  itchat.run()
  itchat.send('Hello, filehelper', toUserName='filehelper')


if __name__ == '__main__':
  run()
