"""
Copyright Aaron E. Lebel
All Rights Reserved

This module does not include sensitive information
"""

###############################################################
#Import statements
###############################################################

import time
import math
import urllib.parse
import requests

###############################################################
#Cex.IO Connections
###############################################################\

#establishes a connection to CEX.IO
main = "https://cex.io/api/"
ticker_ext = "tickers/USD/BTC"
ticker_ext2 = "tickers/USD/EUR/RUB/BTC"

graph_url = "https://cex.io/api/ohlcv/hd/20160228/BTC/USD"

ticker_url = main + ticker_ext
ticker_url2 = main + ticker_ext2


#############################################################
#currency converter data
#############################################################

currency_url = 'http://apilayer.net/api/'

full_currency_url= """
http://apilayer.net/api/live?access_key=b4266d5d05849f9c657069bae3933220&currencies=EUR,%20RUB&source=USD&format=1
"""

USDtoEUR = requests.get(full_currency_url).json()
(USDtoEUR['quotes']['USDEUR'])


#############################################################
#currency conversion functions
#############################################################

#returns current USD to EURO rate
def currentUSDtoEUR():
    USDtoEUR = requests.get(full_currency_url).json()
    final = (USDtoEUR['quotes']['USDEUR'])
    return final
    
#returns current EURO to USD rate
def currentEURtoUSD():
    USDtoEUR = requests.get(full_currency_url).json()
    Inverse  = (USDtoEUR['quotes']['USDEUR'])
    final = 1 / inverse
    return final

#quickly converts from USD to Euros
def convertUSDtoEUR(USDinput, USDtoEURconversion_rate):
    final = USDinput * USDtoEURconversion_rate
    return final

#quickly converts from Euros to USD
def convertEURtoUSD(EURinput, EURtoUSDconversion_rate):
    final = EURinput * EURtoUSDconversion_rate
    return final
    


#############################################################
# Cex.IO Data on conversion from fiat to crypto
#############################################################
           #Commented (#) are currently unusuable#

#opens the databases
json_data1 = requests.get(ticker_url).json()
json_data2 = requests.get(ticker_url2).json()
#json_timeseries = requests.get(graph_url).json()

#BTC to fiat conversions
json_BTCUSD = json_data1['data'][0]
json_BTCEUR = json_data2['data'][4]
json_BTCRUB = json_data2['data'][8]

#Etherium to fiat conversions
json_ETHUSD = json_data1['data'][1]
json_ETHEUR = json_data2['data'][5]
# json_ETHRUB = json_data2['data'][]

#Bitcoin Cash to fiat conversions
json_BCHUSD = json_data1['data'][2]
json_BCHEUR = json_data2['data'][6]
# json_BHCRUB = json_data2['data'][] 

#Crypto to crypto conversions
json_ETHBTC = json_data1['data'][4]
json_BCHBTC = json_data1['data'][5]
# json_DASHBTC = json_data1['data'][6]
# json_GHSBTC = json_data1['data'][7]


###############################################################
#Helper functions
###############################################################

#returns a list of data related to conversion rates
def calldata():
    #opens the databases
    json_data1 = requests.get(ticker_url).json()
    json_data2 = requests.get(ticker_url2).json()
    #json_timeseries = requests.get(graph_url).json()
    
    #BTC to fiat conversions
    json_BTCUSD = json_data1['data'][0]
    json_BTCEUR = json_data2['data'][4]
    json_BTCRUB = json_data2['data'][8]
    
    #Etherium to fiat conversions
    json_ETHUSD = json_data1['data'][1]
    json_ETHEUR = json_data2['data'][5]
    #json_ETHRUB = json_data2['data'][]
    
    #Bitcoin Cash to fiat conversions
    json_BCHUSD = json_data1['data'][2]
    json_BCHEUR = json_data2['data'][6]
    # json_BHCRUB = json_data2['data'][] 
    
    #Crypto to crypto conversions
    json_ETHBTC = json_data1['data'][4]
    json_BCHBTC = json_data1['data'][5]
    # json_DASHBTC = json_data1['data'][6]
    # json_GHSBTC = json_data1['data'][7]
    
    return [json_BTCUSD, json_BTCEUR, json_BTCRUB,
            json_ETHUSD, json_ETHEUR,
            json_BCHUSD, json_BCHEUR,
            json_ETHBTC, json_BCHBTC]