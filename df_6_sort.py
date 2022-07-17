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