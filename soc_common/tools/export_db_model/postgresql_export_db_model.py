# -*- coding: UTF-8 -*-

import logging
from typing import List

from soc_common.config import config
from soc_common.utils import postgresql_utils, str_utils, log_utils
from soc_common.model import ds_model, config_model
from soc_common.tools.export_db_model import export_db_model


class PostgresqlExportDbModel(export_db_model.ExportDbModel):
  def __init__(self):
    self.excludesDb = ['default_db', 'postgres', 'template0', 'template1']
    self.excludesSchema = "'pg_catalog', 'information_schema'"

  def export_model(self, conf: config_model.DataSourceConfig) -> ds_model.DataSourceModel:

    postgresqlUtils = postgresql_utils.get_postgresql_utils(
        host=conf.host, port=conf.port, user=conf.user, passwd=conf.passwd, db=conf.db)

    ver = self.get_db_version(postgresqlUtils)

    if ver == '':
      logging.error(' postgresql conn fail. ')
      return
    dsm = ds_model.DataSourceModel(
        name='%s:%d' % (conf.host, conf.port), dbType=config.DsPostgreSQL, version=ver)

    dsm.dbs = self.get_export_dbs(postgresqlUtils, conf.includes, conf.excludes)
    
    # dsm.dbs [{name:ex_test_db, comment:, charset:en_US.UTF-8, collation_name:, tables:[], create_script:}, {name:soc_test_db, comment:, charset:en_US.UTF-8, collation_name:, tables:[], create_script:}]

    dsm = self.fill_table_fields(conf, dsm)
    
    print(dsm)

    return dsm

  def get_db_version(self, conn: postgresql_utils.PostgresqlUtils) -> str:
    """获取mysql版本

    Args:
        conn (postgresql_utils.PostgresqlUtils): [description]

    Returns:
        str: [description]
    """
    sql = 'select version() as ver;'
    cols = ['ver']
    ver = conn.find_one(sql, (), cols)

    return '' if ver == None else str_utils.format_bytes_to_str(ver.get('ver', ''))

  def get_export_dbs(self, conn: postgresql_utils.PostgresqlUtils, includes: List[str] = [], excludes: List[str] = []) -> List[ds_model.DbModel]:
    """获取需要导出结构的数据库列表

    Args:
        conn (postgresql_utils.PostgresqlUtils): 数据库连接
        includes (List[str], optional): 需要包含的数据库列表. Defaults to [].
        excludes (List[str], optional): 需要排除的数据库列表. Defaults to [].

    Returns:
        List[ds_model.DbModel]: 需要导出的数据库列表
    """
    sql = 'select datname, datcollate from pg_database;'
    cols = ['datname', 'datcollate']
    data = conn.find_all(sql, (), cols)
    dbs = []

    for d in data:
      db_name = str_utils.format_bytes_to_str(d['datname'])
      if db_name in self.excludesDb or db_name in excludes:
        # 需要过滤
        continue
      if len(includes) > 0 and db_name not in includes:
        # 不包含在include中
        continue

      charset = str_utils.format_bytes_to_str(d['datcollate'])
      collation_name = ''
      dbModel = ds_model.DbModel(
          name=db_name, charset=charset, collation_name=collation_name)
      dbs.append(dbModel)

    return dbs

  def fill_table_fields(self, conf: config_model.DataSourceConfig, dsModel: ds_model.DataSourceModel) -> ds_model.DataSourceModel:
    """获取数据库中的表信息

    Args:
        conn (mysql_util.MysqlUtil): 数据库连接
        dsModel (ds_model.DataSourceModel): 数据源，包含数据库列表

    Returns:
        ds_model.DataSourceModel: 数据源
    """

    # 先循环数据库, 根据数据库获取表列信息, 根据数据库信息获取表主键信息, 根据数据库获取表备注信息

    table_column_sql = ''' SELECT 
  A.table_catalog,
	A.table_schema,
	A.table_name,
	A.column_name,
	A.ordinal_position,
	A.column_default,
	A.is_nullable,
	A.data_type,
	A.character_maximum_length,
	A.numeric_precision,
	A.numeric_precision_radix,
	A.numeric_scale,
	A.datetime_precision,
	A.udt_catalog,
	A.udt_schema,
	A.udt_name,
	A.dtd_identifier,
	A.is_identity,
	C.column_name AS pk_column_name
FROM
	information_schema.COLUMNS AS A 
	LEFT JOIN information_schema.table_constraints AS B
	ON A.table_catalog = B."constraint_catalog" 
	AND A.table_schema = B.table_schema 
	AND A."table_name" = B."table_name" 
	AND B.constraint_type = 'PRIMARY KEY' 
	LEFT JOIN information_schema.key_column_usage AS C
	ON C.constraint_name = B.constraint_name
	AND C.column_name = A.column_name
WHERE
	A.table_schema NOT IN ( 'information_schema', 'pg_catalog' ) 
ORDER BY
	A.table_schema ASC,
	A.table_name ASC,
	A.ordinal_position ASC; '''
    table_column_cols = ['table_catalog', 'table_schema', 'table_name', 'column_name', 'ordinal_position', 'column_default', 'is_nullable', 'data_type', 'character_maximum_length', 'numeric_precision', 'numeric_precision_radix', 'numeric_scale', 'datetime_precision', 'udt_catalog', 'udt_schema', 'udt_name', 'dtd_identifier', 'is_identity', 'pk_column_name']

    for db in dsModel.dbs:
      postgresqlUtils = postgresql_utils.get_postgresql_utils(
        host=conf.host, port=conf.port, user=conf.user, passwd=conf.passwd, db=db.name)
      data = postgresqlUtils.find_all(table_column_sql, (), table_column_cols)
      tables: ds_model.TableModel = []
      tableKey = ''
      table = None
      for d in data:
        tableSchema = str_utils.format_bytes_to_str(d['table_schema'])
        tableName = str_utils.format_bytes_to_str(d['table_name'])
        tKey = '%s#%s' % (tableSchema, tableName)
        if tKey != tableKey:
          if table != None:
            tables.append(table)
            if table.name == 'test_student':
              print(table)
          table = ds_model.TableModel(name=tableName, comment='', collation_name='', engine='', fields = [], table_schema=tableSchema)
          tableKey = tKey

        fname = str_utils.format_bytes_to_str(d['column_name'])
        ftype = str_utils.format_bytes_to_str(d['udt_name'])
        column_type = ftype
        length = 0
        scale = 0
        default = str_utils.format_bytes_to_str(d['column_default'])
        nullFlag = str_utils.format_bytes_to_str(d['is_nullable'])
        char_length = str_utils.format_bytes_to_str(d['character_maximum_length'])
        indexFlag = 0 if fname == str_utils.format_bytes_to_str(d['pk_column_name']) else 1
        autoInc = True if default != None and 'nextval' in default else False
        field_index = int(str_utils.format_bytes_to_str(d['dtd_identifier']))

        if char_length != None:
          column_type = '%s(%s)' % (ftype, char_length)
          length = int(char_length)
        else:
          num_prec = str_utils.format_bytes_to_str(d['numeric_precision'])
          num_prec_radix = str_utils.format_bytes_to_str(d['numeric_precision_radix'])
          numeric_scale = str_utils.format_bytes_to_str(d['numeric_scale'])
          if num_prec_radix == '10':
            length = num_prec
            if numeric_scale != None or numeric_scale != '0':
              column_type = '%s(%s)' % (ftype, num_prec)
            else:
              column_type = '%s(%s,%s)' % (ftype, num_prec, numeric_scale)
              scale = int(numeric_scale)

        field = ds_model.FieldModel(name=fname, ftype=ftype, column_type=column_type, length=length, scale=scale, default=default, nullFlag=nullFlag,
            comment='', charset='', collation_name='', indexFlag=indexFlag, indexName='', autoInc=autoInc, field_index = field_index)
        table.fields.append(field)
        logging.info('load table:%s field: %s.' % (tableName, fname))

      if table != None:
        tables.append(table)
      tables = self.get_database_comment(postgresqlUtils, tables=tables)
      db.tables = tables

    return dsModel

  def get_create_script(self, conn: postgresql_utils.PostgresqlUtils, dbName: str, tableName: str) -> str:
    """获取表的创建脚本

    Args:
        conn (mysql_util.MysqlUtil): 数据库连接
        dbName (str): 数据库名称
        tableName (str): 表名称

    Returns:
        str: 创建脚本
    """
    sql = ''' SHOW CREATE TABLE `%s`.`%s` ''' % (dbName, tableName)
    cols = ['Table', 'Create Table']
    data = conn.find_one(sql, (), cols)
    return '' if data == None else str_utils.format_bytes_to_str(data.get('Create Table', ''))

  def get_database_comment(self, conn: postgresql_utils.PostgresqlUtils, tables: List[ds_model.TableModel]) -> List[ds_model.TableModel]:
    """获取数据库中表和列的备注信息

    Args:
        conn (postgresql_utils.PostgresqlUtils): 数据库连接
        tables (List[ds_model.TableModel]): 数据库表列表

    Returns:
        List[ds_model.TableModel]: 表列表
    """
    sql = ''' SELECT
    n.nspname AS table_schema,
    c.relname AS table_name,
		d.objsubid as objsubid,
    d.description AS description
FROM
    pg_class AS c
INNER JOIN
    pg_namespace AS n ON c.relnamespace = n.oid
LEFT JOIN
    pg_description AS d ON c.oid = d.objoid
WHERE
    c.relkind = 'r'
    AND n.nspname NOT IN ('pg_catalog', 'information_schema')
ORDER BY
    table_schema,
    table_name,
		objsubid; '''
    cols = ['table_schema', 'table_name', 'objsubid', 'description']

    data = conn.find_all(sql, (), cols)

    tableKey = ''
    tIndex = 0
    for d in data:
      tableSchema = str_utils.format_bytes_to_str(d['table_schema'])
      tableName = str_utils.format_bytes_to_str(d['table_name'])
      objsubid = str_utils.format_bytes_to_str(d['objsubid'])
      description = str_utils.format_bytes_to_str(d['description'])
      if objsubid == None or objsubid == '':
        continue
      findex = int(objsubid)
      tKey = '%s#%s' % (tableSchema, tableName)
      if tableKey != tKey:
        tableKey = tKey
        for index in range(len(tables)):
          if tables[index].table_schema == tableSchema and tables[index].name == tableName:
            tIndex = index
            break
      if findex == 0:
        # 表备注
        tables[tIndex].comment = description
        continue

      for f in tables[tIndex].fields:
        if f.field_index == findex:
          f.comment = description
          break

    return tables



