import numpy as np
import matplotlib.pyplot as plt


PROBABILITY = 0.4
attempt = np.zeros(100)
summary = np.zeros(100)
ratio = np.zeros(100)


def coin_filp():
    selection = np.random.randint(0, 10)
    if selection < 4:
        return True
    else:
        return False


def rand_action(state):
    return np.random.randint(0, min(state, 100 - state) + 1)


if __name__ == '__main__':
    for i in range(1000):
        # Set initial state randomly
        initial_state = np.random.randint(1, 100)
        state = initial_state
        while 1 <= state <= 99:
            bid = rand_action(state)
            if coin_filp():
                state = state + bid
            else:
                state = state - bid
        attempt[initial_state] += 1
        if state >= 100:
            summary[initial_state] += 1
            print('You won the game with initial state {0}'.format(initial_state))
    for i in range(100):
        if attempt[i] != 0:
            ratio[i] = summary[i] / attempt[i]
    print(attempt)
    print(summary)
    print(ratio)
    plt.plot(ratio)
    plt.show()


