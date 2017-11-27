#!/usr/bin/python
# -*- coding: utf-8 -*-
# encoding: utf-8
# 客户端调用，用于查看API返回结果

from OkcoinSpotAPI import OKCoinSpot
from OkcoinFutureAPI import OKCoinFuture
import logging
import time
import json
import os
import pandas as pd

# 初始化apikey，secretkey,url
fileName = 'key.json'
path = os.path.abspath(os.path.dirname(__file__))
fileName = os.path.join(path, fileName)
# 解析json文件
with open(fileName) as data_file:
    setting = json.load(data_file)
    data_file.close()
apikey = str(setting['apiKey'])
secretkey = str(setting['secretKey'])
okcoinRESTURL = 'www.okex.com'

# 现货API
okcoinSpot = OKCoinSpot(okcoinRESTURL, apikey, secretkey)

# 期货API
okcoinFuture = OKCoinFuture(okcoinRESTURL, apikey, secretkey)

symbol = 'eth_usd'
contracttype = 'quarter'
contractmultiplier = 10
leverage = '20'
fee = -0.00025
ratio = 0.01
amount = 1
ordertype = {"openlong": 1, "openshort": 2, "closelong": 3, "closeshort": 4}

orderinfo = pd.DataFrame(columns=["symbol", "contracttype", "price", "amount", "ordertype"])

print("Started...")
while True:
    try:
        posinfo = okcoinFuture.future_position(symbol, contracttype)
        posinfo = json.loads(posinfo)
        if posinfo['result']:
            posinfo['holding']

        # query orderinfo
        queryorderinfo = okcoinFuture.future_orderinfo(symbol, contracttype, '-1', '1', '0', '50')
        queryorderinfo = json.loads(queryorderinfo)

        if queryorderinfo['result']:
            for order in queryorderinfo['orders']:
                pass

        futureticker = okcoinFuture.future_ticker(symbol, contracttype)
        ticker = futureticker['ticker']
        ask = round(ticker['last'] * (1 + ratio), 3)
        bid = round(ticker['last'] * (1 - ratio), 3)
        # profit = (contractmultiplier / bid - contractmultiplier / ask) * amount*ticker['last'] - fee * amount * contractmultiplier * 2



        orderstatus = okcoinFuture.future_trade(symbol, contracttype, price=ask, amount=amount,
                                                tradeType=ordertype['openshort'], matchPrice='0', leverRate=leverage)
        orderstatus = json.loads(orderstatus)
        if orderstatus['result']:
            orderinfo.loc[orderstatus['order_id']] = [symbol, contracttype, ask, amount, ordertype['openshort']]


    except Exception as e:
        logging.exception(e)

    time.sleep(10)

# print (u' 现货行情 ')
# print (okcoinSpot.ticker('ltc_btc'))

# print (u' 现货深度 ')
# print (okcoinSpot.depth('btc_usd'))

# print (u' 现货历史交易信息 ')
# print (okcoinSpot.trades())

# print (u' 用户现货账户信息 ')
# print (okcoinSpot.userinfo())

# print (u' 现货下单 ')
# print (okcoinSpot.trade('ltc_usd','buy','0.1','0.2'))

# print (u' 现货批量下单 ')
# print (okcoinSpot.batchTrade('ltc_usd','buy','[{price:0.1,amount:0.2},{price:0.1,amount:0.2}]'))

# print (u' 现货取消订单 ')
# print (okcoinSpot.cancelOrder('ltc_usd','18243073'))

# print (u' 现货订单信息查询 ')
# print (okcoinSpot.orderinfo('ltc_usd','18243644'))

# print (u' 现货批量订单信息查询 ')
# print (okcoinSpot.ordersinfo('ltc_usd','18243800,18243801,18243644','0'))

# print (u' 现货历史订单信息查询 ')
# print (okcoinSpot.orderHistory('ltc_usd','0','1','2'))

# print(u' 期货行情信息')
# print(okcoinFuture.future_ticker('ltc_usd', 'this_week'))

# print (u' 期货市场深度信息')
# print (okcoinFuture.future_depth('btc_usd','this_week','6'))

# print (u'期货交易记录信息')
# print (okcoinFuture.future_trades('ltc_usd','this_week'))

# print (u'期货指数信息')
# print (okcoinFuture.future_index('ltc_usd'))

# print (u'美元人民币汇率')
# print (okcoinFuture.exchange_rate())

# print (u'获取预估交割价')
# print (okcoinFuture.future_estimated_price('ltc_usd'))

# print(u'获取虚拟合约的K线信息')
# print(okcoinFuture.future_kline('ltc_usd', 'this_week', '1min', '50'))

# print(u'获取当前可用合约总持仓量')
# print(okcoinFuture.future_hold_amount('ltc_usd', 'this_week'))
#
# print(u'获取合约坐高买价和最低卖价格')
# print(okcoinFuture.future_price_limit('ltc_usd', 'this_week'))
#
# print(u'获取全仓账户信息')
# print(okcoinFuture.future_userinfo())
#
# print(u'获取全仓持仓信息')
# print(okcoinFuture.future_position('ltc_usd', 'this_week'))

# print (u'期货下单')
# print(okcoinFuture.future_trade('etc_usd', 'this_week', '0.1', '1', '1', '0', '20'))

# print (u'期货批量下单')
# print (okcoinFuture.future_batchTrade('ltc_usd','this_week','[{price:0.1,amount:1,type:1,match_price:0},{price:0.1,amount:3,type:1,match_price:0}]','20'))

# print (u'期货取消订单')
# print (okcoinFuture.future_cancel('ltc_usd','this_week','47231499'))

# print (u'期货获取订单信息')
# print (okcoinFuture.future_orderinfo('ltc_usd','this_week','47231812','0','1','2'))

# print (u'期货逐仓账户信息')
# print (okcoinFuture.future_userinfo_4fix())

# print (u'期货逐仓持仓信息')
# print (okcoinFuture.future_position_4fix('ltc_usd','this_week',1))
