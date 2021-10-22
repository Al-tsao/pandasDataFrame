import pandas as pd

fortune = pd.read_csv('fortune1000.csv', index_col='Rank')
sectors = fortune.groupby('sector')

#size()
sectors.size()