#載入模組
import pandas as pd

#載入資料
bond = pd.read_csv("jamesbond.csv", index_col="Film")
bond.sort_index(inplace=True)

#修改遇到問題
directors = bond["Director"]
directors["A View to a Kill"] = "Mister John Glen"
#執行時會遇到這段話-A value is trying to be set on a copy of a slice from a DataFrame
#因為directors其實和原本的bond是有關連的，所以這裡做修改會修改到bond的資料

#修正辦法
directors_copy = bond["Director"].copy()
directors_copy["A View to a Kill"] = "Mister John Glen"