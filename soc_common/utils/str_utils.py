# -*- encoding: utf-8 -*-

import hashlib
import uuid
import sys
import urllib
import re
from datetime import date, datetime, timedelta
import time
from decimal import Decimal
import json

import hmac
import base64


def is_null_or_empty(str):
  return True if str == None or str == '' else False


def format_str_to_list_strip(str, sp):
  ls = str.split(sp)
  l = []
  for i in ls:
    s = i.strip()
    l.append(s)
  return l


def format_str_to_list_filter_empty(str, sp):
  ls = str.split(sp)
  l = []
  for i in ls:
    s = i.strip()
    if is_null_or_empty(s):
      continue
    l.append(s)
  return l


def get_md5(str):
  m = hashlib.md5(str)
  # m.digest()
  return m.hexdigest()


def get_sha1(str):
  m = hashlib.sha1(str)
  # m.digest()
  return m.hexdigest()


def get_hmac_sha256(mac, str):

  return hmac.new(mac, str, digestmod=hashlib.sha256).hexdigest()


def get_uuid():
  return str(uuid.uuid1()).replace('-', '')


def is_list_str_in(sourceList, target, isCasematters=True):
  '''
      判断list的str中是否含有target字符串
      sourceList：源list
      target：目标字符串
      isCasematters：是否区分大小写
  '''
  for source in sourceList:
    if True == isCasematters and target in source:
      return True
    if False == isCasematters and target.lower() in source.lower():
      return True
  return False


def format_url(url, params):
  if '?' in url:
    url = '%s&' % url
  else:
    url = '%s?' % url
  for k in params.keys():
    url = '%s%s=%s&' % (url, k, url_escape(params[k]))
  return url


def url_escape(value):
  """Returns a valid URL-encoded version of the given value."""
  return urllib.quote_plus(utf8(value))


_UTF8_TYPES = (bytes, type(None))


def utf8(value):
  """Converts a string argument to a byte string.
  If the argument is already a byte string or None, it is returned unchanged.
  Otherwise it must be a unicode string and is encoded as utf8.
  """
  if isinstance(value, _UTF8_TYPES):
    return value
  return value.encode("utf-8")


def get_url(url, params):
  type = False
  if '?' in url:
    type = True


def upperFirstWord(inStr):
  ''' 首字母大写 '''
  return inStr[:1].upper() + inStr[1:]


def lowerFirstWord(inStr):
  ''' 首字母小写 '''
  return inStr[:1].lower() + inStr[1:]


def get_url_params(url):
  if 'POSTSTRING:' in url:
    return get_url_post_params(url)
  else:
    return get_url_get_params(url)


def get_url_get_params(url):
  us = url.strip().split('?')
  p = {}
  if len(us) < 2:
    return p

  uss = us[1].split('&')
  for u in uss:
    s = u.split('=')
    if len(s) < 2:
      continue
    p[s[0].lower()] = s[1]
  return p


def get_url_post_params(url):
  us = url.split('POSTSTRING:')
  p = {}
  if len(us) < 2:
    return p

  uss = us[1].split('httpcode:')
  usss = uss[0].strip().split('&')
  for u in usss:
    s = u.split('=')
    p[s[0].lower()] = s[1]
  return p


_num_abc__ = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_1234567890'


def check_num_abc__(str):
  for c in str:
    if c not in _num_abc__:
      return False
  return True


_num_abc_port_ = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_.1234567890'


def check_num_abc_port__(str):
  for c in str:
    if c not in _num_abc_port_:
      return False
  return True


_num = '1234567890'


def check_num(str):
  for c in str:
    if c not in _num:
      return False
  return True


def get_url_host(url):
  proto, rest = urllib.splittype(url)
  host, rest = urllib.splithost(rest)
  return host
  # host, port = urllib.splitport(host)
  # if port is None:
  #    port = 80


def clear_str_end_chart(source: str, clears: list = []) -> str:
  target = source
  for clear in clears:
    count = len(clear)
    if count <= 0:
      continue
    if target[-count:] == clear:
      target = target[:-count]
  return target


class JsonEncoder(json.JSONEncoder):
  def default(self, obj):
    if isinstance(obj, datetime):
      return obj.strftime('%Y-%m-%d %H:%M:%S')
    elif isinstance(obj, date):
      return obj.strftime('%Y-%m-%d')
    else:
      return json.JSONEncoder.default(self, obj)


def json_encode(obj):
  return json.dumps(obj, cls=JsonEncoder)


