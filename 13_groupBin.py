"""
利用欄位裡的代號重新給上新的標籤，像是原本欄位裡面有1和2，可以利用1和2新增加一個欄位，生成男或女
"""

#載入模組
import pandas as pd

#Read Data
df = pd.DataFrame({'A':['X','X','Y','Y','Y','Y','Z','Z','Z','Z','Z','Z'],
                   'B':['one','one','two','two','three','three','four','four','five','five','six','six'],
                   'C':[1,2,3,2,1,1,1,1,1,1,1,1],
                   'D':[3,4]*6})

#讀取column中的title
title = pd.DataFrame({'Title': df.columns})
print('Title名稱', title, sep='\n')
print('============================================')

#分組取名
df['bins'] = pd.cut(df['C'], bins=3, labels=('甲','乙','丙'))
print(df)
