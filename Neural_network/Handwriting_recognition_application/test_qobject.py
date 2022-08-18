from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys

class Student1():
    def __init__(self, name):
        self.name = name


class Student2(Student1, QObject):
    update_gui = pyqtSignal()

    def __init__(self, name):
        Student1.__init__(self, name)
        QObject.__init__(self)
        self.update_gui.connect(self.print_hi)

    def print_hi(self):
        print('Hi')


roy = Student2('Roy')
print(roy.name)