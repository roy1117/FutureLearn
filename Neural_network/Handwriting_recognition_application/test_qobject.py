from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys

class Student1(QObject):
    update_gui = pyqtSignal()

    def __init__(self, name):
        super().__init__()
        self.name = name

    def check_input(self):
        while True:
            if input("Enter input") == 'yes':
                self.update_gui.emit()

class School():
    def __init__(self):
        self.roy = Student1('Roy')
        self.roy.update_gui.connect(self.print_hi)

    def print_hi(self):
        print('Hi')


harvard = School()
harvard.roy.check_input()