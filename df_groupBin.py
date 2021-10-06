#載入模組
import pandas as pd

#Read Data
df = pd.DataFrame({'A':['X','X','Y','Y','Y','Y','Z','Z','Z','Z','Z','Z'],
                   'B':['one','one','two','two','three','three','four','four','five','five','six','six'],
                   'C':[1,2]*6,
                   'D':[3,4]*6})

#讀取column中的title
title = pd.DataFrame({'Title': df.columns})
print('Title名稱', title, sep='\n')
print('============================================')

#分組取名
df['bins'] = pd.cut(df['C'], bins=2, labels=('甲','乙'))
print(df)
