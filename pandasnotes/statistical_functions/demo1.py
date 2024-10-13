#perform statistical function in df

import pandas as pd

df=pd.read_csv('PANDAS-NOTES\pandasnotes\statistical_functions\sales.csv')
# print(df.info())

#sum()
res_df=df[['Revenue','UnitsSold']]
print(res_df.sum())

#if we perform sum in whole df the string values are grouped together and sum will apply for numeric columns only
print(df['Date'].sum())
print(df.sum())

