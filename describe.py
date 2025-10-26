import pandas as pd

# data = {
#   "Name": ["lolu", "molu", "cholu", "babla", "Gupt", "rog"], 
#   "Age": [12, 43, 23, 21, 23, 19], 
#   "Salary": [1000, 2333, 23455, 6566, 44455, 77], 
#   "performanceScore": [68, 87, 99, 92, 78, 93]
# }

# df = pd.DataFrame(data)
# print(df)

# print("Descriptive Statistics: ")
# print(df.describe())

data = {
  "Name": ["lolu", "molu", "cholu", "babla", "Gupt", "rog"], 
  "Age": [12, 43, 23, 21, 23, 19], 
  "Salary": [1000, 2333, 23455, 6566, 44455, 77], 
  "performanceScore": [68, 87, 99, 92, 78, 93]
}

df = pd.DataFrame(data)

print(df.shape)
print(df.columns)

