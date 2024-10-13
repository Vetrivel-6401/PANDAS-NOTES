#aggregate operation on df - get the mean

#iterate the group
import pandas as pd
import numpy as np

data={
    'Name':['Vetri','Vel','Skathi','Vetri','sri','Vel'],
    'Rank':[1,2,4,5,7,3],
    'Points':[299,363,200,400,297,315],
    "year":[2022,2022,2023,2024,2020,2020]
}
df=pd.DataFrame(data)
print(df)


res_df=df.groupby('Name')
print('mean of the player\n\n',res_df['Points'].agg(np.mean))

#we can use directly also
print('\n\n',res_df['Points'].mean())