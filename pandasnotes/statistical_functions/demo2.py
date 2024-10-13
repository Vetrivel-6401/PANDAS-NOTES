#print non empty  values in df
import pandas as pd

df=pd.read_csv('D:\Pandas\PANDAS-NOTES\pandasnotes\statistical_functions\sales.csv')
print(df.count())

#max(),min() will get the max,min value in df

'''if the df contains str and float we cant perform max'''
print('max will display',df['UnitsSold'].max())
print('min will display',df['UnitsSold'].min())

res_df=df[['UnitsSold','Revenue']]
#get mean of the df
print('mean of the columns\n',res_df.mean())

#get the whold statiscal info
print(df.describe()) # it will aply operation numeric values only

print(df['UnitsSold'].median())

print(df['Revenue'].std())