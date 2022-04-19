# -*- encoding: utf-8 -*-

import os
import sys
import json

from soc_common.utils import file_utils, str_utils, mysql_utils


_permission_content = '''
1		海外公交应用权限	os	/os	0	{"oper":[{"code":"*","name":"所有权限"}]}
2	itso	itso权限	itso	/os/itso	1	{"oper":[{"code":"*","name":"itso所有权限"}]}
3	calypso	calypso权限	calypso	/os/calypso	1	{"oper":[{"code":"*","name":"calypso所有权限"}]}
4	itso	itso虚拟卡操作	itso_card	/os/itso/card	2	{"oper":[{"code":"issuecard","name":"开卡"},{"code":"topupcard","name":"充值"},{"code":"issuecard_topupcard","name":"开卡加充值"},{"code":"issuecard_issueproduct","name":"开卡加出票"},{"code":"issuecard_topupcard_issueproduct","name":"开卡加充值加出票"},{"code":"backupcard","name":"迁出/备份"},{"code":"restorecard","name":"迁入/恢复"},{"code":"transfercard","name":"吸卡"},{"code":"refundcard","name":"退卡"},{"code":"topupentitycard","name":"物理卡充值"},{"code":"issueentityproduct","name":"物理卡出票"},{"code":"deletecard","name":"仅删卡"}]}
5	itso	itso票操作	itso_product	/os/itso/product	2	{"oper":[{"code":"issueproduct","name":"出票"},{"code":"refundproduct","name":"退票"}]}
6	calypso	calypso虚拟卡操作	calypso_card	/os/calypso/card	3	{"oper":[{"code":"issuecard","name":"开卡"},{"code":"topupcard","name":"充值"},{"code":"issuecard_topupcard","name":"开卡加充值"},{"code":"issuecard_issueproduct","name":"开卡加出票"},{"code":"issuecard_topupcard_issueproduct","name":"开卡加充值加出票"},{"code":"backupcard","name":"迁出/备份"},{"code":"restorecard","name":"迁入/恢复"},{"code":"transfercard","name":"吸卡"},{"code":"refundcard","name":"退卡"},{"code":"topupentitycard","name":"物理卡充值"},{"code":"issueentityproduct","name":"物理卡出票"},{"code":"deletecard","name":"仅删卡"}]}
7	calypso	calypso票操作	calypso_product	/os/calypso/product	3	{"oper":[{"code":"issueproduct","name":"出票"},{"code":"refundproduct","name":"退票"}]}
'''

_role_content = '''
1	金牌应用
2	银牌应用
'''

_role_permission_content = '''
1	1	2	/os/itso	|*|
2	1	3	/os/calypso	|*|
3	2	4	/os/itso/card	|issuecard|topupcard|issuecard_topupcard|issuecard_issueproduct|issuecard_topupcard_issueproduct|backupcard|restorecard|topupentitycard|issueentityproduct|
4	2	5	/os/itso/product	|issueproduct|refundproduct|
5	2	6	/os/calypso/card	|issuecard|topupcard|issuecard_topupcard|issuecard_issueproduct|issuecard_topupcard_issueproduct|backupcard|restorecard|topupentitycard|issueentityproduct|
6	2	7	/os/calypso/product	|issueproduct|refundproduct|
'''


def export_permission():
  global _permission_content

  index = 0
  for c in _permission_content.split('\n'):
    line = c.strip()
    if line == '':
      continue
    ls = line.split('\t')
    if len(ls) != 7:
      continue
    index += 1
    # sql = '''INSERT INTO `tecm_permission` (`id`, `partner_code`, `name`, `code`, `path`, `parent_id`, `operation`, `remark`, `status`, `creator`, `create_time`, `updator`, `update_time`, `version`, `del_flag`, `sort`) VALUES (%s, '%s', '%s', '%s', '%s', %s, '%s', '', 1, 0, '2021-11-11 17:28:34', 0, '2021-11-11 17:28:34', 1, 2, %s);''' % (
    #     ls[0], ls[1], ls[2], ls[3], ls[4], ls[5], ls[6], index)
    sql = '''INSERT INTO `oss_app_permission` (`id`, `product_line_code`, `name`, `code`, `path`, `parent_id`, `operation`, `remark`, `status`, `creator`, `create_time`, `updator`, `update_time`, `version`, `del_flag`, `sort`) VALUES (%s, '%s', '%s', '%s', '%s', %s, '%s', '', 1, 0, now(), 0, now(), 1, 2, %s);''' % (
        ls[0], ls[1], ls[2], ls[3], ls[4], ls[5], ls[6], index)
    print(sql)


