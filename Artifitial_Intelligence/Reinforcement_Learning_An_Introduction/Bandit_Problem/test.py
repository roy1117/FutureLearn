import numpy as np
import matplotlib.pyplot as plt
import random

reward = np.zeros((10))
print(reward)
for i in range(10):
    reward[i] = np.random.normal(0, 1, None)
print(reward)
x = np.arange(10)
print(x)

b = np.array([5, 2, 3, 4, 5])
choice = np.random.choice(np.flatnonzero(b == b.max()))
print(choice)

print(random.randrange(1, 3))
# plt.plot(x, reward)
# plt.show()