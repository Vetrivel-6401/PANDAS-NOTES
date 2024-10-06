import pandas as pd

data=['\tvetrivel\n!','@  vetri','skathi!']
ser=pd.Series(data)
print("series\n\n",ser)

#print(after removing white space and characters from left only)
print('\n\n',ser.str.rstrip("@!\n\t"))