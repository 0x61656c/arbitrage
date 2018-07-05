"""

Copyright Aaron E. Lebel
All Rights Reserved

This module does not include sensitive information

"""

#############################################################
#import statements
##UseSD of S&P for problemset 4 in global electronic markets
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
#Main
#############################################################

def main():
    t0 = time.time()
    #ArbitraryLoopingSimulation(0,4,100,1.18)
    #ArbitraryStaticSimulation(0,4,100,1.18)
    #repeatedStaticSimulation(0,4,100,1.18)
    DataBasedRepeatedStaticSimulation(0,4,100,1.16, True, 25)
    #DataBasedRepeatedStaticSimulation(0,4,100,1.18,True,1)
    t1 = time.time()
    print("Time taken: %f" %(t1-t0) + " seconds")
    
main()