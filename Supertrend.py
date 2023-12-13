import pandas as pd
import numpy as np
from datetime import datetime
import yfinance as yf
import math
import matplotlib.pyplot as plt

import csv  #importing the library



def Supertrend(df, atr_period, multiplier):
    
    high = df['High']
    low = df['Low']
    close = df['Close']
    
    print(high, low, close)
    
    '''
    print(df)
    print("--------------------------------")
    high = df[1]
    low = df[2]
    close = df[3]
    
    print("--------------high low close------------------")
    print(high, low, close)
    '''
        
    # calculate ATR
    price_diffs = [high - low, 
                   high - close.shift(), 
                   close.shift() - low]
    true_range = pd.concat(price_diffs, axis=1)
    true_range = true_range.abs().max(axis=1)
    # default ATR calculation in supertrend indicator
    atr = true_range.ewm(alpha=1/atr_period,min_periods=atr_period).mean() 
    # df['atr'] = df['tr'].rolling(atr_period).mean()
    
    # HL2 is simply the average of high and low prices
    hl2 = (high + low) / 2
    # upperband and lowerband calculation
    # notice that final bands are set to be equal to the respective bands
    final_upperband = upperband = hl2 + (multiplier * atr)
    final_lowerband = lowerband = hl2 - (multiplier * atr)
    
    # initialize Supertrend column to True
    supertrend = [True] * len(df)
    
    for i in range(1, len(df.index)):
        curr, prev = i, i-1
        
        # if current close price crosses above upperband
        if close[curr] > final_upperband[prev]:
            supertrend[curr] = True
        # if current close price crosses below lowerband
        elif close[curr] < final_lowerband[prev]:
            supertrend[curr] = False
        # else, the trend continues
        else:
            supertrend[curr] = supertrend[prev]
            
            # adjustment to the final bands
            if supertrend[curr] == True and final_lowerband[curr] < final_lowerband[prev]:
                final_lowerband[curr] = final_lowerband[prev]
            if supertrend[curr] == False and final_upperband[curr] > final_upperband[prev]:
                final_upperband[curr] = final_upperband[prev]

        # to remove bands according to the trend direction
        if supertrend[curr] == True:
            final_upperband[curr] = np.nan
        else:
            final_lowerband[curr] = np.nan
    
    return pd.DataFrame({
        'Supertrend': supertrend,
        'Final Lowerband': final_lowerband,
        'Final Upperband': final_upperband
    }, index=df.index)
    
    
atr_period = 7
atr_multiplier = 3.0
file_name = "banknifty_supertrend.csv"


df = pd.read_csv("banknifty.csv", delimiter=",")

'''
with open("banknifty.csv") as csvFile:   #open the file
  df_1 = csv.reader(csvFile, delimiter=',') 
  header = []
  df = next(df_1)
  header #read the data
  
  for row in df:   #loop through each row
    print(row[0])   #print the data
    
csvFile.close()   #close the file


symbol = 'AAPL'
#df = yf.download(symbol, start='2023-07-10')
print("--------------type------------------")

print(type (yf.download(symbol, start='2023-07-10')))


with open("apple.txt", "a") as f:
    f.write(df)
'''
supertrend = Supertrend(df, atr_period, atr_multiplier)

print(supertrend)

df_1 = df.join(supertrend)

print(df_1)

#df.to_csv(file_name, sep='\t', index=False)
df_1.to_csv(file_name)



