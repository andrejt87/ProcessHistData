import urllib
import requests
import time, threading, sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mt
import json
import os
import regex as re
from googlefinance import getQuotes
from datetime import datetime
from time import gmtime, strftime

def ProcessHistData():

    HistData = pd.read_csv('/Users/andrejtupikin/pythonfirststeps/GetHistStockData/Data/VOW.csv', skiprows=1)
    start_string = int(str(HistData).find('a14'))
    str_found = [m.start() for m in re.finditer('\n', str(HistData))]
    
    array = []
    
    for x in range(9, len(str_found)):
        
        delta_string = str(HistData)[str_found[x-1]+1:str_found[x]]
        
        if not delta_string == "]":
        
            start = delta_string.find(',')
        
            array.append(float(delta_string[start+1:]))
        
            plt.plot(array)
            plt.pause(0.0001)
            plt.cla()
    plt.show()
        
    #print string[166:-1].find("\n")
    #print str_found[166:166+38]

if __name__ == "__main__":
    ProcessHistData()
    
    