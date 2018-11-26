#-*- encoding: utf-8 -*-

import os
import sys
import re


path = os.path.split(os.path.realpath(__file__))[0]
sys.path.append(path + os.sep + '..' + os.sep + '..')

from helper import str_helper


java_domain = '''
@NotNull(message = "车场编号未填")
    private Integer parkId; // 车场编号
    @NotBlank(message = "用户编号未填")
    private String memberId; // 用户编号
'''

def run():
    global java_domain

    params = java_domain.split(os.linesep)


    ptype = []
    for p in params:
        if '@' in p:
            ptype.append(p.strip())
        if ';' not in p:
            continue
        l = p.strip()
        pl = l.split(';')
        param = pl[0].replace('\t', ' ')
        ps = param.split()
        if 3 != len(ps):
            continue
        ps[0] = '@RequestParam("'+ps[2]+'")'
        print ' '.join(ptype) + ' ' +' '.join(ps) + ','
        ptype = []



    pass


if __name__ == '__main__':
    run()