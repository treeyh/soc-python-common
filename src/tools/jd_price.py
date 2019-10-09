#-*- encoding: utf-8 -*-

import os
import datetime
import time
import sys
import random

syspath='D:\\00_BaiDuYun\\05_project\\00_selfapp\\04_tree_py_helper\\src'
sys.path.append(syspath)

from helper import str_helper, file_helper, http_helper



#http://p.3.cn/prices/mgets?skuIds=J_970602&type=1

if __name__ == '__main__':
    result = http_helper.http("http://p.3.cn/prices/mgets?skuIds=J_970602&type=1")
    re = str_helper.json_decode(result)
    print(re)

    print(re[0]['p'])