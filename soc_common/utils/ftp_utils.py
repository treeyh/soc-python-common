# -*- encoding: utf-8 -*-

import os
import traceback


def send_file(ip, port, user, password, filePath, targetFloder):
  try:
    ftp = FTP()
    ftp.set_debuglevel(2)  # 打开调试级别2，显示详细信息
    ftp.connect(ip, port)  # 连接
    ftp.login(user, password)  # 登录，如果匿名登录则用空串代替即可

    bufsize = 1024
    targetpath = os.path.join(targetFloder, os.path.basename(filePath))
    # targetpath = '/home/ftpdata/cardinfo/' + os.path.basename(filePath)
    # logger().info(filePath)
    # logger().info(targetpath)
    fp = open(filePath, 'rb')
    ftp.storbinary('STOR ' + targetpath, fp, bufsize)  # 上传文件
    fp.close()  # 关闭文件

    ftp.set_debuglevel(0)
    ftp.quit()
    return True
  except Exception as e:
    # logger().error(traceback.format_exc())
    return False


def get_file(ip, port, user, password, filePath, targetPath):

  try:
    ftp = FTP()
    ftp.set_debuglevel(2)  # 打开调试级别2，显示详细信息
    ftp.connect(ip, port)  # 连接
    ftp.login(user, password)  # 登录，如果匿名登录则用空串代替即可

    # print(ftp.getwelcome()) #显示ftp服务器欢迎信息
    bufsize = 1024  # 设置缓冲块大小
    fp = open(targetPath, 'wb')  # 以写模式在本地打开文件
    ftp.retrbinary('RETR ' + filePath, fp.write, bufsize)  # 接收服务器上文件并写入本地文件
    fp.close()

    ftp.set_debuglevel(0)  # 关闭调试
    ftp.quit()  # 退出ftp服务器
    return targetPath
  except Exception as e:
    logger().error(traceback.format_exc())
    return None
