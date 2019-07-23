# -*- encoding: utf-8 -*-

import hashlib
import uuid
import sys
import urllib
from datetime import date, datetime, timedelta
import time
from decimal import Decimal
import json


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


class JsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        else:
            return json.JSONEncoder.default(self, obj)

def json_encode(obj):
    return json.dumps(obj, cls = JsonEncoder)


def json_decode(value):
    return json.loads(value)


if __name__ == '__main__':
    # print(get_uuid()
    t = int(time.time())
    print(t)
    e = '7000157'
    departmentToken = 'bba76e258bd70fc83b7bd27a9c8e3e62'
    md5str = e + str(t) + departmentToken
    print(md5str)
    print(get_md5(md5str.encode("utf-8")))
    print(get_md5('t8a66572aac6911e99080784f439212b0ree`123'.encode("utf-8")))
    print(get_uuid())
    # for i in range(0, 100):
    #     print(datetime.now().strftime('%Y%m%d%H%M%S') + get_uuid()[14:]
    #     time.sleep(1)
    # print(str(uuid.uuid1())
    # str = '#!@81%sjl=)k' % '123123'
    str = 'wanda123'

