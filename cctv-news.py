# cctv news data analysis
# py

import tushare as ts

ts.set_token('your_token')

pro = ts.pro_api()

df = pro.cctv_news(date='20181211')
