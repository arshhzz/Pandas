import pandas as pd

data = {
  "Name": ["Arun", "Varun", "Kapil", "Sabil", "Deep", "Sharma"], 
  "Age": [28, 34, 32, 44, 32, 28], 
  "Salary": [50000, 60000, 45000, 52000, 480000, 85000]
}

df = pd.DataFrame(data)
print(df)

grouped = df.groupby("Age")["Salary"].sum()
print(grouped)
