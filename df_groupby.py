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


#groupby - single group single column
sglCol = df.groupby(['A'])['C'].sum() #以A作為分組標準，並且對於C做加總，但不會有C的title出現
print('sglCol', sglCol.reset_index(), sep='\n')
print('============================================')

#groupby - multiple columns
multiCol = df.groupby(['A'])[['C','D']].sum() #以A作為分組標準，並且對於C和D個別做加總，且有C和D的title出現
print('multiCol', multiCol.reset_index(), sep='\n')
print('============================================')

#groupby - multiple groups
multiGroup = df.groupby(['A','B'])['C'].sum() #以A、B作為分組條件，對C做加總
print('multiGroup', multiGroup.reset_index(), sep='\n')
print('============================================')

#multiple functions
multiFunc = df.groupby(['A'])['C'].agg(['mean','sum']) #以A作為分組標準，對C進行平均與加總
print('multiFunc', multiFunc.reset_index(), sep='\n')