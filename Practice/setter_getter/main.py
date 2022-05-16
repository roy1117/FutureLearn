class Student:
    def __init__(self, name):
        self._name = name

    def get_name(self):
        print('getter method is called')
        return self._name

    def set_name(self, name):
        print('setter method is called')
        self._name = name

    def del_name(self):
        del self._name
        print('delete method is called')

    message = 'This is help message'
    name = property(fset=set_name, fget=get_name, fdel=del_name, doc=message)

roy = Student('Roy')
roy.name = 'Roy!'
print(roy.name)
del(roy.name)