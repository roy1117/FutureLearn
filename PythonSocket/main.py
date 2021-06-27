# a = 'Hello\nHi'
# print(a.find('p'))
# pos = a.find('\n')
# print(a[:pos])
# print(a[pos + 1:])

def text_function():
    for i in range(0, 10):
        yield i

a= text_function()
print(type(a))
for i in a:
    print(i)

b = [1,2,3]
print(next(b))