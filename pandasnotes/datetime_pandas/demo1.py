#get curren time and date local timezone

import pandas as pd

Today=pd.Timestamp.now()
print('Current date and time',Today)

#day of week

timestamp=pd.Timestamp(year=2024,month=10,day=1)
print("day of week",timestamp.day_of_week)
print('day of year',timestamp.day_of_year)
print("days in month",timestamp.daysinmonth)

#check leap year
print('leap year or not ?',timestamp.is_leap_year)

#last day of the month
print('is last of the month',timestamp.is_month_end)

#first day of the month
print('is firest of the month',timestamp.is_month_start)

#last day of the year
print('is last of the year',timestamp.is_year_end)

#first day of the year
print('is first of the year',timestamp.is_year_start)