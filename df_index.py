#載入模組
import pandas as pd

#載入資料
bond = pd.read_csv("jamesbond.csv")

#設定index
bond.set_index(keys='Film', inplace=True)

#回覆index
bond.reset_index()