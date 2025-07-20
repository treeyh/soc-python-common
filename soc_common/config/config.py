# -*- coding: UTF-8 -*-

import os
from typing import List

from soc_common.model import config_model

# 配置文件
# 生成页面title
DocTitle = "数据模型说明"

# 根路径
BasePath = os.getcwd()
# 全局输出路径
ExportPath = os.path.join(BasePath, "export")
# markdown输出路径
MarkdownExportPath = os.path.join(ExportPath, "md")
# golang输出路径
GolangExportPath = os.path.join(ExportPath, "golang")
# 模板路径
TemplatePath = os.path.join(BasePath, "resources", "template")

# 日志路径
LogPath = os.path.join(ExportPath, "log.log")


# 数据源类型
DsMysql = "MySql"
DsClickHouse = "ClickHouse"
DsPostgreSQL = "PostgreSQL"
DsMariaDB = "MariaDB"

# 支持的数据源类型
SupportDsType = [DsMysql, DsMariaDB, DsClickHouse]

# markdown 建表语句类型
DsMdCreateScriptType = {DsMysql: "sql", DsMariaDB: "sql", DsClickHouse: "sql"}

# 导出数据类型
ExportTypeMarkdown = "markdown"


exportDsConfig: List[config_model.DataSourceConfig] = [
    # config_model.DataSourceConfig(dsType=DsMysql, host='rm-uf6cl3tt9t814wv84.mysql.rds.aliyuncs.com', port=3306, db='tec_find_my_db',
    #                               user='dev_account', passwd='9CrgLlsDN9QlitQFRNW9', includes=[], name='dev测试环境', code='dev-mysql', comment='dev测试环境数据库'),
    # config_model.DataSourceConfig(dsType=DsMysql, host='10.0.45.179', port=3306, db='mp_gcm_db',
    #                               user='rta-sit', passwd='snowball', includes=[], excludes=['pre_mp_rta_transit_db', 'pre_mp_pay_center_db', 'pre_fp_global_business_db', 'pre_mp_gcm_db', 'logan_db'], name='RTA测试环境', code='rta-test', comment='RTA测试环境'),
    # config_model.DataSourceConfig(dsType=DsClickHouse, host='10.0.3.94', port=9000, db='system',
    #                               user='default', passwd='123456', includes=[], name='clickhouse测试环境', code='clickhouse-test', comment='clickhouse测试环境'),
    # 0
    config_model.DataSourceConfig(
        dsType=DsMysql,
        host="192.168.80.129",
        port=3306,
        db="tb_school_db",
        user="root",
        passwd="mysqlpwd",
        includes=["tb_school_db"],
        excludes=[],
        name="MySql测试导出数据库",
        code="Mysql-export",
        comment="MySql测试导出数据库",
    ),
    # 1
    config_model.DataSourceConfig(
        dsType=DsMariaDB,
        host="192.168.80.129",
        port=3307,
        db="tb_school_db",
        user="root",
        passwd="123456",
        includes=[],
        name="MariaDB测试导出数据库",
        code="MariaDB-export",
        comment="MariaDB测试导出数据库",
    ),
    # 2
    config_model.DataSourceConfig(
        dsType=DsClickHouse,
        host="10.0.3.94",
        port=9000,
        db="system",
        user="default",
        passwd="123456",
        includes=[],
        name="clickhouse测试环境",
        code="clickhouse-test",
        comment="clickhouse测试环境",
    ),
    # 3
    config_model.DataSourceConfig(
        dsType=DsPostgreSQL,
        host="127.0.0.1",
        port=5432,
        db="soc_question_db_local",
        user="proot",
        passwd="4pVmsxTuB_5ZlnSX",
        includes=["soc_question_db_local"],
        excludes=[],
        name="Postgresql测试导出数据库",
        code="Postgresql-export",
        comment="Postgresql测试导出数据库",
    ),
    # 4
    config_model.DataSourceConfig(
        dsType=DsPostgreSQL,
        host="192.168.7.160",
        port=5432,
        db="soc_trader_db_dev",
        user="proot",
        passwd="4pVmsxTuB_5ZlnSX",
        includes=["soc_trader_db_dev"],
        excludes=[],
        name="测试数据库",
        code="export",
        comment="测试导出数据库",
    ),
    # 5
    config_model.DataSourceConfig(
        dsType=DsMysql,
        host="1",
        port=3306,
        db="snake_dev",
        user="root",
        passwd="Admin@1234",
        includes=["snake_dev"],
        name="Snake",
        code="Snake-export",
        comment="Snake",
    ),
    # 6
    config_model.DataSourceConfig(
        dsType=DsMysql,
        host="127.0.0.1",
        port=3306,
        db="snake",
        user="root",
        passwd="2Dv_v2VxnZ8PgG26f",
        includes=["snake"],
        name="Snake",
        code="Snake-export",
        comment="Snake",
    ),
    # 7
    config_model.DataSourceConfig(
        dsType=DsMysql,
        host="127.0.0.1",
        port=3306,
        db="snb_webhook_proxy_db",
        user="root",
        passwd="2Dv_v2VxnZ8PgG26f",
        includes=["snb_webhook_proxy_db"],
        name="snb_webhook_proxy_db",
        code="snb_webhook_proxy_db",
        comment="snb_webhook_proxy_db",
    ),
    # 8
    config_model.DataSourceConfig(
        dsType=DsPostgreSQL,
        host="192.168.7.160",
        port=5432,
        db="soc_study_db_dev",
        user="proot",
        passwd="4pVmsxTuB_5ZlnSX",
        includes=["soc_study_db_dev"],
        excludes=[],
        name="测试数据库",
        code="export",
        comment="测试导出数据库",
    ),
    # 9
    config_model.DataSourceConfig(
        dsType=DsPostgreSQL,
        host="192.168.7.160",
        port=5432,
        db="soc_user_db_dev",
        user="proot",
        passwd="4pVmsxTuB_5ZlnSX",
        includes=["soc_user_db_dev"],
        excludes=[],
        name="测试数据库",
        code="export",
        comment="测试导出数据库",
    ),
    # 10
    config_model.DataSourceConfig(
        dsType=DsMysql,
        host="192.168.7.160",
        port=3306,
        db="soc_builder_db",
        user="root",
        passwd="7Dv_v2VxnZ8PgG26f",
        includes=["soc_builder_db"],
        excludes=[],
        name="测试数据库",
        code="export",
        comment="测试导出数据库",
    ),
]

DB_CONFIG = {
    "host": "192.168.7.160",
    "port": 3306,
    "user": "root",
    "passwd": "7Dv_v2VxnZ8PgG26f",
    "db": "soc_builder_db",
    "charset": "utf-8",
}

class CodeGenerateByDb:
    """根据数据库表结构生成代码配置"""

    # 输出路径
    exportPath = os.path.join(ExportPath, "golang")

    # 生成对象是需要去除的表名前缀
    ignoreTablePres = ["cloud_", "chk_", "que_soc_", "soc_", "st_", "tt_", "bs_", "bw_", "ss_", "su_"]

    # 需要生成对象的表名列表，为空则库中所有表都生成
    exportTables = []

    # json 属性格式，1驼峰，2下划线
    jsonPropertyType = 1
