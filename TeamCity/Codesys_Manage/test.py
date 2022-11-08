fruits = ['apple', 'banana', 'tomato']

while True:
    if fruits == []:
        print('nothing left')
        break
    else:
        i = fruits[0]
        print(i)
        fruits.remove(i)
        print(fruits)

print('finished')