import pandas as pd

df=pd.read_csv('D:\Pandas\PANDAS-NOTES\pandasnotes\Timeseries\data.csv',parse_dates=['Date'])
print(df)
#here date column actually a string we need o convert to date so pandas has parse_date=['date column'])
df['Date'] = pd.to_datetime(df['Date'], format='ISO8601')