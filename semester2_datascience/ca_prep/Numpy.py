import numpy as np
import pandas
data = np.array([5, 10, 15, 20, 25])
print("Mean:", np.mean(data))
print("Median:", np.median(data))
print("Std Dev:", np.std(data))
print("Max:", np.max(data))
print("Min:", np.min(data))


pf = pandas.DataFrame(data)
print('Pandas Version: ',pandas.__version__)
print(pf.head())