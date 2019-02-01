# -*- encoding: utf-8 -*-

import os
import sys
import time
import json

import requests
import hashlib

login_url = 'https://api-test-2.cticloud.cn/interface/v10/agent/login'
call_out_url = 'https://api-test-2.cticloud.cn/interface/v10/previewOutcall'


token = 'bba76e258bd70fc83b7bd27a9c8e3e62'
call_center_id = '7000157'
# cno = '2000'
# bindTel = '6000'
cno = '2001'
bindTel = '6001'
bindType = '2'

def get_md5(str):
    m = hashlib.md5(str)
    return m.hexdigest()

def agent_login():
    global call_center_id, cno, bindTel, bindType, login_url
    timestamp = str(int(time.time()))
    md5str = call_center_id + timestamp + token
    sign = get_md5(md5str.encode('utf-8'))
    params = {
        'validateType': '2',
        'enterpriseId': call_center_id,
        'timestamp': timestamp,
        'sign': sign,
        'cno': cno,
        'bindTel': bindTel,
        'bindType': bindType,
    }
    print(login_url)
    print(params)
    content = requests.get(login_url, params)
    print(content.status_code)
    print(content.headers['content-type'])
    print(content.text)

def call_out(calledNo):
    global call_center_id, call_out_url

    timestamp = str(int(time.time()) - 10)
    md5str = call_center_id + timestamp + token
    sign = get_md5(md5str.encode('utf-8'))

    params = {
        'validateType': '2',
        'enterpriseId': call_center_id,
        'timestamp': timestamp,
        'sign': sign,
        'cno': cno,
        'tel': calledNo,
        'requestUniqueId': timestamp,
        'userField': '{"ext":"abcext"}',
    }
    print(call_out_url)
    print(json.dumps(params))
    content = requests.post(call_out_url, params)
    print(content.text)



def run():
    agent_login()
    # call_out('18917637631')


if __name__ == '__main__':
    run()

