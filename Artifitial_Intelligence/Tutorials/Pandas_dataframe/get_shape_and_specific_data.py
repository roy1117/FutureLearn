import pandas as pd
import numpy as np

my_array = np.array([[1, 2, 3], [4, 5, 6]])
print(my_array)

my_data_frame = pd.DataFrame(my_array, index=[0,1], columns=["A", "B", "C"])
print(my_data_frame.shape)
print(my_data_frame.index)

print(my_data_frame.loc[1])
print(my_data_frame.iloc[1])