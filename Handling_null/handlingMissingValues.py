import pandas as pd

# data = {
#   "Name": ["lolu", "molu", "cholu", None, "Gupt", "rog"], 
#   "Age": [12, 43, 23, 21, None, 19], 
#   "Salary": [1000, None, 23455, 6566, 44455, 77], 
#   "performanceScore": [None, 87, 99, 92, 78, 93]
# }

# df = pd.DataFrame(data)
# print(df)

# '''
# NaN -> Not a Number
# None -> (for Object data types)

# isnull()
# True -> NaN is missing
# False -> value is present

# '''

# # print(df.isnull())
# print(df.isnull().sum())



data = {
  "Name": ["lolu", "molu", "cholu", None, "Gupt", "rog"], 
  "Age": [12, 43, 23, 21, None, 19], 
  "Salary": [1000, None, 23455, 6566, 44455, 77], 
  "performanceScore": [None, 87, 99, 92, 78, 93]
}

df = pd.DataFrame(data)
# print(df)

# df.dropna(axis=0, inplace=True) 
'''
so axis here represents that, the cell which has null values, do you want the
column of that to be dropped (axis = 1) or do you want that row to be dropped (axis = 0)
whereas
inplace refers to whether you want the modification to be inplace or not
'''
print(df)

'''
fillna ->   df.fillna(value, inplace)
Here value -> refers to what you want to insert in the place of null
inplace means the same as above

'''
# print(df.isnull())
df['Age'].fillna(df['Age'].mean(), inplace=True)
df['Salary'].fillna(df['Salary'].mean(), inplace=True)

print(df)

