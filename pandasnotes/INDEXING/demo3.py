#to retrieve the index and columns by position using iloc[index position]

import pandas as pd

df=pd.read_excel(r'pandasnotes/Read_Excel/cricket.xlsx',index_col='Player')
print(df)

#To retriev a particular rows data

res_df=df.iloc[2] #3rd row
print(res_df)

# output
#  Rank       1
# Score    118
# Balls     66