from PyQt5.QtWidgets import *
import sys
from pyModbusTCP.server import ModbusServer, DataBank

class Form(QDialog):
    def __init__(self):
        super().__init__()
        self.server = ModbusServer("127.0.0.1", 502, no_block=True)
        self.server.start()
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(20)
        self.tableWidget.setColumnCount(4)

        layout = QGridLayout()
        layout.addWidget(self.tableWidget, 0, 0)
        self.setLayout(layout)

        self.tableWidget.setItem(0, 0, QTableWidgetItem('Apple'))
        self.tableWidget.setItem(1, 1, QTableWidgetItem('Banana'))
        self.tableWidget.setHorizontalHeaderItem(0, QTableWidgetItem('my favorite'))
        self.tableWidget.setHorizontalHeaderItem(1, QTableWidgetItem('what i dont like'))
        self.tableWidget.setVerticalHeaderItem(0, QTableWidgetItem('Frist'))
        self.tableWidget.setVerticalHeaderItem(1, QTableWidgetItem('Second'))

        self.tableWidget.itemClicked.connect(self.print_item)
        self.tableWidget.cellClicked.connect(self.print_index)

    def print_item(self, item):
        print(item.text())

    def print_index(self, row, col):
        print(row, col)

app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()