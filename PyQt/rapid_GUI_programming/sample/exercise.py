from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys

class Form(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        label1 = QLabel("Principla:")
        self.spinbox1 = QDoubleSpinBox()
        self.spinbox1.setSingleStep(10)
        self.spinbox1.setPrefix("$ ")
        label2 = QLabel("Rate:")
        self.spinbox2 = QDoubleSpinBox()
        self.spinbox2.setSuffix(" %")
        label3 = QLabel("Years:")
        self.combobox = QComboBox()
        self.combobox.addItems(["1 years", "2 years", "3 years"])
        label4 = QLabel("Amount")
        self.interest_label = QLabel()
        layout = QGridLayout()
        layout.addWidget(label1, 0, 0)
        layout.addWidget(self.spinbox1, 0, 1)
        layout.addWidget(label2, 1, 0)
        layout.addWidget(self.spinbox2, 1, 1)
        layout.addWidget(label3, 2, 0)
        layout.addWidget(self.combobox, 2, 1)
        layout.addWidget(label4, 3, 0)
        layout.addWidget(self.interest_label, 3, 1)
        self.spinbox1.valueChanged.connect(self.calculate_interest)
        self.spinbox2.valueChanged.connect(self.calculate_interest)
        self.combobox.currentTextChanged.connect(self.calculate_interest)
        self.setLayout(layout)

    def calculate_interest(self):
        principal = self.spinbox1.value()
        rate = self.spinbox2.value()
        years = self.combobox.currentText()
        years = int(years[0])
        interest = principal * ((1+(rate/100.0))**years)
        interest = round(interest, 2)
        self.interest_label.setText("$ "+str(interest))

app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()