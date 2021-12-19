from collections.abc import Iterable

# Iterable type of variables
var_list = [1, 3, 5, 7]
isiterable = isinstance(var_list, Iterable)
print('{0} is iterable : {1}'.format(var_list, isiterable))
for i in var_list:
    print(i)
print('---------------------------------------------------')

var_dict = {"a": 1, "b": 2}
isiterable = isinstance(var_dict, Iterable)
print('{0} is iterable : {1}'.format(var_dict, isiterable))
for i in var_dict:
    print(i)
print('---------------------------------------------------')

var_set = {1, 3}
isiterable = isinstance(var_set, Iterable)
print('{0} is iterable : {1}'.format(var_set, isiterable))
for i in var_set:
    print(i)
print('---------------------------------------------------')

var_str = "abc"
isiterable = isinstance(var_str, Iterable)
print('{0} is iterable : {1}'.format(var_str, isiterable))
for i in var_str:
    print(i)
print('---------------------------------------------------')

var_bytes = b'abcdef'
isiterable = isinstance(var_bytes, Iterable)
print('{0} is iterable : {1}'.format(var_bytes, isiterable))
for i in var_bytes:
    print(i)
print('---------------------------------------------------')

var_tutple = (1, 3, 5, 7)
isiterable = isinstance(var_tutple, Iterable)
print('{0} is iterable : {1}'.format(var_tutple, isiterable))
for i in var_tutple:
    print(i)
print('---------------------------------------------------')

var_range = range(0, 5)
isiterable = isinstance(var_list, Iterable)
print('{0} is iterable : {1}'.format(var_range, isiterable))
for i in var_range:
    print(i)
print('---------------------------------------------------')
