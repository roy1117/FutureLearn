import numpy as np
import matplotlib.pyplot as plt
import copy

REWARD = 1
DISCOUNT_RATE = 1
PROBABILITY = 0.4
attempt = np.zeros(101)
summary = np.zeros(101)
ratio = np.zeros(101)
state_value = np.zeros(101)
policy = np.zeros(101)

def coin_filp():
    selection = np.random.randint(0, 10)
    if selection < 4:
        return True
    else:
        return False


def rand_action(state):
    return np.random.randint(0, min(state, 100 - state) + 1)


def get_action(state):
    return min(state, 100 - state) + 1


def value_evaluaion(old_state_value):
    new_state_value = np.zeros(101)
    for state in range(len(old_state_value) - 1):
        number_of_possible_actions = get_action(state)
        for action in range(number_of_possible_actions):
            temp = 0
            # lose
            temp += (1/number_of_possible_actions) * 0.6 * (DISCOUNT_RATE * old_state_value[state - action])
            # win
            if state + action == 100:
                reward = REWARD
            else:
                reward = 0
            temp += (1/number_of_possible_actions) * 0.4 * (reward + DISCOUNT_RATE * old_state_value[state + action])
            new_state_value[state] += temp
    return new_state_value


def value_iteration(old_state_value):
    new_state_value = np.zeros(101)
    policy = np.zeros(101)
    for state in range(len(old_state_value) - 1):
        number_of_possible_actions = get_action(state)
        temp = np.zeros(number_of_possible_actions)
        for action in range(number_of_possible_actions):
            # lose
            temp[action] += (1/number_of_possible_actions) * 0.6 * (DISCOUNT_RATE * old_state_value[state - action]) * 100000
            # win
            if state + action == 100:
                reward = REWARD
            else:
                reward = 0
            temp[action] += (1/number_of_possible_actions) * 0.4 * (reward + DISCOUNT_RATE * old_state_value[state + action]) * 100000
        max_action = np.argmax(temp)

        if state + max_action == 100:
            reward = REWARD
        else:
            reward = 0

        new_state_value[state] += 0.6 * (DISCOUNT_RATE * old_state_value[state - max_action]) + \
                                  0.4 * (reward + DISCOUNT_RATE * old_state_value[state + max_action])
        policy[state] = max_action
    return new_state_value, policy



if __name__ == '__main__':
    # for i in range(30000):
    #     # Set initial state randomly
    #     initial_state = np.random.randint(1, 100)
    #     state = initial_state
    #     while 1 <= state <= 99:
    #         bid = rand_action(state)
    #         if coin_filp():
    #             state = state + bid
    #         else:
    #             state = state - bid
    #     attempt[initial_state] += 1
    #     if state >= 100:
    #         summary[initial_state] += 1
    #         print('You won the game with initial state {0}'.format(initial_state))
    # for i in range(100):
    #     if attempt[i] != 0:
    #         ratio[i] = summary[i] / attempt[i]
    # print(attempt)
    # print(summary)
    # print(ratio)


    # # Value function test
    # for i in range(5000):
    #     state_value = value_evaluaion(state_value)
    # print(state_value)
    #
    # print(ratio - state_value)
    # print(max(ratio - state_value))

    # Value Iteration
    for i in range(5000):
        state_value, policy = value_iteration(state_value)
    print(state_value)
    print(policy)

    plt.plot(policy)
    plt.show()


