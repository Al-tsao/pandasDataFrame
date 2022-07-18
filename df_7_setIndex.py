import pandas as pd
import numpy as np

data = pd.DataFrame(np.arange(16).reshape(4,4), index = list('abcd'), columns = list('ABCD'))

#1 設定'A'column為index
data.set_index(keys='A', inplace=True)