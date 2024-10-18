import pandas as pd

# read json file with  

# jsonData = pd.read_json('C:/laragon/www/python/users.json')

# print(jsonData)

# # read complete data
# jsonData = pd.read_json('C:/laragon/www/python/users.json')

# print(jsonData.to_string())
# # read complete data with out indexx
# jsonData = pd.read_json('C:/laragon/www/python/users.json')

# print(jsonData.to_string(index=False))
# show into dataframe
jsonData = pd.read_json('C:/laragon/www/python/users.json')

print(pd.DataFrame(jsonData).to_string())