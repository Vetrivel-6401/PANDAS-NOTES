#get size of each group

#iterate the group
import pandas as pd
import numpy as np

data={
    'Name':['Vetri','Vel','Skathi','Vetri','sri','Vel'],
    'Rank':[1,2,4,5,7,3],
    "year":[2022,2022,2023,2024,2020,2020]
}
df=pd.DataFrame(data)
print(df)


res_df=df.groupby('Name')
print('size of each group\n\n',res_df.size())

#we can use agg function also

print("using np\n",res_df.agg(np.size))