import pandas as pd

df=pd.read_csv(r'C:\Users\vetri\OneDrive\PYTHON\pandasnotes\INDEXING\Product_v6.csv',index_col='partNumber')
# print(df.columns) # will display the columns in the dataframe
print(df)
#we can set the columns as index also


#directly using indexing operator []

res_df=df['name']
print(res_df)
