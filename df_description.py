#載入模組
import pandas as pd
import numpy as np

#載入資料
RawData = { "Day":['9/4', '9/5', '9/6', '9/7', '9/8', '9/9', '9/10', '9/11'],
            "Revnue":[100, 120, 130, 110, 200, 160, 100, 180],
            "Cost":[10.0, 12.0, 13.0, 11.0, 20.0, 16.0, 10.0, 18.0]}

#轉化成DataFrame
df = pd.DataFrame(RawData)

#顯示資料前面幾筆
head = df.head(1) #數字是要看顯示幾筆資料

#顯示資料後面幾筆
tail = df.tail(1) #數字是要看顯示幾筆資料

#顯示資料title
title = {'Title': df.columns}
title = pd.DataFrame(title)

#顯示資料大小，共幾行幾列
df.shape

#顯示檔案詳細資訊，包含有多少column、有多少Row的資料(不包含nan)、column資料型態，其中object是有文字和檔案大小
df.info()

#顯示有數據資料相關敘述統計
df.describe()

#顯示每一個column的型態
df.dtypes

#顯示column中到底有多少個不同的值
df['Day'].unique()