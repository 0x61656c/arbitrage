"""
Copyright Aaron E. Lebel
All Rights Reserved

This module does not include sensitive information
"""

#############################################################
#import statements
#############################################################

#builtin packages
import time
import math
import urllib.parse
import requests

#Custom packages
from CryptochainFinancialTools import *
from CryptochainDataTools import *

#############################################################
#currency converter info
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

#arbitrary conversion formula from base currency to secondary 
def convertCurr1toCurr2(curr1Input, conversionrate):
    final = curr1Input * conversionrate
    return final

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