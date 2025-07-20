# -*- coding: UTF-8 -*-

from datetime import datetime, date
from decimal import Decimal
from pydantic import BaseModel
from typing import Dict

# 代码生成器自动生成

# TemplateItem 
class TemplateItem(BaseModel):
  """
  """

  
  # 
  id:int = 0
  
  # 系列编号
  series_code:str = ''
  
  # 系列名
  series_name:str = ''
  
  # 组编号
  group_code:str = ''
  
  # 组名称
  group_name:str = ''
  
  # set编号
  set_code:str = ''
  
  # set名称
  set_name:str = ''
  
  # 名称
  name:str = ''
  
  # 编号
  code:str = ''
  
  # 内容
  content:str = ''

  path:str = ''
  

  def __repr__(self):
    """返回一个对象的描述信息"""
    return "{id:%s, series_code:%s, series_name:%s, group_code:%s, group_name:%s, set_code:%s, set_name:%s, name:%s, code:%s, content:%s, path:%s}" % (str(self.id), str(self.series_code), str(self.series_name), str(self.group_code), str(self.group_name), str(self.set_code), str(self.set_name), str(self.name), str(self.code), str(self.content), str(self.path))