'''

-- 获取表列信息sql
-- http://www.postgres.cn/docs/12/infoschema-columns.html

SELECT 
  A.table_catalog,
	A.table_schema,
	A.table_name,
	A.column_name,
	A.ordinal_position,
	A.column_default,
	A.is_nullable,
	A.data_type,
	A.character_maximum_length,
	A.numeric_precision,
	A.numeric_precision_radix,
	A.numeric_scale,
	A.datetime_precision,
	A.udt_catalog,
	A.udt_schema,
	A.udt_name,
	A.dtd_identifier,
	A.is_identity,
	C.column_name AS pk_column_name
FROM
	information_schema.COLUMNS AS A 
	LEFT JOIN information_schema.table_constraints AS B
	ON A.table_catalog = B."constraint_catalog" 
	AND A.table_schema = B.table_schema 
	AND A."table_name" = B."table_name" 
	AND B.constraint_type = 'PRIMARY KEY' 
	LEFT JOIN information_schema.key_column_usage AS C
	ON C.constraint_name = B.constraint_name
	AND C.column_name = A.column_name
WHERE
	A.table_schema NOT IN ( 'information_schema', 'pg_catalog' ) 
ORDER BY
	A.table_schema ASC,
	A.table_name ASC,
	A.ordinal_position ASC;



-- 获取描述信息sql
SELECT
    n.nspname AS table_schema,
    c.relname AS table_name,
		d.objsubid as objsubid,
    d.description AS description
FROM
    pg_class AS c
INNER JOIN
    pg_namespace AS n ON c.relnamespace = n.oid
LEFT JOIN
    pg_description AS d ON c.oid = d.objoid
WHERE
    c.relkind = 'r' -- 只选择关系类型的对象，即表
    AND n.nspname NOT IN ('pg_catalog', 'information_schema') -- 排除系统命名空间
ORDER BY
    table_schema,
    table_name,
		objsubid;
'''