# -*- coding: UTF-8 -*-

import os
from typing import List

from soc_common.model import config_model

# 配置文件
# 生成页面title
DocTitle = '数据模型说明'

# 根路径
BasePath = os.getcwd()
# 全局输出路径
ExportPath = os.path.join(BasePath, 'export')
# markdown输出路径
MarkdownExportPath = os.path.join(ExportPath, 'md')
# golang输出路径
GolangExportPath = os.path.join(ExportPath, 'golang')
# 模板路径
TemplatePath = os.path.join(BasePath, 'resources', 'template')

# 日志路径
LogPath = os.path.join(ExportPath, 'log.log')


# 数据源类型
DsMysql = 'MySql'
DsClickHouse = 'ClickHouse'
DsPostgreSQL = 'PostgreSQL'
DsMariaDB = 'MariaDB'

# 支持的数据源类型
SupportDsType = [DsMysql, DsMariaDB, DsClickHouse]

# markdown 建表语句类型
DsMdCreateScriptType = {
    DsMysql: 'sql',
    DsMariaDB: 'sql',
    DsClickHouse: 'sql'
}

# 导出数据类型
ExportTypeMarkdown = 'markdown'


exportDsConfig: List[config_model.DataSourceConfig] = [
    # config_model.DataSourceConfig(dsType=DsMysql, host='rm-uf6cl3tt9t814wv84.mysql.rds.aliyuncs.com', port=3306, db='tec_find_my_db',
    #                               user='dev_account', passwd='9CrgLlsDN9QlitQFRNW9', includes=[], name='dev测试环境', code='dev-mysql', comment='dev测试环境数据库'),
    # config_model.DataSourceConfig(dsType=DsMysql, host='10.0.45.179', port=3306, db='mp_gcm_db',
    #                               user='rta-sit', passwd='snowball', includes=[], excludes=['pre_mp_rta_transit_db', 'pre_mp_pay_center_db', 'pre_fp_global_business_db', 'pre_mp_gcm_db', 'logan_db'], name='RTA测试环境', code='rta-test', comment='RTA测试环境'),
    # config_model.DataSourceConfig(dsType=DsClickHouse, host='10.0.3.94', port=9000, db='system',
    #                               user='default', passwd='123456', includes=[], name='clickhouse测试环境', code='clickhouse-test', comment='clickhouse测试环境'),

    config_model.DataSourceConfig(dsType=DsMysql, host='101.133.223.80', port=33309, db='soc_toolkit_data_db',
                                  user='root', passwd='123', includes=['soc_toolkit_data_db'], excludes=[], name='MySql测试导出数据库', code='Mysql-export', comment='MySql测试导出数据库'),
    config_model.DataSourceConfig(dsType=DsMariaDB, host='192.168.80.129', port=3307, db='tb_school_db',
                                  user='root', passwd='123456', includes=[], name='MariaDB测试导出数据库', code='MariaDB-export', comment='MariaDB测试导出数据库'),
    config_model.DataSourceConfig(dsType=DsClickHouse, host='10.0.3.94', port=9000, db='system',
                                  user='default', passwd='123456', includes=[], name='clickhouse测试环境', code='clickhouse-test', comment='clickhouse测试环境'),
]


class CodeGenerateByDb:
  """根据数据库表结构生成代码配置
  """
  # 输出路径
  exportPath = os.path.join(ExportPath, 'golang')

  # 生成对象是需要去除的表名前缀
  ignoreTablePres = ['oscm_', 'osa_', 'osm_', 'ost_', 't_']

  # 需要生成对象的表名列表，为空则库中所有表都生成
  exportTables = []

  # json 属性格式，1驼峰，2下划线
  jsonPropertyType = 1
