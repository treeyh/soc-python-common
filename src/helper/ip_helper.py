# -*- encoding: utf-8 -*-

import socket

from IPy import IP, IPSet


def get_ip_version(ip):
    try:
        return IP(ip).version()
    except Exception as e:
        return None


def check_ip(ip):
    if None is get_ip_version(ip):
        return False
    else:
        return True

def get_local_ip():
    return socket.gethostbyname(socket.gethostname())


if __name__ == '__main__':
    print(check_ip('211-23-11-110.hinet-ip.hinet.net'))
    print(get_local_ip())

