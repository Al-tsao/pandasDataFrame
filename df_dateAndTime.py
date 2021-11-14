#載入模組
import pandas as pd
import datetime as dt

from pandas.core.indexes.period import period_range

#pd.to_datetime: 把資料轉換成pandas的時間格式
dates = pd.DataFrame({'time': ['2021/01/01', '2021/12/31', 'Atome']})
dates['timeFormant']  = pd.to_datetime(dates['time'], errors = 'coerce') 
#errors: 如果沒有設定成coerce則在array中遇到錯誤的時間格式就會抱錯，若使用coerce就會把資料轉乘NaT

#pd.data_range: 建立一段時間序列
dataRangeD = pd.date_range(start = '2021/01/01', end = '2021/12/31', freq = '1D') #freq = '1D': 間格是以1天為單位
dataRangeB = pd.date_range(start = '2021/01/01', end = '2021/12/31', freq = 'B') #freq = 'B': 只取禮拜一到禮拜五
dataRangeW = pd.date_range(start = '2021/01/01', end = '2021/12/31', freq = 'W-MON') #freq = 'W-MON': 只取禮拜一
dataRangeH = pd.date_range(start = '2021/01/01', end = '2021/12/31', freq = '1H') #freq = '1H': 間隔是以1小時為單位
dataRangeM = pd.date_range(start = '2021/01/01', end = '2021/12/31', freq = 'M') #freq = 'M': 只取每個月的最後一天
dataRangeMS = pd.date_range(start = '2021/01/01', end = '2021/12/31', freq = 'MS') #freq = 'MS': 只取每個月的第一天
dataRangeA = pd.date_range(start = '2021/01/01', end = '2030/01/01', freq = 'A') #freq = 'A': 只取每一年的最後一天

dataRangePeridD = pd.date_range(start = '2012/09/09', periods = 3, freq = '1D') # period: 要取多少的數量




print(dataRangePeridD)
