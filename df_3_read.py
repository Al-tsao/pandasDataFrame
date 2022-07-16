import pandas as pd
import numpy as np

df = pd.read_csv('kc_house_data.csv')

data = pd.DataFrame(np.arange(16).reshape(4,4), index = list('abcd'), columns = list('ABCD'))
print(data)