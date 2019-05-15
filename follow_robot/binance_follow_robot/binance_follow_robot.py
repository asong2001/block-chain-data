# -*- coding: utf-8 -*
# using API to follow Binance trading 
# Version 0.1

from binance.client import Client
import time
from xlwt import *
import xlwt
import datetime
import shutil
import json
from binance.enums import *


def timeChange(ms, flag):
    if flag == 1:
        # 服务器时间转换为北京时间
        bj_time = (ms + datetime.timedelta(hours=8)).strftime("%Y-%m-%d %H:%M")
        return bj_time

    elif flag == 2:
        ser_time = (ms - datetime.timedelta(hours=8)).strftime("%Y-%m-%d %H:%M")
        return ser_time

if __name__ == "__main__":
    # Song 
    # API:
    # SecKey: 

    # Chen
    # API:
    # SecKey:

    # 机器人1
    apikey_s = ''
    seckey_s = ''
    client_s = Client(apikey_s,seckey_s)

    # 公共查询机器人
    pub_apikey = ''
    pub_seckey = ''
    pub_client = Client(pub_apikey, pub_seckey)
        
    # 机器人2
    apikey_chen = ''
    seckey_chen = ''
    client_chen = Client(api_key=apikey_chen, api_secret=seckey_chen)

    # 查询服务器时间
    server_time = pub_client.get_server_time()
    ms = server_time['serverTime']
    ms = datetime.datetime.fromtimestamp(ms / 1000)
    print(ms)

    symbol = ['BTC', 'ETH', 'BNB', 'USDT']

    usdt = 'USDT'
    eth = 'ETH'
    ETHUSDT = 'ETHUSDT'
    pair_symbol = ['BTCUSDT','ETHUSDT','BNBUSDT','IOSTUSDT']
    binance_chen_usdt = client_chen.get_asset_balance('BNB')
    binance_song_usdt = client_s.get_asset_balance('USDT')

    # 查询余额
    # GET /api/v3/openOrders  (HMAC SHA256)
    # for k in  symbol:
    #     balance = client_chen.get_asset_balance(k)
    #     balance = json.dumps(balance)
    #     print('tar balance')
    #     print(balance)

    print('song balance')
    for k in  symbol:
        balance = client_s.get_asset_balance(k)
        balance = json.dumps(balance)
        print(balance)

    # 查询目标订单
    ind = -1
    order_tmp = []
    order_chen = []
    for k in pair_symbol:
        ind += 1
        order_book = client_s.get_open_orders(symbol=k)
        if len(order_book) != 0:
            print('已挂单情况'+k)
            order = order_book[0]
            print(order['price'])

    if len(order_chen):
        # 如果存在订单
        pass
    else:
        pass