#join two data Frames diffrence columns and records
import pandas as pd
data1={'Id':[1,2,3,4,5],
     'Name':['Vetri','vel','Tk','Rk','JJ'],
     'RollNo':[111,112,113,114,115]}

df1=pd.DataFrame(data1)
print(df1)

data2={'Marks':[75,86,95,100,99],
       'Rank':[5,4,3,1,2]}


df2=pd.DataFrame(data2)
print(df2)

resDf=df1.join(df2)
print(resDf)