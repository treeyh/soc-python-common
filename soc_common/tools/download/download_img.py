# -*- encoding: utf-8 -*-

'''
@file           :download_img.py
@description    :
@time           :2024-09-26 10:53:03
@author         :Tree
@version        :1.0
'''

import os
from datetime import datetime, date

import requests

from soc_common.utils import file_utils
from soc_common.config import config


urls = [
  '/images/tomcat/tomcat-x-container-1.jpg',
'/images/tomcat/tomcat-x-pipline-6.jpg',
'/images/tomcat/tomcat-x-pipline-5.jpg',
'/images/maven_1.jpg',
'/images/alg/alg-dist-hash-8.jpg',
'/images/alg/alg-dst-paxos-1.jpg',
'/images/alg/alg-dst-paxos-2.jpg',
'/images/alg/alg-dst-raft-1.jpg',
'/images/alg/alg-dst-raft-4.jpg',
'/images/job/job-x4.jpg',
'/images/devops/docker/docker-y-0.jpg',
'/images/develop/package/dev-package-lombok-2.png',
'/images/develop/package/dev-package-lombok-3.png',
'/images/develop/network/dev-network-protocol-1.png',
'/images/develop/network/dev-network-protocol-x1.png',
'/images/develop/network/dev-network-protocol-x2.png',
'/images/develop/network/dev-network-dns-12.png',
'/images/develop/network/dev-network-protocol-10.png',
'/images/security/dev-security-overview-1.png',
'/images/security/dev-security-xss-1.png',
'/images/security/dev-security-xss-3.png',
'/images/security/dev-security-xss-2.png',
'/images/security/dev-security-flow-1.png',
'/images/security/dev-security-flow-2.png',
'/images/develop/ut/dev-ut-1.png',
'/images/spring/spring-interview-1.png',
'/images/spring/spring-interview-3.png',
'/images/spring/springframework/spring-framework-ioc-source-102.png',
'/images/spring/spring-interview-6.png',
'/images/project/project-b-5.png',
'/images/spring/springboot-starter-demo-2.png',
'/images/spring/security/spring-security-3.png',
'/images/spring/security/spring-security-4.png',
'/images/spring/security/spring-security-5.png',
'/images/spring/security/spring-security-6.png',
'/images/spring/security/spring-security-7.png',
'/images/spring/security/spring-security-1.png',
'/images/spring/security/spring-security-2.png',
'/images/develop/package/dev-package-log-5.png',
'/images/develop/package/dev-package-log-4.png',
'/images/jvm/java_jvm_classload_3.png',
'/images/tomcat/tomcat-x-container-3.png',
'/images/tomcat/tomcat-x-lifecycle-1.png',
'/images/tomcat/tomcat-x-lifecycle-2.png',
'/images/tomcat/tomcat-x-lifecycle-3.png',
'/images/tomcat/tomcat-x-listener-3.png',
'/images/git-four-areas.png',
'/images/git-five-states.png',
'/images/arch/arch-x-ev-g-8.png',
'/images/arch/arch-x-ev-g-9.png',
'/images/arch/arch-x-ev-g-10.png',
'/images/arch/arch-xianliu-1.png',
'/images/arch/arch-xianliu-2.png',
'/images/arch/arch-x-reduce-2.png',
'/images/arch/arch-x-reduce-4.png',
'/images/arch/arch-x-reduce-6.png',
'/images/arch/arch-x-lb-1.png',
'/images/arch/arch-x-lb-2.png',
'/images/arch/arch-x-lb-3.png',
'/images/arch/arch-x-lb-4.png',
'/images/arch/arch-x-lb-5.png',
'/images/arch/arch-x-lb-6.png',
'/images/arch/arch-x-lb-7.png',
'/images/arch/arch-z-id-3.png',
'/images/zk/zk-1.png',
'/images/arch/arch-z-trans-3.png',
'/images/arch/arch-z-trans-4.png',
'/images/arch/arch-z-trans-5.png',
'/images/arch/arch-z-trans-6.png',
'/images/db/redis/cache-1.png',
'/images/db/redis/cache-2.png',
'/images/db/redis/cache-3.png',
'/images/job/job-quartz-x1.png',
'/images/job/job-quartz-x2.png',
'/images/job/job-x3.png',
'/images/arch/arch-z-session-1.png',
'/images/arch/arch-z-session-2.png',
'/images/arch/arch-z-session-3.png',
'/images/arch/arch-z-session-4.png',
'/images/arch/arch-z-session-5.png',
'/images/arch/arch-z-session-6.png',
'/images/k8s/k8s-arch-1.png',
'/images/devops/docker/docker-x-1.png',
'/images/devops/cicd/cicd-2.png',
'/images/devops/cicd/cicd-3.png',
'/images/devops/cicd/cicd-4.png',
'/images/devops/cicd/cicd-1.png',
'/images/devops/cicd/cicd-5.png',
'/images/git/git-gitflow-1.png',
'/images/dev_opensource_1.png',
]

pre_url = 'https://pdai.tech'


def download_imgs():
  export_path = os.path.join(config.ExportPath, 'download', 'image', '002')
  file_utils.make_folders(export_path)
  for url in urls:
    u = url
    if not url.startswith('http'):
      u = pre_url + url
    file_name = file_utils.get_file_name(url)
    file_path = os.path.join(export_path, file_name)

    resp = requests.get(u, stream=True)

    if resp.status_code == 200:
      # 打开一个文件以写入二进制数据
      with open(file_path, 'wb') as file:
        # 将内容写入文件
        for chunk in resp.iter_content(chunk_size=8192):
          file.write(chunk)
        print("文件下载成功！"+ file_name)
    else:
      print(f"下载失败，状态码: {resp.status_code}; "+ file_path)