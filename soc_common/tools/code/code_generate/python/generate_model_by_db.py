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


class PythonModelGenerate(object):

  def __init__(self, templatePath: str, exportPath: str):
    """初始化

    Args:
        templatePath (str): 模板路径
        exportPath (str): 输出路径
    """
    filePath = os.path.join(templatePath, 'python')
    self.env = jinja2.Environment(
        loader=jinja2.FileSystemLoader(filePath))
    self.modelTemplate = self.env.get_template('model.template')
    self.exportPath = exportPath

  def generate_model_file(self, conf: config_model.DataSourceConfig):
    """生成bo po文件

    Args:
        conf (config_model.DataSourceConfig): [description]
        ds (ds_model.DataSourceModel): [description]

    Returns:
        [type]: [description]
    """
    ds = mysql_export_db_model.MysqlExportDbModel().export_model(conf)
    print(ds)
    modelPath = os.path.join(self.exportPath, conf.code, 'model')
    file_utils.mkdirs(modelPath, True)
    for db in ds.dbs:
      for table in db.tables:
        modelFilePath = os.path.join(modelPath, table.go_model_file_name() + '.py')
        modelContent = self.modelTemplate.render(tb=table)
        file_utils.write_file(filePath=modelFilePath, content=modelContent)

    return modelPath
