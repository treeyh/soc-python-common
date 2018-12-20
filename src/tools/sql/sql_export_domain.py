# -*- encoding: utf-8 -*-

import os
import sys
import re

path = os.path.split(os.path.realpath(__file__))[0]
sys.path.append(path + os.sep + '..')

from helper import str_helper, file_helper, pymysql_helper

'''
select `TABLE_NAME` from information_schema.`TABLES` where TABLE_SCHEMA = 'merchant_db' and TABLE_TYPE = 'BASE TABLE';

select TABLE_SCHEMA, TABLE_NAME, COLUMN_NAME, IS_NULLABLE, DATA_TYPE, CHARACTER_MAXIMUM_LENGTH, COLUMN_COMMENT , ORDINAL_POSITION 
 from information_schema.`columns` ORDER BY TABLE_SCHEMA DESC, TABLE_NAME DESC, ORDINAL_POSITION ASC;
'''

_get_m_db_name_sql = ''' select `TABLE_NAME` from information_schema.`TABLES` where TABLE_SCHEMA = %s and TABLE_TYPE = 'BASE TABLE';  '''
_get_m_db_name_col = ['TABLE_NAME']

_get_o_db_name_sql = ''' SELECT TABLE_NAME , TABLE_TYPE, COMMENTS from user_tab_comments WHERE TABLE_TYPE = 'TABLE';  '''
_get_o_db_name_col = ['TABLE_NAME', 'TABLE_TYPE', 'COMMENTS']


def get_db_table_list(dbName):
    global _get_m_db_name_sql
    global _get_m_db_name_col
    global _get_o_db_name_sql
    global _get_o_db_name_col
    global _db_type
    global _db

    if 'm' == _db_type:
        params = (dbName)
        tableNames = pymysql_helper.get_mysql_helper(**_db).find_all(_get_m_db_name_sql, params, _get_m_db_name_col)
        return tableNames
    elif 'o' == _db_type:
        tableNames = oracle_helper.find_all(_get_o_db_name_sql, params, _get_o_db_name_col)
        return tableNames
    else:
        return []


_get_m_db_column_sql = ''' select TABLE_SCHEMA, TABLE_NAME, COLUMN_NAME, IS_NULLABLE, DATA_TYPE, CHARACTER_MAXIMUM_LENGTH, COLUMN_COMMENT , ORDINAL_POSITION 
                         from information_schema.`columns` where TABLE_SCHEMA = %s and TABLE_NAME = %s  ORDER BY TABLE_SCHEMA DESC, TABLE_NAME DESC, ORDINAL_POSITION ASC;  '''
_get_o_db_column_sql = ''' SELECT 'TABLE_SCHEMA' AS TABLE_SCHEMA, a.TABLE_NAME, a.COLUMN_NAME, a.NULLABLE AS IS_NULLABLE, a.DATA_TYPE, a.DATA_LENGTH AS CHARACTER_MAXIMUM_LENGTH , b.COMMENTS AS COLUMN_COMMENT , a.COLUMN_ID AS ORDINAL_POSITION  from USER_TAB_COLS a, user_col_comments b WHERE a.TABLE_NAME = b.TABLE_NAME(+) AND a.COLUMN_NAME = b.COLUMN_NAME(+) AND a.TABLE_NAME = %s ORDER BY a.TABLE_NAME ASC, a.COLUMN_ID ASC   '''
_get_m_db_column_col = ['TABLE_SCHEMA', 'TABLE_NAME', 'COLUMN_NAME', 'IS_NULLABLE', 'DATA_TYPE',
                        'CHARACTER_MAXIMUM_LENGTH', 'COLUMN_COMMENT', 'ORDINAL_POSITION']


def get_db_table_column_list(dbName, tableName):
    global _get_m_db_column_sql
    global _get_m_db_column_col
    global _get_o_db_column_sql
    global _db_type
    global _db
    if 'm' == _db_type:
        params = (dbName, tableName)
        tableColumns = pymysql_helper.get_mysql_helper(**_db).find_all(_get_m_db_column_sql, params,
                                                                       _get_m_db_column_col)
        return tableColumns
    elif 'o' == _db_type:
        params = (tableName)
        tableNames = oracle_helper.find_all(_get_o_db_column_sql, params, _get_m_db_column_col)
        return tableNames
    else:
        return []


