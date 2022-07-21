#載入模組
import pandas as pd
import numpy as np

#載入資料
RawData = { "Day":['9/4', '9/5', '9/6', '9/7', '9/8', '9/9', '9/10', '9/11'],
            "Revnue":[100, 120, 130, 110, 200, 160, 100, 180],
            "Cost":[10.0, 12.0, 13.0, 8.0, 20.0, 16.0, 10.0, 1.0]}

#轉化成DataFrame
df = pd.DataFrame(RawData)

#重新排列-單一欄位
df.sort_values("Revnue", ascending = False, inplace=True)

#重新排列-多欄位(排序順序先寫的重要性高)
df.sort_values(['Cost', 'Revnue'], ascending = [False, True], inplace=True)

#重新排列-回復原狀
df.sort_index(ascending=True, inplace=True)
print(df)
