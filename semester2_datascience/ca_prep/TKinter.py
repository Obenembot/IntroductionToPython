import pandas as pd

df = pd.DataFrame({'A': [1, 2, None, 4], 'B': [5, 6, 7, 8]})

# Using inplace=False (default)
df_filled = df.fillna(-55)
print("Original DataFrame (after fillna with inplace=False):\n", df)
print("\nNew DataFrame (df_filled):df_filled \n", df_filled)
print("\nNew DataFrame (df_filled):\n", df)

# Using inplace=True
df.fillna(0, inplace=True)
print("\nOriginal DataFrame (after fillna with inplace=True):\n", df)