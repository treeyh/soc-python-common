# -*- encoding: utf-8 -*-

import os

from soc_common.utils import file_utils


exr = '''
阿富汗尼 Afghani	AFA
阿尔及利亚第纳尔 Algerian Dinar	DZD
安第列斯群岛盾 Antilles Guilder	ANG
奥地利先令 Austria Schilling	ATS
阿鲁巴岛弗罗林 Aruba Florin	AWF
波斯尼亚和黑塞哥维那（波黑）Bosnia and Herzegovina Convertible Mark	BAK
保加利亚列弗 Bulgaria Lev	BGL
文莱元 Brunei Darussalam Dollar	BND
不丹卢比 Bhutan Rupee	BTR
加拿大元 Canada Dollar	CAD
瑞士法郎 Switzerland Franc	CHF
哥伦比亚比索 Colombia Peso	COP
古巴比索 Cuba Peso	CUP
英镑 Britain Pound	GBP
多美尼加比索 Dominican Republic Peso	DOP
缅甸元 Burma Kyat	MMK
厄立特里亚 Eritrea Nakfa	ERN
埃塞俄比亚 Ethiopia Birr	ETB
芬兰 Finland Markka	FIM
加纳塞第 Ghana Cedi	GHC
几内亚法郎 Guinea Franc	GNF
圭亚那 Guyana Dollar	GYD
克罗地亚 Croatia Kuna	HRK
印尼卢比 Indonesia Rupiah	IDR
印度卢比 India Rupee	INR
冰岛克郎 Iceland Krona	ISK
牙买加元 Jamaica Dollar	JMD
肯尼亚先令 Kenya Shilling	KES
赤道几内亚 Equatorial Guinea CFA Franc	XAF
科威特第纳尔 Kuwait Dinar	KWD
黎巴嫩镑 Lebanon Pound	LBP
莱索托 Lesotho Loti	LSL
拉托维亚 Latvia Lat	LVL
摩尔多瓦 Moldova Leu	MDL
加蓬 Gabon CFA Franc	XAF
中国澳门 Macau Pataca	MOP
毛里求斯卢比 Mauritius Rupee	MUR
墨西哥比索 Mexico Peso	MXN
莫桑比克 Mozambique Metical	MZM
尼加拉瓜 Nicaragua Cordoba Oro	NIO
几内亚 Guinea Franc	GNF
阿曼 Oman Sul Rial	OMR
菲律宾比索 Philippines Peso	PHP
巴拉圭 Paraguay Guarani	PYG
俄罗斯卢布 Russia Ruble	RUB
苏丹 Sudan Dinar	SDD
斯洛文尼亚 Slovenia Tolar	SIT
约旦 Jordan Dinar	JOD
斯威士兰 Swaziland Lilangeni	SZL
土库曼斯坦 Turkmenistan Manat	TMM
汤加 Tonga Pa'anga	TOP
坦桑尼亚 Tanzania Shilling	TZS
乌拉圭 Uruguay Peso	UYU
委内瑞拉 Venezuela Bolivar	VEB
也门 Yemen Rial	YER
赞比亚 Zambia Kwacha	ZMK
阿联酋迪拉姆 Dirham	AED
安道尔法郎 Andorra French Franc	FRF
安哥拉 Angola New Kwanza	AON
澳大利亚元 Australia Dollar	AUD
安提瓜和巴布达岛东加勒比海元 Antigua and Barbuda East Caribbean Dollar	XCD
巴巴多斯元 Barbados Dollar	BBD
布隆迪法郎 Burundi Franc	BIF
玻利维亚 Boliviano	BOB
博茨瓦纳 Botswana Pula	BWP
贝宁法郎 Benin CFA Franc	XAF
智利比索 Chile Peso	CLP
哥斯达黎加 Costa Rica Colon	CRC
佛得角 Cape Verde Escudo	CVE
德国马克 Germany Deutsche Mark	DEM
布基纳法索 Burkina Faso CFA Franc	XAF
爱沙尼亚 Estonia Kroon	EEK
西班牙彼萨塔 Spain Peseta	ESP
喀麦隆 Cameroon CFA Franc	XAF
斐济元 Fiji Dollar	FJD
乍得 Chad CFA Franc	XAF
直布罗陀 Gibraltar Pound	GIP
希腊 Greece Drachma	GRD
港币 Hong Kong Dollar	HKD
海地 Haiti Gourde	HTG
爱尔兰 Eire Punt	IEP
伊拉克第纳尔 Iraq Dinar	IQD
荷兰盾 Dutch (The Netherlands) Guilder	NLG
约旦第纳尔 Jordan Dinar	JOD
萨尔瓦多 El Salvador Colon	SVC
韩国 Korea (South) Won	KRW
哈萨克斯坦 Kazakstan Tenge	KZT
斯里兰卡卢比 Sri Lanka Rupee	LKR
立陶宛 Lithuania Lita	LTL
利比亚第纳尔 Libya Dinar	LYD
马达加斯加 Malagasy Franc	MGF
冈比亚 Gambia Dalasi	GMD
毛里塔尼亚 Mauritania Ouguiya	MRO
马尔代夫 Maldives (Maldive Islands) Rufiyaa	MVR
格陵兰 Greenland Danish Krone	DKK
纳米比亚 Namibia Dollar	NAD
危地马拉 Guatemala Quetzal	GTQ
尼泊尔卢比 Nepalese Rupee	NPR
巴拿马 Panama Balboa	PAB
巴基斯坦卢比 Pakistan Rupee	PKR
卡塔尔 Qatar Rial	QAR
卢旺达法郎 Rwanda Franc	RWF
瑞典克郎 Sweden Krona	SEK
斯洛伐克 Slovakia Koruna	SKK
索马里 Somalia Shilling	SOS
泰铢 Thailand Baht（泰国）	THB
突尼斯 Tunisia Dinar	TND
土耳其 Turkey Lira	TRL
乌克兰 Ukraine Hryvnia	UAH
美元 US Dollar	USD
越南 Viet Nam Dong	VND
南斯拉夫 Yugoslavia New Dinar	YUN
津巴布韦 Zimbabwe Dollar	ZWD
阿尔巴尼亚 Albania Lek	ALL
亚美尼亚 Armenia Dram	AMD
阿根廷比索 Argentina Peso	ARP
安圭拉东加勒比海元 Anguilla East Caribbean Dollar	XCD
阿塞拜疆 Azerbaijan Manat	AZM
比利时法郎 Belgium Franc	BEF
巴哈马群岛元 Bahamas Dollar	BSD
巴西 Brazilian Real	BRL
洪都拉斯元 Belize Dollar	BZD
刚果法郎 Congolese Franc	CDF
中国人民币 China Yuan Renminbi	CNY
捷克克郎 Czech Republic Koruna	CZK
塞普路斯镑 Cyprus Pound	CYP
丹麦克郎 Denmark Krone	DKK
厄瓜多尔 Ecuador Sucre	ECS
埃及镑 Egypt Pound	EGP
柬埔寨 Cambodia Riel	KHR
欧元 Euro	EUR
法国法郎 France Franc	FRF
乔治亚 Georgia Lari	GEL
冈比亚 Gambia Dalasi	GMD
危地马拉 Guatemala Quetzal	GTQ
新西兰元 New Zealand Dollar	NZD
匈牙利福林 Hungary Forint	HUF
以色列 Israel Shekel	ILS
伊朗里亚尔 Iran Rial	IRR
意大利里拉 Italy Lira	ITL
日圆 Japan Yen	JPY
朝鲜 Korea (North) Won	KPW
埃塞俄比亚 Ethiopian Birr	ETB
老挝 Laos Kip	LAK
利比里亚元 Liberia Dollar	LRD
卢森堡法郎 Luxembourg Franc	LUF
摩洛哥迪拉姆 Morocco Dirham	MAD
马其顿第纳尔 Macedonia Denar	MKD
蒙古 Mongolia Tugrik	MNT
马耳他 Malta Lira	MTL
希腊德拉玛 Greece Drachma	GRD
马来西亚 Malaysia Ringgit	MYR
尼日利亚奈拉 Nigeria Naira	NGN
挪威克郎 Norway Krone	NOK
新西兰 New Zealand Dollar	NZD
秘鲁 Peru Nuevo Sol	PEN
波兰 Poland Zloty	PLN
罗马尼亚 Romania Leu	ROL
沙特阿拉伯 Saudi Arabia Riyal	SAR
新加坡 Singapore Dollar	SGD
塞拉里昂 Sierra Leone	SLL
叙利亚 Syria Pound	SYP
塔吉克斯坦 Tajikistan Ruble	TJR
拉托维亚 Latvia Lat	LVL
中国台湾 Taiwan Dollar	TWD
乌干达 Uganda Shilling	UGX
乌兹别克斯坦 Uzbekistan Som	UZS
瓦努阿图 Vanuatu Vatu	VUV
南非 South Africa Rand	ZAR
尼加拉瓜 Nicaragua Cordoba Oro	NIO

'''

