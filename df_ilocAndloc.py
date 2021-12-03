# 載入模組
import numpy as np
import pandas as pd

#創建資料
data = pd.DataFrame(np.arange(16).reshape(4,4), index = list('abcd'), columns = list('ABCD'))

"""
結果如下
    A   B   C   D
a   0   1   2   3
b   4   5   6   7
c   8   9  10  11
d  12  13  14  15
"""

#取索引為'a'的row
data.loc['a']
data.iloc[0]

#取'A'的column
data.loc[:,['A']]
data.iloc[:,[0]]

#取特定index和column
data.loc[['a','b'],['A','B']]
data.iloc[[0,1],[0,1]]

#取所有值
data.loc[:,:]
data.iloc[:,:]

#跳著選
data.iloc[:,::2] #start:stop:step ref:https://stackoverflow.com/questions/509211/understanding-slice-notation

#反過來選
data.iloc[:,::-1] #start:stop:step
