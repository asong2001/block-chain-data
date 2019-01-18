# cctv news data analysis
# py

import tushare as ts

ts.set_token('338fb37f45430d7f9699295040b4a0374d84f5b1850d53b29980fa2e')

pro = ts.pro_api()

df = pro.cctv_news(date='20181211')