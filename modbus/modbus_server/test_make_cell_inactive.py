from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys

class Form(QDialog):
    def __init__(self):
        super().__init__()
        self.tableWidget = QTableWidget()
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(10)
        gridlayout = QGridLayout()
        gridlayout.addWidget(self.tableWidget)
        self.setLayout(gridlayout)
        self.testItem = QTableWidgetItem()
        self.testItem.setFlags(Qt.ItemFlags.)
        self.testItem = self.tableWidget.takeItem(1, 1)



app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()