#載入模組
import pandas as pd

#載入資料
week1 = pd.read_csv('Restaurant - Week 1 Sales.csv')
week2 = pd.read_csv('Restaurant - Week 2 Sales.csv')
customers = pd.read_csv('Restaurant - Customers.csv')
foods = pd.read_csv('Restaurant - Foods.csv')

#pd.concat: 直接將兩張表連結在一起
sales = pd.concat(objs = [week1, week2], ignore_index = True) #ignore_index = True: 捨棄原本的index讓index重新自動生成，不然0~249的index會重複兩次
sales = pd.concat(objs = [week1, week2], keys = ['Week 1', 'Week 2']) #keys: 建立雙重index
sales.loc[('Week 1', 240), ['Customer ID', 'Food ID']] #使用loc來找到雙重index的目標

#merge-inner join: 取聯集，如果ID有重複，那新的join也會重複
merged = week1.merge(week2, how = 'inner', on = 'Customer ID', suffixes = ['-Week 1', '-Week 2']) #how = inner: 用交集取
merged = week1.merge(week2, how = 'inner', on = ['Customer ID', 'Food ID']) #on = []: 使用多個columns取交集

#merge-outer join: 取交集，如果ID有重複，那新的join也會重複
merged = week1.merge(week2, how = 'outer', on = 'Customer ID', suffixes = ['-Week 1', '-Week 2'], indicator = True)
#indicator = True: 最後新增一個colmn來顯示交集的資料是從那個table來

#merge-outer join: 取差集
merged = week1.merge(week2, how = 'outer', on = 'Customer ID', suffixes = ['-Week 1', '-Week 2'], indicator = True)
mask = merged['_merge'].isin(['left_only', 'right_only'])
merged[mask]

#merge-left join: 以左邊的table中的某些欄位為基礎，撈取右邊報表相對對映的資料
merged = week1.merge(foods, how = 'left', on = 'Food ID')
print(merged)
