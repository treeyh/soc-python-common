# -*- encoding: utf-8 -*-

import os
import sys

from soc_common.utils import file_utils


_permission_content = '''
1	SNB	GeoTec管理后台	sys	/sys	0	{"oper":[{"code":"*","name":"管理后台所有权限"}]}
2	SNB	系统管理	manager	/sys/manager	1	{"oper":[{"code":"*","name":"系统管理下所有权限"}]}
3	SNB	合作方管理	partnerManager	/sys/manager/partnerManager	2	{"oper":[{"code":"Menu","name":"查看合作方菜单"},{"code":"View","name":"查看合作方"},{"code":"Create","name":"创建合作方"},{"code":"Update","name":"编辑合作方"},{"code":"Delete","name":"删除合作方"}]}
4	SNB	账户管理	accountManager	/sys/manager/accountManager	2	{"oper":[{"code":"Menu","name":"查看账户菜单"},{"code":"View","name":"查看账户"},{"code":"Create","name":"创建账户"},{"code":"Update","name":"编辑账户"},{"code":"Delete","name":"删除账户"}]}
5	SNB	角色管理	roleManager	/sys/manager/roleManager	2	{"oper":[{"code":"View","name":"查看角色"},{"code":"Create","name":"创建角色"},{"code":"Update","name":"编辑角色"},{"code":"Delete","name":"删除角色"}]}
6	SNB	权限管理	permissionManager	/sys/manager/permissionManager	2	{"oper":[{"code":"View","name":"查看权限"},{"code":"Create","name":"创建权限"},{"code":"Update","name":"编辑权限"},{"code":"Delete","name":"删除权限"}]}
7	SNB	资源管理	resourceManager	/sys/manager/resourceManager	2	{"oper":[{"code":"Menu","name":"查看资源菜单"},{"code":"View","name":"查看资源"},{"code":"Create","name":"创建资源"},{"code":"Update","name":"编辑资源"},{"code":"Delete","name":"删除资源"}]}
8	SNB	操作日志管理	operLogManager	/sys/manager/operLogManager	2	{"oper":[{"code":"View","name":"查看操作日志"}]}
9	SNB	配置管理	configManager	/sys/manager/configManager	2	{"oper":[{"code":"View","name":"查看配置"},{"code":"Update","name":"修改配置"}]}
100	SNB	GeoTec管理	geoTec	/sys/geoTec	1	{"oper":[{"code":"*","name":"GeoTec管理下所有权限"}]}
101	SNB	产品管理	productManager	/sys/geoTec/productManager	100	{"oper":[{"code":"Menu","name":"查看产品菜单"},{"code":"View","name":"查看产品"},{"code":"Check","name":"审核产品"},{"code":"Update","name":"编辑产品"}]}
102	SNB	License管理	licenseManager	/sys/geoTec/licenseManager	100	{"oper":[{"code":"Menu","name":"查看License菜单"},{"code":"View","name":"查看License"},{"code":"Download","name":"下载License"}]}
103	SNB	批次管理	batchManager	/sys/geoTec/batchManager	100	{"oper":[{"code":"Menu","name":"查看批次菜单"},{"code":"View","name":"查看批次"}]}
104	SNB	产品类型管理	productCategoryManager	/sys/geoTec/productCategoryManager	100	{"oper":[{"code":"Menu","name":"查看产品类型菜单"},{"code":"View","name":"查看产品类型"},{"code":"Create","name":"创建产品类型"},{"code":"Update","name":"编辑产品类型"},{"code":"Delete","name":"删除产品类型"}]}
200	SNB	FindMy管理	findMy	/sys/findMy	1	{"oper":[{"code":"*","name":"FindMy管理下所有权限"}]}
201	SNB	FindMy产品管理	fmProductManager	/sys/findMy/fmProductManager	200	{"oper":[{"code":"Menu","name":"查看FindMy产品菜单"},{"code":"View","name":"查看FindMy产品"},{"code":"Create","name":"创建FindMy产品"},{"code":"Update","name":"编辑FindMy产品"},{"code":"Delete","name":"删除FindMy产品"}]}
202	SNB	任务管理	fmBatchManager	/sys/findMy/fmBatchManager	200	{"oper":[{"code":"Menu","name":"查看FindMy任务菜单"},{"code":"View","name":"查看FindMy任务"},{"code":"CreateApply","name":"创建FindMy申请任务"},{"code":"CreateAllot","name":"创建FindMy分配任务"},{"code":"CreateDestroy","name":"创建FindMy销毁任务"},{"code":"Update","name":"编辑FindMy任务"},{"code":"Delete","name":"删除FindMy任务"}]}
203	SNB	License管理	fmLicenseManager	/sys/findMy/fmLicenseManager	200	{"oper":[{"code":"Menu","name":"查看FindMyLicense菜单"},{"code":"View","name":"查看FindMyLicense"},{"code":"Create","name":"创建FindMyLicense"},{"code":"Update","name":"编辑FindMyLicense"},{"code":"Delete","name":"删除FindMyLicense"},{"code":"Download","name":"下载FindMyLicense"}]}
1000		合作方自管理	partner	/sys/partner/{partnerCode}	1	{"oper":[{"code":"*","name":"合作方自身下所有权限"}]}
1001		合作方GeoTec管理	geoTec	/sys/partner/{partnerCode}/geoTec	1000	{"oper":[{"code":"*","name":"合作方GeoTec管理下所有权限"}]}
1002		合作方基础信息管理	partnerManager	/sys/partner/{partnerCode}/geoTec/partnerManager	1001	{"oper":[{"code":"Menu","name":"查看基础信息菜单"},{"code":"View","name":"查看合作方"},{"code":"Update","name":"编辑合作方"}]}
1003		合作方应用管理	appManager	/sys/partner/{partnerCode}/geoTec/appManager	1001	{"oper":[{"code":"View","name":"查看应用"},{"code":"Create","name":"创建应用"},{"code":"Update","name":"编辑应用"},{"code":"Delete","name":"删除应用"}]}
1004		合作方应用签名管理	appSignManager	/sys/partner/{partnerCode}/geoTec/appSignManager	1001	{"oper":[{"code":"View","name":"查看应用签名"},{"code":"Create","name":"创建应用签名"},{"code":"Update","name":"编辑应用签名"},{"code":"Delete","name":"删除应用签名"}]}
1005		合作方产品管理	productManager	/sys/partner/{partnerCode}/geoTec/productManager	1001	{"oper":[{"code":"Menu","name":"查看合作方产品菜单"},{"code":"View","name":"查看产品"},{"code":"Create","name":"创建产品"},{"code":"Update","name":"编辑产品"},{"code":"Delete","name":"删除产品"}]}
1006		合作方批次管理	batchManager	/sys/partner/{partnerCode}/geoTec/batchManager	1001	{"oper":[{"code":"View","name":"查看批次"},{"code":"Create","name":"创建批次"},{"code":"Update","name":"编辑批次"},{"code":"Delete","name":"删除批次"}]}
1007		合作方License管理	licenseManager	/sys/partner/{partnerCode}/geoTec/licenseManager	1001	{"oper":[{"code":"View","name":"查看License"},{"code":"Download","name":"下载License"}]}
1008		合作方固件管理	fwManager	/sys/partner/{partnerCode}/geoTec/fwManager	1001	{"oper":[{"code":"View","name":"查看固件"},{"code":"Create","name":"创建固件"},{"code":"Update","name":"编辑固件"},{"code":"Delete","name":"删除固件"}]}
2000		合作方FindMy管理	findMy	/sys/partner/{partnerCode}/findMy	1000	{"oper":[{"code":"*","name":"合作方FindMy管理下所有权限"}]}
2001		合作方FindMy分配管理	fmBatchManager	/sys/partner/{partnerCode}/findMy/fmBatchManager	2000	{"oper":[{"code":"Menu","name":"查看合作方分配菜单"},{"code":"View","name":"查看FindMy合作方分配"}]}
2002		合作方FindMyLicense管理	fmLicenseManager	/sys/partner/{partnerCode}/findMy/fmLicenseManager	2000	{"oper":[{"code":"Menu","name":"查看License管理菜单"},{"code":"View","name":"查看License"},{"code":"Download","name":"下载License"},{"code":"Upload","name":"上传License"},{"code":"Destroy","name":"销毁License"}]}
2003		合作方FindMy操作日志管理	fmOperLogManager	/sys/partner/{partnerCode}/findMy/fmOperLogManager	2000	{"oper":[{"code":"View","name":"查看FindMy操作日志"}]}
'''

