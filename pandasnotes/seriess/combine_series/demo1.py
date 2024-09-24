#combining two series and get the max values from thos for each record
#function paramter compulsory
import pandas as pd
data1=[10,3,23,44,65]
data2=[23,45,1,77,53]

series1=pd.Series(data1)
series2=pd.Series(data2)

print('series1',series1)
print("\n\nseries2",series2)


def maximum(x1,x2):
    if x1>x2:
        return x1
    else:
        return x2
resdf=series1.combine(series2,maximum)

print("\n\n",resdf)