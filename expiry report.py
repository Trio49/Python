import pandas as pd
import os
#read file

expiry=pd.read_csv('expiry.csv')
#sorted by account code
expiry=expiry.sort_values(by=['Account Code'])
#count how many account has
i=expiry['Account Code'].nunique()
