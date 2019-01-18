# get block chain exchange name list

import tushare as ts

pro = ts.pro_api('your_token')

df = pro.query('coinexchanges', area_code='us')

print(df)
