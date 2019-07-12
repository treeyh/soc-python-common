#-*- encoding: utf-8 -*-

import os
import sys





_codes = ''' unicorn / unicorn-bs
unicorn / member-courtesy
comment / info-filter
comment / subscription-platform-timer
comment / comment-platform
comment / comment-platform-timer
member / ucenter-timer-parent
member / ucenter-open-parent
member / right-server-parent
member / growth-server-parent
member / lua-platucenter-parent
member / ucenter-platform-timer
member / database-comparison
member / ucenter-auth-parent
member / web-frame
member / right-timer-parent
member / lua-ucenter-parent
member / ucenter-common
member / ucenter-admin-parent
member / sso-parent
member / growth-timer-parent
member / ucenter-server-parent
membership / member-common-parent
membership / cos-parent
membership / whalecoin-parent
membership / pucenter-parent '''



def clone_code():    
    global _codes
    target_path = '/Users/tree/work/06_wd/07_src/09_member'
    for line in _codes.split(os.linesep):
        
        ls = line.split('/')
        if 2 != len(ls):
            continue

        if os.path.exists(os.path.join(target_path, ls[1].strip())):
            continue

        cmd = '''
        cd %s
        git clone ssh://git@gitlab.ffan.biz:8022/%s/%s.git
        ''' % (target_path, ls[0].strip(), ls[1].strip())
        result = os.popen(cmd).readlines()
        print(result





if __name__ == '__main__':
    clone_code()