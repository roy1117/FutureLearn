from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys

class ZeroSpinBox(QSpinBox):
    atzero = pyqtSignal(int, str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.valueChanged.connect(self.checkzero)
        self.atzero.connect(print_something)

    def checkzero(self, value):
        if value == 0:
            self.atzero.emit(123, 'hi')

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


def print_something(value1, value2, value3=10):
    print(value1, value2, value3)


app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()

