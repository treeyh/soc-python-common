# -*- encoding: utf-8 -*-

from typing import Dict, List

from soc_common.config import config
from soc_common.utils import mysql_utils, date_utils
from soc_common.model.template_item import TemplateItem

class TemplateItemDao(object):
    
  def __init__(self) -> None:
    self.dbUtil = mysql_utils.get_mysql_utils(**config.DB_CONFIG)

    self.selectSql = '''SELECT `id`, `series_code`, `series_name`, `group_code`, `group_name`, `set_code`, `set_name`, `name`, `code`, `content` FROM `template_item` ORDER BY `series_code`, `group_code`, `set_code`, `code` ASC '''

    self.columns = ['id', 'series_code', 'series_name', 'group_code', 'group_name', 'set_code', 'set_name', 'name', 'code', 'content']


  def save(self, obj: TemplateItem) -> int:
    id = self.dbUtil.insert_or_update_or_delete(self.insertSql, params=vars(obj), isbackinsertid=True)
    return id
  

  def get(self, id: int) -> TemplateItem:
    sql = self.selectSql + ' AND "id"=%(id)s '
    data = self.dbUtil.find_one(sql=sql, params={'id': id}, mapcol= self.columns)
    if data is None:
      return None
    return TemplateItem(**data)
  
  def query(self) -> List[TemplateItem]:
    sql = self.selectSql
    data = self.dbUtil.find_all(sql=sql, params=(), mapcol=self.columns)
    result = []
    if data == None:
      return result
    
    for d in data:
      result.append(TemplateItem(**d))
    return result
