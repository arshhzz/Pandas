import pandas as pd

data = {
  "Name": ["lolu", "molu", "cholu", None, "Gupt", "rog"], 
  "Age": [12, 43, 23, 21, None, 19], 
  "Salary": [1000, None, 23455, 6566, 44455, 77], 
  "performanceScore": [None, 87, 99, 92, 78, 93]
}

df = pd.DataFrame(data)
print("Data before Interpolation: ")
print(df)

'''
interpolation refers to handling null or empty values by maintaing: 
> data integrity
> smooth trends
> avoid data loss
'''
print("Data after Interpolation: ")
df['Age'] = df["Age"].interpolate(method="linear", axis = 0)
print(df)


'''
WHEN TO USE INTERPOLATION: 
> timer series data
> numeric data with trends
> avoid dropping rows
'''