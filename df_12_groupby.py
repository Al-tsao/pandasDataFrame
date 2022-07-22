import pandas as pd

df = pd.DataFrame({'A':['X','X','Y','Y','Y','Y','Z','Z','Z','Z','Z','Z'],
                   'B':['one','one','two','two','three','three','four','four','five','five','six','six'],
                   'C':[1,2]*6,
                   'D':[3,4]*6})

#讀取column中的title
title = pd.DataFrame({'Title': df.columns})
print('Title名稱', title, sep='\n')
print('============================================')

#1 groupby: 分組，將資料以'A'欄內資料的方式分組，然後放到dic中
groupbyA = df.groupby('A')
print('groupbyA', groupbyA.groups)
print('============================================')

#2 groupby - single group single column
sglCol = df.groupby(['A'])['C'].sum() #以A作為分組標準，並且對於C做加總，但不會有C的title出現
print('sglCol', sglCol.reset_index(), sep='\n')
print('============================================')

#3 groupby - multiple columns
multiCol = df.groupby(['A'])[['C','D']].sum() #以A作為分組標準，並且對於C和D個別做加總，且有C和D的title出現
print('multiCol', multiCol.reset_index(), sep='\n')
print('============================================')

#4 groupby - multiple groups
multiGroup = df.groupby(['A','B'])['C'].sum() #以A、B作為分組條件，對C做加總
print('multiGroup', multiGroup.reset_index(), sep='\n')
print('============================================')

#5 multiple functions
multiFunc = df.groupby(['A'])['C'].agg(['mean','sum']) #以A作為分組標準，對C進行平均與加總
print('multiFunc', multiFunc.reset_index(), sep='\n')

#6 size()
sectors = df.groupby('A')
sectors.size() #其實跟value_counts()的功能一項，是了解一個series中各分類的總數是多少

#7 get_group()
print(sectors.get_group('Z')) #只會抽取Sector中特定的Z組，將資料傳出來

#8 agg()
countList = [1]*df.shape[0]
df['Count'] = countList #新增Count欄位來計算次數
agg_d = {'C':'sum','Count':'size'} #定義column欄位要做甚麼統計運算
d = {'C':'Sum', 'Count':'Count'}
pd_gp_ca2 = df.groupby(['A','B']).agg(agg_d).rename(columns=d).reset_index() #計算兩群組總和
print(pd_gp_ca2)