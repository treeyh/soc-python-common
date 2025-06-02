# -*- encoding: utf-8 -*-

'''
@file           :read_xqz.py
@description    :
@time           :2025-06-02 15:07:44
@author         :Tree
@version        :1.0
'''

from typing import List
from soc_common.utils import file_utils


def trans_qj(source_file_path: str, target_file_path: str):
    """
    Transforms a file by replacing commas with semicolons and saving the result to a new file.
    
    :param source_file_path: Path to the source file to be transformed.
    :param target_file_path: Path where the transformed file will be saved.
    """
    lines = file_utils.read_all_lines_file(filePath=source_file_path)

    with open(target_file_path, 'w', encoding='utf-8') as f:
        for l in lines:
            f.write(l.strip().replace(',', ';') + '\n')

def read_xqz(file_path:str, target_path:str) -> List[str]:
    """
    Reads a file and returns its content as a list of lines.
    
    :param file_path: Path to the file to be read.
    :return: List of lines in the file.
    收支类型,账单类型,金额,手续费,不计收支,不计预算,分类,子分类,记账日期,备注信息,标签,报销状态,退款状态,退款金额,账本名称,账户名称,转入账户名称,借款账户名称
    """
    lines = file_utils.read_all_lines_file(filePath=file_path)

    qj_content = ['时间,分类,二级分类,类型,金额,币种,账户1,账户2,备注,账单标记,手续费,优惠券,标签,账单图片']
    
    for l in lines:
        ls = l.strip().split(',')
        if ls[3] != '' and ls[3] != '0.00':
            print(ls)
        qjs = [ls[8], ls[6], ls[7], ls[0], ls[2], 'CNY', '', '', ls[9].replace('"', ''), '', '', '', '', '']
        qj_content.append(','.join(qjs))
    
    file_utils.write_file(target_path, '\n'.join(qj_content), encoding='utf-8')
    # print('\n'.join(qj_content))
        # print(len(ls))