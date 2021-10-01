#載入Pandas、numpy模組
import pandas as pd
import numpy as np

#分組計算
pd_gp_cal = pd.DataFrame({'A' : ['X', 'X', 'Y', 'Y',
                      'Y', 'Y', 'Z', 'Z', 'Z', 'Z', 'Z', 'Z'],
                   'B' : ['one', 'one', 'two', 'two',
                          'two', 'two', 'three', 'three', 'three', 'three', 'three', 'three'],
                   'C' : [1,2]*6})
pd_gp_cal2 = pd_gp_cal.groupby(['A','B']).sum() #計算兩群組總和
print(pd_gp_cal2)
