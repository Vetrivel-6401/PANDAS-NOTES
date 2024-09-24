import pandas as pd

df=pd.read_csv(r'pandasnotes\Read_CSV\Product_v6.csv')
print(df)

#head read first n row deafult 5 row

print("\n\n",df.head(6))

##tail read last n rows deafult 5 row

print("\n\n",df.tail(7))