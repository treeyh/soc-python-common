# -*- encoding: utf-8 -*-

import os
from datetime import date, datetime, timedelta
import time
import HtmlTestRunner
from jinja2 import Template
import json


# DEFAULT_TEMPLATE = os.path.join(os.path.dirname(__file__), "report_template.html")

# render_html(
#     testRunner.template,
#     title=testRunner.report_title,
#     header_info=header_info,
#     all_results={test_case_class_name: test_case_tests},
#     status_tags=status_tags,
#     summaries=summaries,
#     **testRunner.template_args
# )



def build_info(module: str, methodName:str, description:str, spendTime:int, status:int, log:list):
  statusName = '失败'
  if status == 0:
    statusName = '成功'
  elif status == -1:
    statusName = '跳过'
  return {
    'className': module,
    'methodName': methodName,
    'description': description,
    'spendTime': str(spendTime) + 'ms',
    'status': statusName,
    'log': log
  }

def build(testName:str, testAll:int, testPass:int, testFail:int, testSkip:int, beginTime:str, totalTime:int, resultInfos:list):
  return {
    'testName': testName,
    'testAll': testAll,
    'testPass': testPass,
    'testFail': testFail,
    'testSkip': testSkip,
    'beginTime': beginTime,
    'totalTime': str(totalTime) + 'ms',
    'testResult': resultInfos
  }



def render_html(template, **kwargs):
  template_file = load_template(template)
  if template_file:
    template = Template(template_file)
    return template.render(**kwargs)


def load_template(template):
  """ Try to read a file from a given path, if file
      does not exist, load default one. """
  file = None
  try:
    if template:
      with open(template, "r") as f:
        file = f.read()
  except Exception as err:
    print("Error: Your Template wasn't loaded", err,
          "Loading Default Template", sep="\n")
  finally:
    if not file:
      with open(DEFAULT_TEMPLATE, "r") as f:
          file = f.read()
    return file


if __name__ == '__main__':
  o = build('name', 1, 2,3, 4, datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'), 1111)
  # print(dir(o))
  print(json.dumps(o, sort_keys=True, indent=4))
  # render_html(
  #   os.path.join(os.path.dirname(__file__), "report_template.html"),
  #   title='report_title',
  #   header_info={
  #     'start_time': datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'),
  #     'statue' : 'header_status',
  #   },
  #   all_results={'test_case_class_name': [{}]},
  #   status_tags=status_tags,
  #   summaries=summaries,    
  # )
