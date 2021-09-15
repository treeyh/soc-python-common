# -*- encoding: utf-8 -*-

from soc_common.utils import str_utils, file_utils, mysql_utils
import os
import sys
import re

path = os.path.split(os.path.realpath(__file__))[0]
sys.path.append(path + os.sep + '..' + os.sep + '..')


'''
select `TABLE_NAME`, `TABLE_COMMENT` from information_schema.`TABLES` where TABLE_SCHEMA = 'merchant_db' and TABLE_TYPE = 'BASE TABLE';

select TABLE_SCHEMA, TABLE_NAME, COLUMN_NAME, IS_NULLABLE, DATA_TYPE, CHARACTER_MAXIMUM_LENGTH, COLUMN_COMMENT , ORDINAL_POSITION 
 from information_schema.`columns` ORDER BY TABLE_SCHEMA DESC, TABLE_NAME DESC, ORDINAL_POSITION ASC;
'''

_get_m_db_name_sql = ''' select `TABLE_NAME`, `TABLE_COMMENT` from information_schema.`TABLES` where TABLE_SCHEMA = %s and TABLE_TYPE = 'BASE TABLE';  '''
_get_m_db_name_col = ['TABLE_NAME', 'TABLE_COMMENT']

_get_o_db_name_sql = ''' SELECT TABLE_NAME , TABLE_TYPE, COMMENTS from user_tab_comments WHERE TABLE_TYPE = 'TABLE';  '''
_get_o_db_name_col = ['TABLE_NAME', 'TABLE_TYPE', 'COMMENTS']


def get_db_table_list(dbName):
  global _get_m_db_name_sql
  global _get_m_db_name_col
  global _get_o_db_name_sql
  global _get_o_db_name_col
  global _db_type
  global _db

  params = (dbName)
  tableNames = mysql_utils.get_mysql_utils(
      **_db).find_all(_get_m_db_name_sql, params, _get_m_db_name_col)
  return tableNames


_get_m_db_column_sql = ''' select TABLE_SCHEMA, TABLE_NAME, COLUMN_NAME, IS_NULLABLE, DATA_TYPE, CHARACTER_MAXIMUM_LENGTH, COLUMN_COMMENT , 
                                  ORDINAL_POSITION , COLUMN_DEFAULT, NUMERIC_PRECISION, NUMERIC_SCALE, COLUMN_KEY, EXTRA 
                         from information_schema.`columns` where TABLE_SCHEMA = %s and TABLE_NAME = %s 
                        ORDER BY TABLE_SCHEMA DESC, TABLE_NAME DESC, ORDINAL_POSITION ASC;  '''
# _get_o_db_column_sql = ''' SELECT 'TABLE_SCHEMA' AS TABLE_SCHEMA, a.TABLE_NAME, a.COLUMN_NAME, a.NULLABLE AS IS_NULLABLE, a.DATA_TYPE, a.DATA_LENGTH AS CHARACTER_MAXIMUM_LENGTH , b.COMMENTS AS COLUMN_COMMENT , a.COLUMN_ID AS ORDINAL_POSITION  from USER_TAB_COLS a, user_col_comments b WHERE a.TABLE_NAME = b.TABLE_NAME(+) AND a.COLUMN_NAME = b.COLUMN_NAME(+) AND a.TABLE_NAME = %s ORDER BY a.TABLE_NAME ASC, a.COLUMN_ID ASC   '''
_get_m_db_column_col = ['TABLE_SCHEMA', 'TABLE_NAME', 'COLUMN_NAME', 'IS_NULLABLE', 'DATA_TYPE',
                        'CHARACTER_MAXIMUM_LENGTH', 'COLUMN_COMMENT', 'ORDINAL_POSITION', 'COLUMN_DEFAULT',
                        'NUMERIC_PRECISION', 'NUMERIC_SCALE', 'COLUMN_KEY', 'EXTRA']


