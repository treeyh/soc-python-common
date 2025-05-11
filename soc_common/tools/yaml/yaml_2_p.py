# -*- encoding: utf-8 -*-

'''
@file           :yaml_2_p.py
@description    :
@time           :2025-05-11 09:38:10
@author         :Tree
@version        :1.0
'''


content = '''数学	ss.subject.math
语文	ss.subject.chinese
英语	ss.subject.english
物理	ss.subject.physics
化学	ss.subject.chemistry
生物	ss.subject.biology
政治	ss.subject.politics
地理	ss.subject.geography
历史	ss.subject.history'''


if __name__ == '__main__':
    lines = content.split('\n')
    for l in lines:
        ls = l.strip().split('\t')
        # print(ls)
        if len(ls) != 2:
            continue
        print('%s=%s' % (ls[1], ls[0]))