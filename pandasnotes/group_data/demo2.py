#iterate the group
import pandas as pd

data={
    'Name':['Vetri','Vel','Skathi','Vetri','sri','Vel'],
    'Rank':[1,2,4,5,7,3],
    "year":[2022,2022,2023,2024,2020,2020]
}
df=pd.DataFrame(data)
print(df)


res_df=df.groupby('Name')
print(type(res_df))

for name,group in res_df:
    print("\n\n",name)
    print("\n",group)

#  Skathi

#       Name  Rank  year
# 2  Skathi     4  2023


#  Vel

#    Name  Rank  year
# 1  Vel     2  2022
# 5  Vel     3  2020


#  Vetri

#      Name  Rank  year
# 0  Vetri     1  2022
# 3  Vetri     5  2024


#  sri

#    Name  Rank  year
# 4  sri     7  2020
