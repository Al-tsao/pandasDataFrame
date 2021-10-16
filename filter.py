#載入模組
import pandas as pd

#載入資料
RawData = { "Day":['9/4', '9/5', '9/6', '9/7', '9/8', '9/9', '9/10', '9/11'],
            "Revenue":[100, 120, 130, 110, 200, 160, 100, 180],
            "Cost":[10.0, 10.0, 13.0, 11.0, 20.0, 16.0, 10.0, 18.0]}

#轉化成DataFrame
df = pd.DataFrame(RawData)


#使用Boolean-選到特定的index
i = df[((df['Day'] == '9/11') & ( df['Revenue'] == 180) & (df['Cost'] == 18.0))].index.tolist()
print(i)

#使用isin
mask_isin = df['Day'].isin(['9/4', '9/11'])

#使用between
mask_bet = df['Revenue'].between(160, 200)

#使用dublicated
mask_dupl = df['Cost'].duplicated()
