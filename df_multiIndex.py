import pandas as pd

bigmac = pd.read_csv('bigmac.csv', parse_dates=['Date']) #使用parse_dates將str的文字轉為時間格式

#set_index
bigmac.set_index(keys=['Date', 'Country'], inplace=True) # 以Date開始往下做分組

#sort_index
bigmac.sort_index(inplace = True) 

#index
bigmac.index #回傳一個multiIndex的陣列