def print_number(a):
    while True:
        a = a + 1
        print('execute until here')
        yield a
        print('next execution')

a = print_number(1)
print(next(a))
print(next(a))
print(next(a))

# example
def fibo():
    base0 = 0
    base1 = 1
    yield base0
    yield base1
    while True:
        sum = base0 + base1
        yield sum
        base0 = base1
        base1 = sum

fibo_number = fibo()
for i in range(10):
    print(next(fibo_number))