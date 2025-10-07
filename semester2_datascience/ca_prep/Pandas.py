import pandas as pd

data = {"Name": ["Sam", "Lebo"], "Age": [25, 30], "salary": ['R200', 'R4000']}
df = pd.DataFrame(data)
print(df.head())


df = pd.read_csv("adult.csv")
df.replace("?", 0, inplace=True)
avg = df['age'].mean()
# df['age'].fillna(avg, inplace=True)

print(df.head())
