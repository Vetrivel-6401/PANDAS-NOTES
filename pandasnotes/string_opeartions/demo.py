import pandas as pd

data=['VetriVel','saKthi','PradeEP','RaM']
series=pd.Series(data)
print(series)

#lower()
print("\n lowercase\n\n",series.str.lower())

#upper()
print("\n uppercase\n\n",series.str.upper())

#Camelcase
print("\n lowercase\n\n",series.str.title())

#len()
print("\n lowercase\n\n",series.str.len())

import numpy as np
data=['VetriVel','saKthi',np.nan,'RaM']
#count()
print("\n count\n\n",series.count())


#contains()
print("\n does the series have ?\n\n",series.str.contains('RaM'))
