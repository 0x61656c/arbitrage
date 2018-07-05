#############################################################
#import statements
#############################################################

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
from CryptochainDataCollection import *
from CryptochainExcelConversion import *

#############################################################
#Data collection methods
#############################################################


def DataBasedRepeatedStaticSimulation(pair1,pair2,initialcapital,conversionrate, datacollect = True, usefuliterations = 100):
    #dif0 cannot be initialized at zero, because this would prevent the first 
    #transaction in some cases--Thus...
    differential0 = 9999999999999999999999999999 #starts at infinity(ish) 
    currCapital = initialcapital
    datahold = []
    count = 0
    
    while count < usefuliterations:
        try:    
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
                count += 1
                
                if datacollect == True:
                    datahold.append(differential)
                    
                print()
                print("Iteration number: %i" %count)
                print("Fees: %f" %fee)
                print("Revenue: %f" %gain)
                print("Profit per Coin: %f" %gainpercoin)
                print("Adjusted profit: %f" %differential)
                print("Current capital: %f" %currCapital)
                print("===============================")
                print()
                time.sleep(6)
            else: time.sleep(6)
            
            writetoExcel("CryptochainData", datahold)
        except:
            print("Cooling down")
            time.sleep(120)
    print("done")    
    
def ExperimentalSimulation(initialcapital,conversionrate = 1, datacollect = True, usefuliterations = 100):
    #dif0 cannot be initialized at zero, because this would prevent the first 
    #transaction in some cases--Thus...
    differential0 = 9999999999999999999999999999 #starts at infinity(ish) 
    currCapital = initialcapital
    datahold = []
    count = 0
    
    while count < usefuliterations:
        differential1 = threeWayDifferentialAnalysis()
        if not differential0 == differential1:
            data = calldata()
            #find latestpricepercoinin USD
            BTCpriceUSD = float(json_data2['data'][0]['last'])
            ETHpriceUSD = float(json_ETHUSD['last'])
            
            #Runs2Dimensional differential analysis
            
            #caches gainpercoin for later printing
            gain = differential1 * (currCapital/ETHpriceUSD)
            
            #this fee is slightly more than the actual fee, but simplifies the 
            #calculation substantially
            fee = 0.002 * (currCapital) * 2
            
            if gain > fee:
                differential = gain - fee
            else: 
                differential = 0
                
            differential0 = differential1
            currCapital += differential
            count += 1
            
            if datacollect == True:
                datahold.append(differential)
                
            print()
            print("Iteration number: %i" %count)
            print("Fees: %f" %fee)
            print("Revenue: %f" %gain)
            print("Profit per Coin: %f" %differential1)
            print("Adjusted profit: %f" %differential)
            print("Current capital: %f" %currCapital)
            print("===============================")
            print()
            time.sleep(6)
        else: time.sleep(6)
        
        writetoExcel("CryptochainData", datahold)
            
    print("Done")