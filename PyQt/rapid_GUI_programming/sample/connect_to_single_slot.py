from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys


class Form(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        button1 = QPushButton("One")
        button2 = QPushButton("Two")
        button3 = QPushButton("Three")
        layout = QHBoxLayout()
        layout.addWidget(button1)
        layout.addWidget(button2)
        layout.addWidget(button3)
        self.setLayout(layout)
        button1.clicked.connect(self.who_clicked)
        button2.clicked.connect(self.who_clicked)
        button3.clicked.connect(self.who_clicked)

    def who_clicked(self):
        who = self.sender().text()
        print('{0} clicked'.format(who))



app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()