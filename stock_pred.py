# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 13:30:53 2020

@author: Vagard Stenberg
"""

import stock_info as si
import time

gainers = si.get_gainers(5)
stock = si.get_stock_data(gainers[1])

buying_price = 0

def SMA(days):
    s = 0
    for i in range(days):
        s += stock[i+1]
    s = s / days
    return s

if(SMA(200) < SMA(50)):
    print("invest!")
    
    buying_price = stock[0]
    
    while True:
        price = stock[0]
        if ((price - buying_price) / buying_price) * 100 > 2:
            print("Sold at a profit of", price - buying_price)
            buying_price = 0
        elif(SMA(200) > SMA(50) and buying_price != 0):
            print("Sold at a loss of", buying_price - stock[0])
        time.sleep(1800)
    

    


    
print("SMA 200:", SMA(200))
print("SMA 50:", SMA(50))