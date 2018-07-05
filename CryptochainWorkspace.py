#import statements
import time
import math
import urllib.parse
import requests
import tkinter

from CryptochainFinancialTools import *
from CryptochainDataTools import *
from CryptochainConversionTools import *
from CryptochainArbitraryDifferentiation import *
from CryptochainSimulationEnvironments import *

#functions

def attempt4(pair1Index,pair2Index,ConversionRate, initialCapital):
        
        def SubSimulation(pair1Index, pair2Index,ConversionRate, initialCapital):
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
    currentCapital = initialCapital
    
    diff0 = 0
    
    while True:
        if gainPer
        