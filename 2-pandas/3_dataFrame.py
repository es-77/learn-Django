import pandas as pd

# dataframe is a mulitidimentional table 

# data = {"role":[1,2,3,4,5],"name":['moon','emmanuel','saleem','john','jin']}

# dataFrame = pd.DataFrame(data)

# print(dataFrame)

# # print one row
# data = {"role":[1,2,3,4,5],"name":['moon','emmanuel','saleem','john','jin']}

# dataFrame = pd.DataFrame(data)

# print(dataFrame.loc[0])

# # print two row
# data = {"role":[1,2,3,4,5],"name":['moon','emmanuel','saleem','john','jin']}

# dataFrame = pd.DataFrame(data)

# print(dataFrame.loc[[0,1]])

# change indexing
data = {"role":[1,2,3,4,5],"name":['moon','emmanuel','saleem','john','jin']}

dataFrame = pd.DataFrame(data,index=['student1','student2','student3','student4','student5'])

print(dataFrame)