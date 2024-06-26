# -*- encoding: utf-8 -*-

import time
# pip install mysql-connector-python
import mysql.connector
import logging
import traceback


class MysqlUtils(object):
  """ MysqlUtils """

  def __init__(self, host, port, user, passwd, db, charset):
    super(MysqlUtils, self).__init__()

    self.host = host
    self.user = user
    self.passwd = passwd
    self.db = db
    self.charset = charset
    self.port = port

  def _getConnection(self):
    i = 0
    count = 5
    while (1):
      try:
        i = i + 1
        conn = mysql.connector.connect(host=self.host, port=self.port,
                                       user=self.user, passwd=self.passwd, db=self.db)  # , use_unicode=True, charset=self.charset,
        return conn
      except BaseException as e:
        logging.error('Error %d: %s' % (e.args[0], e.args[1]))
        if (i >= 3):
          logging.error('sql connection get count %d ' % (count))
          return None
        time.sleep(5)

  def find_one(self, sql, params=(), mapcol=None):
    conn = self._getConnection()
    c = None
    result = None
    try:
      c = conn.cursor()
      c.execute(sql, params)
      yz = c.fetchone()
      if yz == None:
        return None
      if mapcol == None:
        return yz
      result = self._result_to_map(yz, mapcol)
      return result
    except BaseException as e:
      logging.error('Error %d: %s' % (e.args[0], e.args[1]))
      return result
    finally:
      if None != c:
        c.close()
      if None != conn:
        conn.close()

  def find_all(self, sql, params=(), mapcol=None):
    conn = self._getConnection()
    c = None
    try:
      c = conn.cursor()
      c.execute(sql, params)
      yz = c.fetchall()
      if yz == None:
        return None
      if mapcol == None:
        return yz
      result = []
      for y in yz:
        result.append(self._result_to_map(y, mapcol))
      return result
    except BaseException as e:
      logging.error('sql %s, %s ;Error %d: %s' % (sql, str(params), e.args[0], e.args[1]))
      return result
    finally:
      if None != c:
        c.close()
      if None != conn:
        conn.close()

  def insert_or_update_or_delete(self, sql, params=(), isbackinsertid=False):
    conn = self._getConnection()
    c = None
    try:
      c = conn.cursor()
      c.execute(sql, params)
      conn.commit()
      if isbackinsertid == True:
        c.execute('select last_insert_id()')
        yz = c.fetchone()
        return yz[0]
      else:
        return 0
    except BaseException as e:
      logging.error('Error %d: %s, %s' % (e.args[0], e.args[1], traceback.format_exc()))
      return 1
    finally:
      if None != c:
        c.close()
      if None != conn:
        conn.close()

  def insert_more(self, sql, params=[]):
    conn = self._getConnection()
    c = None
    try:
      c = conn.cursor()
      c.executemany(sql, params)
      conn.commit()
      return 0
    except BaseException as e:
      logging.error('Error %d: %s, %s' % (e.args[0], e.args[1], traceback.format_exc()))
      return 1
    finally:
      if None != c:
        c.close()
      if None != conn:
        conn.close()

  def _get_count_sql(self, sql):
    sql = sql.lower()
    a = ' select count(*) ' + sql[sql.find(' from '):-1]
    return a

  def _get_page_sql(self, sql, page, size):
    f = (page - 1) * size
    sql = sql + ' limit ' + str(size) + ' offset ' + str(f)
    return sql

  def find_page(self, sql, params=(), mapcol=None, page=1, size=15):
    conn = self._getConnection()
    c = None
    page_result = {'total': 0, 'pagetotal': 0, 'page': page, 'size': size, 'data': []}
    try:
      c = conn.cursor()
      countsql = self._get_count_sql(sql)
      pagesql = self._get_page_sql(sql, page, size)
      c.execute(countsql, params)
      total = c.fetchone()
      if None == total or 0 == int(total[0]):
        return page_result
      page_result['total'] = int(total[0])
      page_result['pagetotal'] = int((page_result['total'] + size - 1) / size)
      c.execute(pagesql, params)
      yz = c.fetchall()
      if yz == None:
        return page_result
      if mapcol == None:
        page_result['data'] = yz
        return page_result
      result = []
      for y in yz:
        result.append(self._result_to_map(y, mapcol))
      page_result['data'] = result
      return page_result
    except BaseException as e:
      logging.error('Error %d: %s, %s' % (e.args[0], e.args[1], traceback.format_exc()))
      return page_result
    finally:
      if None != c:
        c.close()
      if None != conn:
        conn.close()

  def _result_to_map(self, yz, mapcol):
    if yz == None or mapcol == None:
      return None
    if len(yz) != len(mapcol):
      return None
    i = 0
    map = {}
    for y in yz:
      map[mapcol[i]] = y
      i = i + 1
    return map


_mysql_utils = {}


def get_mysql_utils(host: str, port: int, user: str, passwd: str, db: str, charset: str) -> MysqlUtils:
  global _mysql_utils
  key = '%(host)s_%(port)s_%(user)s_%(db)s' % {
      'host': host, 'port': str(port), 'user': user, 'db': db}
  if None == _mysql_utils.get(key, None):
    mysqlUtils = MysqlUtils(host=host, port=port, user=user, passwd=passwd, db=db, charset=charset)
    _mysql_utils[key] = mysqlUtils

  return _mysql_utils[key]