_role_content = '''
1	SNB	超级管理员
2	SNB	后台管理员
3	SNB	雪球Geo业务管理员
4	SNB	雪球FindMy业务管理员
'''

_role_permission_content = '''
1	SNB	1	1	/sys	|*|
2	SNB	2	2	/sys/manager	|*|
3	SNB	2	100	/sys/geoTec	|*|
4	SNB	2	200	/sys/findMy	|*|
5	SNB	3	1001	/sys/partner/SNB/geoTec	|*|
6	SNB	4	2000	/sys/partner/SNB/findMy	|*|
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
    sql = '''INSERT INTO `tecm_permission` (`id`, `partner_code`, `name`, `code`, `path`, `parent_id`, `operation`, `remark`, `status`, `creator`, `create_time`, `updator`, `update_time`, `version`, `del_flag`, `sort`) VALUES (%s, '%s', '%s', '%s', '%s', %s, '%s', '', 1, 0, '2021-11-11 17:28:34', 0, '2021-11-11 17:28:34', 1, 2, %s);''' % (
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
    if len(ls) != 3:
      continue
    index += 1
    sql = '''INSERT INTO `tecm_role` (`id`, `partner_code`, `name`, `remark`, `status`, `creator`, `create_time`, `updator`, `update_time`, `version`, `del_flag`) VALUES (%s, '%s', '%s', '', 1, 0, '2021-11-11 18:29:00', 0, '2021-11-11 18:29:00', 1, 2);''' % (
        ls[0], ls[1], ls[2])
    print(sql)


def export_role_permission():
  global _role_permission_content

  index = 0
  for c in _role_permission_content.split('\n'):
    line = c.strip()
    if line == '':
      continue
    ls = line.split('\t')
    if len(ls) != 6:
      continue
    index += 1
    sql = '''INSERT INTO `tecm_role_permission` (`id`, `partner_code`, `role_id`, `permission_id`, `permission_path`, `operation_codes`, `remark`, `status`, `creator`, `create_time`, `updator`, `update_time`, `version`, `del_flag`) VALUES (%s, '%s', %s, %s, '%s', '%s', '', 1, 1, '2021-11-11 18:31:38', 1, '2021-11-11 18:31:38', 1, 2);''' % (
        ls[0], ls[1], ls[2], ls[3], ls[4], ls[5])
    print(sql)


def export_card_data_sql(path: str, product_line: str, partner_code: str, partner_card_category_id: str, start_id: int):
  filePaths = file_utils.walk2(path)
  # print(filePaths)

  id = start_id
  content = ''
  for filePath in filePaths:
    if len(filePath) != 2:
      continue
    sql = ''' INSERT INTO `op_card_manager_db`.`oscm_card_data` (`id`, `product_line_code`, `partner_code`, `partner_card_category_id`, `card_no`, `card_info`, `backup_info`, `active_time`, `effective_time`, `task_batch_id`, `renew_count`, `card_id`, `issuer_biz_id`, `order_id`, `backup_biz_id`, `remark`, `status`, `create_time`, `update_time`, `version`, `del_flag`) VALUES (%s, '%s', '%s', %s, '%s', '%s', '', '2021-12-28 14:50:12', '2099-01-01 00:00:00', 0, 0, 0, 0, 0, 0, '', 1, '2021-12-28 14:50:12', '2021-12-28 14:50:12', 1, 2);
    ''' % (
        id, product_line, partner_code, partner_card_category_id, filePath[1].replace('.json', ''), file_utils.read_all_file(os.path.join(filePath[0], filePath[1])).strip())
    id += 1
    content += sql
  file_utils.write_file('d:\\card'+product_line+'.txt', content)


def run():
  # export_permission()
  # print('\n' * 3)
  # export_role()
  # print('\n' * 3)
  # export_role_permission()
  export_card_data_sql(path='C:\\Users\\Tree\\Downloads\\calypso_cardData\\calypso_cardData',
                       product_line='calypso', partner_code='CALYPSO-PTA1', partner_card_category_id='1', start_id=1)
  print('\n' * 3)
  export_card_data_sql(path='C:\\Users\\Tree\\Downloads\\ITSO_cardData\\ITSO_cardData',
                       product_line='itso', partner_code='ITSO-PTA1', partner_card_category_id='2', start_id=1000)


if __name__ == '__main__':
  run()
