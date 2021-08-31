# -*- encoding: utf-8 -*-


import os
import sys

import json
from soc_common.utils import file_utils


_config_info = '''
id	namezh	nameen	typezh	typeen	code	basicsFlag	transitValue
21	尧米	yottameter	公制	metric	Ym	2	1000000000000000000000000
20	泽米	zettameter	公制	metric	Zm	2	1000000000000000000000
19	艾米	exameter	公制	metric	Em	2	1000000000000000000
18	拍米	petameter	公制	metric	Pm	2	1000000000000000
17	太米	terameter	公制	metric	Tm	2	1000000000000
16	吉米	gigameter	公制	metric	Gm	2	1000000000
15	兆米	megameter	公制	metric	Mm	2	1000000
14	千米/公里	kilometer	公制	metric	km	1	1000
1	米	meter	公制	metric	m	1	1
2	分米	decimetre	公制	metric	dm	2	0.1
3	厘米	centimeter	公制	metric	cm	1	0.01
4	毫米	millimeter	公制	metric	mm	1	0.001
5	丝米	decimillimetre	公制	metric	dmm	2	0.0001
6	忽米	centimillimetre	公制	metric	cmm	2	0.0001
7	微米	micrometer	公制	metric	μm	1	0.000001
8	纳米	millimeter	公制	metric	nm	1	0.000000001
9	皮米	picometer	公制	metric	pm	2	0.000000000001
10	飞米	femtometer	公制	metric	fm	2	0.000000000000001
11	阿米	attometer	公制	metric	am	2	0.000000000000000001
12	仄米	zeptometer	公制	metric	zm	2	0.000000000000000000001
13	幺米	yoctometer	公制	metric	ym	2	0.000000000000000000000001
22	里/华里	里/华里	市制	chinese units	huali	1	500
23	丈	丈	市制	chinese units	zhang	1	3.333333333333333333333333
24	尺	尺	市制	chinese units	chi	1	0.333333333333333333333333
25	寸	寸	市制	chinese units	cun	2	0.033333333333333333333333
26	分	分	市制	chinese units	fen	2	0.003333333333333333333333
27	厘	厘	市制	chinese units	li	2	0.000333333333333333333333
28	毫	毫	市制	chinese units	hao	2	0.000033333333333333333333
29	英里	mile	英制	british units		1	1609.344
30	化朗	furlong	英制	british units		2	201.168
31	链	chain	英制	british units		2	20.1168
32	杆	rod	英制	british units		2	5.0292
33	码	yard	英制	british units	yd	2	0.9144
34	英尺	foot	英制	british units		1	0.3048
35	英寸	inch	英制	british units	in	2	0.0254
36	海里	nautical mile	航海	navigation units	n mile	1	1852
37	千秒差距	kiloparsec	天文学	astronomical units	kpc	2	30856775814671915808
38	秒差距	parsec	天文学	astronomical units	pc	2	30856775814671915.808
39	毫秒差距	milliparsec	天文学	astronomical units		2	30856775814671.915808
40	光年	light-year	天文学	astronomical units	ly	1	9460730472580800
41	天文单位	astronomical-unit	天文学	astronomical units	A.U.	2	149597870700
'''


def build_config():
  global _config_info

  lines = _config_info.split('\n')

  configList = []
  titleList = []

  for line in lines:
    l = line.strip()
    if l == '':
      continue
    if len(titleList) <= 0:
      ss = l.split('\t')
      for s in ss:
        titleList.append(s)
      continue
    ss = l.split('\t')
    mmap = {}
    index = 0
    for s in ss:
      title = titleList[index]
      v = s
      if title in ('basicsFlag'):
        v = int(s)
      mmap[titleList[index]] = v
      index += 1
    configList.append(mmap)
  file_utils.write_file('d:\\l.json', json.dumps(configList, ensure_ascii=False))
  return configList
