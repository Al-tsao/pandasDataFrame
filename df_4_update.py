import pandas as pd
import numpy as np

data = pd.DataFrame(np.arange(16).reshape(4,4), index = list('abcd'), columns = list('ABCD'))

#1 修改特定的row: 修改'a'的row
data.loc['a'] = ['a.1', 'a.2', 'a.3', 'a.4']
data.iloc[0] = ['a.1', 'a.2', 'a.3', 'a.4']

#2 修改特定的column: 修改'A'的column
data.loc[:,['A']] = ['A.1', 'A.2', 'A.3', 'A.4']
data.iloc[:,[0]] = ['A.1', 'A.2', 'A.3', 'A.4']

#3 修改Title
data.columns = ['W', 'X', 'Y', 'Z']

#4 插入特定的row 
#4.1 插入到最後一個row後面
dataAdd = pd.DataFrame(np.arange(4).reshape(1,4), index = list('e'), columns = list('WXYZ'))
dataAdd = data.append(dataAdd)

#4.2 插入到指定row後面
#可以先插入到最後一個row後面，然後排序

#5 插入特定column
#5.1 插入到最後一column之後
data['E'] = ['E.1', 'E.2', 'E.3', 'E.4']

#5.2 插入到指定column後面
data['F'] = ['F.1', 'F.2', 'F.3', 'F.4']
new_cols = ['W', 'F', 'Z', 'X', 'E', 'Y']
data = data[new_cols]
#使用insert來完成
df = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
df.insert(1, "newcol", [99, 99])