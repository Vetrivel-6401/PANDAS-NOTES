#dtype
import pandas as pd
data=[1,2,3] #if any data is tsring in the data then dtype will be object
s=pd.Series(data)
print(s.dtype)

#ndim
print("\n dimension",s.ndim)

#size - return number of elemnts
print("no of lements in the  series",s.size)

#name - for that we have to give name to the series

data2=['vetri','vel','pradeep','sakthi']
S=pd.Series(data2,name='Students',index=['Student1','Student2','Student3','Student4'])
print("\nname of the Series:",S.name)
print("\n\nIndices in series:",S.index)