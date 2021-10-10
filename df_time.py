import pandas as pd
df = pd.read_csv('pretend_sales_data.csv')

df['date'] = pd.to_datetime(df['date'], format='%m/%d/%Y')

print(df.dtypes)