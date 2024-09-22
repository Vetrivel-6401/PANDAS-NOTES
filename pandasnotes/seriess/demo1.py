#create pandas series and
#Access values from pandas series , use index number like list tuple

import pandas as pd

data=[10,23,12,15,17]

#series creation
s=pd.Series(data)

print("\n series\n",s)

#accessing value using index
print("element from series : \n",s[2])


d = {'a': 1, 'b': 2, 'c': 3}
ser = pd.Series(data=d, index=['a', 'b', 'c'])
print(ser)

#diffenece
d = {'a': 1, 'b': 2, 'c': 3}
ser = pd.Series(data=d, index=['x', 'y', 'z'])
print(ser)