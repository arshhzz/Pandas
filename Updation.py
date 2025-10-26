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
#.loc -> A method used to access a specific cell/cells, row/rows, col/cols
df.loc[row_index, "col_name"] = new_value

'''

# df.loc[0, "Salary"] = 55000
# print(df)

#Increasing multiple roles
print("Salary Increased")
df['Salary'] = df["Salary"] * 1.05
print(df)

