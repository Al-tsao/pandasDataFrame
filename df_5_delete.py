import pandas as pd

df = pd.DataFrame([['Jhon',15,'A'],['Anna',19,'B'],['Paul',25,'D']])
df.columns = ['Name','Age','Grade']

#1 刪除特定row
df_dropRow = df.drop([0, 1], axis=0) #刪除index是0和1的row，axis=0是row，axis = 1是column
                                     #可以和後面的filter用法搭配使用
df_dropRow

#2 刪除特定的column
df_dropColumn = df.drop(['Age'], axis=1)
df_dropColumn
