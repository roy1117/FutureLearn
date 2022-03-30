from PyQt5.QtWidgets import *
import sys


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__()
        self.setWindowTitle('tutorial1')

        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)

        self.button1 = QPushButton('button')
        self.dial1 = QDial()

        gridlayout = QGridLayout()
        gridlayout.addWidget(self.button1, 0, 0)
        gridlayout.addWidget(self.dial1, 0, 1)
        centralWidget.setLayout(gridlayout)

        self.button1.clicked.connect(self.print_hi)
        self.dial1.valueChanged.connect(self.print_value)

    def print_hi(self):
        print('hi')

    def print_value(self, value):
        print(value)



app = QApplication(sys.argv)
mainwindow = MainWindow()
mainwindow.show()
app.exec_()