def format_domain():
    global _table_list
    global _db_name
    global _file_path
    global _db

    tableNames = get_db_table_list(_db_name)
    print tableNames
    if None == tableNames:
        print 'NULL INFO'
    tab = '\t'
    linesep = file_helper.get_line_sep()
    for tableName in tableNames:
        tbname = tableName['TABLE_NAME']
        if tbname not in _table_list or len(_table_list) > 0:
            continue
        classInfo = u'public class %s { %s' % (tableName['TABLE_NAME'], linesep)
        tableColumns = get_db_table_column_list(_db_name, tableName['TABLE_NAME'])
        print tableColumns
        if None == tableColumns:
            continue
        for column in tableColumns:
            t = 'UnKnow'
            c = column['DATA_TYPE'].lower()
            if c in ['varchar', 'text', 'char', 'longtext', 'enum', 'mediumtext', 'tinytext']:
                t = 'String'
            elif c in ['int', 'tinyint', 'smallint', 'mediumint', 'bit']:
                t = 'Integer'
            elif c in ['bigint']:
                t = 'Long'
            elif c in ['float', 'double', 'boolean', 'decimal', 'peal']:
                t = 'Double'
            elif c in ['date', 'datetime', 'timestamp', 'time', 'year']:
                t = 'Date'

            classInfo = '''%s%s%s/* %s%s * %s%s%s */%s%sprivate %s %s;%s''' % (
            classInfo, linesep, tab, linesep, tab, column['COLUMN_COMMENT'], linesep, tab, linesep, tab, t,
            column['COLUMN_NAME'], linesep)

        classInfo = '%s}' % (classInfo)

        file_helper.write_file(_file_path + tableName['TABLE_NAME'] + '.txt', classInfo + os.linesep, 'a')


def format_json_domain():
    global _table_list
    global _db_name
    global _file_path
    global _db
    tableNames = get_db_table_list(_db_name)
    print tableNames
    if None == tableNames:
        print 'NULL INFO'
    tab = '\t'
    linesep = file_helper.get_line_sep()
    for tableName in tableNames:
        tbname = tableName['TABLE_NAME']
        if tbname not in _table_list:
            continue
        classInfo = u'{%s' % (linesep)
        tableColumns = get_db_table_column_list(_db_name, tableName['TABLE_NAME'])
        print tableColumns
        if None == tableColumns:
            continue
        for column in tableColumns:
            t = 'UnKnow'
            c = column['DATA_TYPE'].lower()
            if c in ['varchar', 'text', 'char', 'longtext', 'enum', 'mediumtext', 'tinytext']:
                t = '"%s" : ""' % (column['COLUMN_NAME'])
            elif c in ['int', 'tinyint', 'smallint', 'mediumint', 'bit']:
                t = '"%s" : 0 ' % (column['COLUMN_NAME'])
            elif c in ['bigint']:
                t = '"%s" : 0 ' % (column['COLUMN_NAME'])
            elif c in ['float', 'double', 'boolean', 'decimal', 'peal']:
                t = '"%s" : 0.0 ' % (column['COLUMN_NAME'])
            elif c in ['date', 'datetime', 'timestamp', 'time', 'year']:
                t = '"%s" : "1970-01-01 00:00:00" ' % (column['COLUMN_NAME'])

            classInfo = '%s%s,%s' % (classInfo, t, linesep)
            # classInfo = '''%s%s%s/* %s%s * %s%s%s */%s%sprivate %s %s;%s''' % (classInfo, linesep, tab, linesep, tab, column['COLUMN_COMMENT'], linesep, tab, linesep, tab, t, column['COLUMN_NAME'], linesep)

        classInfo = '%s}' % (classInfo)

        file_helper.write_file(_file_path + tableName['TABLE_NAME'] + '.txt', classInfo + os.linesep, 'a')


def format_select_sql():
    global _table_list
    global _db_name
    global _file_path
    global _db

    tableNames = get_db_table_list(_db_name)
    print tableNames
    if None == tableNames:
        print 'NULL INFO'
    tab = '\t'
    linesep = file_helper.get_line_sep()
    for tableName in tableNames:
        tbname = tableName['TABLE_NAME']
        if tbname not in _table_list and len(_table_list) > 0:
            continue
        sqlInfo = u'SELECT'
        tableColumns = get_db_table_column_list(_db_name, tableName['TABLE_NAME'])
        print tableColumns
        if None == tableColumns:
            continue
        for column in tableColumns:
            sqlInfo = '%s a.`%s`,' % (sqlInfo, column['COLUMN_NAME'])
        sqlInfo = '%s FROM `%s` AS a ' % (sqlInfo[0:-1], tableName['TABLE_NAME'])
        file_helper.write_file(_file_path + tableName['TABLE_NAME'] + '.txt', sqlInfo + os.linesep, 'a')


