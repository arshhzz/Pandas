'''
> select specific columns
> filter rows
> combine multiple conditions
'''

'''
1 > square brackets (selecting columns):
- a series
- dataframe multiple columns of data
  column = df["column name"]
  subset = df["col1", "col2"]

2 > Filtering rows
-boolean indexing 
>> based on a single condition 
filtered_rows = df[df["Salary"] > 50000]

>> based on multiple conditions
filtered_rows = df[(df["Salary"] > 50000) & (df["Salary"] < 80000)]

'''

import pandas as pd

data = {
  "Name": ["Ram", "Sham", "Mogu", "Gogu", "Rabi", "Baba", "Kamli", "Mano"], 
  "Age": [28, 43, 33, 21, 43, 23, 28, 20], 
  "Salary": [50000, 30000, 28000, 45000, 60000, 71000, 52000, 60000], 
  "perfromanceScore" : [83, 91, 92, 88, 89, 95, 98, 93]
}

df = pd.DataFrame(data)
print(df.info)

# print("Single column : ")
# print(df["Age"])

# print("Multiple columns : ")
# subset = df[["Name", "Salary"]]
# print(subset)

## Return the names of the people where salary is greater than 5000
print("People having salary greater than 50000 : ")
res = df[df["Salary"] > 50000]

# ans = res["Name"] // in case you only want to return the name
# print(ans)

print(res)

## Return the rows that have salry greater than 30000 and age lesser than 35

print("Entries with salary over 30000 and age lesser than 30 : ")
res = df[(df["Salary"] > 30000) & (df["Age"] < 30)]
print(res)
