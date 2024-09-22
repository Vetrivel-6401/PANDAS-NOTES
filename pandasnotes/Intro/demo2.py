import pandas as pd

data={
    'Students':['vetri','vel','pradeep','sakthi'],
    'Age':[23,22,19,22],
    'Class':['bio','cs','cs','commerce']
}

df=pd.DataFrame(data,index=['row1','row2','row3','row4'])
print(df,'\n\n')

#retrive student data column corrosponding to the row1 Label

print("name of STudent from row1=: ",df.loc['row1','Students'])