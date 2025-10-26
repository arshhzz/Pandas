import pandas as pd

data = {
  "Name": ["Ram", "Sham", "Mogu", "Gogu", "Rabi", "Baba", "Kamli", "Mano"], 
  "Age": [28, 43, 33, 21, 43, 23, 28, 20], 
  "Salary": [50000, 30000, 28000, 45000, 60000, 71000, 52000, 60000], 
  "perfromanceScore" : [83, 91, 92, 88, 89, 95, 98, 93]
}

df = pd.DataFrame(data)
print(df)

df["Bonus"] = df["Salary"] * 0.1
print(df)

# using insert() -> industrial standards 

# df.insert(loc, "Column", some_data)
'''
loc -> index (location where we want to insert the data, (int64))
2nd param -> The column name that we want to insert in this
3rd param -> The Data that we want the column to contain

'''
df.insert(0, "Emp_Id", [121, 212, 343, 235, 244, 644, 654, 675])
print(df)