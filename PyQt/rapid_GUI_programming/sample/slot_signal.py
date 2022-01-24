from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys

class ZeroSpinBox(QSpinBox):
    atzero = pyqtSignal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.valueChanged.connect(self.checkzero)

    def checkzero(self, value):
        if value == 0:
            self.atzero.emit('hi')

class Form(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        dial = QDial()
        dial.setNotchesVisible(True)
        spinbox = ZeroSpinBox()
        layout = QHBoxLayout()
        layout.addWidget(dial)
        layout.addWidget(spinbox)
        self.setLayout(layout)
        dial.valueChanged.connect(spinbox.setValue)
        spinbox.valueChanged.connect(dial.setValue)
        spinbox.atzero.connect(self.print_something)

    def print_something(self, value):
        print(value)


app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()

