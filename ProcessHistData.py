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

def ProcessHistData(strCurrentMnemonic):
    
    strMnemonicDataPath = "/Users/andrejtupikin/pythonfirststeps/GetHistStockData/Data/AllData/15d_60s/" + strCurrentMnemonic + ".csv"
    
    HistData = pd.read_csv(strMnemonicDataPath, skiprows=1)
    start_string = int(str(HistData).find('a14'))
    str_found = [m.start() for m in re.finditer('\n', str(HistData))]
    str_found_dates = [m.start() for m in re.finditer('a14', str(HistData))]
    
    w, h = len(str_found_dates),511;
    
    Matrix = [[0 for x in range(w)] for y in range(h)];
    
    for x in range(0,len(str_found_dates)):
    
        unix_date       = str(HistData)[str_found_dates[x]+1:str_found_dates[x]+11]
        
        Matrix[0][x]    = (datetime.fromtimestamp(int(unix_date)).strftime('%Y-%m-%d %H:%M:%S'))
        
        if (x < len(str_found_dates)-1): 
        
            strCurDateToNextDate = str(HistData)[str_found_dates[x]:str_found_dates[x+1]]
            
        else:
                
            strCurDateToNextDate = str(HistData)[str_found_dates[x]:-1]
        
        strFoundValuesStart = [m.start() for m in re.finditer(',', str(strCurDateToNextDate))]
        strFoundValuesEnd   = [m.start() for m in re.finditer('\n', str(strCurDateToNextDate))]
            
        for y in range(1,len(strFoundValuesStart)+1):
                
            intCurVal = float((strCurDateToNextDate)[strFoundValuesStart[y-1]+1:strFoundValuesEnd[y-1]]);
            
            if (y == len(strFoundValuesStart)):
                
                intNumber = intNumber + 1;
                
            else:
            
                intNumber = int((strCurDateToNextDate)[strFoundValuesEnd[y-1]:strFoundValuesStart[y]]);
            
            Matrix[intNumber][x] = intCurVal;
            
        #print [row[x] for row in Matrix]
                
    return Matrix
            

def firststrategytry(maData):
    
    print maData
    

if __name__ == "__main__":
    
    strMnemonic = "BMW";
    
    maCurrentMnemonicData = ProcessHistData(strMnemonic);
    
    firststrategytry(maCurrentMnemonicData);