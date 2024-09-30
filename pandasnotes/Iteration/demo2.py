#iterate ovre rowes using itertuples()
import pandas as pd
data={'Name':['Vetri','Vel','Sakthi','Shree','sai'],
      "Marks":[92,93,88,79,99],
      'Subject':['Tamil','Tamil','Tamil','Tamil','Tamil']}

df=pd.DataFrame(data)
print(df)

#iteraton

for i in df.itertuples():
    print(i)