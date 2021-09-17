#載入Pandas模組
import pandas as pd

#使用Dictionary建立Series
dic = {
    'Year': [2021, 2022, 2023, 2024, 2025],
}
pd_dic = pd.DataFrame(dic)

#自訂index
pd_dic = pd.DataFrame(dic, index=['A', 'B', 'C', 'D', 'E'])

#將Series反轉成Dictionary
dic_r = pd_dic.to_dict()

#資料數量
pd_dic.size #看有多少筆資料

#資料形狀
pd_dic.shape #看有多少Row和Column，先Row在Column

#取得特定Row
pd_dic[0:1] #只顯示前兩個Row
test = pd_dic.iloc[1] #列編號按順序由0開始往下，會轉換成Seires型態，title變成index
pd_dic.loc['C'] #利用index做篩選，會轉換成Seires型態，title變成index

#取得特定Column
pd_dic["Year"] #方法一
pd_dic.Year #方法一，這種寫法欄位名稱中間不能有間隔
test = pd_dic.columns #返回所有欄位的名稱

#建立新欄為
Revenue = [100, 200, 300, 400, 500]
Cost = [10, 20, 30, 40, 50]
Gross_Margin = [90, 180, 270, 360, 450]
pd_dic['Revenue'] = Revenue #使用列表型態
pd_dic['Cost'] = pd.Series(Cost, index=['A', 'B', 'C', 'D', 'E']) #使用Series建立，如果原本的DataFrame有index，則用Seires新增Column也要有index
print("列表", pd_dic, sep="\n")