def json_decode(value):
  return json.loads(value)


def under_score_case_to_camel_case(value):
  if "_" in value:
    """ 
            #方法二：
            strlist = str.split("_")
            Strlist = [s.capitalize() for s in strlist]
            outStr = "".join(Strlist)
            print(outStr)
    """
    # 方法一：
    return "".join(map(lambda x: x.capitalize(), value.split("_")))

  return value.capitalize()


def hump2underline(hunp_str):
  '''
  驼峰形式字符串转成下划线形式
  :param hunp_str: 驼峰形式字符串
  :return: 字母全小写的下划线形式字符串
  '''
  # 匹配正则，匹配小写字母和大写字母的分界位置
  p = re.compile(r'([a-z]|\d)([A-Z])')
  # 这里第二个参数使用了正则分组的后向引用
  sub = re.sub(p, r'\1_\2', hunp_str).lower()
  return sub


def underline2hump(underline_str):
  '''
  下划线形式字符串转成驼峰形式
  :param underline_str: 下划线形式字符串
  :return: 驼峰形式字符串
  '''
  # 这里re.sub()函数第二个替换参数用到了一个匿名回调函数，回调函数的参数x为一个匹配对象，返回值为一个处理后的字符串
  sub = re.sub(r'(_\w)', lambda x: x.group(1)[1].upper(), underline_str)
  return sub


def json_hump2underline(hump_json_str):
  '''
  把一个json字符串中的所有字段名都从驼峰形式替换成下划线形式。
  注意点：因为考虑到json可能具有多层嵌套的复杂结构，所以这里直接采用正则文本替换的方式进行处理，而不是采用把json转成字典再进行处理的方式
  :param hump_json_str: 字段名为驼峰形式的json字符串
  :return: 字段名为下划线形式的json字符串
  '''
  # 从json字符串中匹配字段名的正则
  # 注：这里的字段名只考虑由英文字母、数字、下划线组成
  attr_ptn = re.compile(r'"\s*(\w+)\s*"\s*:')

  # 使用hump2underline函数作为re.sub函数第二个参数的回调函数
  sub = re.sub(attr_ptn, lambda x: '"' + hump2underline(x.group(1)) + '" :', hump_json_str)
  return sub


def format_bytes_to_str(val):
  """bytes对象转str

  Args:
      val ([type]): [description]

  Returns:
      [type]: [description]
  """
  vtype = type(val).__name__
  if vtype == 'bytes':
    return val.decode('utf-8', 'replace')
  else:
    return val


if __name__ == '__main__':
  # print(get_uuid()
  # t = int(time.time())
  # print(t)
  # e = '7000157'
  # departmentToken = 'bba76e258bd70fc83b7bd27a9c8e3e62'
  # md5str = e + str(t) + departmentToken
  # print(md5str)
  # print(get_md5(md5str.encode("utf-8")))
  # print(get_uuid())
  # # for i in range(0, 100):
  # #     print(datetime.now().strftime('%Y%m%d%H%M%S') + get_uuid()[14:]
  # #     time.sleep(1)
  # # print(str(uuid.uuid1())
  # # str = '#!@81%sjl=)k' % '123123'
  # str = 'wanda123'
  # print(get_md5('4399bfa6a6b211e99c47f01e3412b52aqwe123'.encode("utf-8")))

  # print(UnderScoreCase2CamelCase("aaaaa_bbbbb_ccccc_123"))

  print(get_uuid())

  # ms = {
  #     'app_code': 'abc',
  #     'type': '1',
  #     'x-snbps-cplc': '1234567890',
  #     'x-snbps-vendor': 'xiaomi',
  #     'x-snbps-module': 'Redmi k20 pro',
  #     'x-snbps-imei': 'imei',
  #     'x-snbps-rom-version': 'Android 11',
  #     'x-snbps-os-version': 'Android 11',
  #     'x-snbps-account-id': '0',
  #     'x-snbps-sdk-ver': 'v1.0.0',
  # }

  # # ks = sorted(ms.keys())
  # # print(ks)
  # str = '123&1600313751&'
  # body = '{"id":1,"name":"abc"}'
  # for k in sorted(ms.keys()):
  #     str += k + '=' + ms[k] + '&'
  # str1 = str + body
  # str += body + '&abcdefg'

  # print(str.encode('utf-8'))
  # print(get_sha1(str.encode('utf-8')))

  # print(str1)
  # print(get_hmac_sha256('abcdefg'.encode('utf-8'), str1.encode('utf-8')))
