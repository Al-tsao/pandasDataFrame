"""
原本資料結構:
           A         B         C
0   0.658625 -0.864408 -1.331512
1   0.796499 -1.204141  0.911970
2  -1.175742 -0.250042 -0.416713
3  -0.794052  0.293647 -0.202033
4  -0.238233 -0.003650  0.558622

轉換資料結構:
        Value Column Name  Index
0   -1.820150           A      0
1    0.856483           B      0
2   -0.391973           C      0
3   -1.062139           A      1
4    0.250473           B      1
"""

#載入模組
import numpy as np
import pandas as pd

#載入資料
df = pd.DataFrame(np.random.randn(100, 3), columns = ['A', 'B', 'C'])
df = df.stack().reset_index().iloc[:, ::-1]
df.columns = ['Value', 'Column Name', 'Index']
print(df)