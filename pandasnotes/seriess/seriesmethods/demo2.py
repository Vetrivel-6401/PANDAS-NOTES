import numpy as np
import pandas as pd

#hasnans  Return True if NaN value present in the series
data2=['vetri','vel','pradeep',np.nan,'sakthi']
S=pd.Series(data2,name='Students',index=['Student1','Student2','Student3','Student4','Student5'])
print("does the series has  NaN:",S.hasnans)
print("\n\n",S)

#head()-Return first n rows
print("\n\n",S.head(3))

#tail()-Return last n rows
print("\n\n",S.tail(3))

#info()
print("\n Info of the series",S.info())