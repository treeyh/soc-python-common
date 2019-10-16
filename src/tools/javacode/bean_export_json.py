
import os
import sys
import re
import json


path = os.path.split(os.path.realpath(__file__))[0]
sys.path.append(path + os.sep + '..' + os.sep + '..')

from utils import str_utils, file_utils



params = '''
private String id;

    private String callTaskId;

    private String providerFileUrl;

    private String callFileHost;

    private String callFilePath;

    private String provider;

    private String providerTaskId;

    private String providerCallSheetId;

    private Date callerRingTime;

    private Date calledRingTime;

    private Date beginTime;

    private Date endTime;

    private Date queueTime;

    private String queue;

    private String province;

    private String district;

    private Integer duration;

    private String ivrKey;

    private String status;

    private Byte downloadStatus;

    private Byte downloadCount;

    private Date createTime;

    private Date updateTime;
'''



def run():
    global params
    lines = params.split(os.linesep)
    paramsMap = {}

    for line in lines:
        l = line.strip()
        if '' == l:
            continue
        ls = l.split()
        if len(ls) == 2:
            ptype = ls[0].lower()
            pname = ls[1][0:str(ls[1]).index(';')]
        elif len(ls) == 3:
            ptype = ls[1].lower()
            pname = ls[2][0:str(ls[2]).index(';')]
        else:
            continue

        if 'int' == ptype or 'integer' == ptype or 'long' == ptype or 'byte' == ptype:
            paramsMap[pname] = 0
        elif 'string' == ptype:
            paramsMap[pname] = ''
        elif 'date' == ptype:
            paramsMap[pname] = '1970-01-01 00:00:00'
        else:
            paramsMap[pname] = {}
    print(json.dumps(paramsMap))




if __name__ == '__main__':
    run()