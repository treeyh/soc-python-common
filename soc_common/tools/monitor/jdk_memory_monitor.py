# -*- encoding: utf-8 -*-

import os
import logging
import time
import traceback


''' 程序日志文件路径 '''
_log_path = '/data/app/python-tools/run.log'

''' 筛选docker实例名 '''
_docker_filter_name = 'canal_admin'

''' 筛选jps -l进程名 '''
_java_filter_name = 'canal'

''' docker镜像中保存快照文件路径 '''
_memory_dump_path = '/home/app'

''' 宿主机中镜像文件保存路径 '''
_cp_dump_path = '/data/app/python-tools/'

''' 启动快照内存占用阈值 '''
_memory_limit = 2000

# 正常循环周期 sleep时间，秒
_period_sleep = 30

# 出现dump后 sleep时间，秒
_period_dump_sleep = 300


_logger = True


def logger(msg: str):
  global _log_path, _logger
  if True == _logger:
    logging.basicConfig(filename=_log_path, level=logging.INFO,
                        format=' %(asctime)s - %(levelname)s - %(message)s')
    _logger = False
  logging.info(msg)


def run_cmd(cmd: str):
  ''' 执行系统命令 '''
  return os.popen(cmd).readlines()


def get_docker(name: str):
  ''' 筛选docker实例 '''
  cmd = 'docker ps -a'
  dockerInfos = run_cmd(cmd)
  for docker in dockerInfos:
    if name in docker:
      return docker.strip()
  return None


def get_docker_container_id(docker: str):
  ''' 获取容器id '''
  if None == docker:
    return None
  ds = docker.split()
  return ds[0]


def get_java_pid(name: str, cid: str):
  ''' 获取java进程id '''
  cmd = 'docker exec -it %s /bin/bash -c  "jps -l"' % cid
  logger('get_java_pid_cmd:%s' % cmd)
  jpids = run_cmd(cmd)
  for jpid in jpids:
    if name in jpid:
      jps = jpid.strip().split()
      return jps[0]
  return None


def get_java_memory(cid: str, pid: str):
  ''' 获取java 内存 '''
  global _memory_dump_path
  cmd = 'docker exec -it %s /bin/bash -c  "jstat -gc %s"' % (cid, pid)
  logger('get_java_memory:%s' % cmd)
  memorys = run_cmd(cmd)
  if None != memorys:
    logger('get_java_memory result:%s' % ' '.join(memorys))
  else:
    logger('get_java_memory result:None')

  if len(memorys) != 2:
    return 0
  logger('get_java_memory0:%s' % memorys[0].strip())
  logger('get_java_memory1:%s' % memorys[1].strip())
  titles = memorys[0].split()
  ouIndex = 0
  s0uIndex = 0
  s1uIndex = 0
  euIndex = 0
  muIndex = 0
  for i in range(0, len(titles)):
    if 'OU' == titles[i]:
      ouIndex = i
    elif 'S0U' == titles[i]:
      souIndex = i
    elif 'S1U' == titles[i]:
      s1uIndex = i
    elif 'EU' == titles[i]:
      euIndex = i
    elif 'S0U' == titles[i]:
      souIndex = i
    elif 'MU' == titles[i]:
      muIndex = i

  values = memorys[1].split()
  oum = float(values[ouIndex])
  s0um = float(values[s0uIndex])
  s1um = float(values[s1uIndex])
  eum = float(values[euIndex])
  mum = float(values[muIndex])
  memoryCount = oum + s0um + s1um + eum + mum
  logger('get_java_memory memoryCount:%f ou:%f s0u:%f s1u:%f eu:%f mu:%f' %
         (memoryCount, oum, s0um, s1um, eum, mum))

  return memoryCount


def dump_java_memory(cid: str, pid: str):
  global _memory_dump_path
  path = '%s/map_%s.hprof' % (_memory_dump_path, str(time.time()))
  cmd = 'docker exec -it %s /bin/bash -c  "jmap -dump:live,format=b,file=%s %s"' % (cid, path, pid)
  logger('dump_java_memory_cmd:%s' % cmd)
  v = run_cmd(cmd)
  return path


def dump_java_stack(cid: str, pid: str):
  global _memory_dump_path
  path = '%s/jstack_%s.log' % (_memory_dump_path, str(time.time()))
  cmd = 'docker exec -it %s /bin/bash -c  "jstack %s > %s"' % (cid, pid, path)
  logger('dump_java_stack:%s' % cmd)
  v = run_cmd(cmd)
  return path


def cp_docker_file(cid: str, path: str):
  global _cp_dump_path
  cmd = 'docker cp %s:%s %s' % (cid, path, _cp_dump_path)
  logger('cp_docker_file_cmd:%s' % cmd)
  v = run_cmd(cmd)
  return


def rm_docker_file(cid: str, path: str):
  cmd = 'docker exec -it %s /bin/bash -c  "rm -rf %s"' % (cid, path)
  logger('rm_docker_file:%s' % cmd)
  v = run_cmd(cmd)
  return


def run():
  global _docker_filter_name, _java_filter_name, _memory_limit, _period_sleep, _period_dump_sleep

  while True:

    try:
      logger('jdk-memory-monitor start....')

      docker = get_docker(_docker_filter_name)
      if None == docker:
        logger('jdk-memory-monitor get_docker None.')
        time.sleep(_period_sleep)
        continue

      cid = get_docker_container_id(docker)
      if None == cid:
        logger('jdk-memory-monitor get_docker_container_id None.')
        time.sleep(_period_sleep)
        continue
      logger('docker cid:%s' % cid)

      jpid = get_java_pid(_java_filter_name, cid)
      if None == jpid:
        logger('jdk-memory-monitor get_java_pid None.')
        time.sleep(_period_sleep)
        continue
      logger('docker java pid:%s' % jpid)

      memoryCount = get_java_memory(cid, jpid)
      logger('docker java memory:%f' % memoryCount)

      if memoryCount <= _memory_limit:
        logger('jdk-memory-monitor end.')
        time.sleep(_period_sleep)
        continue

      path = dump_java_memory(cid, jpid)
      logger('docker java memory dump:%s' % path)
      cp_docker_file(cid, path)
      rm_docker_file(cid, path)

      path = dump_java_stack(cid, jpid)
      logger('docker java stack:%s' % path)
      cp_docker_file(cid, path)
      rm_docker_file(cid, path)

      logger('jdk-memory-monitor memory dump end.')
      break
    except:
      logger(traceback.format_exc())
      time.sleep(_period_sleep)


if __name__ == '__main__':
  run()
