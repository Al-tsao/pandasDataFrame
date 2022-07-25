"""
效果跟filter一樣，雖然簡潔但是限制比較多，column名稱不能有空格，裡面要篩選的文字內容還要再用'或者"包起來
"""

#載入模組
import numpy as np
import pandas as pd

#載入資料
df = pd.DataFrame(np.random.randn(100, 3), columns = ['A', 'B', 'C'])
df = df.stack().reset_index().iloc[:, ::-1]
df.columns = ['Value', 'Column_Name', 'Index']
#使用query
df1 =df.query("Column_Name == 'A'") #篩選的A一定要用''，包起來不然會報錯
#使用filter
mask = df['Column_Name'] == 'A'
df2 = df[mask]