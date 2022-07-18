import pandas as pd
import numpy as np

#1 By index
df = pd.DataFrame([1, 2, 3, 4, 5], index=[100, 29, 234, 1, 150], columns=['A'])
df = df.sort_index()
df = df.sort_index(ascending=False)
print (df)

#2 By values
df = pd.DataFrame({
    'col1': ['A', 'A', 'B', np.nan, 'D', 'C'],
    'col2': [2, 1, 9, 8, 7, 4],
    'col3': [0, 1, 9, 4, 2, 3],
    'col4': ['a', 'B', 'c', 'D', 'e', 'F']
})
#2.1 Sort by column
df = df.sort_values(by=['col1'])

#2.2 Sort by multiple columns: 重新排列-多欄位(排序順序先寫的重要性高)
df = df.sort_values(by=['col1', 'col2'], ascending = [False, True])

#2.3 Sort Descending
df.sort_values(by='col1', ascending=False)

#2.4 Sort Descending: 有NaN的放在前面
df.sort_values(by='col1', ascending=False, na_position='first')