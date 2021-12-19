var_list = [1, 2, 'a', 'c']

for i in var_list:
    print(i)
# enumerate is useful when we need index of each element
for index, val in enumerate(var_list):
    print('index : {}'.format(index))
    print('value : {}'.format(val))

for i in enumerate(var_list):
    print(i)