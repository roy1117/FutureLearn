import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

matrix = np.matrix([[1, 3], [2, 5]])
print('numpy matrix')
print(matrix)

df = pd.DataFrame(matrix, columns=["math", "computer", "color"], index=['A', 'B'])
print('pandas data frame')
print(df)

df.plot.bar()
df.plot.line()
df.plot.scatter(x='math', y='computer', color='blue', label='A')
plt.show()