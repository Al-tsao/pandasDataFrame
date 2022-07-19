import pandas as pd
import numpy as np

RawData = { "Day":['9/4', '9/5', '9/6', '9/7', '9/8', '9/9', '9/10', '9/11'],
            "Revenue":[100, 120, 130, 110, 200, 160, 100, 180],
            "Cost":[10.0, 10.0, 13.0, 11.0, 20.0, 16.0, 10.0, 18.0]}
df = pd.DataFrame(RawData)

#1 使用Boolean篩選
#1.1 單一條件
mask = df['Day']=='9/4'

#1.2 多條件篩選
mask = (df['Day'] == '9/11') & ( df['Revenue'] == 180) & (df['Cost'] == 18.0)
df[mask]

#1.3 使用Boolean選到特定的index
i = df[((df['Day'] == '9/4') & ( df['Revenue'] == 100) & (df['Cost'] == 18.0))].index.tolist()
df.loc[i]