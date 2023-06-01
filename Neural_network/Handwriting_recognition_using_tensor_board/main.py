import mnist_loader
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import random
import torch
import numpy as np
from torch.utils.tensorboard import SummaryWriter
training_data, validation_data, test_data = mnist_loader.load_data_wrapper()

training_data_x, training_data_y = list(zip(*training_data))
training_data_x = training_data_x[0:10000]
training_data_y = training_data_y[0:10000]
training_data_x = np.array(training_data_x)
training_data_y = np.array(training_data_y)
training_data_x = torch.tensor(training_data_x, dtype=torch.float)
training_data_y = torch.tensor(training_data_y, dtype=torch.float)
training_data_x = training_data_x.reshape(len(training_data_x), 1, 784)
training_data_y = training_data_y.reshape(len(training_data_y), 1, 10)
training_data = zip(training_data_x, training_data_y)
training_data = list(training_data)

test_data_x, test_data_y = list(zip(*test_data))
test_data_x = np.array(test_data_x)
test_data_y = np.array(test_data_y)
test_data_x = torch.tensor(test_data_x, dtype=torch.float)
test_data_x = test_data_x.reshape(len(test_data_x), 1, 784)
test_data = zip(test_data_x, test_data_y)
test_data = list(test_data)

class Network(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super().__init__()
        self.linear1 = nn.Linear(input_size, hidden_size)
        self.linear2 = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        x = F.sigmoid(self.linear1(x))
        x = F.sigmoid(self.linear2(x))
        return x


class Trainer:
    def __init__(self, model, lr):
        self.lr = lr
        self.model = model
        self.optimizer = optim.Adam(model.parameters(), lr=self.lr)
        self.criterion = nn.MSELoss()

    def train_step(self, training_data, test_data, epochs, mini_batch_size):
        for j in range(epochs):
            random.shuffle(training_data)
            n = len(training_data)
            n_test= len(test_data)
            mini_batches = [
                training_data[k:k + mini_batch_size]
                for k in range(0, n, mini_batch_size)]
            for mini_batch in mini_batches:
                for x, y in mini_batch:
                    self.optimizer.zero_grad()
                    pred = self.model(x)
                    loss = self.criterion(y, pred)
                    loss.backward()
                    self.optimizer.step()
            writer = SummaryWriter("torchlogs/")
            writer.add_graph(model, x)
            writer.close()
            print("Epoch {} : {} / {}".format(j, self.evaluate(test_data), n_test))
            print("Epoch {} complete".format(j))


    def evaluate(self, test_data):
        """Return the number of test inputs for which the neural
        network outputs the correct result. Note that the neural
        network's output is assumed to be the index of whichever
        neuron in the final layer has the highest activation."""
        test_results = []
        for x, y in test_data:
            pred = model(x)
            test_results.append((torch.argmax(pred), y))
        return sum(int(x == y) for (x, y) in test_results)

if __name__ == '__main__':
    model = Network(784, 32, 10)
    trainer = Trainer(model, 0.03)
    trainer.train_step(training_data, test_data, 30, 1)
