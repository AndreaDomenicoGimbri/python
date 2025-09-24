import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

s=pd.Series([2, -3, 2.4, 5])
print(s)


print(np.exp(s))

print(s + [1000,2000,3000,4000])
#BRODCASTING: add same value to all elements
print (s + 1000)

print(s<0)

# Use string As index
s2= pd.Series([1,2,3] , index=["alice", "bob", "charlie"])
print(s2)

print(s2["bob"])

print(s2.iloc[1]) 

print(s2.loc["bob"])

# slicing by index label the secon index is not included
print(s2.iloc[0:3])


# how to manipulate the index of a list
s4=pd.Series(s2,index=["charlie", "alice"])
print(s4)



# associate a name to a series
s3=pd.Series([1,2,3] , index=["alice", "bob", "charlie"], name="my_series")
print(s3)