# -*- encoding: utf-8 -*-

'''
@file           :build_soc_builder_json.py
@description    :
@time           :2025-07-17 23:10:58
@author         :Tree
@version        :1.0
'''

import os
import json
from typing import List, Dict
from soc_common.config import config
from soc_common.utils import mysql_utils, file_utils

from soc_common.model import template_fragment, template_item

from soc_common.dao import template_fragment_dao, template_item_dao

_NAME = 'name'
_CODE = 'code'
_GROUPS = 'groups'
_TYPE = 'type'
_PATH = 'path'
_CONTENT = 'content'
_FRAGMENTS = 'fragments'

_TemplateSeries = 'TemplateSeries'
_TemplateGroup = 'TemplateGroup'
_TemplateSet = 'TemplateSet'
_TemplateItem = 'TemplateItem'

_SPAN = '-'

_fragments: List[template_fragment.TemplateFragment] = []
_items: List[template_item.TemplateItem] = []

template = {
  _NAME: '模板定义',
  _CODE: "TemplateDefinition",
  _GROUPS: []
}

LEVEL_CODE = ['series_code', 'group_code', 'set_code', 'code']


def build_soc_builder_json():
  init_template_data()
  build_template()

def init_template_data():
  global _fragments, _items
  _items = template_item_dao.TemplateItemDao().query()
  _fragments = template_fragment_dao.TemplateFragmentDao().query()

  for item in _items:
    item.path = build_path(item)  
  for fragment in _fragments:
    fragment.path = build_path(fragment)  


def build_template():
  global _items, template
  for item in _items:
    build_template_node(item)
  
  file_utils.write_file('export/soc_builder.json', json.dumps(template, ensure_ascii=False, indent=2))

  
    

  

def build_path(item: template_item.TemplateItem | template_fragment.TemplateFragment) -> str:
  global _SPAN
  path = item.series_code.strip()
  if item.group_code.strip() != '':
    path += _SPAN + item.group_code
  if item.set_code.strip() != '':
    path += _SPAN + item.set_code
  return path


def build_template_node(item: template_item.TemplateItem) -> Dict:
  global template, _SPAN
  series_name = item.series_name.strip()
  group_name = item.group_name.strip()
  set_name = item.set_name.strip()
  name = item.name.strip()

  if item.series_code == '':
      return
  series = None
  for s in template[_GROUPS]:
    if item.series_code == s[_CODE]:
      series = s
      break  
  if series is None:    
    series = {
      _NAME: series_name,
      _CODE: item.series_code,
      _TYPE: _TemplateSeries,
      _PATH: item.path,
      _GROUPS: [],
      _FRAGMENTS: []
    }
    series = add_template_fragments(node=series)
    template[_GROUPS].append(series)
  
  if item.group_code == '':
      return
  group = None
  for g in series[_GROUPS]:
    if item.group_code == g[_CODE]:
      group = g
      break
  if group is None:
    group = {
      _NAME: group_name,
      _CODE: item.group_code,
      _TYPE: _TemplateGroup,
      _PATH: item.path,
      _GROUPS: [],
      _FRAGMENTS: []
    }
    group = add_template_fragments(node=group)
    series[_GROUPS].append(group)

  if item.set_code == '':
      return
  set = None
  for s in group[_GROUPS]:
    if item.set_code == s[_CODE]:
      set = s
      break
  if set is None:
    set = {
      _NAME: set_name,
      _CODE: item.set_code,
      _TYPE: _TemplateSet,
      _PATH: item.path,
      _GROUPS: [],
      _FRAGMENTS: []
    }
    set = add_template_fragments(node=set)
    group[_GROUPS].append(set)
  
  if item.code == '':
      return
  item = {
      _NAME: name,
      _CODE: item.code,
      _TYPE: _TemplateSet,
      _PATH: item.path + _SPAN + item.code,
      _CONTENT: {
        'template': item.content,
      },
      _GROUPS: []
  }
  set[_GROUPS].append(item)

  

def add_template_fragments(node: Dict) -> Dict:
  global _fragments, _SPAN

  for fragment in _fragments:
    if fragment.path == node[_PATH]:
      node[_FRAGMENTS].append({
        _NAME: fragment.name,
        _CODE: fragment.code,
        _CONTENT: fragment.content,
        _PATH: node[_PATH] + _SPAN + fragment.code
      })
      
  return node
