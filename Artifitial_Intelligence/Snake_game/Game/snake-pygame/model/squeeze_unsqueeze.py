import torch
import numpy as np

np_array = np.array([[[1, 1], [2, 2], [3, 3]]])
print(np_array)
tensor_array = torch.tensor(np_array)
print(tensor_array)
print(tensor_array.size())

squeezed_array = tensor_array.squeeze()
print(squeezed_array)
print(squeezed_array.size())

unsqueezed_array = squeezed_array.unsqueeze(1)
print(unsqueezed_array)
print(unsqueezed_array.size())


test_array = np.array([1, 2, 3, 4, 5])
print(len(torch.tensor(test_array).size()))