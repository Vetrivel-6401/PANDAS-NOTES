import pandas as pd

data={
    'Name':['vetr','pradeep','lalit'],
    'Age':[14,56,21],
    'job':['It','Accounts','clerk']
}

df=pd.DataFrame(data,index=['Row1','Row2','Row3'])

print("\nDataFrame\n",df)

#dtype = return the data type in the df

print('\n\nDtypes of df \n', df.dtypes)

#ndim = Return the dimension of the df

print('\n\nDimension of the dataframe= \n', df.ndim)

#size = Return the number of elentsin the dataframe
print('\n\nTotal elements in df \n', df.size)

#shape=return dimensionality of df in the form of tuple

print('\n dimension of df \n', df.shape)  #shape[0]=number of rows,[1]=columns

#index = return the indices of the df

print('\n\nIndices of df \n', df.index)

#T= Tranpose the rows(columns) and columns(row)

print(df.T)

#head= Return first n number of rows default first 5 

print("\n",df.head(2))

#tail= Return last n number of rows default last 5 

print("\n",df.tail(2))

