import torch
from torch import nn

class MyNetwork(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(MyNetwork, self).__init__()
        self.nn1 = nn.Linear(input_size, hidden_size)
        self.nn2 = nn.Linear(hidden_size, output_size)
        print('nn1 weight: ', self.nn1.weight)
        print('nn1 bias: ', self.nn1.bias)
        print('nn2 weight: ', self.nn2.weight)
        print('nn2 bias: ', self.nn2.bias)

    def forward(self, inputs):
        temporary = self.nn1(inputs)
        return self.nn2(temporary)

input_data = torch.rand(5, 10)
print('input data: ', input_data)
myNetwrok = MyNetwork(10, 3, 3)
output = myNetwrok(input_data)
print('output: ', output)
print(1)
print(2)
print(3)

