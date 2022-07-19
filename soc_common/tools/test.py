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
'tool.networkDns.host': 'Host',
   'tool.networkDns.aRecord': 'A record',
   'tool.networkDns.cname': 'Cname',
   'tool.networkDns.ptrRecord': 'Ptr record',
   'tool.networkDns.nsRecord': 'Ns record',
   'tool.networkDns.maxRecord': 'Max record',
   'tool.networkDns.txtRecord': 'Txt record',

  }

  content = ''
  for k, v in langMap.items():
    ks = k.split('.')
    key = ks[0] + ''.join([str_utils.upperFirstWord(i) for i in ks[1:]])
    content += '  static String get %s =>\'%s\'.tr;\n' % (key, k)
  print(content)


def build_late_widget(v, count):
  code = v['code']
  code2 = str_utils.upperFirstWord(code)
  name = v['name']
  for i in range(1, count):
    print('/// '+name + ' ' + str(i))
    print('late final FocusNode '+code+'ValueFocusNode'+str(i) +
          ';\nlate final TextEditingController '+code+'ValueController'+str(i)+';\n')


def build_dispose_widget(v, count):
  code = v['code']
  code2 = str_utils.upperFirstWord(code)
  name = v['name']
  for i in range(1, count):
    print(code+'ValueFocusNode'+str(i)+'.dispose();\n' +
          code+'ValueController'+str(i)+'.dispose();\n')


def build_init_widget(v, count):
  code = v['code']
  code2 = str_utils.upperFirstWord(code)
  name = v['name']
  for i in range(1, count):
    print(code+'ValueFocusNode'+str(i)+' = FocusNode();\n' +
          code+'ValueController'+str(i)+' = TextEditingController();\n' +
          code+'ValueController'+str(i)+'.text = \'\';\n')


def build_focus_widget(v, count):
  code = v['code']
  code2 = str_utils.upperFirstWord(code)
  name = v['name']
  for i in range(1, count):
    print('controller.' + code+'ValueFocusNode'+str(i)+',')


def build_func_widget(v, count):
  code = v['code']
  code2 = str_utils.upperFirstWord(code)
  name = v['name']
  content = ''

  for i in range(1, count):
    content += '''        SocTextField(
          key: const Key('%(code)sValueController%(i)s'),
          keyName: '%(code)sValueController%(i)s',
          focusNode: controller.%(code)sValueFocusNode%(i)s,
          controller: controller.%(code)sValueController%(i)s,
          labelText: \'${Langs.toolCalcVolumeSideLength}(a)\',
          keyboardType: TextInputType.numberWithOptions(decimal: true),
          maxDecimalLength: 8,
          clearIconFlag: true,
        ),
        BaseStyle.vGap12,''' % {'code': code, 'i': str(i)}

  print('''  /// 构建%(name)s输入view
  Widget _build%(code2)sInputs(BuildContext context) {
    return Column(
      children: [
        %(content)s
      ],
    );
  }''' % {'name': name, 'code2': code2, 'content': content})


def build_const_widget(v, count):
  code = v['code']
  code2 = str_utils.upperFirstWord(code)
  name = v['name']

  print('  /// %(name)s\n  static const String %(code)s = \'%(code)s\';' %
        {'code': code, 'name': name})


def build_supports_widget(v, count):
  print(v['code'] + ',')


def build_map_widget(v, count):
  code = v['code']
  print('CalcPerimeterController.%s: _build%sInputs,' % (code, str_utils.upperFirstWord(code)))


def build_all_widget():
  lists = []

  lists.append({
      'code': 'square',
      'name': '正方形',
      'count': 2,
  })
  lists.append({
      'code': 'rectangle',
      'name': '长方形',
      'count': 3,
  })
  lists.append({
      'code': 'circular',
      'name': '圆形',
      'count': 3,
  })
  lists.append({
      'code': 'triangle',
      'name': '三角形',
      'count': 4,
  })
  lists.append({
      'code': 'parallelogram',
      'name': '四边形',
      'count': 5,
  })
  lists.append({
      'code': 'ellipse',
      'name': '椭圆形',
      'count': 3,
  })
  lists.append({
      'code': 'sector1',
      'name': '扇形1',
      'count': 3,
  })
  lists.append({
      'code': 'sector2',
      'name': '扇形2',
      'count': 3,
  })

  for v in lists:
    # build_late_widget(v, v['count'])
    # build_dispose_widget(v, v['count'])

    # build_init_widget(v, v['count'])
    # build_focus_widget(v, v['count'])
    build_func_widget(v, v['count'])

    # build_const_widget(v, v['count'])
    # build_supports_widget(v, v['count'])
    # build_map_widget(v, v['count'])


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
  # build_all_widget()
  format_b()

  # import_id()


if __name__ == '__main__':
  run()
