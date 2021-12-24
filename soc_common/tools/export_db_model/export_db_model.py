# -*- coding: UTF-8 -*-

from abc import ABCMeta, abstractmethod

from typing import List

from soc_common.model import ds_model, config_model


class ExportDbModel(object):
  """定义导出接口

  Args:
      object ([type]): [description]
  """
  @abstractmethod
  def export_model(self, conf: config_model.DataSourceConfig) -> ds_model.DataSourceModel:
    """根据数据源导出模型，需要实现该接口

    Args:
        conf (DataSourceConfig): [description]

    Returns:
        ds_model.DataSourceModel: [description]
    """
    pass
