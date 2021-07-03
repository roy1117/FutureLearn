a = ''
if not a:
    print('yes')
else:
    print('No')

a = None
if not a:
    print('yes')
else:
    print('No')

a = 0
if not a:
    print('yes')
else:
    print('No')

a = False
if not a:
    print('yes')
else:
    print('No')

print(False == 0)
print(not '')
print(not None)


def yield_test(message):
    for i in message:
        yield i


a = 'Hello, world!'
# iterate generator function
for i in yield_test(a):
    print(i)


# another way to iterate generator function but not efficient
b = iter(yield_test(a))
print(next(yield_test(b)))
print(next(yield_test(b)))
print(next(yield_test(b)))# iterate generator function
print(next(yield_test(b)))
print(next(yield_test(b)))


b = iter('Hi! Mike')
print(next(yield_test(b)))
print(next(yield_test(b)))
print(next(yield_test(b)))
print(next(yield_test(b)))
print(next(yield_test(b)))


