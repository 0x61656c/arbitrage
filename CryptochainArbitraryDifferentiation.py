"""
Copyright Aaron E. Lebel
All Rights Reserved


This module does not include sensitive information
"""
##########################################################
#import statements
##########################################################
#builtin packages

import time
import math
import urllib.parse
import requests
import tkinter

#Custom packages
from CryptochainFinancialTools import *
from CryptochainDataTools import *


def mainOneDimensional(index):
    print()
    print("    Running Single Variable Financial Analysis")
    print("""
    =====================================================
                      Loop index = 1
    =====================================================
     """)
    loopindex = 1
    
    while True:
        #calls data
        data = calldata()

        print("""
    ===================================================
                      Loop index = %d""" %loopindex + """
    ===================================================
            """)
    print("Done")
    
    #returns current price data of pair input
def MultiDimensionalMethod(pair1, pair2):  
    data = calldata()
    
    #these data calls use INDEX not name
    pair1 = data[pair1]
    pair2 = data[pair2]
    
    pair1price = pair1['last']
    pair2price = pair2['last']
    #Returns price data as list
    return [pair1price, pair2price]
    
    #runs differential analysis basedon pair index input
    
    #calculates the differential given arbitrary inputs
    #NOTE THAT THIS FUNCTION TAKES ARBITRARY INPUTS IN THE FORM OF INDECES
    
    #Runs differential analysis script for two pairs using a predetermined 
    #conversion rate
    
def ComparativeDifferentialAnalysis(pair1index ,pair2index ,conversionrate):
    
    #Creates a price list based on inputs, outputs a list
    prices = MultiDimensionalMethod(pair1index, pair2index)
    
    #quantifies prices (previously stored in lists)
    price1 = prices[0]
    print("Price1: ", end = "")
    print(price1)
    price2 = prices[1]


    #requantifies prices as floating point values
    price1 = float(price1)
    price2 = float(price2)
    #print("%s" %pair1index + "toBTC" + ": %f" %price1)
    #print("%s" %pair2index + "toBTC" + ": %f" %price2)
    
    #converts price2 to price2*currency1/currency2 
    price2converted = convertCurr1toCurr2(price2, conversionrate)
    print("Price2: ", end = "")
    print(price2converted)
    #print("%s" %pair1index + "to%s" %pair2index + "toBTC : " "%f" %price2converted)
    
    #checks whether price1 is greater than price2
    if price1 > price2converted: 
        #Calculates the differential if so
        differential = price1 - price2converted
    else:
        differential = 0 #else, the differential is stored as zero (for now)
        
    return differential 
    
def threeWayDifferentialAnalysis():
    data = calldata()
    
    #prices
    USDpriceBTC = float(data[0]['last'])
    ETHpriceBTC = float(data[8]['last'])
    ETHpriceUSD = float(data[3]['last'])
    #ETH/BTC * USD/ETH
    ETHpriceETH = (USDpriceBTC * ETHpriceBTC)
    
    return abs(ETHpriceETH-ETHpriceUSD)


    