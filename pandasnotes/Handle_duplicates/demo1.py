#find duplicate using duplicate()
import pandas as pd
import numpy as np

data={
    "Name":['vetri','vel','vel','Pradeep','sai'],
    "Marks":[477,489,489,399,378],
    "Rank":[3,1,1,4,5]}

df=pd.DataFrame(data)
print(df)

#find duplicates
res=df.duplicated()
print("Dulicate data \n\n",res) # it will return bool for each record , return True if duplicate found
