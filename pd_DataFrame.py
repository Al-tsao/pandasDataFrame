#載入Pandas、numpy模組
import pandas as pd
import numpy as np

#使用Dictionary建立Series
dic = {
    'Year': [2021, 2022, 2023, 2024, 2025],
}
pd_dic = pd.DataFrame(dic)

#自訂index
pd_dic_index = pd.DataFrame(dic, index=['A', 'B', 'C', 'D', 'E'])

#將Series反轉成Dictionary
dic_r = pd_dic.to_dict()

#資料數量
pd_dic.size #看有多少筆資料

#資料形狀
pd_dic.shape #看有多少Row和Column，先Row在Column

#資料index
pd_dic.index #看有甚麼index

#取得特定Row
pd_dic[0:1] #只顯示前兩個Row
test = pd_dic.iloc[1] #列編號按順序由0開始往下，會轉換成Seires型態，title變成index
pd_dic_index.loc['C'] #利用index做篩選，會轉換成Seires型態，title變成index

#取得特定Column
pd_dic["Year"] #方法一
pd_dic.Year #方法一，這種寫法欄位名稱中間不能有間隔
test = pd_dic.columns #返回所有欄位的名稱

#建立新欄位
Revenue = [100, 200, 300, 400, 500]
Cost = [10, 20, 30, 40, 50]
Gross_Margin = [90, 180, 270, 360, 450]
pd_dic['Revenue'] = Revenue #使用列表型態
pd_dic['Cost'] = pd.Series(Cost) #使用Series建立，如果原本的DataFrame有index，則用Seires新增Column也要有index
# print("列表", pd_dic, sep="\n")

#從舊得DataFrame擷取部分columns作為新的DataFrame
pd_dic_new = pd.DataFrame(pd_dic, columns=['Year','Revenue']) #摘取部分column作為新的DataFrame

#集合Series變成DataFrame
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

#資料篩選
#利用row和column篩選
pd_filter = pd_dic.loc[0:1,['Year', 'Revenue']] 
#建立與資料數量對應的布林值列表
condition = [False, True, True, False, False] 
filtered_pd_dic = pd_dic[condition]
#直接用比較運算建立布林值列表
condition2 = pd_dic["Year"] > 2021
filtered2_pd_dic = pd_dic[condition2]

#分組
Group = {
    'Rev': [100, 200, 300, 400],
    'Sales': ['A', 'A', 'B', 'B']
}
pd_gp = pd.DataFrame(Group)
pd_gp = pd_gp.groupby('Sales')
# print(pd_gp.groups)

#分組計算
pd_gp_cal = pd.DataFrame({'A' : ['foo', 'bar', 'foo', 'bar',
                      'foo', 'bar', 'foo', 'foo'],
                   'B' : ['one', 'one', 'two', 'three',
                          'two', 'two', 'one', 'three'],
                   'C' : np.random.randint(1, 10, 8),
                   'D' : np.random.randint(1, 10, 8)})
pd_gp_cal1 = pd_gp_cal.groupby('A').sum() #計算總和
pd_gp_cal2 = pd_gp_cal.groupby(['A','B']).sum() #計算兩群組總和

#計算
pd_gp_cal['Total'] = pd_gp_cal['C']*pd_gp_cal['D']
print(pd_gp_cal)
