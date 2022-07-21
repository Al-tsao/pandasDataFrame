import pandas as pd
import numpy as np

#1. 使用Dictionary建立Series
dic = {
    'Year': [2021, 2022, 2023, 2024, 2025],
}
pd_dic = pd.DataFrame(dic)

#2. 使用Dictionary建立DataFrame
RawData = { 
    "Day":['9/4', '9/5', '9/6', '9/7', '9/8', '9/9', '9/10', '9/11'],
    "Revnue":[100, 120, 130, 110, 200, 160, 100, 180],
    "Cost":[10.0, 12.0, 13.0, 11.0, 20.0, 16.0, 10.0, 18.0]
}
df = pd.DataFrame(RawData)
print(df)

data = pd.DataFrame(np.arange(16).reshape(4,4), index = list('abcd'), columns = list('ABCD'))
print(data)