def format_insert_sql():
    global _table_list
    global _db_name
    global _file_path
    global _db
    tableNames = get_db_table_list(_db_name)
    print tableNames
    if None == tableNames:
        print 'NULL INFO'
    tab = '\t'
    linesep = file_helper.get_line_sep()
    for tableName in tableNames:
        tbname = tableName['TABLE_NAME']
        if tbname not in _table_list and len(_table_list) > 0:
            continue
        sqlInfo = u'INSERT INTO %s(' % (tableName['TABLE_NAME'])
        pinfo = ''
        tableColumns = get_db_table_column_list(_db_name, tableName['TABLE_NAME'])
        print tableColumns
        if None == tableColumns:
            continue
        for column in tableColumns:
            sqlInfo = '%s `%s`,' % (sqlInfo, column['COLUMN_NAME'])
            pinfo = pinfo + ' %s,'
        sqlInfo = '%s ) VALUES (%s) ' % (sqlInfo[0:-1], pinfo[0:-1])
        file_helper.write_file(_file_path + tableName['TABLE_NAME'] + '.txt', sqlInfo + os.linesep, 'a')


def format_update_sql():
    global _table_list
    global _db_name
    global _file_path
    global _db
    tableNames = get_db_table_list(_db_name)
    print tableNames
    if None == tableNames:
        print 'NULL INFO'
    tab = '\t'
    linesep = file_helper.get_line_sep()
    for tableName in tableNames:
        tbname = tableName['TABLE_NAME']
        if tbname not in _table_list and len(_table_list) > 0:
            continue
        sqlInfo = u'UPDATE `%s` SET ' % (tableName['TABLE_NAME'])
        pinfo = ''
        tableColumns = get_db_table_column_list(_db_name, tableName['TABLE_NAME'])
        print tableColumns
        if None == tableColumns:
            continue
        for column in tableColumns:
            # sqlInfo = '%s `%s` = ? ,' % (sqlInfo, column['COLUMN_NAME'])
            sqlInfo = sqlInfo + '`' + column['COLUMN_NAME'] + '` = %s ,'
        # sqlInfo = '%s ) VALUES (%s) ' % (sqlInfo[0:-1], pinfo[0:-1])
        sqlInfo = sqlInfo[0:-1]
        file_helper.write_file(_file_path + tableName['TABLE_NAME'] + '.txt', sqlInfo + os.linesep, 'a')


def format_column_list():
    global _table_list
    global _db_name
    global _file_path
    global _db
    tableNames = get_db_table_list(_db_name)
    print tableNames
    if None == tableNames:
        print 'NULL INFO'
    tab = '\t'
    linesep = file_helper.get_line_sep()
    for tableName in tableNames:
        tbname = tableName['TABLE_NAME']
        if tbname not in _table_list and len(_table_list) > 0:
            continue
        sqlInfo = u'['
        tableColumns = get_db_table_column_list(_db_name, tableName['TABLE_NAME'])
        print tableColumns
        if None == tableColumns:
            continue
        for column in tableColumns:
            sqlInfo = "%s'%s', " % (sqlInfo, column['COLUMN_NAME'])
        sqlInfo = '%s ]' % (sqlInfo[0:-2])
        file_helper.write_file(_file_path + tableName['TABLE_NAME'] + '.txt', sqlInfo + os.linesep, 'a')