jj = {
    "USD": 1,
    "AED": 3.67,
    "AFN": 82.69,
    "ALL": 102.93,
    "AMD": 493.18,
    "ANG": 1.79,
    "AOA": 633.65,
    "ARS": 97.89,
    "AUD": 1.36,
    "AWG": 1.79,
    "AZN": 1.7,
    "BAM": 1.65,
    "BBD": 2,
    "BDT": 85.05,
    "BGN": 1.65,
    "BHD": 0.376,
    "BIF": 1979.82,
    "BMD": 1,
    "BND": 1.34,
    "BOB": 6.89,
    "BRL": 5.21,
    "BSD": 1,
    "BTN": 73.62,
    "BWP": 11.05,
    "BYN": 2.52,
    "BZD": 2,
    "CAD": 1.27,
    "CDF": 1983.7,
    "CHF": 0.921,
    "CLP": 779.74,
    "CNY": 6.46,
    "COP": 3825.05,
    "CRC": 621.51,
    "CUC": 1,
    "CUP": 25.75,
    "CVE": 93.11,
    "CZK": 21.52,
    "DJF": 177.72,
    "DKK": 6.3,
    "DOP": 56.7,
    "DZD": 135.98,
    "EGP": 15.71,
    "ERN": 15,
    "ETB": 46.07,
    "EUR": 0.844,
    "FJD": 2.07,
    "FKP": 0.726,
    "FOK": 6.3,
    "GBP": 0.726,
    "GEL": 3.11,
    "GGP": 0.726,
    "GHS": 6.03,
    "GIP": 0.726,
    "GMD": 52.04,
    "GNF": 9781.17,
    "GTQ": 7.72,
    "GYD": 208.87,
    "HKD": 7.77,
    "HNL": 23.92,
    "HRK": 6.36,
    "HTG": 98.44,
    "HUF": 296.53,
    "IDR": 14391.88,
    "ILS": 3.22,
    "IMP": 0.726,
    "INR": 73.62,
    "IQD": 1457.65,
    "IRR": 41833.85,
    "ISK": 127.33,
    "JMD": 150.75,
    "JOD": 0.709,
    "JPY": 110.22,
    "KES": 109.99,
    "KGS": 84.72,
    "KHR": 4075.49,
    "KID": 1.36,
    "KMF": 415.42,
    "KRW": 1165.68,
    "KWD": 0.3,
    "KYD": 0.833,
    "KZT": 426.01,
    "LAK": 9565.71,
    "LBP": 1507.5,
    "LKR": 199.68,
    "LRD": 171.72,
    "LSL": 14.23,
    "LYD": 4.5,
    "MAD": 8.92,
    "MDL": 17.57,
    "MGA": 3917.16,
    "MKD": 51.88,
    "MMK": 1644.68,
    "MNT": 2840.4,
    "MOP": 8.01,
    "MRU": 36.23,
    "MUR": 42.39,
    "MVR": 15.42,
    "MWK": 811.5,
    "MXN": 19.93,
    "MYR": 4.15,
    "MZN": 63.97,
    "NAD": 14.23,
    "NGN": 422.42,
    "NIO": 35.08,
    "NOK": 8.7,
    "NPR": 117.79,
    "NZD": 1.41,
    "OMR": 0.384,
    "PAB": 1,
    "PEN": 4.09,
    "PGK": 3.52,
    "PHP": 50.15,
    "PKR": 167.5,
    "PLN": 3.82,
    "PYG": 6961.17,
    "QAR": 3.64,
    "RON": 4.18,
    "RSD": 99.38,
    "RUB": 73.3,
    "RWF": 1008.28,
    "SAR": 3.75,
    "SBD": 7.95,
    "SCR": 13.7,
    "SDG": 443.56,
    "SEK": 8.61,
    "SGD": 1.34,
    "SHP": 0.726,
    "SLL": 10508.7,
    "SOS": 577.89,
    "SRD": 21.3,
    "SSP": 177.63,
    "STN": 20.69,
    "SYP": 1626.88,
    "SZL": 14.23,
    "THB": 32.77,
    "TJS": 11.31,
    "TMT": 3.5,
    "TND": 2.78,
    "TOP": 2.26,
    "TRY": 8.44,
    "TTD": 6.78,
    "TVD": 1.36,
    "TWD": 27.68,
    "TZS": 2315.54,
    "UAH": 26.7,
    "UGX": 3527.07,
    "UYU": 42.51,
    "UZS": 10709.55,
    "VES": 4058147.01,
    "VND": 22802.78,
    "VUV": 110.58,
    "WST": 2.54,
    "XAF": 553.89,
    "XCD": 2.7,
    "XDR": 0.702,
    "XOF": 553.89,
    "XPF": 100.76,
    "YER": 250.33,
    "ZAR": 14.23,
    "ZMW": 16.15
}


def run():
  global jj, exr

  # print(exr)

  exrs = exr.split('\n')
  fc = ''
  for k in jj.keys():
    content = k
    for ex in exrs:
      exs = ex.split('\t')
      if len(exs) != 2:
        continue
      if k != exs[1]:
        continue
      content += '\t' + '\t'.join(exs[0].split(' ', 1))
    fc += content + '\n'

  file_utils.write_file('d:\\a.txt', fc)
