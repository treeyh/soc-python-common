# -*- encoding: utf-8 -*-

from utils import str_utils, file_utils
import os
import sys
import re

path = os.path.split(os.path.realpath(__file__))[0]
sys.path.append(path + os.sep + '..')


base_path = '/Users/tree/work/99_tree/03_github/soc-python-common/src/tools/sql/md'

file_sqls = [
    # {
    #     'name' : 'ppm_bas_project_type.log',
    #     'comment' : '项目类型',
    #     'begin' : 1,
    #     'end' : -1,
    #     'sql' : '''INSERT INTO ppm_bas_project_type( `id`, `lang_code`, `name`, `sort`, `remark`, `status`, `creator`, `create_time`, `updator`, `update_time`, `version`, `is_delete` )
    #     VALUES ( %s, '%s', '%s', %s, '%s', 1, 1, now(), 1, now(), 1, 0);''',
    # },
    {
        'name': 'ppm_bas_object_id.log',
        'comment': '对象id生成',
        'begin': 1,
        'end': -1,
        'sql': '''INSERT INTO ppm_bas_object_id( `id`, `org_id`, `code`, `max_id`, `step`, `creator`, `create_time`, `updator`, `update_time`, `version`, `is_delete` ) 
        VALUES ( %s, %s,  '%s', %s, %s, 1, now(), 1, now(), 1, 2);''',
    },
    {
        'name': 'ppm_rol_operation.log',
        'comment': '操作',
        'begin': 1,
        'end': -1,
        'sql': '''INSERT INTO ppm_rol_operation (`id`, `code`, `name`, `remark`, `status`	, `creator`, `create_time`, `updator`, `update_time`, `version`	, `is_delete`) 
    VALUES (%s, '%s', '%s', '%s', 1	, 1, now(), 1, now(), 1, 2);''',
    },
    {
        'name': 'ppm_rol_permission.log',
        'comment': '权限项类型',
        'begin': 1,
        'end': -2,
        'sql': '''INSERT INTO ppm_rol_permission( `id`, `org_id`, `lang_code`, `code`, `name`, `parent_id`, `type`, `path`, `remark`, `status`, `creator`, `create_time`, `updator`, `update_time`, `version`, `is_delete` ) 
    VALUES ( %s, %s, '%s', '%s', '%s', %s, %s, '%s', '', 1, 1, now(), 1, now(), 1, 2);''',
    },
    {
        'name': 'ppm_rol_permission_operation.log',
        'comment': '权限关联操作',
        'begin': 1,
        'end': -1,
        'sql': '''INSERT INTO ppm_rol_permission_operation( `id`, `org_id`, `permission_id`, `lang_code`, `name`, `operation_codes`, `remark`, `status`, `creator`, `create_time`, `updator`, `update_time`, `version`, `is_delete` ) 
    VALUES ( %s, %s, %s, '%s', '%s', '%s', '%s', 1, 1, now(), 1, now(), 1, 2);''',

        # |1|1|2|PermissionOperation.Sys.Dic.View|查看数据字典|View||
    },
    {
        'name': 'ppm_rol_role_group.log',
        'comment': '角色组',
        'begin': 1,
        'end': -1,
        'sql': '''INSERT INTO ppm_rol_role_group( `id`, `org_id`, `lang_code`, `name`, `remark`, `type`, `is_readonly`, `is_show`, `is_default`, `status`, `creator`, `create_time`, `updator`, `update_time`, `version`, `is_delete` ) 
        VALUES ( %s, %s, '%s', '%s', '%s', %s, %s, %s, %s, 1, 1, now(), 1, now(), 1, 2);''',
    },
    {
        'name': 'ppm_rol_role.log',
        'comment': '角色',
        'begin': 1,
        'end': -2,
        'sql': '''INSERT INTO ppm_rol_role( `id`, `org_id`, `lang_code`, `name`, `remark`, `is_readonly`, `is_modify_permission`, `is_default`, `role_group_id`, `status`, `creator`, `create_time`, `updator`, `update_time`, `version`, `is_delete` ) 
        VALUES ( %s, %s, '%s', '%s', '%s', %s, %s, %s, %s, 1, 1, now(), 1, now(), 1, 2);''',
    },
    {
        'name': 'ppm_rol_role_permission_operation.log',
        'comment': '角色',
        'begin': 1,
        'end': -1,
        'trans': True,
        'sql': '''INSERT INTO ppm_rol_role_permission_operation( `id`, `org_id`, `role_id`, `project_id`, `permission_id`, `permission_path`, `operation_codes`, `creator`, `create_time`, `updator`, `update_time`, `version`, `is_delete` )        
        VALUES ( %s, %s, %s, %s, %s, '%s', '%s', 1, now(), 1, now(), 1, 2);''',

    },
    {
        'name': 'ppm_tre_trends.log',
        'comment': '角色',
        'begin': 1,
        'end': -1,
        'sql': '''INSERT INTO ppm_tre_trends( `id`, `org_id`, `uuid`, `module1`, `module2_id`, `module2`, `module3_id`, `module3`, `oper_code`, `oper_obj_id`, `oper_obj_type`, `oper_obj_property`, `relation_obj_id`, `relation_obj_type`, `relation_type`, `new_value`, `old_value`, `ext`, `creator`, `create_time`, `is_delete` ) 
        VALUES ( %s, %s, '%s', '%s', %s, '%s', %s, '%s', '%s', %s, '%s', '%s', %s, '%s', '%s', '%s', '%s', '%s', 1, now(), 2);''',
    },
    {
        'name': 'ppm_prs_process_status.log',
        'comment': '流程状态',
        'begin': 1,
        'end': -1,
        'sql': '''INSERT INTO ppm_prs_process_status( `id`, `org_id`, `lang_code`, `name`, `sort`, `bg_style`, `font_style`, `type`, `category`, `remark`, `status`, `creator`, `create_time`, `updator`, `update_time`, `version`, `is_delete` ) 
        VALUES ( %s, %s, '%s', '%s', %s, '%s', '%s', %s, %s, '%s', 1, 1, now(), 1, now(), 1, 2);''',
    },
    {
        'name': 'ppm_prs_process.log',
        'comment': '流程',
        'begin': 1,
        'end': -1,
        'sql': '''INSERT INTO ppm_prs_process( `id`, `org_id`, `lang_code`, `name`, `is_default`, `type`, `sort`, `creator`, `create_time`, `updator`, `update_time`, `version`, `is_delete` ) 
        VALUES ( %s, %s, '%s', '%s', %s, %s, %s, 1, now(), 1, now(), 1, 2);''',
    },
    {
        'name': 'ppm_prs_process_process_status.log',
        'comment': '流程与流程状态关联',
        'begin': 1,
        'end': -1,
        'sql': '''INSERT INTO ppm_prs_process_process_status( `id`, `org_id`, `process_id`, `process_status_id`, `is_init_status`, `sort`, `creator`, `create_time`, `updator`, `update_time`, `version`, `is_delete` ) 
        VALUES ( %s, %s, %s, %s, %s, %s, 1, now(), 1, now(), 1, 2);''',
    },
    {
        'name': 'ppm_prs_process_step.log',
        'comment': '流程步骤',
        'begin': 1,
        'end': -1,
        'sql': '''INSERT INTO ppm_prs_process_step( `id`, `org_id`, `process_id`, `lang_code`, `name`, `start_status`, `end_status`, `sort`, `is_default`, `remark`, `status`, `creator`, `create_time`, `updator`, `update_time`, `version`, `is_delete` ) 
        VALUES ( %s, %s, %s, '%s', '%s', %s, %s, %s, %s, '', 1, 1, now(), 1, now(), 1, 2);''',
    },
    {
        'name': 'ppm_prs_project_type.log',
        'comment': '项目类型',
        'begin': 1,
        'end': -1,
        'sql': '''INSERT INTO ppm_prs_project_type( `id`, `org_id`, `lang_code`, `name`, `sort`, `default_process_id`, `category`, `mode`, `is_readonly`, `remark`, `status`, `creator`, `create_time`, `updator`, `update_time`, `version`, `is_delete` ) 
        VALUES ( %s, %s, '%s', '%s', %s, %s, %s, %s, %s, '%s', 1, 1, now(), 1, now(), 1, 2);''',
    },
    {
        'name': 'ppm_prs_project_object_type.log',
        'comment': '项目对象类型',
        'begin': 1,
        'end': -1,
        'sql': '''INSERT INTO ppm_prs_project_object_type( `id`, `org_id`, `lang_code`, `pre_code`, `name`, `object_type`, `bg_style`, `font_style`, `icon`, `sort`, `remark`, `is_readonly`, `status`, `creator`, `create_time`, `updator`, `update_time`, `version`, `is_delete` ) 
        VALUES ( %s, %s, '%s', '%s', '%s', %s, '', '', '', %s, '%s', %s, 1, 1, now(), 1, now(), 1, 2);''',
    },
    {
        'name': 'ppm_prs_project_type_project_object_type.log',
        'comment': '项目类型项目对象关联',
        'begin': 1,
        'end': -1,
        'sql': '''INSERT INTO ppm_prs_project_type_project_object_type( `id`, `org_id`, `project_type_id`, `project_object_type_id`, `remark`, `default_process_id`, `is_readonly`, `status`, `creator`, `create_time`, `updator`, `update_time`, `version`, `is_delete` ) 
        VALUES ( %s, %s, %s, %s, '%s', %s, %s, 1, 1, now(), 1, now(), 1, 2);''',
    },
    {
        'name': 'ppm_bas_app_info.log',
        'comment': '应用信息',
        'begin': 1,
        'end': -1,
        'sql': '''INSERT INTO ppm_bas_app_info( `id`, `name`, `code`, `secret1`, `secret2`, `owner`, `check_status`, `remark`, `status`, `creator`, `create_time`, `updator`, `update_time`, `version`, `is_delete` ) 
        VALUES ( %s, '%s', '%s', '%s', '%s', '%s', %s, '%s', 1, 1, now(), 1, now(), 1, 2);''',
    },
    {
        'name': 'ppm_bas_source_channel.log',
        'comment': '来源渠道',
        'begin': 1,
        'end': -1,
        'sql': '''INSERT INTO ppm_bas_source_channel( `id`, `code`, `name`, `remark`, `status`, `creator`, `create_time`, `updator`, `update_time`, `version`, `is_delete` ) 
        VALUES ( %s, '%s', '%s', '%s', 1, 1, now(), 1, now(), 1, 2);''',
    },

]


def read_file(path):
  lines = file_utils.read_all_lines_file(path)
  return lines


def format_sql(sql, ls):

  return sql % tuple(ls)


def run():
  global base_path
  global file_sqls

  init_path = os.path.join(base_path, 'init.log')

  lines = read_file(init_path)

  content = ''.join(lines)

  for fs in file_sqls:
    p = os.path.join(base_path, fs['name'])

    content += os.linesep + os.linesep + os.linesep + '-- ' + fs['comment']
    content += os.linesep + 'truncate table ' + fs['name'].replace('.log', '') + ';' + os.linesep

    lines = read_file(p)

    for line in lines:
      ls = line.strip().split('|')

      if len(ls) < 2:
        continue

      ll = []
      for s in ls:
        if fs.get('trans', None) == True:
          ll.append(s.strip().replace(',', '|'))
        else:
          ll.append(s.strip())

      # print( ls)
      sql = format_sql(fs['sql'], ll[fs['begin']:fs['end']])

      content += os.linesep + sql

  result_path = os.path.join(base_path, 'init_data.log')
  file_utils.write_file(result_path, content)


if __name__ == '__main__':
  run()
