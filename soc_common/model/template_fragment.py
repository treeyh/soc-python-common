# -*- coding: UTF-8 -*-

from datetime import datetime, date
from decimal import Decimal
from pydantic import BaseModel
from typing import Dict

# 代码生成器自动生成

# TemplateFragment 
class TemplateFragment(BaseModel):
  """
  """

  
  # 
  id:int = 0
  
  # 系列编号
  series_code:str = ''
  
  # 组编号
  group_code:str = ''
  
  # set编号
  set_code:str = ''
  
  # 名称
  name:str = ''
  
  # 编号
  code:str = ''
  
  # 内容
  content:str = ''
  
  path: str = ''

  def __repr__(self):
    """返回一个对象的描述信息"""
    return "{id:%s, series_code:%s, group_code:%s, set_code:%s, name:%s, code:%s, content:%s, path:%s}" % (str(self.id), str(self.series_code), str(self.group_code), str(self.set_code), str(self.name), str(self.code), str(self.content), str(self.path))