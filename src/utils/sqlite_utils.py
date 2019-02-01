# -*- encoding: utf-8 -*-

import sqlite3
import traceback


class SqliteUtils(object):
    """docstring for MysqlHelper"""

    def __init__(self, db_path, init_sql):
        super(SqliteUtils, self).__init__()

        self._db_path = db_path
        self._init_sql = init_sql
        self._init_type = False

    def _get_connection(self):
        try:
            conn = sqlite3.connect('file:%s' % self._db_path, uri=True)
            if not self._init_type:
                conn.execute(self._init_sql)
                self._init_type = True
        except Exception as e:
            print('SqliteUtils error: %s' % traceback.format_exc())
            raise e
        return conn

    def insert_or_update_or_delete(self, sql, params=(), is_back_intert_id=False):
        conn = self._get_connection()
        c = None
        try:
            c = conn.cursor()
            c.execute(sql, params)
            conn.commit()
            if is_back_intert_id is True:
                c.execute('select last_insert_rowid()')
                yz = c.fetchone()
                return yz[0]
            else:
                return 0
        except Exception as e:
            print('SqliteUtils error: %s' % traceback.format_exc())
            return 1
        finally:
            if None is not c:
                c.close()
            if None is not conn:
                conn.close()

    def insert_more(self, sql, params=[]):
        conn = self._get_connection()
        c = None
        try:
            c = conn.cursor()
            c.executemany(sql, params)
            conn.commit()
            return 0
        except Exception as e:
            print('SqliteUtils error: %s' % traceback.format_exc())
            return 1
        finally:
            if None is not c:
                c.close()
            if None is not conn:
                conn.close()

    def find_one(self, sql, params=(), mapcol=None):
        conn = self._get_connection()
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
        except Exception as e:
            print('SqliteUtils error: %s' % traceback.format_exc())
            return 1
        finally:
            if None is not c:
                c.close()
            if None is not conn:
                conn.close()

    def find_all(self, sql, params=(), mapcol=None):
        conn = self._get_connection()
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
        except Exception as e:
            print('SqliteUtils error: %s' % traceback.format_exc())
            return 1
        finally:
            if None is not c:
                c.close()
            if None is not conn:
                conn.close()

    def _get_count_sql(self, sql):
        sql = sql.lower()
        a = ' select count(1) ' + sql[sql.find(' from '):-1]
        return a

    def _get_page_sql(self, sql, page, size):
        f = (page - 1) * size
        sql = sql + ' limit ' + str(f) + ', ' + str(size)
        return sql

    def find_page(self, sql, params=(), mapcol=None, page=1, size=15):
        conn = self._get_connection()
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
        except Exception as e:
            print('SqliteUtils error: %s' % traceback.format_exc())
            return 1
        finally:
            if None is not c:
                c.close()
            if None is not conn:
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


_sqlite_utils = {}


def get_sqlite_utils(db_path, init_sql):
    global _sqlite_utils
    key = '%(db_path)s' % {'db_path': db_path}
    if None is _sqlite_utils.get(key, None):
        sqliteUtils = SqliteUtils(db_path=db_path, init_sql=init_sql)
        _sqlite_utils[key] = sqliteUtils

    return _sqlite_utils[key]
