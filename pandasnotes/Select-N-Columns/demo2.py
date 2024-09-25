#select columns in a range
import pandas as pd

data={
    'Id':['s01','s02','s03','s04','s05'],
    'Student':['vetri','vel','Jp','PP','sakthi'],
    'Marks':[100,33,44,98,97],
    'Subject':['tamil','tamil','tamil','tamil','tamil'],
    'Result':['pass','pass','pass','pass','pass']
}

df=pd.DataFrame(data)
print(df)

#N range of columns

print("\n\n",df[df.columns[1:4]])