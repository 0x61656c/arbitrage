"""
Copyright Aaron E. Lebel
All Rights Reserved

This module does not include sensitive information
"""

###############################################################
#Import statements
###############################################################
import urllib.parse
import requests
import time

#Custom Package
from CryptochainDataTools import *
from CryptochainConversionTools import *

#############################################################
#currency converter info
#############################################################

currency_url = 'http://apilayer.net/api/'

full_currency_url= """
http://apilayer.net/api/live?access_key=b4266d5d05849f9c657069bae3933220&currencies=EUR,%20RUB&source=USD&format=1
"""

USDtoEUR = requests.get(full_currency_url).json()
(USDtoEUR['quotes']['USDEUR'])

######################################################################
#Methods
######################################################################

#method for doing one dimensional analysis
def OneDimensionalMethod(pair):
    c = pair
    print("                          " + c['pair'])
    print()
    print('           High: '+ c['high'], end = "")
    print('    ////     Low: ' + c['low'])
    
    print('                         Bid: ' + str(c['bid']))
    print('                         Ask: ' + str(c['ask']))
    print()


    #function only works with compatible values!
    
######################################################################    
    
    #THIS FUNCTION CALLS PAIR INDECES; NOT PAIR VALUES 
def MultiDimensionalMethod(pair1, pair2):  
    data = calldata()
    
    #these data calls use INDEX not name
    pair1 = data[pair1]
    pair2 = data[pair2]
    
    pair1price = pair1['last']
    pair2price = 1 / pair2['last']
    
    return [pair1price, pair2price]


######################################################################
#main() functions
######################################################################

#main function for executing one dimensional analysis. 
#contains relevant data and functional methods
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
        
        data = calldata()
        OneDimensionalMethod(data[index])
        loopindex += 1
        
        time.sleep(6)
        print("""
    ===================================================
                      Loop index = %d"""%loopindex + """
    ===================================================
            """)
    print("Done")
    
######################################################################

#defaults to USDtoBTC and EURtoBTC
def main2DimensionalDifferentialSeeking(pair1 = 0, pair2 = 4):
    #establish differential, call data
    differential = 0
    data = calldata()
    #last prices defaults to USDtoBTC and EURtoBTC
    lastprices = MultiDimensionalMethod(pair1, pair2)
    
    price1 = lastprices[0]
    price2 = lastprices[1]
    
    price1 = float(price1)
    price2 = float(price2)
    print("USDtoBTC: %f" %price1)
    print("EURtoBTC: %f" %price2)
    
    conversionrate = 1.18
    price2converted = convertEURtoUSD(price2, conversionrate)
    print("EURtoUSDtoBTC: %f" %price2converted)
    
    if price1 > price2converted: 
        differential = price1 - price2converted
    else:
        differential = 0
        
    return differential 

######################################################################
#Transaction functions

""" Functions in this section are designed to execute transactions. Currently
under construction. Algorithms will run simulation, check for positive roi, and
then execute """
######################################################################


def executeBTCtoUSD(amount):
    return 42

def executeUSDtoBTC(amount):
    return 42
    
def executeBTCtoEUR(amount):
    return 42
    
def executeEURtoBTC(amount):
    return 42


######################################################################
#Simulation functions
######################################################################

#By default, runs a simulation of (USD TO BTC) AND (EUR TO BTC)
#takes float input
def USDEURBTCsimulation(startingcapital):
    currCapital = startingcapital
    loopindex = 0

    while True:
        loopindex += 1
        print("Loop index: %d" %loopindex)
        
        print("===========================")
        
        #establish gain based on main2dANALYSIS and call data
        data = calldata()
        #find latestpricepercoinin USD
        pricepercoin = float(json_BTCUSD['last'])
        
        #Runs2Dimensional differential analysis
        gain = main2DimensionalDifferentialSeeking() 
        #caches gain percoin for later printing
        gainpercoin = gain
        
        gain = gain * (currCapital/pricepercoin)
        
        #this fee is slightlymore than the actual fee, but simplifies the 
        #calculation substantially
        fee = 0.002 * currCapital * 2
        
        #restarts loop if newGPC = oldGPC. This is the most efficient way to account   
        #for volume not updating without creating an entire simulated market

        if gain > fee:
            differential = gain - fee
        else: 
            differential = 0
        currCapital += differential
        
        #prints out relevant data for user benefit
        print()
        print("Fees: %f" %fee)
        print("Revenue: %f" %gain)
        print("Profit per Coin: %f" %gainpercoin)
        print("Adjusted profit: %f" %differential)
        print("Current capital: %f" %currCapital)
        print("===========================")
        print()
        time.sleep(3)
    print("Done")
    
    #aggProfit += profit
    
    





