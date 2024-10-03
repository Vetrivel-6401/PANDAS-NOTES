#select two columns from dataframe 

import pandas as pd

data={
    'Student':['vetri','vel','Jp','PP','sakthi'],
    'Marks':[100,33,44,98,97],
    'Subject':['tamil','tamil','tamil','tamil','tamil']
}

df=pd.DataFrame(data)
print(df)

print("\n\n ",df[['Subject','Marks']]) # do not mention innecessary columns