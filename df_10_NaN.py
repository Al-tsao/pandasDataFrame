import pandas as pd
import numpy as np

RawData = { "Day":['9/4', '9/5', '9/6', '9/7', '9/8', '9/9', '9/10', '9/11'],
            "Revenue":[100, np.nan, 130, 110, 200, 160, 100, 180],
            "Cost":[10.0, np.nan, 13.0, 11.0, np.nan, 16.0, 10.0, np.nan]}
df = pd.DataFrame(RawData)

#1 使用where: 讓不符合的值變成NaN
mask = df['Day'] != '9/4' 
df.where(mask)

#2 使用dropna(): 只要一個NaN就會整row刪除
df.dropna()

#3 使用dropna(how='all'): 要全部NaN就，才會刪除整個row
df.dropna(how='all')

#4 使用dropna(subset=[]): 可以指定哪個Column中的缺值可以被移除
df = df.dropna(subset=['Revenue'])
print(df)