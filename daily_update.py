# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 23:30:59 2019

@author: Win10
"""

import datetime
import requests
from io import StringIO
import pandas as pd
Today = datetime.date.today()
time_f = Today.strftime("%Y%m%d")
df_final = pd.DataFrame(columns=[2,3,4,5,6,7,8,9,10,11,12,13])
for i in range(7):
    Day = Today - datetime.timedelta(days = i)
    time_y = int(Day.strftime("%Y"))
    time_m = int(Day.strftime("%m"))
    time_d = int(Day.strftime("%d"))
    payload ={
    'queryType': '1',
    'doQuery': '1',
    'queryDate': str(time_y)+"/"+str(time_m)+"/"+str(time_d),
    }
    #print(payload)
    r = requests.post('https://www.taifex.com.tw/cht/3/futAndOptDate' , data = payload)
    r.encoding = 'gbk'.strip()
    dfs = pd.read_html(StringIO(r.text))
    try:
        dfs[5:6][0].columns = ['']*len(dfs[5:6][0].columns)
        df = dfs[5:6][0][2:3]
        #print(df)
        
        df.columns=[1,2,3,4,5,6,7,8,9,10,11,12,13]
        df[14] = str(time_y)+'/'+str(time_m)+'/'+str(time_d)
        df1 = df[[2,3,4,5,6,7,8,9,10,11,12,13,14]]
        df1 = df1.set_index(14)
        #print(df1)
        df_final = df_final.append(df1)
    except:
        pass
df_final = df_final.iloc[::-1]
df_final.to_csv(time_f+'11234.csv')