from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from time import sleep
import sys

class Form(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        progressLabel = QLabel('Progress')
        layout = QGridLayout()
        layout.addWidget(progressLabel, 0, 0)
        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)
        centralWidget.setLayout(layout)
        QTimer.singleShot(5000, self.load_files)

    def load_files(self):
        for i in range(10):
            print('Hi')
            sleep(1)

    def print_hi(self):
            print('hi')

app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()
