import pandas as pd

df=pd.read_excel(r'C:\Users\vetri\OneDrive\PYTHON\pandasnotes\Read_Excel\cricket.xlsx')
print(df)

#head read first n row deafult 5 row

print("\n\n",df.head(2))

##tail read last n rows deafult 5 row

print("\n\n",df.tail(3))