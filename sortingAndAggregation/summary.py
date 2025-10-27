import pandas as pd



data = {
  "Name": ["Arun", "Varun", "Charun", "Kapil", "Rao"], 
  "Age": [22, 28, 34, 41, 39], 
  "CibilScore": [728, 891, 344, 545, 900]
}

df = pd.DataFrame(data)

avg_cibil = df["CibilScore"].mean()
print(avg_cibil)

'''
> .sum ()
> .min ()
> .max ()
> .mean()
'''