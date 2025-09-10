import pandas as pd

data = {"Name": ["Sam", "Lebo"], "Age": [25, 30], "salary": ['R200', 'R4000']}
df = pd.DataFrame(data)
print(df.head())
