#delete columns using drop()
import pandas as pd

data={
    'Student':['vetri','vel','Jp','PP','sakthi'],
    'Marks':[100,33,44,98,97],
    'Subject':['tamil','tamil','tamil','tamil','tamil']
}

df=pd.DataFrame(data)
print(df)

df=df.drop(labels=['Marks','Subject'],axis=1) #axis='columns' aslo same

print(df)