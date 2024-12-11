# -*- encoding: utf-8 -*-

'''
@file           :compare_list.py
@description    :
@time           :2024-11-27 14:52:04
@author         :Tree
@version        :1.0
'''

list1 = '''i-uf6agx'''

list2 = '''i-uf6645tooe'''

def compare_list():
  global list1, list2

  ls1 = list1.split('\n')
  ls2 = list2.split('\n')
  print(ls1)
  print(ls2)

  print('list1 不在 list2 的列表')
  for l in ls1:
    if l not in ls2:
      print(l)

  print('list2 不在 list1 的列表')
  for l in ls2:
    if l not in ls1:
      print(l)


_list = '''i-uf6iqojec11nth	2025-01-17T16:00Z'''


def get_date():
  global _list
  lists = _list.split('\n')
  lm = {}
  for l in lists:
    ls = l.split('	')
    lm[ls[0]] = ls[1]
  
  es = '''i-uf66'''

  ess = es.split('\n')
  print(ess)
  for e in ess:
    print(lm[e])


if __name__ == '__main__':
  # compare_list()
  get_date()