def export_role():
  global _role_content

  index = 0
  for c in _role_content.split('\n'):
    line = c.strip()
    if line == '':
      continue
    ls = line.split('\t')
    if len(ls) != 2:
      continue
    index += 1
    # sql = '''INSERT INTO `tecm_role` (`id`, `partner_code`, `name`, `remark`, `status`, `creator`, `create_time`, `updator`, `update_time`, `version`, `del_flag`) VALUES (%s, '%s', '%s', '', 1, 0, '2021-11-11 18:29:00', 0, '2021-11-11 18:29:00', 1, 2);''' % (
    #     ls[0], ls[1], ls[2])
    sql = '''INSERT INTO `oss_app_level` (`id`, `name`, `remark`, `status`, `creator`, `create_time`, `updator`, `update_time`, `version`, `del_flag`) VALUES (%s, '%s', '', 1, 0, now(), 0, now(), 1, 2);''' % (
        ls[0], ls[1])
    print(sql)


def export_role_permission():
  global _role_permission_content

  index = 0
  for c in _role_permission_content.split('\n'):
    line = c.strip()
    if line == '':
      continue
    ls = line.split('\t')
    if len(ls) != 5:
      continue
    index += 1
    # sql = '''INSERT INTO `tecm_role_permission` (`id`, `partner_code`, `role_id`, `permission_id`, `permission_path`, `operation_codes`, `remark`, `status`, `creator`, `create_time`, `updator`, `update_time`, `version`, `del_flag`) VALUES (%s, '%s', %s, %s, '%s', '%s', '', 1, 1, '2021-11-11 18:31:38', 1, '2021-11-11 18:31:38', 1, 2);''' % (
    #     ls[0], ls[1], ls[2], ls[3], ls[4], ls[5])
    sql = '''INSERT INTO `oss_app_level_permission` (`id`, `app_level_id`, `permission_id`, `permission_path`, `operation_codes`, `remark`, `status`, `creator`, `create_time`, `updator`, `update_time`, `version`, `del_flag`) VALUES (%s, %s, '%s', '%s','%s', '', 1, 1, now(), 1, now(), 1, 2);''' % (
        ls[0], ls[1], ls[2], ls[3], ls[4])
    print(sql)


def export_card_data_sql(path: str, product_line: str, partner_code: str, partner_card_category_id: str, start_id: int):
  filePaths = file_utils.walk2(path)
  # print(filePaths)

  id = start_id
  content = ''
  for filePath in filePaths:
    if len(filePath) != 2:
      continue
    card_no = filePath[1].replace('.json', '')
    cid = int(card_no[8:], 16)
    sql = ''' INSERT INTO `oscm_card_data` (`id`, `product_line_code`, `partner_code`, `partner_card_category_id`, `card_no`, `uid`, `card_info`, `backup_info`, `active_time`, `effective_time`, `task_batch_id`, `renew_count`, `card_id`, `issuer_biz_id`, `backup_biz_id`, `remark`, `status`, `create_time`, `update_time`, `version`, `del_flag`) VALUES (%s, '%s', '%s', %s, '%d', %d, '%s', '', '2021-12-28 14:50:12', '2099-01-01 00:00:00', 0, 0, 0, 0, 0, '', 1, '2021-12-28 14:50:12', '2021-12-28 14:50:12', 1, 2);
    ''' % (
        id, product_line, partner_code, partner_card_category_id, cid, cid, file_utils.read_all_file(os.path.join(filePath[0], filePath[1])).strip())
    id += 1
    content += sql
  file_utils.write_file('d:\\card_'+product_line+'.sql', content)


