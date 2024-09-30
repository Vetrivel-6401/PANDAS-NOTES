#iterate ovre columns using items()
import pandas as pd
data={'Name':['Vetri','Vel','Sakthi','Shree','sai'],
      "Marks":[92,93,88,79,99],
      'Subject':['Tamil','Tamil','Tamil','Tamil','Tamil']}

df=pd.DataFrame(data)
print(df)

#iteraton
print("\n\n")
for col,row in df.items():
    print(col) # col will return the column name alone like Name,Marks,Subjcet
    print(row) #row will return the datas of the columns