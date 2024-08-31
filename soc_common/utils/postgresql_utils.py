# -*- encoding: utf-8 -*-

import sys
import logging
import traceback

from psycopg_pool import ConnectionPool


class PostgresqlUtils(object):
  """Postgresql Utils

  Args:
      object (_type_): _description_
  """

  def __init__(self, host, port, user, passwd, db, sslmode = 'disable', timeZone = 'Asia/Shanghai'):
    super(PostgresqlUtils, self).__init__()

    self.host = host
    self.user = user
    self.passwd = passwd
    self.db = db
    self.sslmode = sslmode
    self.port = port

    # self.dsn = 'user=%s password=%s dbname=%s port=%s sslmode=%s timezone=%s' % (user, passwd, db, str(port), sslmode, timeZone)
    self.dsn = 'postgresql://%s:%s@%s:%s/%s?sslmode=%s' % (user, passwd, host, str(port), db, sslmode)

    try:
      self.pool = ConnectionPool(self.dsn)
      self.pool.open()
    except BaseException as e:
      logging.error('Postgresql init Error %s' % (e.args))
      sys.exit(1)


  def find_one(self, sql, params=(), mapcol=None):
    with self.pool.connection() as conn:
      result = None
      try:
        yz = conn.execute(sql, params).fetchone()
        if yz == None:
          return None
        if mapcol == None:
          return yz
        result = self._result_to_map(yz, mapcol)
        return result
      except BaseException as e:
        logging.error('Error %s' % (e.args))
        return result

  def find_all(self, sql, params=(), mapcol=None):
    with self.pool.connection() as conn:
      try:
        yz = conn.execute(sql, params).fetchall()
        if yz == None:
          return None
        if mapcol == None:
          return yz
        result = []
        for y in yz:
          result.append(self._result_to_map(y, mapcol))
        return result
      except BaseException as e:
        logging.error('sql %s, %s ;Error %s' % (sql, str(params), e.args))
        return result

  def insert_or_update_or_delete(self, sql, params=(), isbackinsertid=False):
    # INSERT INTO charts (name, file_name, scale,) VALUES (%(name)s, %(fileName)s, %(scale)s) RETURNING id;
    with self.pool.connection() as conn:
      try:
        if isbackinsertid == True:
          cursor = conn.execute(sql, params)
          yz = cursor.fetchone()
          conn.commit()
          return yz[0]
        else:
          conn.execute(sql, params).commit()
          return 0
      except BaseException as e:
        logging.error('Error %s, %s, %s, %s' % (e.args, sql, params, traceback.format_exc()))
        return 1

  def insert_more(self, sql, params=[]):
    with self.pool.connection() as conn:
      try:
        conn.executemany(sql, params).commit()
        return 0
      except BaseException as e:
        logging.error('Error %s, %s' % (e.args, traceback.format_exc()))
        return 1

  def _get_count_sql(self, sql):
    sql = sql.lower()
    a = ' select count(*) ' + sql[sql.find(' from '):-1]
    return a

  def _get_page_sql(self, sql, page, size):
    f = (page - 1) * size
    sql = sql + ' limit ' + str(size) + ' offset ' + str(f)
    return sql

  def find_page(self, sql, params=(), mapcol=None, page=1, size=15):
    with self.pool.connection() as conn:
      page_result = {'total': 0, 'pagetotal': 0, 'page': page, 'size': size, 'data': []}
      try:
        countsql = self._get_count_sql(sql)
        pagesql = self._get_page_sql(sql, page, size)
        total = conn.execute(countsql, params).fetchone()
        if None == total or 0 == int(total[0]):
          return page_result
        page_result['total'] = int(total[0])
        page_result['pagetotal'] = int((page_result['total'] + size - 1) / size)
        yz = conn.execute(pagesql, params).fetchall()
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


_postgresql_utils = {}


def get_postgresql_utils(host: str, port: int, user: str, passwd: str, db: str, sslmode = 'disable', timeZone = 'Asia/Shanghai') -> PostgresqlUtils:
  global _postgresql_utils
  key = '%(host)s_%(port)s_%(user)s_%(db)s_%(sslmode)s_%(timeZone)s' % {
      'host': host, 'port': str(port), 'user': user, 'db': db, 'sslmode': sslmode, 'timeZone': timeZone}
  if None == _postgresql_utils.get(key, None):
    postgresqlUtils = PostgresqlUtils(host=host, port=port, user=user, passwd=passwd, db=db, sslmode=sslmode, timeZone=timeZone)
    _postgresql_utils[key] = postgresqlUtils

  return _postgresql_utils[key]
