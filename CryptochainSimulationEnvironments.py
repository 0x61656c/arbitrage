"""
Copyright Aaron E. Lebel
All Rights Reserved


This module does not include sensitive information
"""

import time
import math
import urllib.parse
import requests



from CryptochainFinancialTools import *
from CryptochainDataTools import *
from CryptochainConversionTools import *
from CryptochainArbitraryDifferentiation import *
from CryptochainSimulationEnvironments import *


#THIS SIMULATION USES INDEXED VALUES AS INPUTS. USING OTHER INPUTS WILL RESULT 
#IN CATESTROPHIC FAILURE. BE CAREFUL!!!!!!!!!!!!!!!!!!!!!!!! 
def ArbitraryLoopingSimulation(pair1, pair2, initialcapital,conversionrate):
   
    if pair1 == pair2:
        return "Done"
    
    currCapital = initialcapital
    loopindex = 0
    
    while True:
        loopindex += 1
        print("Loop index: %d" %loopindex)
        print("===========================")
        
        #establish gain based on main2dANALYSIS and call data
        data = calldata()
        #find latestpricepercoinin USD
        DomesticPricePercoin = float(json_data2['data'][pair1]['last'])
        
        #Runs2Dimensional differential analysis
        gainpercoin = ComparativeDifferentialAnalysis(pair1,pair2,conversionrate)

        #caches gainpercoin for later printing
        gain = gainpercoin * (currCapital/DomesticPricePercoin)
        
        #this fee is slightlymore than the actual fee, but simplifies the 
        #calculation substantially
        fee = 0.002 * (currCapital / DomesticPricePercoin)
        
        if gain > fee:
            differential = gain - fee
        else: 
            differential = 0
        
        #refreshes current capital based on differential
        currCapital += differential
        
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


def ArbitraryStaticSimulation(pair1, pair2, initialcapital,conversionrate):
    if pair1 == pair2:
        return "Done"
    
    currCapital = initialcapital
    print("Running Static Data Analysis")
    print("===============================")
    
    #establish gain based on main2dANALYSIS and call data
    data = calldata()
    #find latestpricepercoinin USD
    DomesticPricePercoin = float(json_data2['data'][pair1]['last'])
    
    #Runs2Dimensional differential analysis
    gainpercoin = ComparativeDifferentialAnalysis(pair1,pair2,conversionrate)
    
    #caches gainpercoin for later printing
    gain = gainpercoin * (currCapital/DomesticPricePercoin)
    
    #this fee is slightlymore than the actual fee, but simplifies the 
    #calculation substantially
    fee = 0.002 * (currCapital / DomesticPricePercoin)
    
    if gain > fee:
        differential = gain - fee
    else: 
        differential = 0
    
    #refreshes current capital based on differential
    currCapital += differential
    
    print()
    print("Fees: %f" %fee)
    print("Revenue: %f" %gain)
    print("Profit per Coin: %f" %gainpercoin)
    print("Adjusted profit: %f" %differential)
    print("Current capital: %f" %currCapital)
    print("===============================")
    print()
    print("Done")

#This simulation is currently the most powerful of the suite
"""WWWWWWW"""
def repeatedStaticSimulation(pair1,pair2,initialcapital,conversionrate):
    differential0 = 9999999999999999999999999999
    currCapital = initialcapital
    while True:
        
        gainpercoin = ComparativeDifferentialAnalysis(pair1,pair2,conversionrate)
        if not differential0 == gainpercoin:
            data = calldata()
            #find latestpricepercoinin USD
            DomesticPricePercoin = float(json_data2['data'][pair1]['last'])
            
            #Runs2Dimensional differential analysis
            
            #caches gainpercoin for later printing
            gain = gainpercoin * (currCapital/DomesticPricePercoin)
            
            #this fee is slightly more than the actual fee, but simplifies the 
            #calculation substantially
            fee = 0.002 * (currCapital) * 2
            
            if gain > fee:
                differential = gain - fee
            else: 
                differential = 0
                
            differential0 = gainpercoin
            currCapital += differential
                
            print()
            print("Fees: %f" %fee)
            print("Revenue: %f" %gain)
            print("Profit per Coin: %f" %gainpercoin)
            print("Adjusted profit: %f" %differential)
            print("Current capital: %f" %currCapital)
            print("===============================")
            print()
        
        else: time.sleep(5)
            
    print("Done")
        
        


#Runs a simulation with USD/BTC as pair1 and EUR/BTC as pair 2
#This exists as a sample upon which to base other functions. Hard coded
#for speed of functionality
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
        
        #PrintStatements for user benefit
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
    
