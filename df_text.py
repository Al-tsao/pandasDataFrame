import pandas as pd

chicago = pd.read_csv('chicago.csv')

#確認每個column的種類
print(chicago.nunique())

#了解到Department有最少的分類，利用category type來降低檔案大小
chicago['Department'] = chicago['Department'].astype('category')
