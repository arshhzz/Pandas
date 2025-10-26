import pandas as pd

data = {
  "Name": ["Ram", "Sham", "Mogu", "Gogu", "Rabi", "Baba", "Kamli", "Mano"], 
  "Age": [28, 43, 33, 21, 43, 23, 28, 20], 
  "Salary": [50000, 30000, 28000, 45000, 60000, 71000, 52000, 60000], 
  "perfromanceScore" : [83, 91, 92, 88, 89, 95, 98, 93]
}

df = pd.DataFrame(data)
print(df)

'''
let's say you want to remove a column from the df, 
so you can use df.drop(columns = ["ColumnName"], inplace=True)
'''

df.drop(columns=["perfromanceScore"], inplace=True)
print(df)