import numpy as np
import copy


CURRENT_STATE = np.zeros((8, 8))
CURRENT_POLICY = [[0, 0, 0, 0],
                  [0, 0, 0, 0],
                  [0, 0, 0, 0],
                  [0, 0, 0, 0]]
random_policy = (0.25, 0.25, 0.25, 0.25)
for i in range(4):
    for j in range(4):
        CURRENT_POLICY[i][j] = random_policy
print(CURRENT_POLICY)


def get_randome_action():
    selection = np.random.randint(0, 4)
    return selection


def test_get_action(iteration):
    summary = np.zeros(4)
    for i in range(iteration):
        choice = get_randome_action()
        summary[choice] += 1
    print(summary)


def get_actual_action(choice):
    result = np.random.randint(0, 10)
    if result <= 1:
        return get_randome_action()
    else:
        return choice


def test_get_actual_action(iteration, choice):
    summary = np.zeros(4)
    for i in range(iteration):
        result = get_actual_action(choice)
        summary[result] += 1
    print(summary)


def evaluate_value_function(state, policy):
    new_state = copy.deepcopy(state)
    col, row = np.shape(state)
    for i in range(col):
        for j in range(row):
            temp



if __name__ == '__main__':
    test_get_actual_action(1000, 1)