import numpy as np

height = np.array([1, 2, 3])
print(height)
print(type(height))

weight = np.array([100, 200 ,300])

ratio = height * weight
print(ratio)

wrong_height_data = np.array([False, 2, '3'])
print(wrong_height_data)
# ratio = wrong_height_data * weight
print(ratio)

height1 = [172, 174.4, 180]
height2 = [169, 178, 189]
height = height1 + height2
print(height)

height1 = np.array([172, 174.4, 180])
height2 = np.array([169, 178, 189])
height = height1 + height2
print(height)

print(height1 > 173)
print(height1[height1>173])

print(height1[np.array([False, False, True])])