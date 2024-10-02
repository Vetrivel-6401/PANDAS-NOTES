#remove duplicate usinf drop-duplicate()
import pandas as pd
data={
    "Name":['vetri','vel','vel','Pradeep','sai'],
    "Marks":[477,489,489,399,378],
    "Rank":[3,1,1,4,5]}

df=pd.DataFrame(data)
print(df)

#remov duplicates
res=df.drop_duplicates()

print("after removing duplictes\n\n",res)