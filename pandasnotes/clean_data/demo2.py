#find null/NaN values -- null values will be returned a sFlase in not null

import pandas as pd

df=pd.read_csv(r'pandasnotes\clean_data\uncleaned.csv')
print(df)


res_df=df.notnull()
print("finding null values\n\n",res_df.to_string())