#載入模組
import pandas as pd

#載入資料
bond = pd.read_csv("jamesbond.csv", index_col='Film')

#整理index-整理過後的index在找尋時速度會比較快
bond.sort_index(inplace=True)