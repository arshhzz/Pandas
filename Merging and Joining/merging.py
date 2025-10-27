'''
pd.merge(dfq, df2, on="col_name", how="Type_of_join")
'''
import pandas as pd

df_customers = pd.DataFrame ({
  "Customer_id": [1, 2, 3], 
  "Customer_Name": ["Ramesh", "Mahesh", "Kalpesh"], 
})

df_orders = pd.DataFrame({
  "Customer_id" : [1, 2, 4], 
  "Order_Amount": [240, 450, 540]
})

df_merged = pd.merge(df_customers, df_orders, on="Customer_id", how="inner")
print(df_merged)