def get_db_table_column_list(dbName, tableName):
  global _get_m_db_column_sql
  global _get_m_db_column_col
  global _get_o_db_column_sql
  global _db_type
  global _db

  params = (dbName, tableName)
  tableColumns = mysql_utils.get_mysql_utils(**_db).find_all(_get_m_db_column_sql, params,
                                                             _get_m_db_column_col)
  return tableColumns
  #
  # if 'm' == _db_type:
  #     params = (dbName, tableName)
  #     tableColumns = pymysql_helper.get_mysql_helper(**_db).find_all(_get_m_db_column_sql, params,
  #                                                                    _get_m_db_column_col)
  #     return tableColumns
  # elif 'o' == _db_type:
  #     params = (tableName)
  #     tableNames = oracle_helper.find_all(_get_o_db_column_sql, params, _get_m_db_column_col)
  #     return tableNames
  # else:
  #     return []


def format_excel():
  global _db_name, _table_list
  tableNames = get_db_table_list(_db_name)
  print(tableNames)
  for tableName in tableNames:
    if len(_table_list) > 0 and tableName['TABLE_NAME'] not in _table_list:
      continue
    tableInfo = format_table_excel(_db_name, tableName['TABLE_NAME'], tableName['TABLE_COMMENT'])
    print(tableInfo)
    print('')


def format_table_excel(dbName, tableName, tableComment):
  tableInfo = ''
  tableInfo += ('表名\t%s\t%s%s' % (tableName, tableComment, os.linesep))
  columns = get_db_table_column_list(dbName, tableName)
  tableInfo += ('列名\t类型\t是否可为空\t是否为主键\t默认值\t描述' + os.linesep)
  for c in columns:
    if c['CHARACTER_MAXIMUM_LENGTH'] is None:
      if c['NUMERIC_PRECISION'] is None:
        length = 'None'
      else:
        length = str(c['NUMERIC_PRECISION'])
        if c['NUMERIC_SCALE'] is not None and 0 < c['NUMERIC_SCALE']:
          length += ',' + str(c['NUMERIC_SCALE'])
    else:
      length = str(c['CHARACTER_MAXIMUM_LENGTH'])

    # 列名 类型 是否可为空 是否为主键 默认值 描述
    if 'None' == length:
      cmsg = '%s\t%s\t%s\t%s\t%s\t%s' % (c['COLUMN_NAME'], c['DATA_TYPE'], c['IS_NULLABLE'], c['COLUMN_KEY'],
                                         get_column_default(
          c['COLUMN_DEFAULT'], c['EXTRA'], c['COLUMN_KEY']),
          c['COLUMN_COMMENT'])
    else:
      cmsg = '%s\t%s\t%s\t%s\t%s\t%s' % (c['COLUMN_NAME'], c['DATA_TYPE'] + '(' + length + ')',
                                         c['IS_NULLABLE'], c['COLUMN_KEY'],
                                         get_column_default(
          c['COLUMN_DEFAULT'], c['EXTRA'], c['COLUMN_KEY']),
          c['COLUMN_COMMENT'])
    tableInfo += (cmsg + os.linesep)
  return tableInfo


def get_column_default(defVal, extra, columnKey):
  if 'PRI' == columnKey:
    return ''
  if 'on update CURRENT_TIMESTAMP' in extra:
    return 'on update CURRENT_TIMESTAMP'
  if defVal is None:
    return 'null'
  if '' == defVal:
    return '“”'
  return defVal


_db_type = 'm'  # 数据库类型，m表示mysql，o表示oracle
_db_name = 'polaris_project_manage'

# 需要打印结构的表，空列表则打印库所有表
_table_list = []
_file_path = os.path.split(os.path.realpath(__file__))[0] + os.sep + 'domain' + os.sep

_db = {

    'host': '192.168.1.148',
    'user': 'root',
    'passwd': 'mysqldev',
    'db': 'polaris_project_manage',
    'charset': 'utf8mb4',
    'port': 3306,
}

if __name__ == '__main__':
  import sys

  format_excel()
