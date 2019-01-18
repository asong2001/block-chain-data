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
ACCESS_KEY = '1a8b52b3-8e272038-69e4409e-1ea2a'
SECRET_KEY = '0cb2eb13-f2a0a0a7-fde986bb-318de'

dm = HuobiDM(URL, ACCESS_KEY, SECRET_KEY)

print(u' 获取K线数据 ')
pprint(dm.get_contract_kline(symbol='BTC_CW', period='60min', size=20))
