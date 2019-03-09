# -*- coding: utf-8 -*
# using this to check binance.com balance
# running in the server

from binance.client import Client
import time
from xlwt import *
import datetime

def main():
    apikey = 'hjtkUKanfJZ6iLw3sZaCiNz23vmKXYmJKbUW2spaSdu6y7jeRq2dY9Cr2Q7ImjUU'
    sec_key = 'dIkCVVMTws7EwkarWgnOYqEPzwBuaIDMWzt0hx1hSDUCdFjuccj3e50fSYXWg5rB'
    client = Client(apikey, sec_key)

    time_server = client.get_server_time()
    ms = time_server['serverTime']
    ms = datetime.datetime.fromtimestamp(ms / 1000.0)
    print(time_server)

    symbol = ["BTCUSDT", "LTCUSDT", "ETHUSDT", "EOSUSDT", "BNBUSDT"]
    data = []

    # request time
    origin_time = time.localtime()
    req_time = time.strftime("%d %b,%Y", origin_time)
    stop_time = req_time + time.strftime(" %H %M %S", origin_time)
    print('Stop time' + stop_time)
    for s in symbol:
        # fetch weekly klines since it listed
        klines = client.get_historical_klines(s, Client.KLINE_INTERVAL_1DAY, req_time)
        kk = klines[0]
        data.append(klines[0])
    content = data

    # build excel
    # fileName = stop_time + '.xls'
    fileName = 'latest.xls'
    workbook = Workbook(encoding='utf-8')
    xlsheet = workbook.add_sheet("1", cell_overwrite_ok=True)
    table_head = [ 
        ['币种'],
        ['开盘价'],
        ['最高价'],
        ['最低价'],
        ['收盘价（K线未结束为最后时刻）'],
        ['成交量'],
        ['收盘时间'],
        ['成交笔数'],
        ['主动买入成交量'],
        ['主动买入成交额'],
        ['无意义参数']
    ]

    # write head
    headlen = len(table_head)
    for i in range(headlen):
        xlsheet.write(0, i, table_head[i])

    t = -1
    contentRow = len(content)  # 
    for row in range(contentRow):
        for col in range(0, len(content[row])):
            t = t + 1
            if col == 0:
                xlsheet.write(row + 1, col, symbol[row])
            elif col == 6:
                ms = content[row][col]
                ldate = datetime.datetime.fromtimestamp(ms / 1000.0)
                ldate = str(ldate)
                xlsheet.write(row + 1, col, ldate)
            else:
                xlsheet.write(row + 1, col, content[row][col])

    workbook.save(fileName)
    print('Done')


if __name__ == '__main__':
   main()
