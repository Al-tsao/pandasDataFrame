import pandas as pd

chicago = pd.read_csv('chicago.csv').dropna(how='all')

#確認每個column的種類
chicago.nunique()

#了解到Department有最少的分類，利用category type來降低檔案大小
chicago['Department'] = chicago['Department'].astype('category')

#lower(), upper(), titile(), len()
chicago['Name'] = chicago['Name'].str.lower() #因為python原本就有內建lower()的function，為了要和內建的功能有區別，所以在前面加上.str

#replace()  
chicago['Department'] = chicago['Department'].str.replace('MGMNT', 'MANAGEMENT')
chicago['Employee Annual Salary'] = chicago['Employee Annual Salary'].str.replace('$','', regex=True).astype(float)

#contains()
mask_contains = print(chicago['Position Title'].str.lower().str.contains('water')) #先將字體通通轉換成小寫統一格式，然後尋找字串中是否含有water，回傳布林值陣列

#startswith()
mask_startswith = print(chicago['Position Title'].str.lower().str.startswith('water')) #先將字體通通轉換成小寫統一格式，然後尋找開頭是否還有water

#endswith()
mask_endswith = print(chicago['Position Title'].str.lower().str.endswith('water')) #先將字體通通轉換成小寫統一格式，然後尋找結尾是否還有water

#strip(), lstrip(), rstrip()
chicago["Name"].str.strip() #移除前後空格
