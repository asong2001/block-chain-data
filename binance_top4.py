# using this to check binance.com balance
# 需求
# 查询币安四大币种净值

from binance.client import Client
import time
from xlwt import *
import datetime

def main():
    apikey = ''
    sec_key = ''
    client = Client(apikey, sec_key)

    time_server = client.get_server_time()
    ms = time_server['serverTime']
    ms = datetime.datetime.fromtimestamp(ms / 1000.0)
    print(time_server)

    symbol = ["BTCUSDT", "LTCUSDT", "ETHUSDT", "EOSUSDT", "BNBUSDT"]
    data = []

    # 请求时间
    origin_time = time.localtime()
    req_time = time.strftime("%d %b,%Y", origin_time)
    stop_time = req_time + time.strftime(" %H %M %S", origin_time)
    print('请求截止时间' + stop_time)
    for s in symbol:
        # fetch weekly klines since it listed
        klines = client.get_historical_klines(s, Client.KLINE_INTERVAL_1DAY, req_time)
        kk = klines[0]
        data.append(klines[0])
    content = data

    # 创建excel表
    fileName = stop_time + '.xls'
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

    # 写入表头
    headlen = len(table_head)
    for i in range(headlen):
        xlsheet.write(0, i, table_head[i])

    t = -1
    contentRow = len(content)  # 列表元素个数  = 待写入内容行数
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