def format_php_domain():
    global _table_list
    global _db_name
    global _file_path
    global _db
    tableNames = get_db_table_list(_db_name)
    print tableNames
    if None == tableNames:
        print 'NULL INFO'
    tab = '\t'
    linesep = file_helper.get_line_sep()
    for tableName in tableNames:
        classInfo = u'public class %s { %s' % (tableName['TABLE_NAME'], linesep)
        tableColumns = get_db_table_column_list(_db_name, tableName['TABLE_NAME'])
        print tableColumns
        if None == tableColumns:
            continue
        for column in tableColumns:
            t = 'UnKnow'
            c = column['DATA_TYPE'].lower()
            if c in ['varchar', 'text', 'char', 'longtext', 'enum', 'mediumtext', 'tinytext']:
                t = "''"
            elif c in ['int', 'tinyint', 'smallint', 'mediumint', 'bit']:
                t = '0'
            elif c in ['bigint']:
                t = '0'
            elif c in ['float', 'double', 'boolean', 'decimal', 'peal']:
                t = '0'
            elif c in ['date', 'datetime', 'timestamp', 'time', 'year']:
                t = "''"

            classInfo = '''%s%s%s/* %s%s * %s%s%s */%s%spublic $%s = %s;%s''' % (
            classInfo, linesep, tab, linesep, tab, column['COLUMN_COMMENT'], linesep, tab, linesep, tab,
            column['COLUMN_NAME'], t, linesep)

        classInfo = '%s}' % (classInfo)

        file_helper.write_file(_file_path + tableName['TABLE_NAME'] + '.txt', classInfo + os.linesep, 'a')


def format_php_info():
    global _table_list
    global _db_name
    global _file_path
    global _db
    tableNames = get_db_table_list(_db_name)
    print tableNames
    if None == tableNames:
        print 'NULL INFO'
    tab = '\t'
    linesep = file_helper.get_line_sep()
    for tableName in tableNames:
        if tableName['TABLE_NAME'] not in _table_list:
            continue
        tableColumns = get_db_table_column_list(_db_name, tableName['TABLE_NAME'])
        print tableColumns
        if None == tableColumns:
            continue
        classInfo = ''
        for column in tableColumns:
            classInfo = '''%s%s//%s%s%s$item['%s'] = %s;%s''' % (
            classInfo, tab, column['COLUMN_COMMENT'], linesep, tab, column['COLUMN_NAME'], '""', linesep)

        file_helper.write_file(_file_path + tableName['TABLE_NAME'] + '.txt', classInfo + os.linesep, 'a')


def format_php_info_object():
    global _table_list
    global _db_name
    global _file_path
    global _db
    tableNames = get_db_table_list(_db_name)
    print tableNames
    if None == tableNames:
        print 'NULL INFO'
    tab = '\t'
    linesep = file_helper.get_line_sep()
    for tableName in tableNames:
        if tableName['TABLE_NAME'] not in _table_list:
            continue
        tableColumns = get_db_table_column_list(_db_name, tableName['TABLE_NAME'])
        print tableColumns
        if None == tableColumns:
            continue
        classInfo = ''
        for column in tableColumns:
            classInfo = '''%s%s//%s%s%s$item->%s = %s;%s''' % (
            classInfo, tab, column['COLUMN_COMMENT'], linesep, tab, column['COLUMN_NAME'], '""', linesep)

        file_helper.write_file(_file_path + tableName['TABLE_NAME'] + '.txt', classInfo + os.linesep, 'a')


def format_php_params():
    global _table_list
    global _db_name
    global _file_path
    global _db
    tableNames = get_db_table_list(_db_name)
    print tableNames
    if None == tableNames:
        print 'NULL INFO'
    tab = '\t'
    linesep = file_helper.get_line_sep()
    for tableName in tableNames:
        tbname = tableName['TABLE_NAME']
        if tbname not in _table_list:
            continue
        sqlInfo = u'SELECT '
        tableColumns = get_db_table_column_list(_db_name, tableName['TABLE_NAME'])
        print tableColumns
        if None == tableColumns:
            continue
        for column in tableColumns:
            sqlInfo = '%s $%s ,' % (sqlInfo, column['COLUMN_NAME'])
        sqlInfo = '%s FROM `%s` AS a ' % (sqlInfo[0:-1], tableName['TABLE_NAME'])
        file_helper.write_file(_file_path + tableName['TABLE_NAME'] + '.txt', sqlInfo + os.linesep, 'a')


def format_php_data_params():
    global _table_list
    global _db_name
    global _file_path
    global _db
    tableNames = get_db_table_list(_db_name)
    print tableNames
    if None == tableNames:
        print 'NULL INFO'
    tab = '\t'
    linesep = file_helper.get_line_sep()
    for tableName in tableNames:
        tbname = tableName['TABLE_NAME']
        if tbname not in _table_list:
            continue
        sqlInfo = u'SELECT '
        tableColumns = get_db_table_column_list(_db_name, tableName['TABLE_NAME'])
        print tableColumns
        if None == tableColumns:
            continue
        for column in tableColumns:
            sqlInfo = '%s \'%s\' => $%s , %s' % (sqlInfo, column['COLUMN_NAME'], column['COLUMN_NAME'], os.linesep)
        sqlInfo = '%s FROM `%s` AS a ' % (sqlInfo[0:-1], tableName['TABLE_NAME'])
        file_helper.write_file(_file_path + tableName['TABLE_NAME'] + '.txt', sqlInfo + os.linesep, 'a')


