#載入模組
import pandas as pd

#Read Data
df = pd.DataFrame({'A':['X','X','Y','Y','Y','Y','Z','Z','Z','Z','Z','Z'],
                   'B':['one','one','two','two','two','two','three','three','three','three','three','three'],
                   'C':[1,2]*6,
                   'D':[3,4]*6})

#讀取column中的title
title = pd.DataFrame({'Title': df.columns})
print('Title名稱', title, sep='\n')
print('============================================')


#groupby - single group single column
sglCol = df.groupby(['A'])['C'].sum() #將A分組，並且對於C做加總，但不會有C的title出現
print('sglCol', sglCol.reset_index(), sep='\n')
print('============================================')

#groupby - multiple columns
multiCol = df.groupby(['A'])[['C','D']].sum() #將A分組，並且對於C和D個別做加總，且有C和D的title出現
print('multiCol', multiCol.reset_index(), sep='\n')

#groupby - multiple columns