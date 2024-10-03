import pandas as pd

df=pd.read_csv(r'pandasnotes\Read_CSV\Product_v6.csv')
print(df)

#C:\\Users\\vetri\\OneDrive\\PYTHON\\pandasnotes\\Read_CSV\\Product_v6.csv
#save file as csv MS-DOS----go to Tools web options -->UTF-8 else simply put r"filepath"

#head read first n row deafult 5 row

print("\n\n",df.head(6))

##tail read last n rows deafult 5 row

print("\n\n",df.tail(7))