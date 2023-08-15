import numpy as np

VS1 = np.zeros((4, 4))
VS2 = np.zeros((4, 4))


def update_value_function(old_value_function):
    new_value_function = np.zeros((4, 4))
    for i, j in np.ndindex(old_value_function.shape):
        if (i == 0 and j == 0) or (i == 3 and j == 3):
            pass
        else:
            summation = 0
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
    for i in range(2000):
        VS2 = update_value_function(VS1)
        VS1 = VS2
    print(VS2)
