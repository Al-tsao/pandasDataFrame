#載入模組
import pandas as pd
import datetime as dt

#pd.to_datetime: 把資料轉換成pandas的時間格式
dates = pd.DataFrame({'time': ['2021/01/01', '2021/12/31', 'Atome']})
dates['timeFormant']  = pd.to_datetime(dates['time'], errors = 'coerce') 
#errors: 如果沒有設定成coerce則在array中遇到錯誤的時間格式就會抱錯，若使用coerce就會把資料轉乘NaT

print(dates.info())
