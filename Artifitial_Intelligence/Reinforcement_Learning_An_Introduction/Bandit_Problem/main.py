import matplotlib.pyplot as plt
import numpy as np
import random

EPSILON = 0.3
TOTAL_NUMBER_OF_RUNS = 20000
expected_value = np.random.normal(0, 1, 10)
print(expected_value)
is_action_value_initial = np.ones(10, dtype=bool)
print(is_action_value_initial)
action_value = np.zeros(10)
optimal_choice_probability = np.zeros(TOTAL_NUMBER_OF_RUNS)


def get_actual_reward(action_choice):
    reward = np.random.normal(expected_value[action_choice], 1, 1)
    return reward


def get_max_action_value():
    return np.random.choice(np.flatnonzero(action_value == action_value.max()))


def make_decision():
    # Random move
    if random.random() < EPSILON:
        return random.randrange(0, 10)
    else:
        return get_max_action_value()


def update_action_value(action_choice, reward, n):
    action_value[action_choice] = (n * action_value[action_choice] + reward) / (n + 1)


def update_optimal_choice_probability(action_choice, n):
    if action_choice == np.argmax(expected_value):
        is_optimal_choice = 1
    else:
        is_optimal_choice = 0
    if n == 0:
        optimal_choice_probability[0] = is_optimal_choice / 1
    else:
        optimal_choice_probability[n] = (optimal_choice_probability[n-1] * n + is_optimal_choice) / (n + 1)


for n in range(0, TOTAL_NUMBER_OF_RUNS):
    action_choice = make_decision()
    print(action_choice)
    reward = get_actual_reward(action_choice)
    update_action_value(action_choice, reward, n)
    update_optimal_choice_probability(action_choice, n)

print('Estimation was')
print(action_value)
print('Actual value was')
print(expected_value)
print('Optimal choice was')
print(np.argmax(expected_value))

plt.plot(np.arange(TOTAL_NUMBER_OF_RUNS), optimal_choice_probability)
plt.show()