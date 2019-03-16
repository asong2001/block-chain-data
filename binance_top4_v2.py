# -*- coding: utf-8 -*
# using this to check binance.com balance
# running in the server

from binance.client import Client
import time
from xlwt import *
import xlwt
import datetime
import shutil

def main():
    # ref https://blog.csdn.net/qq_31489933/article/details/80323426
    # 设置单元格格式
    # 设置边框
    borders = xlwt.Borders()
    borders.left = xlwt.Borders.THIN
    borders.right = xlwt.Borders.THIN
    borders.top = xlwt.Borders.THIN
    borders.bottom = xlwt.Borders.THIN
    
    #设置居中
    alignment = xlwt.Alignment()
    alignment.horz = xlwt.Alignment.HORZ_CENTER

    # 设置样式
    style1 = xlwt.XFStyle()
    style1.borders = borders
    style1.alignment = alignment

    style2 = xlwt.XFStyle()
    style2.alignment = alignment    
    style2.borders = borders     

    apikey = 'hjtkUKanfJZ6iLw3sZaCiNz23vmKXYmJKbUW2spaSdu6y7jeRq2dY9Cr2Q7ImjUU'
    sec_key = 'dIkCVVMTws7EwkarWgnOYqEPzwBuaIDMWzt0hx1hSDUCdFjuccj3e50fSYXWg5rB'
    client = Client(apikey, sec_key)

    time_server = client.get_server_time()
    ms = time_server['serverTime']
    ms = datetime.datetime.fromtimestamp(ms / 1000.0)
    print(ms)

    symbol = ["BTCUSDT", "LTCUSDT", "ETHUSDT", "EOSUSDT", "BNBUSDT"]
    data = []

    # request time
    origin_time = time.localtime()
    req_time = time.strftime("%d %b,%Y ", origin_time)
    # 截止到当前时间的上一个整点时刻
    stop_time = req_time + time.strftime("%H %M", origin_time)

    # 北京时间
    bj_time = (datetime.datetime.now() + datetime.timedelta(hours=8)).strftime("%Y-%m-%d %H:%M")
    print('Beijing time:' + bj_time)
    print('Stop time:' + stop_time)

    # 手动设置日期并设置数据
    # req_time = '15 Mar,2019'

    for s in symbol:
        # fetch weekly klines since it listed
        klines = client.get_historical_klines(s, Client.KLINE_INTERVAL_1DAY, req_time)
        data.append(klines[0])
    content = data

    # build excel
    fileName = 'latest.xls'
    # fileName = stop_time + '.xls'
    historyName = stop_time + '.xls'
    workbook = Workbook(encoding='utf-8')
    xlsheet = workbook.add_sheet("1", cell_overwrite_ok=True)

    table_head = [ 
        ['币种'],
        ['开盘价'],
        ['最高价'],
        ['最低价'],
        ['收盘价'],
        ['振幅'],
        ['涨幅']
    ]
    '''
    取消数据
    ['成交量'],
    ['收盘时间'],
    ['成交笔数'],
    ['主动买入成交量'],
    ['主动买入成交额'],
    '''

    # 写入文件头部
    headlen = len(table_head)
    for i in range(headlen):
        xlsheet.write(0, i, table_head[i], style = style1)

    t = -1
    contentRow = len(content)  # 
    for row in range(contentRow):
        for col in range(0, len(content[row])):
            t = t + 1
            if col == 0:
                xlsheet.write(row + 1, col, symbol[row], style = style1)
                
            elif col == 5 or col == 7 or col == 8 or col == 9:
                # 交易时间和成交量等数据
                # add round
                '''
                ldata = round(float(content[row][col]))
                xlsheet.col(col).width = 256 * 10
                xlsheet.write(row + 1, col, ldata, style = style2)
                '''
                pass

            elif col == 6:
                # ms = content[row][col]
                # ldate = datetime.datetime.fromtimestamp(ms / 1000.0)
                # 修改为显示更新的时间
                '''
                ldate = str(bj_time)
                xlsheet.col(col).width = 256 * 15
                xlsheet.write(row + 1, col, ldate, style = style2)
                '''
                pass

            elif col == 10:
                # 振幅
                highest = float(content[row][2])
                lowest = float(content[row][3])
                amp = (highest - lowest) / lowest
                amp = '%.2f%%' % (amp * 100)
                content[row][col] = amp
                xlsheet.col(col).width = 256 * 6
                xlsheet.write(row + 1, 5, content[row][col], style = style2)

            elif col == 11:
                # 涨幅
                close_value = float(content[row][4])
                open_value = float(content[row][1])
                gain = (close_value - open_value) / open_value
                gain = '%.2f%%' % (gain * 100)
                content[row][col] = gain
                xlsheet.col(col).width = 256 * 6
                xlsheet.write(row + 1, 6, content[row][col], style = style2)

            else:
                # 其余数据
                wdata = float(content[row][col])
                wdata = round(wdata, 2)
                xlsheet.col(col).width = 256 * 10
                xlsheet.write(row + 1, col, wdata, style = style2)

    workbook.save(fileName)
    ms = content[1][6]
    ldate = datetime.datetime.fromtimestamp(ms / 1000.0)
    print(ldate)

    shutil.copyfile('latest.xls', './tmp/latest.xls')
    # 保留历史数据
    path2 = './tmp/history/' + historyName
    shutil.copyfile('latest.xls', path2)

    print('Done')


if __name__ == '__main__':
   main()
