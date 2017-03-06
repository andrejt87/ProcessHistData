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

    HistData = pd.read_csv('/Users/andrejtupikin/pythonfirststeps/GetHistStockData/Data/AllData/15d_60s/BMW.csv', skiprows=1)
    start_string = int(str(HistData).find('a14'))
    str_found = [m.start() for m in re.finditer('\n', str(HistData))]
    str_found_dates = [m.start() for m in re.finditer('a14', str(HistData))]
    
    w, h = len(str_found_dates),3;
    Matrix = [[0 for x in range(w)] for y in range(h)]
    
    for x in range(0,len(str_found_dates)):
    
        unix_date       = str(HistData)[str_found_dates[x]+1:str_found_dates[x]+11]
        
        Matrix[0][x]    = (datetime.fromtimestamp(int(unix_date)).strftime('%Y-%m-%d %H:%M:%S'))

        if not (x == len(str_found_dates)-1):
            
            str_found = [m.start() for m in re.finditer('\n', str(HistData))]
            
            #Schleife über str_found
            
            
            strStingCurDateToEnd    = str(HistData)[str_found_dates[x]:-1]
            
            intStartValDig          = int(strStingCurDateToEnd.find(','))
            intEndValDig            = int(strStingCurDateToEnd.find('\n'))
            
            intCurVal               = float(str(strStingCurDateToEnd)[intStartValDig+1:intEndValDig])
            
            
    
    
    #data = str(HistData)[str_found_dates[0]+12:str_found_dates[1]]
        
    #print string[166:-1].find("\n")
    #print str_found[166:166+38]

if __name__ == "__main__":
    ProcessHistData()
    
    