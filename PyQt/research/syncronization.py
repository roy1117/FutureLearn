from PyQt5.QtWidgets import *
import sys


class Form(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        tempsensor1 = Sensor(tag='tempsensor')
        tempsensor2 = Sensor(tag='tempsensor')
        tempsensor3 = Sensor(tag='tempsensor')
        pressuresensor1 = Sensor(tag='pressuresensor')
        pressuresensor2 = Sensor(tag='pressuresensor')
        pressuresensor3 = Sensor(tag='pressuresensor')
        gridlayout = QGridLayout()
        gridlayout.addWidget(tempsensor1, 0, 0)
        gridlayout.addWidget(tempsensor2, 0, 1)
        gridlayout.addWidget(tempsensor3, 0, 2)
        gridlayout.addWidget(pressuresensor1, 1, 0)
        gridlayout.addWidget(pressuresensor2, 1, 1)
        gridlayout.addWidget(pressuresensor3, 1, 2)
        self.setLayout(gridlayout)


class Sensor(QDial):
    sensor_group = {}

    def __init__(self, parent=None, tag=None):
        super().__init__(parent)
        self.tag = tag
        if tag in self.sensor_group:
            self.connect_group(tag)
            self.sensor_group[tag].append(self)
        else:
            self.sensor_group[tag] = [self]
        self.valueChanged.connect(self.print_value)

    def print_value(self, value):
        print('{0} : {1}'.format(self.tag, value))

    def connect_group(self, tag):
        for i in self.sensor_group[tag]:
            i.updateValue.connect(self.setValue)
        for i in self.sensor_group[tag]:
            self.valueChanged.connect(i.setValue)


app = QApplication(sys.argv)
form = Form()
form.show()
app.exec()



