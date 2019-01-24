# -*- encoding: utf-8 -*-

import urllib
import socket
import sys

from os.path import basename

_req_type = False
try:
    import requests

    _req_type = True
except Exception as e:
    pass

cookies = None


# http://www.python-requests.org/en/latest/
def get(url, params=None, headers=None, cookies=None, timeout=20, allow_redirects=True):
    '''
        使用requests扩展调用http-get
        url:访问url
        params:get参数
        headers:http头
        cookie:传入cookie
        timeout:超时时间，秒
        allow_redirects:是否支持跳转，默认为True支持
    '''
    r = requests.get(url=url, params=params, headers=headers, cookies=cookies)
    # print r.url
    return r


def post(url, params=None, data=None, headers=None, filePath=None, cookies=None, allow_redirects=True):
    files = None
    if filePath != None:
        files = {'file': open(filePath, 'rb')}
    r = requests.post(url=url, params=params, data=data, files=files, headers=headers, cookies=cookies)
    return r


class MyAdapter(requests.adapters.HTTPAdapter):
    def init_poolmanager(self, connections, maxsize):
        self.poolmanager = PoolManager(num_pools=connections,
                                       maxsize=maxsize,
                                       ssl_version=ssl.PROTOCOL_SSLv3)


if __name__ == '__main__':
    default_encoding = 'utf-8'
    if sys.getdefaultencoding() != default_encoding:
        reload(sys)
        sys.setdefaultencoding(default_encoding)

    # url = 'http://192.168.73.51/mobi/vod/st02/2015/12/25/Q350_2024797990.3gp?sign=588B4ED04707A3FC06699F551F00C184&tm=567d0336&vw=2&ver=v1.1&qualityCode=511&version=1&guid=1dfaddab-7f99-f656-050b-851301c5bf4c&app=108020310095&cookie=567cf976512fa&session=567cf976512fa&uid=104300041552163151119&uname=18912638032&time=20151225164958&videotype=2&cid=C37480675&cname=&cateid=&dev=000001&ep=1&etv=&os=30&ps=0099&clienttype=HTC+D816v&deviceid=null&appver=5.2.30.3ctch1&res=720%252A1184&channelid=20040101&pid=1000000228&orderid=1100359956945&nid=&netype=11&isp=&cp=00000124&sp=00000014&ip=180.168.5.182&ipSign=cbc1772921e64448e8c67ce1cf179596&cdntoken=api_567d0336e0bf0&pvv=0'
    # r = requests.get(url = url, headers = headers)
    # print r.url
    # # print r.content
    # print r.status_code

    # url = 'http://127.0.0.1:8080/addUser'
    # url = 'http://127.0.0.1:8080/hello'
    # # url = 'http://127.0.0.1:8080/getUser'
    # data = '{"id":1,"name":"aaaaaaaaaaaaaaaaaaaaaaa"}'
    # # data = '1231231231231231231231'
    # r = post(url = url, params ={'name':'AAA'}, data = data)
    # print '1'
    # print r.text
    # print '2'

    # url = 'http://127.0.0.1:8080/openIdLogin'
    # data = '{"openId":"11222333","facilitatorId":"12","authComeFrom":"WX"}'

    # # data = '1231231231231231231231'
    # r = post(url = url, params ={'name':'AAA'}, data = data)
    # obj = str_utils.json_decode(r.text)
    # print '1'
    # print obj['info']['userAccountId']
    # print r.text
    # print '2'

    # # url = 'http://127.0.0.1:8080/getUser'
    # # data = '{"openId":"11222333","facilitatorId":"12","authComeFrom":"WX"}'
    # r = post(url = url, params ={'name':'AAA'}, data = data)
    # print '1'
    # print r.text
    # print '2'

    url = 'http://211.151.134.222:80/V3/BookingDriver/getBookingRideList'
    headers = {
        'User-Agent': 'DidaPinche/5.9.3(iOS 10.1.1;iPhone9,2) Mozilla/5.0 (iPhone; CPU iPhone OS 10_1_1 like Mac OS X) AppleWebKit/602.2.14 (KHTML, like Gecko)',
        'ddcinfo': 'ehAq+CFEfF3VHAlCYotA5KP4PHD7A6vsDBWiVXTBvZWyY2ytxhSK7eSGARv7KY6cWQ0ki4dQ41pRbXD1VkyXFKUHuoLyclWr5sgeT86d+TV0CifBPtOfOWUopU4M4yzlK8G5e6YItBuOZ3kYLVyp8rQ+mkH8ALn1as6lwuq0XlK6U5Y9OE3Q4Z0azqNVZmXHxT65/VMxFbFScNNuqQhsVMUnaKq8VQbzgwBRhGwWBb9LPhBMBa7WbBQxU9AQdOQSRCqe/hjkndqQhwegPw/SpKrJjlyIzGpnI/Swvkdu6N+JIOMSZct1VT8t1Y836p4VFs4Gj3oaQc3ajk5iu0yq8Eg5sttyh7tvhbNA05mt/Ql6T8JN53/wlJP6jzcG72EJhZfEVFF7mQHhBW38uSUxQakPsp32yAaaQyws/wvYHhkftihwfkeJzGcp1bs7rtv67qJf7x/dlY+cG49VIulKEwWJC6aKU20Lfsh9YvnZJ3Y=',
        'Accept-Language': 'zh-Hans-CN;q=1',
    }
    cookies = {
        'PHPSESSID': 'o4u4n812mt3cg441hfn0j6f856',
    }
    data = 'actid=dida_app&mobiletype=1&page=1&page_size=20&ride_type=2&sig=464f9db20c0ce03daba195e6d9e9aa3f&token=a5fccb03-8285-48c7-8489-bb334beb354e&ts=20170622160405&user_cid=3b81ee35-d1c8-4d21-a3e3-5c426cef6bd8&version=5.9.3&vkey=ECF118CE701C29BEB81F871E416AE657'
    info = requests.post(url=url, headers=headers, cookies=cookies, data=data)
    print(info.text)


