#載入模組
import pandas as pd

#載入數據
df = pd.DataFrame([['Jhon',15,'A'],['Anna',19,'B'],['Paul',25,'D']])
df. columns = ['Name','Age','Grade']

print(df)

#選到特定的index
i = df[((df.Name == 'Jhon') & ( df.Age == 15) & (df.Grade == 'A'))].index.tolist()