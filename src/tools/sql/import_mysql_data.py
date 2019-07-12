# -*- encoding: utf-8 -*-

import os
import sys
import re
import time
import random

path = os.path.split(os.path.realpath(__file__))[0]
sys.path.append(path + os.sep + '..')

from helper import str_helper, file_helper, pymysql_helper

_db = {

    'host': '127.0.0.1',
    'user': 'root',
    'passwd': 'mysqlpw',
    'db': 'demo',
    'charset': 'utf8mb4',
    'port': 3306,
}

'''
select `TABLE_NAME` from information_schema.`TABLES` where TABLE_SCHEMA = 'merchant_db' and TABLE_TYPE = 'BASE TABLE';

select TABLE_SCHEMA, TABLE_NAME, COLUMN_NAME, IS_NULLABLE, DATA_TYPE, CHARACTER_MAXIMUM_LENGTH, COLUMN_COMMENT , ORDINAL_POSITION 
 from information_schema.`columns` ORDER BY TABLE_SCHEMA DESC, TABLE_NAME DESC, ORDINAL_POSITION ASC;
'''

_INSERT_SQL = ''' INSERT INTO active_info (`code`, `size`, `score`, `type`, `status`, `create_time`, `update_time`) VALUE(%s,%s,%s,%s,%s, now(), now())  '''


def save_value(code, size, score, type, status):
    global _INSERT_SQL

    global _db

    params = (code, size, score, type, status,)
    id = pymysql_helper.get_mysql_helper(**_db).insert_or_update_or_delete(_INSERT_SQL, params, True)

    print(id)


if __name__ == '__main__':
    for i in range(1, 9000):
        status = random.randint(1, 5)
        if status != 2:
            status = 1
        size = random.randint(100, 1000)
        score = random.uniform(20, 1200)

        save_value(str(i), size, score, random.randint(1, 4), status)
        time.sleep(0.5)

    # print(31 % 16
