# using huobi API
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 15:48:13 2018

@author: zhaobo
"""

from HuobiDMService import HuobiDM
from pprint import pprint

URL = "https://api.hbdm.com"

####  input your access_key and secret_key below:
ACCESS_KEY = ''
SECRET_KEY = ''

dm = HuobiDM(URL, ACCESS_KEY, SECRET_KEY)

print(u' 获取K线数据 ')
pprint(dm.get_contract_kline(symbol='BTC_CW', period='60min', size=20))
