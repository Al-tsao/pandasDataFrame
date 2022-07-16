import pandas as pd

houses = pd.read_csv('kc_house_data.csv')
houses

#1 .head() 顯示資料前面幾筆
houses.head(10) #數字是要看顯示幾筆資料

#2 .tail()
houses.tail(10)#數字是要看顯示幾筆資料

#3 .columns 返回所有欄位的名稱
houses.columns

#4 .shape 顯示資料大小，共幾行幾列
houses.shape

#5 .size 看有多少筆資料，就是column x row
houses.size

#6 .info() 顯示檔案詳細資訊，包含有多少column、有多少Row的資料(不包含nan)、column資料型態
# 其中object是有文字和檔案大小
houses.info()

#7 .describe() 顯示相關敘述統計
#7.1 顯示有數據資料相關敘述統計
houses.describe()
#7.2 顯示有文字資料相關敘述統計
houses.describe(include = 'object')

#8 .unique() 顯示column中到底有多少個不同的值
houses['date'].unique()

#9 .dtypes 顯示每一個column的型態
houses.dtypes
