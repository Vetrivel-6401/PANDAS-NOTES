#iterate pandas df

import pandas as pd

data={
    'Students':['vetri','vel','pradeep','sakthi'],
    'Age':[23,22,19,22],
    'Class':['bio','cs','cs','commerce']
}

df=pd.DataFrame(data)

#iterate column names
for col in df:
    print(col)

print(df.columns)