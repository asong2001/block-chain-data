# get block chain value

import tushare as ts

pro = ts.pro_api('your_token')

# exchange name
exchange_name = 'okex'

# exchange pair
coin_pair = 'btcusdt'

# pair of coin
fr = 'daily'

# start date
s_date = '20180801'

# end date
e_date = '20180830'

df = pro.query('coinbar', exchange=exchange_name, symbol=coin_pair, freq=fr, start_date=s_date, end_date=e_date)

print(df)

file_name = exchange_name + '_' + coin_pair + '_' + fr + '_' + s_date + '_' + e_date

# 保存
df.to_excel('excel/' + file_name + '.xlsx')
