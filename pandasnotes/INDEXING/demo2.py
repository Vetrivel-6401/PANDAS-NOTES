#to retrieve single row record from df use loc['index name']
import pandas as pd

df=pd.read_excel(r'pandasnotes/Read_Excel/cricket.xlsx',index_col='Player')
print(df)

#To retriev a particular rows data

print("\n\n",df.loc['Virat']) 

# output
#  Rank       1
# Score    118
# Balls     66