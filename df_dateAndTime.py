#載入模組
import pandas as pd

from pandas.core.indexes.period import period_range

#pd.to_datetime: 把資料轉換成pandas的時間格式
dates = pd.DataFrame({'time': ['2021/01/01', '2021/12/31', 'Atome']})
dates['timeFormant']  = pd.to_datetime(dates['time'], errors = 'coerce', format = '%Y/%m/%d') 
#errors: 如果沒有設定成coerce則在array中遇到錯誤的時間格式就會報錯，若使用coerce就會把資料轉乘NaT
#format: pandas可以自己判定時間格式，但是有些時間格式太詭異這時候可以用format告訴pandas格式是如何

#pd.data_range: 建立一段時間序列
#利用區間建立時間序列，序列的格式是DataFrame，如果要使用dt方法要先轉成Series
dataRangeD = pd.date_range(start = '2021/01/01', end = '2021/12/31', freq = '1D') #freq = '1D': 間格是以1天為單位
dataRangeB = pd.date_range(start = '2021/01/01', end = '2021/12/31', freq = 'B') #freq = 'B': 只取禮拜一到禮拜五
dataRangeW = pd.date_range(start = '2021/01/01', end = '2021/12/31', freq = 'W-MON') #freq = 'W-MON': 只取禮拜一
dataRangeH = pd.date_range(start = '2021/01/01', end = '2021/12/31', freq = '1H') #freq = '1H': 間隔是以1小時為單位
dataRangeM = pd.date_range(start = '2021/01/01', end = '2021/12/31', freq = 'M') #freq = 'M': 只取每個月的最後一天
dataRangeMS = pd.date_range(start = '2021/01/01', end = '2021/12/31', freq = 'MS') #freq = 'MS': 只取每個月的第一天
dataRangeA = pd.date_range(start = '2021/01/01', end = '2030/01/01', freq = 'A') #freq = 'A': 只取每一年的最後一天
#利用指定數量建立時間序列-從頭往後推
dataRangePeridStartD = pd.date_range(start = '2012/09/4', periods = 8, freq = '1D') # period: 要取多少的數量
#利用指定數量建立時間序列-從尾往前推
dataRangePeridEndD = pd.date_range(end = '2012/09/11', periods = 8, freq = '1D') # period: 要取多少的數量

#dt使用
#dt和str一樣，使用這個方法後可以用dt中的attributes和methods
dataRangeD = pd.DataFrame(dataRangeD, columns = ['Time'])
dataRangeD['Time'].dt.day
dataRangeD['Time'].dt.isocalendar().week #看是第幾周
dataRangeD['Time'].dt.month
dataRangeD['Time'].dt.day_name()
dataRangeD['Time'].dt.month_name()

