# -*- coding: utf-8 -*
# using this to check binance.com balance
# running in the server

from binance.client import Client
import time
from xlwt import *
import xlwt
import datetime
import shutil
from lxml import html
import requests
import xlrd


def aicoin_data():
    # header /html/body/div[1]/div[2]/div[2]/div[4]/div/div[2]
    puburl = 'https://www.aicoin.net.cn/currencies/'

    id_list = ['bitcoin',
               'ethereum',
                'binanceCoin',
                'huobiToken',
                'okb']

    # market_over_view = cmc_tree.xpath('//*[@id="currencies_wrapper"]')
    headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}

    volume24h = []
    value24h = []
    globalRatio = []

    for id in id_list:
        url = puburl + id + '.html'
        aicoin_pages = requests.get(url,headers=headers)
        aicoin_tree = html.fromstring(aicoin_pages.text)
        p = '//*[@id="tab-select-pane-1"]/div/div[1]/div/div[2]/div[1]/div[2]/span[2]/span/span[1]/text()'
        volume24h.append(aicoin_tree.xpath(p))

        # 24小时交易量
        p2 = '//*[@id="tab-select-pane-1"]/div/div[1]/div/div[2]/div[1]/div[3]/span[2]/span/span[1]/text()'
        value24h.append(aicoin_tree.xpath(p2))

        # 全球市值占比
        p3 = '//*[@id="tab-select-pane-1"]/div/div[1]/div/div[1]/div[2]/div[2]/div[1]'
        globalRatio.append(aicoin_tree.xpath(p3))

    print('24 小时额/亿')
    print(value24h)

    print('24 小时量/万')
    print((volume24h))

    print('全球市值占比')
    print(globalRatio)

    return value24h,volume24h

if __name__ == "__main__":
    # 创建excel文件
    origin_time = time.localtime() # 时间设置
    req_time = time.strftime("%d %b,%Y ", origin_time)
    stop_time = req_time + time.strftime("%H %M", origin_time)

    historyName = stop_time + '.xls'
    workbook = Workbook(encoding='utf-8')
    xlsheet = workbook.add_sheet("1", cell_overwrite_ok=True)

    fileName = 'market.xls'
    # -------- 写入币种头部 --------#
    symbol = ["BTC", "ETH", "BNB", "HT", "OKB"]
    headlen = len(symbol)
    for i in range(headlen):
        xlsheet.write(i+1, 0, symbol[i])
    workbook.save(fileName)

    # -------- 写入文件头部 --------#
    table_head = [
        ['币种'],
        ['24H交易量/w'],
        ['24H成交额/亿']
                    ]
    # 写入文件头部
    headlen = len(table_head)
    for i in range(headlen):
        xlsheet.write(0, i, table_head[i])
    workbook.save(fileName)

    # ----------------------AI coin-------------------#
    [value24h, volume24h] = aicoin_data()

    # volume 24h 交易量
    content = volume24h
    contentRow = len(content)  #
    for row in range(contentRow):
        col = 1
        # t = t + 1
        c = content[row]
        d = c
        xlsheet.write(row + 1, col, d)
    workbook.save(fileName)

    # value 24h 交易额
    content = value24h
    contentRow = len(content)  #
    for row in range(contentRow):
        col = 2
        # t = t + 1
        c = content[row]
        d = c
        xlsheet.write(row + 1, col, d)
    workbook.save(fileName)

    # -------- 移动文件 ------- #
    '''
    path2 = '/home/buddysong_42/block-chain-data/tmp/history/' + historyName
    shutil.copyfile('latest.xls', path2)
    '''