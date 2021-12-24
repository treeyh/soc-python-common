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
from soc_common.tools.export_db_model import mysql_export_db_model


class GolangBoPoGenerate(object):

  def __init__(self, templatePath: str, exportPath: str):
    """初始化

    Args:
        templatePath (str): 模板路径
        exportPath (str): 输出路径
    """
    self.env = jinja2.Environment(
        loader=jinja2.FileSystemLoader(os.path.join(templatePath, 'golang')))
    self.boTemplate = self.env.get_template('bo.template')
    self.poTemplate = self.env.get_template('po.template')
    self.tableNameTemplate = self.env.get_template('table_name.template')
    self.columnNameTemplate = self.env.get_template('column_name.template')
    self.exportPath = exportPath

  def generate_po_bo_file(self, conf: config_model.DataSourceConfig, ds: ds_model.DataSourceModel):
    """生成bo po文件

    Args:
        conf (config_model.DataSourceConfig): [description]
        ds (ds_model.DataSourceModel): [description]

    Returns:
        [type]: [description]
    """
    ds = mysql_export_db_model.MysqlExportDbModel().export_model(conf)
    poPath = os.path.join(self.exportPath, conf.code, 'po')
    boPath = os.path.join(self.exportPath, conf.code, 'bo')
    file_utils.mkdirs(poPath, True)
    file_utils.mkdirs(boPath, True)
    tables = {}
    fields = {}
    for db in ds.dbs:
      # dbPath = os.path.join(dsPath, db.name)
      # file_util.mkdirs(dsPath, True)
      for table in db.tables:
        # filePath = os.path.join(dbPath, table.name + '_po.go')
        poFilePath = os.path.join(poPath, table.name + '_po.go')
        poContent = self.poTemplate.render(tb=table)
        file_utils.write_file(filePath=poFilePath, content=poContent)

        boFilePath = os.path.join(boPath, table.name + '_bo.go')
        boContent = self.boTemplate.render(tb=table)
        file_utils.write_file(filePath=boFilePath, content=boContent)

        tables['Tn'+table.go_model_name()] = table.name
        for field in table.fields:
          fields['Cn'+field.go_field_name()] = field.name

    poTableFilePath = os.path.join(poPath, 'table_name.go')
    poContent = self.tableNameTemplate.render(tables=tables)
    file_utils.write_file(filePath=poTableFilePath, content=poContent)

    poColumnFilePath = os.path.join(poPath, 'column_name.go')
    poContent = self.columnNameTemplate.render(fields=fields)
    file_utils.write_file(filePath=poColumnFilePath, content=poContent)
    return poPath
