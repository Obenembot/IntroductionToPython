import numpy as np
import pandas as pd

data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# df = pd.DataFrame(np.random.randn(5, 3), columns=['A', 'B', 'C'])
df = pd.DataFrame(data, columns=['Numbers'])
print(df)

print("=============================")

data = np.array([5, 10, 15, 20, 25])
print("Mean:", np.mean(data))
print("Median:", np.median(data))
print("Std Dev:", np.std(data))
print("Max:", np.max(data))
print("Min:", np.min(data))

print("============")

data = {"Name": ["Sam", "Lebo"], "Age": [25, 30], "salary": ['R200', 'R4000']}
df = pd.DataFrame(data)
print(df.head())

import matplotlib.pyplot as plt

df['Age'].hist()
plt.show()
