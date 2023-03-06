import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

matrix = np.matrix([[10, 30], [20, 50], [100, 50]])
print('numpy matrix')
print(matrix)

df = pd.DataFrame(matrix, columns=["math", "computer"], index=['A', 'B', 'C'])
print('pandas data frame')
print(df)
colors = ['red', 'blue', 'orange']
print(df.head(0))
# df.plot.bar()
# df.plot.line()
# df.plot.scatter(x='math', y='computer', color=colors, label='A')
# plt.show()