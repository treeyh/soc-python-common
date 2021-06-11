# -*- encoding: utf-8 -*-

from utils import http_utils, str_utils
import os
import datetime
import time
import sys
import random

syspath = 'D:\\00_BaiDuYun\\05_project\\00_selfapp\\04_tree_py_helper\\src'
sys.path.append(syspath)


# http://p.3.cn/prices/mgets?skuIds=J_970602&type=1

if __name__ == '__main__':
  result = http_utils.get("http://p.3.cn/prices/mgets?skuIds=J_970602&type=1")
  re = str_utils.json_decode(result)
  print(re)

  print(re[0]['p'])
