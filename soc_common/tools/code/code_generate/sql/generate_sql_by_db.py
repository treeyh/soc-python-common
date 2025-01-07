# -*- encoding: utf-8 -*-

import os
import sys
import re
import logging
import jinja2

from typing import Dict, List

from soc_common.config import config
from soc_common.utils import file_utils, date_utils
from soc_common.model import ds_model, config_model
from soc_common.tools.export_db_model import mysql_export_db_model, postgresql_export_db_model


class SqlModelGenerate(object):

  def __init__(self, templatePath: str, exportPath: str):
    """初始化

    Args:
        templatePath (str): 模板路径
        exportPath (str): 输出路径
    """
    filePath = os.path.join(templatePath, 'sql')
    self.env = jinja2.Environment(
        loader=jinja2.FileSystemLoader(filePath))
    self.postgresqlTemplate = self.env.get_template('postgresql.template')
    self.mysqlTemplate = self.env.get_template('mysql.template')
    self.exportPath = exportPath

  def generate_sql_file(self, conf: config_model.DataSourceConfig):
    """生成sql文件

    Args:
        conf (config_model.DataSourceConfig): [description]
        ds (ds_model.DataSourceModel): [description]

    Returns:
        [type]: [description]
    """
    if conf.dsType == config.DsMysql or conf.dsType == config.DsMariaDB:
      ds = mysql_export_db_model.MysqlExportDbModel().export_model(conf)
    else:
      ds = postgresql_export_db_model.PostgresqlExportDbModel().export_model(conf=conf)
    
    templatePath = os.path.join(self.exportPath, conf.code, 'sql')
    file_utils.mkdirs(templatePath, True)
    for db in ds.dbs:
      for table in db.tables:
        templateFilePath = os.path.join(templatePath, table.go_model_file_name() + '.sql')


        if conf.dsType == config.DsMysql or conf.dsType == config.DsMariaDB:
          modelContent = self.mysqlTemplate.render(tb=table)
        else:
          modelContent = self.postgresqlTemplate.render(tb=table)
        
        file_utils.write_file(filePath=templateFilePath, content=modelContent)

    return templatePath
  

  