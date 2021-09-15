# -*- encoding: utf-8 -*-

import os
import sys
import re
import logging
import javalang
from jinja2 import Template

from soc_common.utils import str_utils, file_utils, attr_display_utils


# java model 源码目录
_source_folder = 'D:\\tmp\\tmp'

# 生成代码目标目录
_target_folder = 'D:\\tmp\\tmp2'

_golang_code_template = os.path.join(os.path.dirname(
    __file__), 'template', 'golang_domain.template')

# golang 包名
_package_name = 'dto'

# 清楚java类后缀
_clear_suffixs = ['BO', 'DTO', 'PO', 'DAO', 'VO']


def get_java_files():
  global _source_folder

  javaFiles = file_utils.walk2(_source_folder)

  return javaFiles


def analysis_java_class_info(cla) -> list:
  """解析java class

  Args:
      cla ([type]): [description]

  Returns:
      list: 输出JavaClass对象数组
  """
  global _clear_suffixs, _package_name
  javaClasses = []
  javaClass = JavaClass(str_utils.clear_str_end_chart(
      cla.name, _clear_suffixs), packageName=_package_name)
  javaClass.fileName = str_utils.hump2underline(javaClass.name) + '_' + _package_name
  if cla.extends != None:
    javaClass.extends.append(cla.extends.name)
  if cla.documentation != None:
    javaClass.comment = cla.documentation

  for fie in cla.body:

    if type(fie).__name__ == 'FieldDeclaration':
      # 属性字段

      if 'static' in fie.modifiers:
        # 静态变量忽略
        # TODO @JsonIgnore @JsonIgnoreProperties @JSONField(serialize = false) 也需要忽略，待实现
        continue
      fieName = str_utils.upperFirstWord(fie.declarators[0].name)
      typeType = type(fie.type).__name__
      typeName = str_utils.clear_str_end_chart(fie.type.name, _clear_suffixs)
      listFlag = False
      mapFlag = False
      subTypes = []
      if typeName in ('List', 'ArrayList', 'LinkList', 'Set', 'HashSet', 'TreeSet'):
        listFlag = True
        subTypes = [str_utils.clear_str_end_chart(fie.type.arguments[0].type.name, _clear_suffixs)]
        typeName = '[]'+subTypes[0]
      elif typeName in ('Map', 'HashMap', 'TreeMap', 'LinkedHashMap', 'Hashtable'):
        mapFlag = True
        subTypes = [str_utils.clear_str_end_chart(fie.type.arguments[0].type.name, _clear_suffixs), str_utils.clear_str_end_chart(
            fie.type.arguments[1].type.name, _clear_suffixs)]
        # TODO 还需要判断不是基本类型才能加 {}
        typeName = 'map['+subTypes[0]+']'+subTypes[1]+'{}'

      jsonName = fie.declarators[0].name
      comment = fie.documentation if fie.documentation != None else ''
      javaClass.fields.append(Field(fieName, typeType, typeName=typeName, subTypes=subTypes,
                                    jsonName=jsonName, comment=comment, listFlag=listFlag, mapFlag=mapFlag))
      javaClasses.append(javaClass)
    elif type(fie).__name__ == 'ClassDeclaration':
      # 内部类
      javaClasses.extend(analysis_java_class_info(fie))
  return javaClasses


def analysis_java_class(javaFiles):

  javaClasses = []

  if len(javaFiles) <= 0:
    return javaClasses

  for j in javaFiles:
    filePath = os.path.join(j[0], j[1])
    if 'java' != file_utils.get_file_suffix(filePath).lower() or j[1] != 'WhitelistDTO.java':
      continue
    javaInfo = javalang.parse.parse(file_utils.read_all_file(filePath))

    for ja in javaInfo.types:
      if type(ja).__name__ != 'ClassDeclaration':
        continue
      javaClasses.extend(analysis_java_class_info(ja))

  # print(javaClasses)
  return javaClasses


def build_gloang_code_info(javaClass) -> str:

  pass


def build_golang_code(javaClasses: list):
  global _clear_suffixs, _package_name, _golang_code_template
  template_info = file_utils.read_all_file(_golang_code_template)
  print(template_info)
  template = Template(template_info)
  for javaClass in javaClasses:

    html = template.render(packageName=javaClass.packageName, comment=javaClass.comment,
                           name=javaClass.name, extends=javaClass.extends, fields=javaClass.fields)
    print(html)
  pass


def run():
  javaFiles = get_java_files()

  javaClasses = analysis_java_class(javaFiles)
  build_golang_code(javaClasses)

  # val = '1234567890'
  # print(val[-2:])
  # print(len('123'))
  # print(val[:-2])


class Field(attr_display_utils.AttrDisplay):
  def __init__(self, name: str, typeType, typeName: str = '', subTypes: list = [],
               jsonName: str = '', comment: str = '', listFlag: bool = False, mapFlag: bool = False):
    self.name = name
    self.typeType = typeType
    self.typeName = typeName
    self.subTypes = subTypes
    self.jsonName = jsonName
    self.comment = comment
    self.listFlag = listFlag
    self.mapFlag = mapFlag


class JavaClass(attr_display_utils.AttrDisplay):
  def __init__(self, name, fileName: str = '', extends: list = [], fields: list = [], comment: str = '', packageName='dto'):
    self.name = name
    self.fileName = fileName
    self.extends = extends
    self.fields = fields
    self.comment = comment
    self.packageName = packageName
