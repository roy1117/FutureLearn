class Student1():
    def __init__(self, name):
        print("Student1")
        self.name = name

class Student2():
    def __init__(self, number):
        print("Student2")
        self.number = number

class Student3(Student1, Student2):
    def __init__(self, name, number):
        Student1.__init__(self, name)
        Student2.__init__(self, number)

roy = Student3("Roy", 1234)
