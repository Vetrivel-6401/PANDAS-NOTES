import pandas as pd

data={
    'Student':['vetri','vel','Jp','PP','sakthi'],
    'Marks':[100,33,44,98,97],
    'Subject':['tamil','tamil','tamil','tamil','tamil']
}

df=pd.DataFrame(data)
print(df)

df.insert(1,'rollno',[101,102,103,104,105])

print("\nupdated\n",df)