# -*- encoding: utf-8 -*-

from soc_common.tools.code.code_generate.golang import generate_by_java
from soc_common.tools.toolkit.config import convert_unit


cu = {
    "version": 1631881752,
    "default": "exchangeRate",
    "items": [
        {
            "namezh": "汇率换算",
            "nameen": "Exchange rate conversion",
            "code": "exchangeRate",
            "source": "CNY",
            "target": "USD",
            "baseline": "None",
            "ratioFlag": 1,
            "items": [
                {
                    "code": "USD",
                    "namezh": "美元",
                    "nameen": "US Dollar",
                    "typezh": "A",
                    "typeen": "A",
                    "unit": "USD",
                    "base": 1,
                    "scale": 0
                },
                {
                    "code": "AED",
                    "namezh": "阿联酋迪拉姆",
                    "nameen": "Dirham",
                    "typezh": "A",
                    "typeen": "A",
                    "unit": "AED",
                    "base": 1,
                    "scale": 0
                },
                {
                    "code": "AFN",
                    "namezh": "阿富汗尼",
                    "nameen": "Afghani",
                    "typezh": "A",
                    "typeen": "A",
                    "unit": "AFN",
                    "base": 2,
                    "scale": 0
                },
                {
                    "code": "ALL",
                    "namezh": "阿尔巴尼亚",
                    "nameen": "Albania Lek",
                    "typezh": "A",
                    "typeen": "A",
                    "unit": "ALL",
                    "base": 2,
                    "scale": "0"
                },
                {
                    "code": "AMD",
                    "namezh": "亚美尼亚",
                    "nameen": "Armenia Dram",
                    "typezh": "A",
                    "typeen": "A",
                    "unit": "AMD",
                    "base": 2,
                    "scale": "0"
                },
                {
                    "code": "ANG",
                    "namezh": "安第列斯群岛盾",
                    "nameen": "Antilles Guilder",
                    "typezh": "A",
                    "typeen": "A",
                    "unit": "ANG",
                    "base": 2,
                    "scale": "0"
                },
                {
                    "code": "AOA",
                    "namezh": "安哥拉宽扎",
                    "nameen": "Angolan Kwanzas",
                    "typezh": "A",
                    "typeen": "A",
                    "unit": "AOA",
                    "base": 2,
                    "scale": "0"
                },
                {
                    "code": "ARS",
                    "namezh": "阿根廷比索",
                    "nameen": "Argentine Peso",
                    "typezh": "A",
                    "typeen": "A",
                    "unit": "ARS",
                    "base": 1,
                    "scale": "0"
                },
                {
                    "code": "AUD",
                    "namezh": "澳大利亚元",
                    "nameen": "Australia Dollar",
                    "typezh": "A",
                    "typeen": "A",
                    "unit": "AUD",
                    "base": 1,
                    "scale": "0"
                },
                {
                    "code": "AWG",
                    "namezh": "阿鲁巴盾",
                    "nameen": "Aruban or Dutch Guilders",
                    "typezh": "A",
                    "typeen": "A",
                    "unit": "AWG",
                    "base": 2,
                    "scale": "0"
                },
                {
                    "code": "AZN",
                    "namezh": "阿塞拜疆马纳特",
                    "nameen": "Azərbaycan manat",
                    "typezh": "A",
                    "typeen": "A",
                    "unit": "AZN",
                    "base": 2,
                    "scale": "0"
                },
                {
                    "code": "BAM",
                    "namezh": "波黑马克",
                    "nameen": "convertible mark",
                    "typezh": "A",
                    "typeen": "A",
                    "unit": "BAM",
                    "base": 2,
                    "scale": "0"
                },
                {
                    "code": "BBD",
                    "namezh": "巴巴多斯元",
                    "nameen": "Barbados Dollar",
                    "typezh": "A",
                    "typeen": "A",
                    "unit": "BBD",
                    "base": 2,
                    "scale": "0"
                },
                {
                    "code": "BDT",
                    "namezh": "孟加拉塔卡",
                    "nameen": "Bangladeshi Taka",
                    "typezh": "A",
                    "typeen": "A",
                    "unit": "BDT",
                    "base": 2,
                    "scale": "0"
                },
                {
                    "code": "BGN",
                    "namezh": "保加利亚列弗",
                    "nameen": "Bulgarian lev",
                    "typezh": "A",
                    "typeen": "A",
                    "unit": "BGN",
                    "base": 1,
                    "scale": "0"
                },
                {
                    "code": "BHD",
                    "namezh": "巴林第纳尔",
                    "nameen": "Bahraini Dinar",
                    "typezh": "A",
                    "typeen": "A",
                    "unit": "BHD",
                    "base": 2,
                    "scale": "0"
                },
                {
                    "code": "BIF",
                    "namezh": "布隆迪法郎",
                    "nameen": "Burundi Franc",
                    "typezh": "A",
                    "typeen": "A",
                    "unit": "BIF",
                    "base": 2,
                    "scale": "0"
                },
                {
                    "code": "BMD",
                    "namezh": "百慕大群岛元",
                    "nameen": "Bermudian Dollars",
                    "typezh": "A",
                    "typeen": "A",
                    "unit": "BMD",
                    "base": 2,
                    "scale": "0"
                },
                {
                    "code": "BND",
                    "namezh": "文莱元",
                    "nameen": "Brunei Darussalam Dollar",
                    "typezh": "A",
                    "typeen": "A",
                    "unit": "BND",
                    "base": 2,
                    "scale": "0"
                },
                {
                    "code": "BOB",
                    "namezh": "玻利维亚币",
                    "nameen": "Bolivian Bolivianos",
                    "typezh": "A",
                    "typeen": "A",
                    "unit": "BOB",
                    "base": 2,
                    "scale": "0"
                },
                {
                    "code": "BRL",
                    "namezh": "巴西雷亚尔",
                    "nameen": "Brazilian Real",
                    "typezh": "A",
                    "typeen": "A",
                    "unit": "BRL",
                    "base": 1,
                    "scale": "0"
                },
                {
                    "code": "BSD",
                    "namezh": "巴哈马群岛元",
                    "nameen": "Bahamas Dollar",
                    "typezh": "A",
                    "typeen": "A",
                    "unit": "BSD",
                    "base": 2,
                    "scale": "0"
                },
                {
                    "code": "BTN",
                    "namezh": "不丹努尔特鲁姆",
                    "nameen": "Bhutanese Ngultrums",
                    "typezh": "A",
                    "typeen": "A",
                    "unit": "BTN",
                    "base": 2,
                    "scale": "0"
                },
                {
                    "code": "BWP",
                    "namezh": "博茨瓦纳普拉",
                    "nameen": "Botswana Pule",
                    "typezh": "A",
                    "typeen": "A",
                    "unit": "BWP",
                    "base": 2,
                    "scale": "0"
                },
                {
                    "code": "BYN",
                    "namezh": "白俄罗斯卢布",
                    "nameen": "Belarusian Rubles",
                    "typezh": "A",
                    "typeen": "A",
                    "unit": "BYN",
                    "base": 1,
                    "scale": "0"
                },
                {
                    "code": "BZD",
                    "namezh": "洪都拉斯元",
                    "nameen": "Belize Dollar",
                    "typezh": "A",
                    "typeen": "A",
                    "unit": "BZD",
                    "base": 2,
                    "scale": "0"
                },
                {
                    "code": "CAD",
                    "namezh": "加拿大元",
                    "nameen": "Canada Dollar",
                    "typezh": "A",
                    "typeen": "A",
                    "unit": "CAD",
                    "base": 1,
                    "scale": "0"
                },
                {
                    "code": "CDF",
                    "namezh": "刚果法郎",
                    "nameen": "Congolese Franc",
                    "typezh": "A",
                    "typeen": "A",
                    "unit": "CDF",
                    "base": 2,
                    "scale": "0"
                },
                {
                    "code": "CHF",
                    "namezh": "瑞士法郎",
                    "nameen": "Switzerland Franc",
                    "typezh": "A",
                    "typeen": "A",
                    "unit": "CHF",
                    "base": 1,
                    "scale": "0"
                },
                {
                    "code": "CLP",
                    "namezh": "智利比索",
                    "nameen": "Chile Peso",
                    "typezh": "A",
                    "typeen": "A",
                    "unit": "CLP",
                    "base": 1,
                    "scale": "0"
                },
                {
                    "code": "CNY",
                    "namezh": "中国人民币",
                    "nameen": "China Yuan Renminbi",
                    "typezh": "A",
                    "typeen": "A",
                    "unit": "CNY",
                    "base": 1,
                    "scale": "0"
                },
                {
                    "code": "COP",
                    "namezh": "哥伦比亚比索",
                    "nameen": "Colombia Peso",
                    "typezh": "A",
                    "typeen": "A",
                    "unit": "COP",
                    "base": 2,
                    "scale": "0"
                },
                {
                    "code": "CRC",
                    "namezh": "哥斯达黎加",
                    "nameen": "Costa Rica Colon",
                    "typezh": "A",
                    "typeen": "A",
                    "unit": "CRC",
                    "base": 2,
                    "scale": "0"
                },
                {
                    "code": "CUC",
                    "namezh": "古巴可兑换比索",
                    "nameen": "Cuban Convertible Peso",
                    "typezh": "A",
                    "typeen": "A",
                    "unit": "CUC",
                    "base": 2,
                    "scale": "0"
                },
                {
                    "code": "CUP",
                    "namezh": "古巴比索",
                    "nameen": "Cuban Pesos",
                    "typezh": "A",
                    "typeen": "A",
                    "unit": "CUP",
                    "base": 1,
                    "scale": "0"
                },
                {
                    "code": "CVE",
                    "namezh": "佛得角埃斯库多",
                    "nameen": "Cape Verdean Escudos",
                    "typezh": "A",
                    "typeen": "A",
                    "unit": "CVE",
                    "base": 2,
                    "scale": "0"
                },
                {
                    "code": "CZK",
                    "namezh": "捷克克郎",
                    "nameen": "Czech Republic Koruna",
                    "typezh": "A",
                    "typeen": "A",
                    "unit": "CZK",
                    "base": 1,
                    "scale": "0"
                },
                {
                    "code": "DJF",
                    "namezh": "吉布提法郎",
                    "nameen": "Djiboutian Francs",
                    "typezh": "A",
                    "typeen": "A",
                    "unit": "DJF",
                    "base": 2,
                    "scale": "0"
                },
                {
                    "code": "DKK",
                    "namezh": "丹麦克郎",
                    "nameen": "Denmark Krone",
                    "typezh": "A",
                    "typeen": "A",
                    "unit": "DKK",
                    "base": 1,
                    "scale": "0"
                },
                {
                    "code": "DOP",
                    "namezh": "多美尼加比索",
                    "nameen": "Dominican Republic Peso",
                    "typezh": "A",
                    "typeen": "A",
                    "unit": "DOP",
                    "base": 2,
                    "scale": "0"
                },
                {
                    "code": "DZD",
                    "namezh": "阿尔及利亚第纳尔",
                    "nameen": "Algerian Dinar",
                    "typezh": "A",
                    "typeen": "A",
                    "unit": "DZD",
                    "base": 2,
                    "scale": "0"
                },
                {
                    "code": "EGP",
                    "namezh": "埃及镑",
                    "nameen": "Egypt Pound",
                    "typezh": "A",
                    "typeen": "A",
                    "unit": "EGP",
                    "base": 1,
                    "scale": "0"
                },
                {
                    "code": "ERN",
                    "namezh": "厄立特里亚纳克法",
                    "nameen": "Eritrean Nakfas",
                    "typezh": "A",
                    "typeen": "A",
                    "unit": "ERN",
                    "base": 2,
                    "scale": "0"
                },
                {
                    "code": "ETB",
                    "namezh": "埃塞俄比亚比尔",
                    "nameen": "Ethiopian Birrs",
                    "typezh": "A",
                    "typeen": "A",
                    "unit": "ETB",
                    "base": 2,
                    "scale": "0"
                },
                {
                    "code": "EUR",
                    "namezh": "欧元",
                    "nameen": "Euro",
                    "typezh": "A",
                    "typeen": "A",
                    "unit": "EUR",
                    "base": 1,
                    "scale": "0"
                },
                {
                    "code": "FJD",
                    "namezh": "斐济元",
                    "nameen": "Fiji Dollar",
                    "typezh": "A",
                    "typeen": "A",
                    "unit": "FJD",
                    "base": 2,
                    "scale": "0"
                },
                {
                    "code": "FKP",
                    "namezh": "福克兰群岛镑",
                    "nameen": "Falkland Island Pounds",
                    "typezh": "A",
                    "typeen": "A",
                    "unit": "FKP",
                    "base": 2,
                    "scale": "0"
                },
                {
                    "code": "GBP",
                    "namezh": "英镑",
                    "nameen": "Britain Pound",
                    "typezh": "A",
                    "typeen": "A",
                    "unit": "GBP",
                    "base": 1,
                    "scale": "0"
                },
                {
                    "code": "GEL",
                    "namezh": "格鲁吉亚拉里",
                    "nameen": "Georgian Lari",
                    "typezh": "A",
                    "typeen": "A",
                    "unit": "GEL",
                    "base": 2,
                    "scale": "0"
                },
                {
                    "code": "GGP",
                    "namezh": "根西岛镑",
                    "nameen": "Guernsey Pounds",
                    "typezh": "A",
                    "typeen": "A",
                    "unit": "GGP",
                    "base": 2,
                    "scale": "0"
                },
                {
                    "code": "GHS",
                    "namezh": "加纳塞地",
                    "nameen": "Ghanaian Cedis",
                    "typezh": "A",
                    "typeen": "A",
                    "unit": "GHS",
                    "base": 2,
                    "scale": "0"
                },
                {
                    "code": "GIP",
                    "namezh": "直布罗陀镑",
                    "nameen": "Gibraltar Pounds",
                    "typezh": "A",
                    "typeen": "A",
                    "unit": "GIP",
                    "base": 2,
                    "scale": "0"
                },
                {
                    "code": "GMD",
                    "namezh": "冈比亚达拉西",
                    "nameen": "Gambian Dalasis",
                    "typezh": "A",
                    "typeen": "A",
                    "unit": "GMD",
                    "base": 2,
                    "scale": "0"
                },
                {
                    "code": "GNF",
                    "namezh": "几内亚法郎",
                    "nameen": "Guinean Francs",
                    "typezh": "A",
                    "typeen": "A",
                    "unit": "GNF",
                    "base": 2,
                    "scale": "0"
                },
                {
                    "code": "GTQ",
                    "namezh": "危地马拉格查尔",
                    "nameen": "Guatemalan Quetzales",
                    "typezh": "A",
                    "typeen": "A",
                    "unit": "GTQ",
                    "base": 2,
                    "scale": "0"
                },
                {
                    "code": "GYD",
                    "namezh": "圭亚那",
                    "nameen": "Guyana Dollar",
                    "typezh": "A",
                    "typeen": "A",
                    "unit": "GYD",
                    "base": 2,
                    "scale": "0"
                },
                {
                    "code": "HKD",
                    "namezh": "港币",
                    "nameen": "Hong Kong Dollar",
                    "typezh": "A",
                    "typeen": "A",
                    "unit": "HKD",
                    "base": 1,
                    "scale": "0"
                },
                {
                    "code": "HNL",
                    "namezh": "洪都拉斯伦皮拉",
                    "nameen": "Honduran Lempiras",
                    "typezh": "A",
                    "typeen": "A",
                    "unit": "HNL",
                    "base": 2,
                    "scale": "0"
                },
                {
                    "code": "HRK",
                    "namezh": "克罗地亚库纳",
                    "nameen": "Croatian Kunas",
                    "typezh": "A",
                    "typeen": "A",
                    "unit": "HRK",
                    "base": 2,
                    "scale": "0"
                },
                {
                    "code": "HTG",
                    "namezh": "海地古德",
                    "nameen": "Haitian Gourdes",
                    "typezh": "A",
                    "typeen": "A",
                    "unit": "HTG",
                    "base": 2,
                    "scale": "0"
                },
                {
                    "code": "HUF",
                    "namezh": "匈牙利福林",
                    "nameen": "Hungary Forint",
                    "typezh": "A",
                    "typeen": "A",
                    "unit": "HUF",
                    "base": 2,
                    "scale": "0"
                },
                {
                    "code": "IDR",
                    "namezh": "印尼卢比",
                    "nameen": "Indonesia Rupiah",
                    "typezh": "A",
                    "typeen": "A",
                    "unit": "IDR",
                    "base": 2,
                    "scale": "0"
                },
                {
                    "code": "ILS",
                    "namezh": "以色列谢克尔",
                    "nameen": "Israeli New Shekels",
                    "typezh": "A",
                    "typeen": "A",
                    "unit": "ILS",
                    "base": 1,
                    "scale": "0"
                },
                {
                    "code": "IMP",
                    "namezh": "曼岛镑",
                    "nameen": "Isle of Man Pounds",
                    "typezh": "A",
                    "typeen": "A",
                    "unit": "IMP",
                    "base": 2,
                    "scale": "0"
                },
                {
                    "code": "INR",
                    "namezh": "印度卢比",
                    "nameen": "India Rupee",
                    "typezh": "A",
                    "typeen": "A",
                    "unit": "INR",
                    "base": 1,
                    "scale": "0"
                },
                {
                    "code": "IQD",
                    "namezh": "伊拉克第纳尔",
                    "nameen": "Iraq Dinar",
                    "typezh": "A",
                    "typeen": "A",
                    "unit": "IQD",
                    "base": 2,
                    "scale": "0"
                },
                {
                    "code": "IRR",
                    "namezh": "伊朗里亚尔",
                    "nameen": "Iranian Rials",
                    "typezh": "A",
                    "typeen": "A",
                    "unit": "IRR",
                    "base": 2,
                    "scale": "0"
                },
                {
                    "code": "ISK",
                    "namezh": "冰岛克郎",
                    "nameen": "Iceland Krona",
                    "typezh": "A",
                    "typeen": "A",
                    "unit": "ISK",
                    "base": 2,
                    "scale": "0"
                },
                {
                    "code": "JMD",
                    "namezh": "牙买加元",
                    "nameen": "Jamaica Dollars",
                    "typezh": "A",
                    "typeen": "A",
                    "unit": "JMD",
                    "base": 2,
                    "scale": "0"
                },
                {
                    "code": "JOD",
                    "namezh": "约旦第纳尔",
                    "nameen": "Jordanian Dinars",
                    "typezh": "A",
                    "typeen": "A",
                    "unit": "JOD",
                    "base": 2,
                    "scale": "0"
                },
                {
                    "code": "JPY",
                    "namezh": "日圆",
                    "nameen": "Japan Yen",
                    "typezh": "A",
                    "typeen": "A",
                    "unit": "JPY",
                    "base": 1,
                    "scale": "0"
                },
                {
                    "code": "KES",
                    "namezh": "肯尼亚先令",
                    "nameen": "Kenya Shilling",
                    "typezh": "A",
                    "typeen": "A",
                    "unit": "KES",
                    "base": 2,
                    "scale": "0"
                },
                {
                    "code": "KGS",
                    "namezh": "吉尔吉斯斯坦索姆",
                    "nameen": "Kyrgyzstani Soms",
                    "typezh": "A",
                    "typeen": "A",
                    "unit": "KGS",
                    "base": 2,
                    "scale": "0"
                },
                {
                    "code": "KHR",
                    "namezh": "柬埔寨瑞尔",
                    "nameen": "Cambodian Riels",
                    "typezh": "A",
                    "typeen": "A",
                    "unit": "KHR",
                    "base": 1,
                    "scale": "0"
                },
                {
                    "code": "KID",
                    "namezh": "基里巴斯货币",
                    "nameen": "Kiribati Currency",
                    "typezh": "A",
                    "typeen": "A",
                    "unit": "KID",
                    "base": 2,
                    "scale": "0"
                },
                {
                    "code": "KMF",
                    "namezh": "科摩罗法郎",
                    "nameen": "Comoros Franc",
                    "typezh": "A",
                    "typeen": "A",
                    "unit": "KMF",
                    "base": 2,
                    "scale": "0"
                },
                {
                    "code": "KRW",
                    "namezh": "韩元",
                    "nameen": "South Korean Won",
                    "typezh": "A",
                    "typeen": "A",
                    "unit": "KRW",
                    "base": 1,
                    "scale": "0"
                },
                {
                    "code": "KWD",
                    "namezh": "科威特第纳尔",
                    "nameen": "Kuwait Dinar",
                    "typezh": "A",
                    "typeen": "A",
                    "unit": "KWD",
                    "base": 2,
                    "scale": "0"
                },
                {
                    "code": "KYD",
                    "namezh": "开曼群岛元",
                    "nameen": "Cayman Islands Dollar",
                    "typezh": "A",
                    "typeen": "A",
                    "unit": "KYD",
                    "base": 2,
                    "scale": "0"
                },
                {
                    "code": "KZT",
                    "namezh": "哈萨克斯坦坚戈",
                    "nameen": "Kazakstan Tenge",
                    "typezh": "A",
                    "typeen": "A",
                    "unit": "KZT",
                    "base": 2,
                    "scale": "0"
                },
                {
                    "code": "LAK",
                    "namezh": "老挝基普",
                    "nameen": "Laos Kip",
                    "typezh": "A",
                    "typeen": "A",
                    "unit": "LAK",
                    "base": 2,
                    "scale": "0"
                },
                {
                    "code": "LBP",
                    "namezh": "黎巴嫩镑",
                    "nameen": "Lebanon Pound",
                    "typezh": "A",
                    "typeen": "A",
                    "unit": "LBP",
                    "base": 2,
                    "scale": "0"
                },
                {
                    "code": "LKR",
                    "namezh": "斯里兰卡卢比",
                    "nameen": "Sri Lanka Rupee",
                    "typezh": "A",
                    "typeen": "A",
                    "unit": "LKR",
                    "base": 2,
                    "scale": "0"
                },
                {
                    "code": "LRD",
                    "namezh": "利比里亚元",
                    "nameen": "Liberia Dollar",
                    "typezh": "A",
                    "typeen": "A",
                    "unit": "LRD",
                    "base": 2,
                    "scale": "0"
                },
                {
                    "code": "LSL",
                    "namezh": "莱索托",
                    "nameen": "Lesotho Loti",
                    "typezh": "A",
                    "typeen": "A",
                    "unit": "LSL",
                    "base": 2,
                    "scale": "0"
                },
                {
                    "code": "LYD",
                    "namezh": "利比亚第纳尔",
                    "nameen": "Libya Dinar",
                    "typezh": "A",
                    "typeen": "A",
                    "unit": "LYD",
                    "base": 2,
                    "scale": "0"
                },
                {
                    "code": "MAD",
                    "namezh": "摩洛哥迪拉姆",
                    "nameen": "Morocco Dirham",
                    "typezh": "A",
                    "typeen": "A",
                    "unit": "MAD",
                    "base": 2,
                    "scale": "0"
                },
                {
                    "code": "MDL",
                    "namezh": "摩尔多瓦",
                    "nameen": "Moldova Leu",
                    "typezh": "A",
                    "typeen": "A",
                    "unit": "MDL",
                    "base": 2,
                    "scale": "0"
                },
                {
                    "code": "MGA",
                    "namezh": "马达币",
                    "nameen": "Malagasy Ariary",
                    "typezh": "A",
                    "typeen": "A",
                    "unit": "MGA",
                    "base": 2,
                    "scale": "0"
                },
                {
                    "code": "MKD",
                    "namezh": "马其顿第纳尔",
                    "nameen": "Macedonia Denar",
                    "typezh": "A",
                    "typeen": "A",
                    "unit": "MKD",
                    "base": 2,
                    "scale": "0"
                },
                {
                    "code": "MMK",
                    "namezh": "缅甸元",
                    "nameen": "Burma Kyat",
                    "typezh": "A",
                    "typeen": "A",
                    "unit": "MMK",
                    "base": 2,
                    "scale": "0"
                },
                {
                    "code": "MNT",
                    "namezh": "蒙古图格里克",
                    "nameen": "Mongolian Tugriks",
                    "typezh": "A",
                    "typeen": "A",
                    "unit": "MNT",
                    "base": 1,
                    "scale": "0"
                },
                {
                    "code": "MOP",
                    "namezh": "澳门元",
                    "nameen": "Macau Patacas",
                    "typezh": "A",
                    "typeen": "A",
                    "unit": "MOP",
                    "base": 1,
                    "scale": "0"
                },
                {
                    "code": "MRU",
                    "namezh": "毛里塔尼亚乌吉亚",
                    "nameen": "Mauritanian Ouguiyas",
                    "typezh": "A",
                    "typeen": "A",
                    "unit": "MRU",
                    "base": 2,
                    "scale": "0"
                },
                {
                    "code": "MUR",
                    "namezh": "毛里求斯卢比",
                    "nameen": "Mauritius Rupee",
                    "typezh": "A",
                    "typeen": "A",
                    "unit": "MUR",
                    "base": 2,
                    "scale": "0"
                },
                {
                    "code": "MVR",
                    "namezh": "马尔代夫拉菲亚",
                    "nameen": "Maldivian Rufiyaa",
                    "typezh": "A",
                    "typeen": "A",
                    "unit": "MVR",
                    "base": 2,
                    "scale": "0"
                },
                {
                    "code": "MWK",
                    "namezh": "马拉维克瓦查",
                    "nameen": "Malawian Kwachas",
                    "typezh": "A",
                    "typeen": "A",
                    "unit": "MWK",
                    "base": 2,
                    "scale": "0"
                },
                {
                    "code": "MXN",
                    "namezh": "墨西哥比索",
                    "nameen": "Mexico Peso",
                    "typezh": "A",
                    "typeen": "A",
                    "unit": "MXN",
                    "base": 1,
                    "scale": "0"
                },
                {
                    "code": "MYR",
                    "namezh": "马来西亚林吉特",
                    "nameen": "Malaysia Ringgit",
                    "typezh": "A",
                    "typeen": "A",
                    "unit": "MYR",
                    "base": 1,
                    "scale": "0"
                },
                {
                    "code": "MZN",
                    "namezh": "莫桑比克梅蒂卡尔",
                    "nameen": "Mozambican Meticais",
                    "typezh": "A",
                    "typeen": "A",
                    "unit": "MZN",
                    "base": 2,
                    "scale": "0"
                },
                {
                    "code": "NAD",
                    "namezh": "纳米比亚元",
                    "nameen": "Namibia Dollars",
                    "typezh": "A",
                    "typeen": "A",
                    "unit": "NAD",
                    "base": 2,
                    "scale": "0"
                },
                {
                    "code": "NGN",
                    "namezh": "尼日利亚奈拉",
                    "nameen": "Nigeria Naira",
                    "typezh": "A",
                    "typeen": "A",
                    "unit": "NGN",
                    "base": 2,
                    "scale": "0"
                },
                {
                    "code": "NIO",
                    "namezh": "尼加拉瓜科多巴",
                    "nameen": "Nicaraguan Cordobas",
                    "typezh": "A",
                    "typeen": "A",
                    "unit": "NIO",
                    "base": 2,
                    "scale": "0"
                },
                {
                    "code": "NOK",
                    "namezh": "挪威克郎",
                    "nameen": "Norway Krone",
                    "typezh": "A",
                    "typeen": "A",
                    "unit": "NOK",
                    "base": 1,
                    "scale": "0"
                },
                {
                    "code": "NPR",
                    "namezh": "尼泊尔卢比",
                    "nameen": "Nepalese Rupee",
                    "typezh": "A",
                    "typeen": "A",
                    "unit": "NPR",
                    "base": 2,
                    "scale": "0"
                },
                {
                    "code": "NZD",
                    "namezh": "新西兰元",
                    "nameen": "New Zealand Dollar",
                    "typezh": "A",
                    "typeen": "A",
                    "unit": "NZD",
                    "base": 1,
                    "scale": "0"
                },
                {
                    "code": "OMR",
                    "namezh": "阿曼里亚尔",
                    "nameen": "Omani Rials",
                    "typezh": "A",
                    "typeen": "A",
                    "unit": "OMR",
                    "base": 2,
                    "scale": "0"
                },
                {
                    "code": "PAB",
                    "namezh": "巴拿马巴波亚",
                    "nameen": "Panamanian Balboa",
                    "typezh": "A",
                    "typeen": "A",
                    "unit": "PAB",
                    "base": 2,
                    "scale": "0"
                },
                {
                    "code": "PEN",
                    "namezh": "秘鲁索尔",
                    "nameen": "Peruvian Soles",
                    "typezh": "A",
                    "typeen": "A",
                    "unit": "PEN",
                    "base": 2,
                    "scale": "0"
                },
                {
                    "code": "PGK",
                    "namezh": "巴布亚新几内亚基那",
                    "nameen": "Papua New Guinean Kina",
                    "typezh": "A",
                    "typeen": "A",
                    "unit": "PGK",
                    "base": 2,
                    "scale": "0"
                },
                {
                    "code": "PHP",
                    "namezh": "菲律宾比索",
                    "nameen": "Philippine Pesos",
                    "typezh": "A",
                    "typeen": "A",
                    "unit": "PHP",
                    "base": 1,
                    "scale": "0"
                },
                {
                    "code": "PKR",
                    "namezh": "巴基斯坦卢比",
                    "nameen": "Pakistani Rupees",
                    "typezh": "A",
                    "typeen": "A",
                    "unit": "PKR",
                    "base": 1,
                    "scale": "0"
                },
                {
                    "code": "PLN",
                    "namezh": "波兰兹罗提",
                    "nameen": "Polish Zlotych",
                    "typezh": "A",
                    "typeen": "A",
                    "unit": "PLN",
                    "base": 2,
                    "scale": "0"
                },
                {
                    "code": "PYG",
                    "namezh": "巴拉圭瓜拉尼",
                    "nameen": "Paraguay Guarani",
                    "typezh": "A",
                    "typeen": "A",
                    "unit": "PYG",
                    "base": 2,
                    "scale": "0"
                },
                {
                    "code": "QAR",
                    "namezh": "卡塔尔里亚尔",
                    "nameen": "Qatari Rials",
                    "typezh": "A",
                    "typeen": "A",
                    "unit": "QAR",
                    "base": 2,
                    "scale": "0"
                },
                {
                    "code": "RON",
                    "namezh": "罗马尼亚新列伊",
                    "nameen": "Romanian Lei",
                    "typezh": "A",
                    "typeen": "A",
                    "unit": "RON",
                    "base": 1,
                    "scale": "0"
                },
                {
                    "code": "RSD",
                    "namezh": "塞尔维亚第纳尔",
                    "nameen": "Serbian Dinars",
                    "typezh": "A",
                    "typeen": "A",
                    "unit": "RSD",
                    "base": 2,
                    "scale": "0"
                },
                {
                    "code": "RUB",
                    "namezh": "俄罗斯卢布",
                    "nameen": "Russia Ruble",
                    "typezh": "A",
                    "typeen": "A",
                    "unit": "RUB",
                    "base": 1,
                    "scale": "0"
                },
                {
                    "code": "RWF",
                    "namezh": "卢旺达法郎",
                    "nameen": "Rwanda Franc",
                    "typezh": "A",
                    "typeen": "A",
                    "unit": "RWF",
                    "base": 2,
                    "scale": "0"
                },
                {
                    "code": "SAR",
                    "namezh": "沙特里亚尔",
                    "nameen": "Saudi Arabia Riyal",
                    "typezh": "A",
                    "typeen": "A",
                    "unit": "SAR",
                    "base": 1,
                    "scale": "0"
                },
                {
                    "code": "SBD",
                    "namezh": "所罗门群岛元",
                    "nameen": "Solomon Islander Dollars",
                    "typezh": "A",
                    "typeen": "A",
                    "unit": "SBD",
                    "base": 2,
                    "scale": "0"
                },
                {
                    "code": "SCR",
                    "namezh": "塞舌尔卢比",
                    "nameen": "Seychellois Rupees",
                    "typezh": "A",
                    "typeen": "A",
                    "unit": "SCR",
                    "base": 1,
                    "scale": "0"
                },
                {
                    "code": "SDG",
                    "namezh": "苏丹镑",
                    "nameen": "Sudanese Pounds",
                    "typezh": "A",
                    "typeen": "A",
                    "unit": "SDG",
                    "base": 2,
                    "scale": "0"
                },
                {
                    "code": "SEK",
                    "namezh": "瑞典克郎",
                    "nameen": "Sweden Krona",
                    "typezh": "A",
                    "typeen": "A",
                    "unit": "SEK",
                    "base": 1,
                    "scale": "0"
                },
                {
                    "code": "SGD",
                    "namezh": "新加坡元",
                    "nameen": "Singapore Dollars",
                    "typezh": "A",
                    "typeen": "A",
                    "unit": "SGD",
                    "base": 1,
                    "scale": "0"
                },
                {
                    "code": "SHP",
                    "namezh": "圣赫勒拿镑",
                    "nameen": "Saint Helenian Pounds",
                    "typezh": "A",
                    "typeen": "A",
                    "unit": "SHP",
                    "base": 2,
                    "scale": "0"
                },
                {
                    "code": "SLL",
                    "namezh": "塞拉利昂利昂",
                    "nameen": "Sierra Leonean Leones",
                    "typezh": "A",
                    "typeen": "A",
                    "unit": "SLL",
                    "base": 2,
                    "scale": "0"
                },
                {
                    "code": "SOS",
                    "namezh": "索马里先令",
                    "nameen": "Somali Shillings",
                    "typezh": "A",
                    "typeen": "A",
                    "unit": "SOS",
                    "base": 2,
                    "scale": "0"
                },
                {
                    "code": "SRD",
                    "namezh": "苏里南元",
                    "nameen": "Surinamese Dollars",
                    "typezh": "A",
                    "typeen": "A",
                    "unit": "SRD",
                    "base": 2,
                    "scale": "0"
                },
                {
                    "code": "SSP",
                    "namezh": "南苏丹镑",
                    "nameen": "South Sudanese pound",
                    "typezh": "A",
                    "typeen": "A",
                    "unit": "SSP",
                    "base": 2,
                    "scale": "0"
                },
                {
                    "code": "STN",
                    "namezh": "圣多美多布拉",
                    "nameen": "Sao Tomean Dobras",
                    "typezh": "A",
                    "typeen": "A",
                    "unit": "STN",
                    "base": 2,
                    "scale": "0"
                },
                {
                    "code": "SYP",
                    "namezh": "叙利亚镑",
                    "nameen": "Syrian Pounds",
                    "typezh": "A",
                    "typeen": "A",
                    "unit": "SYP",
                    "base": 2,
                    "scale": "0"
                },
                {
                    "code": "SZL",
                    "namezh": "斯威士兰里兰吉尼",
                    "nameen": "Swazi Emalangeni",
                    "typezh": "A",
                    "typeen": "A",
                    "unit": "SZL",
                    "base": 2,
                    "scale": "0"
                },
                {
                    "code": "THB",
                    "namezh": "泰铢",
                    "nameen": "Thailand Baht",
                    "typezh": "A",
                    "typeen": "A",
                    "unit": "THB",
                    "base": 1,
                    "scale": "0"
                },
                {
                    "code": "TJS",
                    "namezh": "塔吉克斯坦索莫尼",
                    "nameen": "Tajikistani Somoni",
                    "typezh": "A",
                    "typeen": "A",
                    "unit": "TJS",
                    "base": 2,
                    "scale": "0"
                },
                {
                    "code": "TMT",
                    "namezh": "土库曼斯坦马纳特",
                    "nameen": "Turkmenistani Manats",
                    "typezh": "A",
                    "typeen": "A",
                    "unit": "TMT",
                    "base": 2,
                    "scale": "0"
                },
                {
                    "code": "TND",
                    "namezh": "突尼斯第纳尔",
                    "nameen": "Tunisian Dinars",
                    "typezh": "A",
                    "typeen": "A",
                    "unit": "TND",
                    "base": 2,
                    "scale": "0"
                },
                {
                    "code": "TOP",
                    "namezh": "汤加潘加",
                    "nameen": "Tongan Pa'anga",
                    "typezh": "A",
                    "typeen": "A",
                    "unit": "TOP",
                    "base": 2,
                    "scale": "0"
                },
                {
                    "code": "TRY",
                    "namezh": "土耳其里拉",
                    "nameen": "Turkish Lire",
                    "typezh": "A",
                    "typeen": "A",
                    "unit": "TRY",
                    "base": 1,
                    "scale": "0"
                },
                {
                    "code": "TTD",
                    "namezh": "特立尼达元",
                    "nameen": "Trinidadian Dollars",
                    "typezh": "A",
                    "typeen": "A",
                    "unit": "TTD",
                    "base": 2,
                    "scale": "0"
                },
                {
                    "code": "TVD",
                    "namezh": "图瓦卢元",
                    "nameen": "Tuvaluan Dollars",
                    "typezh": "A",
                    "typeen": "A",
                    "unit": "TVD",
                    "base": 2,
                    "scale": "0"
                },
                {
                    "code": "TWD",
                    "namezh": "新台币",
                    "nameen": "Taiwan New Dollars",
                    "typezh": "A",
                    "typeen": "A",
                    "unit": "TWD",
                    "base": 1,
                    "scale": "0"
                },
                {
                    "code": "TZS",
                    "namezh": "坦桑尼亚先令",
                    "nameen": "Tanzanian Shillings",
                    "typezh": "A",
                    "typeen": "A",
                    "unit": "TZS",
                    "base": 2,
                    "scale": "0"
                },
                {
                    "code": "UAH",
                    "namezh": "乌克兰格里夫纳",
                    "nameen": "Ukrainian Hryvni",
                    "typezh": "A",
                    "typeen": "A",
                    "unit": "UAH",
                    "base": 2,
                    "scale": "0"
                },
                {
                    "code": "UGX",
                    "namezh": "乌干达先令",
                    "nameen": "Ugandan Shillings",
                    "typezh": "A",
                    "typeen": "A",
                    "unit": "UGX",
                    "base": 2,
                    "scale": "0"
                },
                {
                    "code": "UYU",
                    "namezh": "乌拉圭比索",
                    "nameen": "Uruguayan Pesos",
                    "typezh": "A",
                    "typeen": "A",
                    "unit": "UYU",
                    "base": 2,
                    "scale": "0"
                },
                {
                    "code": "UZS",
                    "namezh": "乌兹别克斯坦索姆",
                    "nameen": "Uzbekistani Sums",
                    "typezh": "A",
                    "typeen": "A",
                    "unit": "UZS",
                    "base": 2,
                    "scale": "0"
                },
                {
                    "code": "VES",
                    "namezh": "委内瑞拉玻利瓦尔",
                    "nameen": "Venezuelan Bolívares",
                    "typezh": "A",
                    "typeen": "A",
                    "unit": "VES",
                    "base": 2,
                    "scale": "0"
                },
                {
                    "code": "VND",
                    "namezh": "越南盾",
                    "nameen": "Vietnamese Dongs",
                    "typezh": "A",
                    "typeen": "A",
                    "unit": "VND",
                    "base": 1,
                    "scale": "0"
                },
                {
                    "code": "VUV",
                    "namezh": "瓦努阿图瓦图",
                    "nameen": "Ni-Vanuatu Vatu",
                    "typezh": "A",
                    "typeen": "A",
                    "unit": "VUV",
                    "base": 2,
                    "scale": "0"
                },
                {
                    "code": "WST",
                    "namezh": "萨摩亚塔拉",
                    "nameen": "Samoan Tala",
                    "typezh": "A",
                    "typeen": "A",
                    "unit": "WST",
                    "base": 2,
                    "scale": "0"
                },
                {
                    "code": "XAF",
                    "namezh": "中非法郎",
                    "nameen": "Central African CFA franc",
                    "typezh": "A",
                    "typeen": "A",
                    "unit": "XAF",
                    "base": 2,
                    "scale": "0"
                },
                {
                    "code": "XCD",
                    "namezh": "东加勒比元",
                    "nameen": "East Caribbean Dollars",
                    "typezh": "A",
                    "typeen": "A",
                    "unit": "XCD",
                    "base": 2,
                    "scale": "0"
                },
                {
                    "code": "XDR",
                    "namezh": "国际货币基金组织特别提款权",
                    "nameen": "IMF Special Drawing Rights",
                    "typezh": "A",
                    "typeen": "A",
                    "unit": "XDR",
                    "base": 2,
                    "scale": "0"
                },
                {
                    "code": "XOF",
                    "namezh": "CFA 法郎",
                    "nameen": "CFA Francs",
                    "typezh": "A",
                    "typeen": "A",
                    "unit": "XOF",
                    "base": 2,
                    "scale": "0"
                },
                {
                    "code": "XPF",
                    "namezh": "CFP 法郎",
                    "nameen": "CFP Francs",
                    "typezh": "A",
                    "typeen": "A",
                    "unit": "XPF",
                    "base": 2,
                    "scale": "0"
                },
                {
                    "code": "YER",
                    "namezh": "也门里亚尔",
                    "nameen": "Yemeni Rials",
                    "typezh": "A",
                    "typeen": "A",
                    "unit": "YER",
                    "base": 2,
                    "scale": "0"
                },
                {
                    "code": "ZAR",
                    "namezh": "南非兰特",
                    "nameen": "South Africa Rand",
                    "typezh": "A",
                    "typeen": "A",
                    "unit": "ZAR",
                    "base": 1,
                    "scale": "0"
                },
                {
                    "code": "ZMW",
                    "namezh": "赞比亚克瓦查",
                    "nameen": "Zambian Kwacha",
                    "typezh": "A",
                    "typeen": "A",
                    "unit": "ZMW",
                    "base": 2,
                    "scale": "0"
                }
            ]
        }
    ]
}


def main():
  # global cu
  convert_unit.build_config()

  # from soc_common.utils import file_utils

  # for i in cu['items'][0]['items']:
  #   fileName = 'D:\\01_work\\flags\\4x3\\'+ i['code'][:2].lower() +'.svg'
  #   if not file_utils.exists_file(fileName):
  #     print(fileName)


if __name__ == '__main__':
  generate_by_java.run()
