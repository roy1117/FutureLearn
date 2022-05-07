class Student:
    def __init__(self, number):
        self.number = number

    def __add__(self, Student):
        return self.number + Student.number


roy = Student(13)
mike = Student(2)

result = roy + mike
print(result)