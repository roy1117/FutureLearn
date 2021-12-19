import copy

a = 3
b = a
print(id(a))
print(id(b))

# even though it looks like a's value has been changed.
# actually what happened is
# one more int object is created and a is now referenced to that new object
a = 4
print(a)
print(b)
print(id(a))
print(id(b))

list1 = [1, 2, 'abc']
for i in list1:
    print(i)
tuple1 = (1, 2, 'abc')
for i in list1:
    print(i)
# even though list and tuple look the same but tuple is immutable
print(list1[0])
print(tuple1[0])

# tuple you can't change value inside
list1[0] = 10
# tuple1[0] = 10

print(id(tuple1))
# the only way to change its value is to create other tuple object
tuple1 = (10, 2, 'abc')
print(id(tuple1))

# copy & deep copy
list1 = [1, 2, 3]
list2 = list1
list1[0] = 0
print(list2)

def change_list(list):
    list[0] = 0
    return list

list3 = [1, 2, 3]
list4 = list3
change_list(list3)
print(list4)

list5 = [1, 2, 3]
list6 = copy.deepcopy(list5)
change_list(list3)
print(list6)
