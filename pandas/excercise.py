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

temperatures = pd.Series([ 3,4, 28, 25,12,34,12,11,43,4,32,23], name="Daily Temperatures")

# plot used to plot the series that means create a graph

dates=pd.date_range("20250101", periods=12, freq="D")
print(dates)
temp_Date=pd.Series(temperatures.values,dates, name="Daily Temperatures")
temp_Date.plot(title="Daily Temperatures in 2025",kind="bar")
print(temp_Date)
plt.grid()
plt.show()



# DataFrame
data = {
    "Name": pd.Series(["Alice", "Bob", "Charlie"], index=[0, 1, 2]),
    "Age": pd.Series([25, 30, 35]),
    "City": pd.Series(["New York", "Los Angeles", "Chicago"])
}

people_df = pd.DataFrame(data)




data2 = [
     ["Alice", 25, "New York"],
     ["Bob", 30, "Los Angeles"],
     ["charlie", 35, "Chicago"]
]

people_df2=pd.DataFrame(data2, columns=["Name", "Age", "City"],index=["1", "2", "3"])
print(people_df2)

#multi indexing 
multi_index_df = pd.DataFrame( 
    {("public","birthyear") :
     {("Paris","Alice"): 1985,("Paris","Bob"): 1990,("London","Charlie"): 1980}
     ,("public","hobby") :
     {("Paris","Alice"): "Dancing",("Paris","Bob"): "skiing",("London","Charlie"): "biking"}
    ,("private","salary") :
    {("Paris","Alice"): 70000,("Paris","Bob"): 80000,("London","Charlie"): 90000}
   }
)


print(multi_index_df)
print(multi_index_df["public"])
print(multi_index_df["private"])

#in this example we have two levels of column and two levels of index.To drop a level we can use (name of the dataframe).columns/index.droplevel(level=0 or 1)
multi_index_df.columns=multi_index_df.columns.droplevel(level=0)
print(multi_index_df)
multi_index_df.index=multi_index_df.index.droplevel(level=0)
print(multi_index_df)
# the level of index or column represent one of the two values in the tuple in my case ("public","birthyear") or ("Paris","Alice")

Swap_df=multi_index_df.T
print(Swap_df)


Stacked_df=Swap_df.stack(future_stack=True)
print(Stacked_df)

#if I use loc function i can obtain a specific row of my dataframe by specifying the index value
print(multi_index_df.loc[("Alice")])
#using iloc function I can obtain a specific row of my dataframe by specifying the index position
print(multi_index_df.iloc[1:3])
#using boolean indexing i can specify a condition to filter the rows of my dataframe
print(multi_index_df[np.array([True, False, True])])
#using this expression I can filter the rows of my dataframe where the birthyear is greater than 1985
print(multi_index_df[multi_index_df["birthyear"]<=1985])



#adding or removing a column from my dataframe
multi_index_df["age"]=2025-multi_index_df["birthyear"]
multi_index_df["over 30"]=multi_index_df["age"]>30
multi_index_df.drop(columns="birthyear", inplace=True)
print(multi_index_df)

multi_index_df.insert(2,"pets",["cat","dog","fish"])
multi_index_df.insert(1,"height",[172,189,156])
multi_index_df.insert(1,"weight",[78,72,48])
print(multi_index_df)


# i can also use assign function to add a new column to my dataframe but it will return a new dataframe with out modifying the original one
# remember i cannot acces to column created with the same assignment 

new_multi_index_df=multi_index_df.assign(
body_mass_index= multi_index_df["weight"]/(multi_index_df["height"]/100)**2,
has_pets=multi_index_df["pets"]!="none"
)
print(new_multi_index_df)
#validate if the body mass index is greater than 25 true an expression that is evalueted by function val()
print(new_multi_index_df.eval("weight/(height/100)**2>25"))
#variant of the same function before is with the use of a global or local variable
threshold=25
print(new_multi_index_df.eval("weight/(height/100)**2>@threshold"))
#interrogate a dataframe with query function
print(new_multi_index_df.query("height>175 and pets=='dog'"))
#sort the dataframe by index in descending order
#new_multi_index_df=new_multi_index_df.sort_index(ascending=False)
#sort the dataframe by a specific column
new_multi_index_df=new_multi_index_df.sort_values(by="weight",ascending=False)
print(new_multi_index_df)

#line graph
new_multi_index_df.plot(title="people information",kind="line", y=["weight","height"], use_index=True)
plt.grid()
plt.show()

#similarity between numpy's array and pandas dataframe

grades_array=np.array([[85, 90, 78], [88, 92, 80], [90, 85, 88]])
grades=pd.DataFrame(grades_array, columns=["Math", "Science", "English"], index=["Alice", "Bob", "Charlie"])
print(grades)

#grades=np.sqrt(grades)
print(grades+1)
print(grades["Math"]>88)
print(grades.mean())


bonus_points=np.array([[5, 10, 15],[2,5,6],[1,2,3]])
bonus_points_df=pd.DataFrame(bonus_points, columns=["Math", "Science", "English"], index=["Alice", "Bob", "Charlie"])

grades=grades+bonus_points_df
print(grades)
#when additioned two dataframe with different index or column the result will be NaN for the missing values to avoid this we can use fillna() function
