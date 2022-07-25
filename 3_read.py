import pandas as pd
import numpy as np

data = pd.DataFrame(np.arange(16).reshape(4,4), index = list('abcd'), columns = list('ABCD'))

# 提取DataFrame中特定位置
#1 取索引為'a'的row
data.loc['a'] #利用index做篩選，會轉換成Seires型態，title變成index
data.iloc[0] #列編號按順序由0開始往下，會轉換成Seires型態，title變成index

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

#7 建立新欄位
dic = {
    'Year': [2021, 2022, 2023, 2024, 2025],
}
pd_dic = pd.DataFrame(dic)
Revenue = [100, 200, 300, 400, 500]
Cost = [10, 20, 30, 40, 50]
Gross_Margin = [90, 180, 270, 360, 450]
pd_dic['Revenue'] = Revenue #使用列表型態
pd_dic['Cost'] = pd.Series(Cost) #使用Series建立，如果原本的DataFrame有index，則用Seires新增Column也要有index
# print("列表", pd_dic, sep="\n")

#8 從舊得DataFrame擷取部分columns作為新的DataFrame
pd_dic_new = pd.DataFrame(pd_dic, columns=['Year','Revenue']) #摘取部分column作為新的DataFrame

#9 集合Series變成DataFrame
#方法一
dataA = {'A':['a1','a2','a3']}
dataB = {'B':['b1','b2','b3']}
dataC = {'C':['c1','c2','c3']}
data1 = pd.Series(dataA['A'])
data2 = pd.Series(dataB['B'])
data3 = pd.Series(dataC['C'])
SeriesToDataFrame = pd.DataFrame([data1,data2,data3], index = ['A','B','C'])
# print(SeriesToDataFrame)
SeriesToDataFrame = SeriesToDataFrame.T #做反轉
# print(SeriesToDataFrame)
#方法二
col = ['class','name','hbd']
data = [['class0', 'user0', '1993-10-01'],
        ['class0', 'user1', '1992-10-02'],
        ['class1', 'user2', '1990-10-01'],
        ['class2', 'user3', '1983-10-03'],
        ['class1', 'user4', '1991-10-02'],
        ['class0', 'user5', '2001-10-03']]
frame = pd.DataFrame(data,columns=col)