# get block chain exchange name list

import tushare as ts

pro = ts.pro_api('338fb37f45430d7f9699295040b4a0374d84f5b1850d53b29980fa2e')

df = pro.query('coinexchanges', area_code='us')

print(df)
