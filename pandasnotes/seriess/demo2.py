#Name your own indexes in pandas series

#use index paramter , length should same as data

import pandas as pd

data=[10,23,12,15,17]

s=pd.Series(data,index=["row1","row2","row3","row4","row5"])

print("\n series\n",s)

print("element from series : \n",s['row2'])

