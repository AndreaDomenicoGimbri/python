import pandas as pd 
import numpy as np


s=pd.Series([1,3,5,6,8])
print(s)
s=s+[100,200,300,400,500]
print(s)
#brodcasting add a single value to all the elements of the series
s=s+200
print(s)
print(s>0)