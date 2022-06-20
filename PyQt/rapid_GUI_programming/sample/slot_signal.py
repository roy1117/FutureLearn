from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys

class Student:
    def __init__(self, name=None):
        self.name = name

class ZeroSpinBox(QSpinBox):
    # when we defined custom signal, we should pass python types which we want to emit
    # we can emit even user defined class
    atzero = pyqtSignal(int, str, Student)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.valueChanged.connect(self.checkzero)
        # Connection of signal to slot
        self.atzero.connect(print_something)

    def checkzero(self, value):
        # We generate signal at certain place of application
        if value == 0:
            roy = Student()
            self.atzero.emit(123, 'hi', roy)


class Form(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        dial = QDial()
        dial.setNotchesVisible(True)
        spinbox = ZeroSpinBox()
        spinbox2 = ZeroSpinBox()
        layout = QHBoxLayout()
        layout.addWidget(dial)
        layout.addWidget(spinbox)
        layout.addWidget(spinbox2)
        self.setLayout(layout)
        dial.valueChanged.connect(spinbox.setValue)
        spinbox.valueChanged.connect(dial.setValue)

# When we use signal-slot approach, we should be careful with number of parameters and parameter type.
# If there is mismatch, program ends without proper error message.
# Is it good idea to put exception handling in all slots?
def print_something(value1, value2, value3=10):
    try:
        print(value1, value2, value3.name)
    except Exception as e:
        print(e)


app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()

