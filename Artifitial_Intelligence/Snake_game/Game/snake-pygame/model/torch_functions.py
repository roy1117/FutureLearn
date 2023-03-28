import torch

tensor = torch.tensor([[1, 2, 3], [4, 5, 6]])
print(tensor)
max_component = torch.max(tensor)
print(max_component)
print(max_component.item())
calculation = 3 * max_component
print(calculation)

