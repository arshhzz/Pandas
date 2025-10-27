import pandas as pd

data = {
  "Name": ["Arun", "Varun", "Charun", "Kapil", "Rao"], 
  "Age": [22, 28, 34, 41, 39], 
  "CibilScore": [728, 891, 344, 545, 900]
}

df = pd.DataFrame(data)
print(df)

print("After Cibil based sorting: ")
df.sort_values(by="CibilScore", ascending=True, inplace=True)
print(df)


'''
In case you want to sort on base of multiple columns, you can simply pass on a list
of columns inside the sort_values() function.
viz : 
df.sort_values(by = ["col1", "col2"], ascending =["True", "False"], inplace = True)
'''