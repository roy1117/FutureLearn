# string slicing
string = "Hello World and eveyone!"
print(string[-1])
print(string[:-1])
# including start letter and excluding end letter
print(string[2:-1])
# order is [start:stop:step]
print(string[2:8:2])
for i in string[2:4:1]:
    print(i)

# dictionary
dictionary = {"address": "abc123", "phone_number": "123-456"}
# dictionary isn't ordered variable
# print(dictionary[0])

# set
set = {"happy", "angry", "trauma"}
# set isn't ordered variable
# print(set[1])

