import pandas as pd

# print(pd.__version__)

# in pandas series is like a table colums 
# create a array 

# array = [1,2,3,4,5]
# newArray = pd.Series(array)
# print(newArray)

# # give lable into index
# array = [1,2,3,4,5]
# newArray = pd.Series(array,index=['one','two','three','four','five'])
# print(newArray)

# # acess value through index
# array = [1,2,3,4,5]
# newArray = pd.Series(array,index=['one','two','three','four','five'])
# print(newArray['five'])

# # use series in dictionation 
# dictionery = {'name':"emmanuel",'father':"saleem"}
# newdiction = pd.Series(dictionery)
# print(newdiction)

# only get first index value
dictionery = {'name':"emmanuel",'father':"saleem"}
newdiction = pd.Series(dictionery,index=['name'])
print(newdiction)
