import pandas as pd
import numpy as np

data = pd.DataFrame(np.arange(16).reshape(4,4), index = list('abcd'), columns = list('ABCD'))

# 提取DataFrame中特定位置
#1 取索引為'a'的row
data.loc['a']
data.iloc[0]

#2 取A和D的column
data.loc[:,['A', 'D']]
data.iloc[:,[0, 3]]

#3 取特定index和column
data.loc[['a','b'],['A','B']]
data.iloc[[0,1],[0,1]]

#4 取所有值
data.loc[:,:]
data.iloc[:,:]

#5 跳著選
data.iloc[:,::2] 
#start:stop:step ref:https://stackoverflow.com/questions/509211/understanding-slice-notation

#6 反過來選
data.iloc[:,::-1] #start:stop:step