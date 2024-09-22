import pandas as pd
data1={'Id':[1,2,3,4,5],
     'Name':['Vetri','vel','Tk','Rk','JJ'],
     'RollNo':[111,112,113,114,115]}

df1=pd.DataFrame(data1)
print(df1)


data2={'Id':[6,7,8,9,10],
     'Name':['Vetri','vel','Tk','Rk','JJ'],
     'RollNo':[116,117,118,119,120]}

df2=pd.DataFrame(data2)
print(df1)

resDf=pd.concat([df1,df2])
print(resDf)


#axis=0 stacking on row(not overlapping index) , axis=1 means stacking on column
resDf=pd.concat([df1,df2],axis=0)
print(resDf)