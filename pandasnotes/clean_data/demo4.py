#replace  null values using fillna(x)

import pandas as pd

df=pd.read_csv(r"C:\Users\vetri\OneDrive\PYTHON\pandasnotes\clean_data\uncleaned.csv")
print(df)

res_df=df.fillna(2.2)

print("df after filling x values to null values\n\n",res_df)