def format_php_data_domain():
    global _table_list
    global _db_name
    global _file_path
    global _db
    tableNames = get_db_table_list(_db_name)
    print tableNames
    if None == tableNames:
        print 'NULL TABLE'

    temp = file_helper.read_all_file('./temp.php')
    linesep = file_helper.get_line_sep()
    for tableName in tableNames:
        tbname = tableName['TABLE_NAME']
        if tbname not in _table_list:
            continue

        tbs = tbname.split('_')
        tbs2 = []
        for tb in tbs:
            tbs2.append(tb.capitalize())
        dmName = 'Data' + ''.join(tbs2)

        tableColumns = get_db_table_column_list(_db_name, tbname)
        if None == tableColumns:
            continue
        fields = ''
        fid = tableColumns[0]['COLUMN_NAME']
        fname = tableColumns[0]['COLUMN_NAME']

        for column in tableColumns:
            t = 'string'
            c = column['DATA_TYPE'].lower()
            if c in ['varchar', 'text', 'char', 'longtext', 'enum', 'mediumtext', 'tinytext']:
                t = "string"
            elif c in ['int', 'tinyint', 'smallint', 'mediumint', 'bit']:
                t = 'int'
            elif c in ['bigint']:
                t = 'int'
            elif c in ['float', 'double', 'boolean', 'decimal', 'peal']:
                t = 'float'
            elif c in ['date', 'datetime', 'timestamp', 'time', 'year']:
                t = "string"

            if 'name' == column['COLUMN_NAME']:
                fname = column['COLUMN_NAME']
            if 'title' == column['COLUMN_NAME']:
                fname = column['COLUMN_NAME']
            fields = '''%s%s        $fields['%s'] = $this->setFieldInfo('%s' ,'%s' ,0 , '%s'); ''' % (
            fields, linesep, column['COLUMN_NAME'], column['COLUMN_NAME'], t, column['COLUMN_COMMENT'])

        domain = temp.replace('{DomainName}', dmName)
        domain = domain.replace('{TableName}', tbname)
        domain = domain.replace('{fields}', fields)
        domain = domain.replace('{id}', fid)
        domain = domain.replace('{name}', fname)
        file_helper.write_file(_file_path + dmName + '.php', domain + os.linesep, 'a')

    return


_db_type = 'm'  # 数据库类型，m表示mysql，o表示oracle
# _db_name = 'soc_stock'
# _db_name = 'testdb'
_db_name = 'cloudparking'
_table_list = ['cloudparking_etcp_order_relation', 'cloudparking_finance', 'cloudparking_finance_coupon_detail']
_file_path = os.path.split(os.path.realpath(__file__))[0] + os.sep + 'domain' + os.sep

_db = {
    # # 'host' : '192.168.18.187', 
    # 'host' : '192.168.36.55',
    # 'user' : 'root', 
    # # 'passwd' : 'mysqlpw',
    # 'passwd' : 'fXL2bO$RQgaRS^lH',
    # # 'db' : 'soc_stock',
    # # 'db' : 'soc_server_monitor',
    # 'db' : 'testdb',
    # 'charset' : 'utf8', 
    # 'port' : 3306,

    # 'host' : '192.168.77.66',
    # 'user' : 'logview',
    # 'passwd' : 'logview',
    # 'db' : 'http_status',
    # 'charset' : 'utf8',
    # 'port' : 3306,

    'host': '10.209.44.12',
    'user': 'cloudparking',
    'passwd': '234fsdsdkjj',
    'db': 'cloudparking',
    'charset': 'utf8',
    'port': 10043,
}

if __name__ == '__main__':
    import sys

    reload(sys)
    sys.setdefaultencoding('utf-8')
    # format_php_data_domain()
    # format_domain()   #java bean
    # format_select_sql()   #select 语句
    # format_update_sql()
    format_insert_sql()
    # format_column_list()
    # format_php_params()    #php方法参数
    # format_php_data_params()
    # format_json_domain()
