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
    
    w, h = len(str_found_dates),510;
    
    Matrix = [[0 for x in range(w)] for y in range(h)]
    
    for x in range(0,len(str_found_dates)):
    
        unix_date       = str(HistData)[str_found_dates[x]+1:str_found_dates[x]+11]
        
        Matrix[0][x]    = (datetime.fromtimestamp(int(unix_date)).strftime('%Y-%m-%d %H:%M:%S'))
        
        if (x < len(str_found_dates)-1): 
        
            strCurDateToNextDate = str(HistData)[str_found_dates[x]:str_found_dates[x+1]]
            
        else:
                
            strCurDateToNextDate = str(HistData)[str_found_dates[x]:-1]
        
        strFoundValuesStart = [m.start() for m in re.finditer(',', str(strCurDateToNextDate))]
        strFoundValuesEnd   = [m.start() for m in re.finditer('\n', str(strCurDateToNextDate))]
        
        print len(strFoundValuesStart)
            
        for y in range(1,len(strFoundValuesStart)+1):
                
            intCurVal = float((strCurDateToNextDate)[strFoundValuesStart[y-1]+1:strFoundValuesEnd[y-1]]);
            
            Matrix[y][x] = intCurVal;
                
    print Matrix
            
    
    
    #data = str(HistData)[str_found_dates[0]+12:str_found_dates[1]]
        
    #print string[166:-1].find("\n")
    #print str_found[166:166+38]

if __name__ == "__main__":
    ProcessHistData()
    
    