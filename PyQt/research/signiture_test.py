import inspect

def signiture_test(a, b, c=10):
    print(a, b, c)


sig = inspect.signature(signiture_test)
for i in sig.parameters.values():
    print(i.name)