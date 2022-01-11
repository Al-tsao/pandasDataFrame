#載入模組
import pandas as pd

#載入數據
df = pd.DataFrame([['Jhon',15,'A'],['Anna',19,'B'],['Paul',25,'D']])
df.columns = ['Name','Age','Grade']

print(df)

#刪除特定row
i = df[((df.Name == 'Jhon') & ( df.Age == 15) & (df.Grade == 'A'))].index.tolist()
df_dropRow = df.drop(i, axis=0)

#刪除特定column
df_dropColumn = df.drop(['Age'], axis=1)