class Student:
    def __init__(self):
        self.name = None

    def set_name(self, name):
        self.name = name

    def set_name(self, name, number):
        self.name = name
        print(number)

roy = Student()
roy.set_name('roy')
print(roy.name)