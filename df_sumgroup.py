#載入Pandas、numpy模組
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

#分組計算
pd_gp_cal = df = pd.DataFrame({'A' : ['X','X','Y','Y','Y','Y','Z','Z','Z','Z','Z','Z'],
                               'B' : ['one','one','two','two','two','two','three','three','three','three','three','three'],
                               'C' : [1,2]*6})

#計算次數與總和
countList = [1]*pd_gp_cal.shape[0]
pd_gp_cal['Count'] = countList #新增Count欄位來計算次數
agg_d = {'C':'sum','Count':'size'} #定義column欄位要做甚麼統計運算
d = {'C':'Sum', 'Count':'Count'}
pd_gp_ca2 = pd_gp_cal.groupby(['A','B']).agg(agg_d).rename(columns=d).reset_index() #計算兩群組總和
print(pd_gp_ca2)

sns.set()
heatmap = sns.scatterplot(data=pd_gp_ca2, x="A", y="B")
plt.show()