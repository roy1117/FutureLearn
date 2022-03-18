class A:
    counter = 99

    def __init__(self):
        print(self.counter)

a = A()
print(A.counter)