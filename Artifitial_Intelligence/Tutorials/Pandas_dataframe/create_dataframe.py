import pandas as pd
import numpy as np

my_2darray = np.array([[1, 2, 3], [4, 5, 6]])
print(my_2darray)

my_dataframe1 = pd.DataFrame(my_2darray)
print(my_dataframe1)

my_dict = {"a": ['1', '3'], "b": ['1', '2'], "c": ['2', '4']}
print(my_dict)
my_dataframe2 = pd.DataFrame(my_dict)
print(my_dataframe2)

my_dataframe3 = pd.DataFrame(my_2darray, index=range(0, 2), columns=["A", "B", "C"])
print(my_dataframe3)