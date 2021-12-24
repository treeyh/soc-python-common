# -*- coding: UTF-8 -*-


import sys
import logging
import argparse
import shutil

from typing import Dict, List

from soc_common.config import config
from soc_common.utils import log_utils, file_utils
from soc_common.model import ds_model, config_model
from soc_common.tools.export_db_model import mysql_export_db_model
from soc_common.tools.code.code_generate.golang import generate_bo_po_by_db


def _parse_option():
  """获取命令行参数

  Returns:
                  [type]: [description]
  """
  parser = argparse.ArgumentParser(description='Echoscope')
  parser.add_argument('-g', '--generate', type=str, default='markdown',
                      help='generate file type. support: markdown')
  options = parser.parse_args()

  return options, sys.argv[1:]


def init():
  """初始化
  """
  file_utils.mkdirs(config.LogPath, False)
  log_utils.log_init(path=config.LogPath)


def main():
  init()
  options, args = _parse_option()
  shutil.rmtree(path=config.ExportPath, ignore_errors=True)

  generate = generate_bo_po_by_db.GolangBoPoGenerate(config.TemplatePath, config.ExportPath)
  generate.generate_po_bo_file(config.exportDsConfig[0], ds_model.DataSourceModel(name='test'))


if __name__ == '__main__':
  main()
