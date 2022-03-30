from threading import Thread, Lock
from time import sleep

number_of_students = 0
lock = Lock()

class Calculator(Thread):

    global number_of_students

    def __init__(self, identifier):
        super().__init__()
        self.identifier = identifier

    def run(self):
        self.increase_number(self.identifier)

    @ classmethod
    def increase_number(cls, identifier):
        global number_of_students
        for _ in range(100000):
            number_of_students += 1

    @ classmethod
    def safe_increase_number(cls, identifier):
        global number_of_students
        lock.acquire()
        number_of_students += 1
        lock.release()


for i in range(70):
    i = Calculator(i)
    i.start()
    i.join()
print(number_of_students)

