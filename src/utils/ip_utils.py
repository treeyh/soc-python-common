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


def get_host_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()

    return ip

if __name__ == '__main__':
    print(get_local_ip())
    print(get_host_ip())