def format_langs():
  langMap = {



      'tool.lifeGeoCode.lat': '纬度',
      'tool.lifeGeoCode.lng': '经度',
      'tool.lifeGeoCode.latOrlngEmpty': '请输入经纬度',
  }

  content = ''
  for k, v in langMap.items():
    ks = k.split('.')
    key = ks[0] + ''.join([str_utils.upperFirstWord(i) for i in ks[1:]])
    content += '  static String get %s =>\'%s\'.tr;\n' % (key, k)
  print(content)


# def import_id():
#   path = 'D:\\01_work\\77_github\\chinese-xinhua\\data\\xiehouyu.json'
#   content = file_utils.read_all_file(path)
#   cs = json.loads(content)

#   sql = ''' INSERT INTO `tb_school_db`.`t_tool_xiehouyu` ( `riddle`, `answer`) VALUES ( %s, %s);
# '''
#   print(len(cs))
#   mysqlUtil = mysql_utils.get_mysql_utils('192.168.80.129', 3306, 'root',
#                                           'mysqlpwd', 'tb_school_db', 'utf8mb4')
#   index = 0
#   for c in cs:
#     # if len(c['answer']) > 64:
#     #   print(c['riddle'])
#     #   print(c['answer'])
#     mysqlUtil.insert_or_update_or_delete(
#         sql, (c['riddle'], c['answer']))
#     index += 1
#     if index % 100 == 0:
#       print(index)
#   pass

def format_b():
  path = 'd:\\contenttype.csv'
  lines = file_utils.read_all_lines_file(path)
  content = ''

  index = 1
  index2 = 2
  for line in lines:

    ls = line.strip().split(',')
    if len(ls) != 4:
      continue

    sql = '''INSERT INTO `t_tool_content_type_comparison` (`id`, `suffix`, `code`, `remark_zh`, `remark_en`, `sync_time`, `status`, `create_time`, `update_time`, `version`, `del_flag`) VALUES (%d, '%s', '%s', '', '', '2022-04-02 19:54:17', 1, '2022-04-02 19:54:17', '2022-04-02 19:54:17', 1, 2);
INSERT INTO `t_tool_content_type_comparison` (`id`, `suffix`, `code`, `remark_zh`, `remark_en`, `sync_time`, `status`, `create_time`, `update_time`, `version`, `del_flag`) VALUES (%d, '%s', '%s', '', '', '2022-04-02 19:54:17', 1, '2022-04-02 19:54:17', '2022-04-02 19:54:17', 1, 2);
''' % (
        index, ls[0][1:], ls[1], index2, ls[2][1:], ls[3])

    index += 2
    index2 += 2

    content += sql + '\n'
  file_utils.write_file('d:\\contenttype.sql', content)


def run():
  # export_permission()
  # print('\n' * 3)
  # export_role()
  # print('\n' * 3)
  # export_role_permission()

  # export_card_data_sql(path='C:\\Users\\Tree\\Downloads\\calypso_card_data_2000',
  #                      product_line='calypso', partner_code='CALYPSO-PTA1', partner_card_category_id='1', start_id=5000)

  # export_card_data_sql(path='C:\\Users\\Tree\\Downloads\\calypso_card_data_2000',
  #                      product_line='snb_obot', partner_code='SNB', partner_card_category_id='4', start_id=7000)

  # print('\n' * 3)
  # export_card_data_sql(path='C:\\Users\\Tree\\Downloads\\ITSO_cardData\\ITSO_cardData',
  #                      product_line='itso', partner_code='ITSO-PTA1', partner_card_category_id='2', start_id=1000)

  # format_langs()

  format_b()

  # import_id()


if __name__ == '__main__':
  run()
