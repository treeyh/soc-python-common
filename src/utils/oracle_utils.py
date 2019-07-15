#-*- encoding: utf-8 -*-

import time
import cx_Oracle


_host = '192.168.23.107'
_user = 'vision'
_passwd = 'W83fKNArKM'
_db = 'ucms'
_charset = 'utf8'
_port = 1521

# _host = '192.168.99.83'
# _user = 'root'
# _passwd = 'fXL2bO$RQgaRS^lH'
# _db = 'work_manager'
# _charset = 'utf8'
# _port = 3306


def _getConnection():
    global _host, _user, _passwd, _db, _charset, _port
    i=0
    count = 5
    tns=cx_Oracle.makedsn(host = _host, port = _port,service_name = _db)
    while(1):
        try:
            i=i+1
            conn = cx_Oracle.connect(_user, _passwd, tns)
            return conn
        except cx_Oracle.Error:
            if(i>= 3):
                print('sql connection get count %d ' % (count))
                return None
            time.sleep(5)


# def mysql_encode(val):
#     return cx_Oracle.escape_string(val)


def insert_or_update_or_delete(sql, params = (), isbackinsertid = False):
    conn=_getConnection()
    c = None
    try:
        c=conn.cursor()
        # print(sql
        # print(params
        c.execute(sql, params)
        conn.commit()
        if isbackinsertid == True:
            c.execute('select last_insert_id()')
            yz = c.fetchone()
            return yz[0]
        else:
            return 0
    except cx_Oracle.Error:
        return 1
    finally:
        if None != c:
            c.close()
        if None != conn:
            conn.close()

def insert_more(sql, params = []):
    conn=_getConnection()
    c = None
    try:
        c=conn.cursor()
        c.executemany(sql, params)
        conn.commit()
        return 0
    except cx_Oracle.Error:
        return 1
    finally:
        if None != c:
            c.close()
        if None != conn:
            conn.close()

def find_one(sql, params= {}, mapcol=None):
    conn=_getConnection()
    c = None
    result = None
    try:
        c=conn.cursor()
        c.execute(sql, params)
        yz = c.fetchone()
        if yz == None:
            return None
        if mapcol == None:
            return yz
        result = _result_to_map(yz, mapcol)
        return result
    except cx_Oracle.Error:
        return result
    finally:
        if None != c:
            c.close()
        if None != conn:
            conn.close()

def find_all(sql, params={}, mapcol=None):
    conn=_getConnection()
    c = None
    try:
        c=conn.cursor()
        c.execute(sql, params)
        yz = c.fetchall()
        if yz == None:
            return None
        if mapcol == None:
            return yz
        result = []
        for y in yz:
            result.append( _result_to_map(y, mapcol))
        return result
    except cx_Oracle.Error:
        return []
    finally:
        if None != c:
            c.close()
        if None != conn:
            conn.close()

def _get_count_sql(sql):
    sql = sql.lower()
    a = ' select count(1) ' + sql[sql.find(' from '):-1]
    return a

def _get_page_sql(sql, page, size):
    f = (page - 1) * size
    sql = sql + ' limit ' + str(f) + ', ' + str(size)
    return sql

def find_page(sql, params={}, mapcol=None, page=1, size = 15):
    conn=_getConnection()
    c = None
    page_result = {'total':0,'pagetotal':0, 'page':page, 'size':size, 'data':[]}
    try:
        c=conn.cursor()
        countsql = _get_count_sql(sql)
        pagesql = _get_page_sql(sql, page, size)
        c.execute(countsql, params)
        total = c.fetchone()
        if None == total or 0 == int(total[0]):
            return page_result
        page_result['total'] = int(total[0])
        page_result['pagetotal'] = int((page_result['total'] + size - 1)/size)
        c.execute(pagesql, params)
        yz = c.fetchall()
        if yz == None:
            return page_result
        if mapcol == None:
            page_result['data'] = yz
            return page_result
        result = []
        for y in yz:
            result.append( _result_to_map(y, mapcol))
        page_result['data'] = result
        return page_result
    except cx_Oracle.Error:
        return page_result
    finally:
        if None != c:
            c.close()
        if None != conn:
            conn.close()


def _result_to_map(yz, mapcol):
    if yz == None or mapcol == None:
        return None
    if len(yz) != len(mapcol):
        return None
    i = 0
    map = {}
    for y in yz:
        map[mapcol[i]] = y
        i = i +1
    return map
