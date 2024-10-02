#remove null values using dropns()

import pandas as pd

df=pd.read_csv(r"C:\Users\vetri\OneDrive\PYTHON\pandasnotes\clean_data\uncleaned.csv")
print(df)

res_df=df.dropna()

print("df after removing duplicates\n\n",res_df)