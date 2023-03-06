import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D

# Read in data
x_vals = np.loadtxt('data/x.txt')
y_vals = np.loadtxt('data/y.txt')

# Throw out one data point so that there
# are an equal number from each class.
class_one = x_vals[:49, :]
class_two = x_vals[50:, :]

# Create data array for plotting
data = np.hstack((class_one, class_two))

# Create Pandas DataFrame for holding binary class data.
df = pd.DataFrame(data, columns=['x', 'y', 'x1', 'x2'])
print(df)
# Create scatter plot of data points in both classes.
class_ax = df.plot.scatter(x='x', y='y', color='Orange', label='+1')
df.plot.scatter(x='x1', y='x2', color='LightBlue', label='-1', ax=class_ax)

plt.show()