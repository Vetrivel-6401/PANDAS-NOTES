import pandas as pd

data={
    'Student':['vetri','vel','Jp','PP','sakthi'],
    'Marks':[100,33,44,98,97],
    'Subject':['tamil','tamil','tamil','tamil','tamil']
}

df=pd.DataFrame(data)
print(df)


res_df=df.assign(rolln=[101,102,103,104,105]) #column will be added at last
print('update\n',res_df)