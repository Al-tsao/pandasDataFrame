#載入模組
import pandas as pd
import numpy as np

#載入資料
RawData = { "Day":['9/4', '9/5', '9/6', '9/7', '9/8', '9/9', '9/10', '9/11'],
            "Revnue":[100, 120, 130, 110, 200, 160, 100, 180],
            "Cost":[10.0, 12.0, 13.0, 11.0, 20.0, 16.0, 10.0, 18.0]}

#轉化成DataFrame
df = pd.DataFrame(RawData)
print(df)

#方法一將float轉換成int
df['Cost'] = df['Cost'].astype('int')

#方法二將分類的column轉換成category格式
df['Day'] = df['Day'].astype('category')