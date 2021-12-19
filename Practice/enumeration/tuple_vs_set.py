var_tuple = (1, 1, 'a', 'c')
print(var_tuple[1])
for i in var_tuple:
    print(i)

var_set = {1, 1, 2, 'a'}
# generate error
# print(var_set[1])
for i in var_set:
    print(i)

var_set1 = {1, 2, 3}
var_set2 = {1, 2, 4}
var_set3 = {1, 2}
print(var_set1.difference(var_set2))
print(var_set1.intersection(var_set2))
print(var_set3.issubset(var_set1))