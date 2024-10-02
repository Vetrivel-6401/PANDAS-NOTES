#sort value using sort_values #default asc
import pandas as pd
data={
    "Name":['vetri','vel','Skathi','Pradeep','sai'],
    "Marks":[477,489,480,399,378],
    "Rank":[3,1,2,4,5]}

df=pd.DataFrame(data)
print(df)

print('after sorting \n',df.sort_values(by='Marks')) #default asc

#to desc

print("descending df",df.sort_values(by="Marks",ascending=False))