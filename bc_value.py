# get block chain value

import tushare as ts

pro = ts.pro_api('338fb37f45430d7f9699295040b4a0374d84f5b1850d53b29980fa2e')

# pro = ts.pro_api()

df = pro.query('coinbar', exchange='okex', symbol='btcusdt', freq='daily', start_date='20180801', end_date='20180830')

print(df)
