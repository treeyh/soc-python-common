#-*- encoding: utf-8 -*-

import os
import sys
import re


path = os.path.split(os.path.realpath(__file__))[0]
sys.path.append(path + os.sep + '..' + os.sep + '..')

from utils import str_utils, file_utils





def format_level(level):
    s = ''
    for i in range(0, level):
        s += '    '
    return s


def check_date(value):
    if len(value) != 19:
        return False
    p = re.compile('^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}')
    v = p.match(value).group()
    if v == value:
        return True
    return False

def merged_dic(ls):
    d = {}
    for l in ls:
        if type(l) != dict:
            continue
        d = dict(d, **l)
    return d



def format_list_domain(domain, key, domainstr, level):
    if len(domain) <= 0:
        return

    t = type(domain[0])
    if t == int:
        domainstr += format_level(level) + 'private List<Integer> ' + key + ';'+ os.linesep
    elif t == bool:
        domainstr += format_level(level) + 'private List<Boolean> ' + key + ';'+ os.linesep
    elif t == float:
        domainstr += format_level(level) + 'private List<Double> ' + key + ';'+ os.linesep
    elif t == str:
        v1 = domain[0]
        if check_date(v1):
            domainstr += format_level(level) + 'private List<Date> ' + key + ';'+ os.linesep
        else:
            domainstr += format_level(level) + 'private List<String> ' + key + ';'+ os.linesep
    elif t == dict:
        d = merged_dic(domain)
        domainstr += format_level(level) + 'private List<'+key+'> ' + key + ';'+ os.linesep
        domainstr = format_domain(d, key, domainstr, level + 1)
    elif t == list:
        domainstr += format_level(level) + 'private List<List<'+key+'>> ' + key + ';'+ os.linesep
        domainstr = format_list_domain(domain[0], key, domainstr, level+1)
    return domainstr


def format_domain(domain, key, domainstr, level):    
    domainstr += format_level(level - 1) + 'public class ' + key + '{'+ os.linesep

    for k, v in domain.items():
        t = type(v)
        if t == dict:
            domainstr += format_level(level) + 'private '+k+' ' + k + ';'+ os.linesep
            domainstr = format_domain(v, k, domainstr, level + 1)
        elif t == list:
            if len(v) <= 0:
                continue
            domainstr = format_list_domain(v, k, domainstr, level)
        elif t == int:
            domainstr += format_level(level) + 'private Integer ' + k + ';'+ os.linesep
        elif t == bool:
            domainstr += format_level(level) + 'private Boolean ' + k + ';'+ os.linesep
        elif t == float:
            domainstr += format_level(level) + 'private Double ' + k + ';'+ os.linesep
        elif t == str:
            v1 = v
            if check_date(v1):
                domainstr += format_level(level) + 'private Date ' + k + ';'+ os.linesep
            else:
                domainstr += format_level(level) + 'private String ' + k + ';'+ os.linesep
        else:
            domainstr += format_level(level) + '  key  value:' + k + ';'+ os.linesep

    domainstr += format_level(level - 1) + '}'+ os.linesep
    return domainstr


j = '''
{
    "ret": 1,
    "start": -1,
    "end": -1,
    "country": "美国",
    "province": "",
    "city": "",
    "district": "",
    "isp": "",
    "type": "",
    "desc": ""
}
'''


if __name__ == '__main__':
    obj = str_utils.json_decode(j)
    string = ''

    string = format_domain(obj , 'domain', string, 1)
    print(string)

