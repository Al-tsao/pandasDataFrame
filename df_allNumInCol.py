"""
目的是要看單一個colum中是否nan的存在
"""

import numpy as np
import pandas as pd

df = pd.DataFrame({'col' : [1,2, 10, np.nan, 10], 
                   'col2': ['a', 10, 30, 40 ,50],
                   'col3': [1,2,3,4,5.0]})
print(pd.to_numeric(df['col'], errors='coerce').notnull().all())