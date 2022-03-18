from model import Ui_MainWindow
from PyQt5.QtWidgets import *
import sys

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.centralwidget.setLayout(self.gridLayout)


# class MainWindow(QMainWindow):
#     def __init__(self, parent=None):
#         super().__init__(parent)
#         centralWidget = QWidget()
#         self.setCentralWidget(centralWidget)
#
#         pushbutton1 = QPushButton('button1')
#         pushbutton2 = QPushButton('button2')
#
#         gridlayout = QGridLayout()
#         gridlayout.addWidget(pushbutton1, 0, 0)
#         gridlayout.addWidget(pushbutton2, 0, 1)
#         centralWidget.setLayout(gridlayout)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()