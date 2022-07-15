import pandas as pd

houses = pd.read_csv('kc_house_data.csv')
houses

# .head() 顯示資料前面幾筆
print(' ')
print('***********head***********')
print('head', houses.head(10)) #數字是要看顯示幾筆資料

# .tail()
print(' ')
print('***********tail***********')
print(houses.tail(10)) #數字是要看顯示幾筆資料

# .columns 返回所有欄位的名稱
print(' ')
print('***********columns***********')
print(houses.columns)

# .shape 顯示資料大小，共幾行幾列
print(' ')
print('***********shape***********')
print(houses.shape)

# .size 看有多少筆資料，就是column x row
print(' ')
print('***********size***********')
print(houses.size)

# .info() 顯示檔案詳細資訊，包含有多少column、有多少Row的資料(不包含nan)、column資料型態
# 其中object是有文字和檔案大小
print(' ')
print('***********info***********')
print(houses.info())

# .describe() 顯示相關敘述統計*
    # 顯示有數據資料相關敘述統計
print(' ')
print('***********describe***********')
print(houses.describe())
    #顯示有文字資料相關敘述統計
print(' ')
print('***********describe***********')
print(houses.describe(include = 'object'))

# .unique() 顯示column中到底有多少個不同的值
print(' ')
print('***********unique***********')
print(houses['date'].unique())

# .dtypes 顯示每一個column的型態
print(' ')
print('***********dtypes***********')
print(houses.dtypes)
