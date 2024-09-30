#delete rows using drop()
#in axis we can use 0 or use index to delete rows

import pandas as pd

data={
    'Student':['vetri','vel','Jp','PP','sakthi'],
    'Marks':[100,33,44,98,97],
    'Subject':['tamil','tamil','tamil','tamil','tamil']
}

df=pd.DataFrame(data)
print(df)


#delete rows 

res_df=df.drop(labels=2,axis='index') # or use axis =0
#labeks=2 means index 3rd row will be deleted

print('updated df\n',res_df)