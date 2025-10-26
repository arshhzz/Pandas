import pandas as pd

# df = pd.read_excel("Sample-Superstore.xlsx")
# print(df)

data = {
    "Name": ["Ram", "Sham", "Ghanshyam"],
    "Age" : [10, 20, 30], 
    "City" : ["Jammu", "Delhi", "Chandhigarh"]
}

df = pd.DataFrame(data)
print(df)

# df.to_csv("Output.csv", index=False)

print("Displaying the info of the data set: ")
print(df.info())


sampleStoreDf = pd.read_excel("Sample-Superstore.xlsx")
print("Printing the head -> ")
print(sampleStoreDf.head())

print("Printing the Tail -> ")
print(sampleStoreDf.tail())