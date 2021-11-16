#載入模組
import pandas as pd

#資料載入
dataRangeD = pd.date_range(start = '2021/09/01', end = '2021/9/30', freq = '1D') #freq = '1D': 間格是以1天為單位
dates = pd.DataFrame(dataRangeD, columns = ['Date'])
dates['Data'] = [1]*dates.shape[0]
dates.insert(2, "Day of Week", dates['Date'].dt.day_name())

print(dates)