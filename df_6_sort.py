import pandas as pd
import numpy as np

#1 By index
df = pd.DataFrame([1, 2, 3, 4, 5], index=[100, 29, 234, 1, 150], columns=['A'])
df = df.sort_index()
df = df.sort_index(ascending=False)
print (df)