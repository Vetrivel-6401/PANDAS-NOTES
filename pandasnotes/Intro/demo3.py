import pandas as pd

data={
    'Students':['vetri','vel','pradeep','sakthi'],
    'Age':[23,22,19,22],
    'Class':['bio','cs','cs','commerce']
}

df=pd.DataFrame(data,index=['row1','row2','row3','row4'])
print(df,'\n\n')


#Access group of rows and columns by integer value from dataframe

print("name of STudent from row1=: ",df.iloc[[1,3]])

#Note if use df.loc[1,2] it will retrive the column name alone