import numpy as np
# Declaring two arrays to store both old and new state values
VS1 = np.zeros((4, 4))
VS2 = np.zeros((4, 4))

# The function takes old state values and gives new state values
def update_value_function(old_value_function):
    # To store new state values temporarily
    new_value_function = np.zeros((4, 4))
    for i, j in np.ndindex(old_value_function.shape):
        # To skip update in case of terminal states
        if (i == 0 and j == 0) or (i == 3 and j == 3):
            pass
        else:
            # We are going to accumulate all possible immediate reward and next state value pairs
            summation = 0
            # Four actions are possible
            for k in range(4):
                if k == 0:
                    # upward
                    x = i - 1
                    y = j
                if k == 1:
                    # downward
                    x = i + 1
                    y = j
                if k == 2:
                    # left
                    x = i
                    y = j - 1
                if k == 3:
                    # right
                    x = i
                    y = j + 1
                # Make position unchanged in case we take off the grid action
                if x < 0:
                    x = 0
                if x > 3:
                    x = 3
                if y < 0:
                    y = 0
                if y > 3:
                    y = 3
                summation = summation + (-1 + old_value_function[x][y]) * 0.25
            new_value_function[i][j] = summation
    return new_value_function

if __name__ == '__main__':
    # k is how many times we are going to calculate approximation
    k = 2000
    for i in range(k):
        VS2 = update_value_function(VS1)
        VS1 = VS2
    print('K = {0}, Our approximation is'.format(k))
    print(VS2)
