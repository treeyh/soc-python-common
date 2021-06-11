#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import json
import requests
import socket
import os
import sys
import getopt


def usage():
  print("\n")
  print("Usage: ./%s --type [cluster_health_ck|sync_ck]" % os.path.basename(__file__))
  print("\t --type cluster_health_ck   check ES cluster")
  print("\t --type sync_ck    check ES sync status")
  print("\n")
  sys.exit(1)


try:
  opts, args = getopt.getopt(sys.argv[1:], '-h', ['help', 'type='])
  for opt_name, opt_value in opts:
    if opt_name in ('-h', '--help'):
      usage()
      sys.exit()
    if opt_name in ('--type'):
      type = opt_value
except Exception as err_code:
  print("Err:getopt error->", err_code)
  sys.exit(2)


# parameter num check
if (len(sys.argv[1:]) < 1):
  print("check error")
  usage()
  sys.exit(2)


def get_sing():
  import time
  import hmac
  import hashlib
  import base64
  import urllib.parse

  timestamp = str(round(time.time() * 1000))
  secret = 'SEC1194f0d1764b640653223010fd94c760f36d14646be3300dd6b4e03aa4118c12'
  secret_enc = secret.encode('utf-8')
  string_to_sign = '{}\n{}'.format(timestamp, secret)
  string_to_sign_enc = string_to_sign.encode('utf-8')
  hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
  sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))
  return timestamp, sign


"""
查询本机ip地址
:return:
"""
try:
  s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  s.connect(('8.8.8.8', 80))
  ip = s.getsockname()[0]
finally:
  s.close()
now_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))


def dingmessage(txt, url):
  # 请求的URL，WebHook地址
  timestamp, sign = get_sing()
  webhook = "https://oapi.dingtalk.com/robot/send?access_token=66f560a136bec89f2cf6c1f893cab27ae842b4c77e099ee1bef46ed9f34f2556&timestamp={}&sign={}".format(
      timestamp, sign)
# 构建请求头部
  header = {
      "Content-Type": "application/json",
      "Charset": "UTF-8"
  }
# 构建请求数据
  tex = """
    告警触发:  %s
    基本信息：
    告警时间:  %s
    详细指标:
    告警标签:  %s
    异常分钟:  1 分钟
    当前数值:  1
    故障主机:  %s
    """ % (txt, now_time, url, ip)
  message = {
      "msgtype": "text",
      "text": {
          "content": tex
      },
      "at": {
          "isAtAll": False
      }
  }
# 对请求的数据进行json封装
  message_json = json.dumps(message)
# 发送请求
  info = requests.post(url=webhook, data=message_json, headers=header)
# 打印返回的结果
  print(info.text)
  # print(tex)


def write_sign(count):
  with open("/tmp/.es_sync_count", "w") as f:
    f.write(count)


def read_sign():
  with open("/tmp/.es_sync_count", "r") as f:
    return f.read().strip()


def read_mtime():
  return os.stat("/tmp/.es_sync_count").st_mtime


if __name__ == "__main__":

  if (type == 'cluster_health_ck'):
    print("INFO: cluster_health_ck -> cluster_health_ck")
    url = r"http://10.0.59.189:9200/_cluster/health?pretty"
    res = requests.get(url)
    status = dict(json.loads(res.content)).get("status")
    if status != "green":
      txt = "ES集群异常"
      print(txt, url)
      dingmessage(txt)
    else:
      print("ES集群正常")

  elif (type == 'sync_ck'):
    print("INFO: sync_ck -> sync_ck")
    filemtime = read_mtime()
    nowtime = time.time()
    nowhour = time.localtime().tm_hour
    interval = 2 * 60
    if nowhour >= 23 or nowhour < 6:
      # 晚上23点到早上6点前，时间时间间隔判断调整为5分钟，其他时间为2分钟
      interval = 5 * 60
    url = r"http://10.0.59.189:9200/order_index/_count"
    res = requests.get(url)
    count = dict(json.loads(res.content)).get("count")
    # 如果获取的结果和1分钟之前结果一样，则表示不同步了，有异常
    if count == int(read_sign()):
      if nowtime > (filemtime + interval):
        print(count)
        txt = "ES同步异常"
        print(txt)
        dingmessage(txt, url)
    else:
      # 否则没有异常，写入临时文件
      write_sign(str(count))
      print("ES同步正常")
  else:
    usage()
