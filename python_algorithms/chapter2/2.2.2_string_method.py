names = ['mike', 'jake', 'julia']
tuple_names = ('mike', 'jake', 'julia')
people = ",".join(names)
print(people)
people = ",".join(tuple_names)
print(people)

greeting = "hello World"
for i in reversed(greeting):
    print(i)

# split method
greeting = "Hi\nwho goes there"
words = greeting.splitlines()
print(words)

# spilt
path = r'C:\Users\taehy\AppData\Local\Programs\Python\Python38'
components = path.split("\\", 2)
print(components)

def erase_space_from_string(text):
    words = text.split()
    result = "".join(words)
    return result

a = erase_space_from_string(greeting)
print(a)