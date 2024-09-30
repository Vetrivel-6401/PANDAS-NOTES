#iterate ovre rowes using iterrows()
import pandas as pd
data={'Name':['Vetri','Vel','Sakthi','Shree','sai'],
      "Marks":[92,93,88,79,99],
      'Subject':['Tamil','Tamil','Tamil','Tamil','Tamil']}

df=pd.DataFrame(data)
print(df)

#iteraton

for i in df.iterrows():
    print(type(i))