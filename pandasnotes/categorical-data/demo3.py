#add category in series

import pandas as pd

series1=pd.Series(['p','r','s','s'],dtype="category")


#to add categories
series1=series1.cat.add_categories('q')

print(series1)

#to remove catgory
series1=series1.cat.remove_categories('s')
print("\n",series1)