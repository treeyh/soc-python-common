# -*- coding: UTF-8 -*-


import sys
import logging
import argparse
import shutil

from typing import Dict, List

from soc_common.config import config
from soc_common.utils import log_utils, file_utils, crypto_utils
from soc_common.model import ds_model, config_model
from soc_common.tools.export_db_model import postgresql_export_db_model
# from soc_common.tools.code.code_generate import sql_export_domain
from soc_common.tools.code.code_generate.golang import generate_bo_po_by_db
from soc_common.tools.code.code_generate.python import generate_model_by_db
from soc_common.tools.code.code_generate.sql import generate_sql_by_db

# from soc_common.tools.code.code_generate import sql_export_domain

# from soc_common.tools.git import pull_code
# from soc_common.tools.encrypt import ecc_demo
from soc_common.tools.gitlab import gitlab_utils


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
  log_utils.init(path=config.LogPath)


def main():
  init()
  options, args = _parse_option()

  # shutil.rmtree(path=config.ExportPath, ignore_errors=True)

  # generate = generate_bo_po_by_db.GolangBoPoGenerate(config.TemplatePath, config.ExportPath)
  # generate.generate_po_bo_file(config.exportDsConfig[3])

  # generate = generate_model_by_db.PythonModelGenerate(config.TemplatePath, config.ExportPath)
  # generate.generate_model_file(config.exportDsConfig[4])

  # generate = generate_sql_by_db.SqlModelGenerate(config.TemplatePath, config.ExportPath)
  # generate.generate_sql_file(config.exportDsConfig[4])

  # sql_export_domain.format_select_sql()  # select 语句
  # sql_export_domain.format_update_sql()  # select 语句
  # sql_export_domain.format_insert_sql()  # select 语句
  # sql_export_domain.format_column_list()

  # from soc_common.tools import test
  # test.run()

  # from soc_common.tools.toolkit.config import convert_unit
  # convert_unit.build_config()

  # pull_code.main()
  # from soc_common.tools.toolkit.lang import convert_lang_2_ts
  # # convert_lang_2_ts.run()

  # from soc_common.tools import rename_img_name
  # rename_img_name.main()

  # ecc_demo.run()
  # gitlab_utils.get_project_access()

  # dbConf = config_model.DataSourceConfig(dsType=config.DsPostgreSQL, host='127.0.0.1', port=5432, db='soc_question_db_local',
  #                                 user='proot', passwd='4pVmsxTuB_5ZlnSX', includes=['soc_question_db_local'], excludes=[], name='Postgresql测试导出数据库', code='Postgresql-export', comment='Postgresql测试导出数据库')
  # generate = generate_bo_po_by_db.GolangBoPoGenerate(config.TemplatePath, config.ExportPath)
  # generate.generate_po_bo_file(config.exportDsConfig[5])
  
  # postgresqlExp = postgresql_export_db_model.PostgresqlExportDbModel()
  # postgresqlExp.export_model(dbConf)

  # from soc_common.tools.download import download_img

  # download_img.download_imgs()

  # key = crypto_utils.get_aes256_key()
  # print(f"AES-256 密钥: {key}")
  # print(type(key))
  # new_key = crypto_utils.derive_aes_key(bytes(key, encoding='utf8'), b'LTAI5tS8cAu13Ax3u18d2D6T')
  # print(f"AES-256 新密钥: {new_key}")

  key = crypto_utils.get_aes512_key()
  print(f"AES-256 密钥: {key}")
  print(type(key))
  new_key = crypto_utils.derive_aes512_key(bytes(key, encoding='utf8'), b'LTAI5tS8cAu13Ax3u18d2D6T')
  print(f"AES-256 新密钥: {new_key}")



if __name__ == '__main__':
  main()
