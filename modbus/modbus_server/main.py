from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
from threading import Thread
from pyModbusTCP.server import ModbusServer, DataBank
import time

class Form(QMainWindow):
    def __init__(self):
        super().__init__()
        self.prev_data = [0] * 40
        self.connectionForm = ConnectionForm()
        self.address = None
        self.port = None
        self.make_connection()

        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(10)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.itemChanged.connect(self.print_changed_item)

        self.testLabel = QLabel('Hello')

        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)

        layout = QGridLayout()
        layout.addWidget(self.tableWidget, 0, 0)
        layout.addWidget(self.testLabel, 0, 1)
        centralWidget.setLayout(layout)

        fileNewAction = QAction("&Connection", self)
        helpText = "Connection Setting"
        fileNewAction.setToolTip(helpText)
        fileNewAction.setStatusTip(helpText)
        fileNewAction.triggered.connect(self.make_connection)

        fileMenu = QMenuBar()
        fileMenu.addAction(fileNewAction)
        self.setMenuBar(fileMenu)

        # data_update_thread = Thread(target=self.check_data_bank_changed)
        # data_update_thread.daemon = True
        # data_update_thread.start()
        self.number = 0
        self.check_data_bank_changed()

    def make_connection(self):
        if self.connectionForm.exec_():
            try:
                self.address, self.port = self.connectionForm.get_connection_info()
                self.server = ModbusServer(self.address, self.port, no_block=True)
                self.server.start()
                self.setWindowTitle('modbus slave, ip address : {0}, port : {1}'.format(self.address, self.port))
            except Exception as e:
                print(e)
                QMessageBox.warning(self, 'Connection error', 'cannot make a connection!')
                self.make_connection()

    def print_changed_item(self, item):
        row = item.row()
        col = item.column()
        address = col * 10 + row
        pre_val = DataBank.get_words(address)[0]
        if item.text() == str(pre_val):
            return
        else:
            try:
                val = int(item.text())
                self.set_modbus_value(address, val)
            except Exception as e:
                # QMessageBox.warning(self, 'Warning', 'Only integer is acceptable')
                self.tableWidget.setItem(row, col, QTableWidgetItem(str(pre_val)))
                print(e)

    def set_modbus_value(self, address, val):
        DataBank.set_words(address, [val])

    def check_data_bank_changed(self):

        # new_data = DataBank.get_words(0, 40)
        # for i in range(40):
        #     if self.prev_data[i] != new_data[i]:
        #         row = i % 10
        #         col = int(i / 10)
        #         self.tableWidget.setItem(row, col, QTableWidgetItem(str(new_data[i])))
        #         self.tableWidget.update()
        #         self.prev_data[i] = new_data[i]
        self.number = self.number + 1
        self.tableWidget.setItem(1, 1, QTableWidgetItem(str(self.number)))
        self.tableWidget.resize(self.tableWidget.width(), self.tableWidget.height())
        self.testLabel.setText(str(self.number))
        self.timer = QTimer()
        self.timer.setInterval(1)
        self.timer.timeout.connect(self.check_data_bank_changed)


class ConnectionForm(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('connection setting')
        self.address = '127.0.0.1'
        self.port = 502
        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok |
                                     QDialogButtonBox.Cancel)

        addressLabel = QLabel("&Ip address")
        self.addressEdit = QLineEdit(self.address)
        addressLabel.setBuddy(self.addressEdit)

        portLabel = QLabel("&Port")
        self.portEdit = QLineEdit(str(self.port))
        portLabel.setBuddy(self.portEdit)

        layout = QGridLayout()
        layout.addWidget(addressLabel, 0, 0)
        layout.addWidget(self.addressEdit, 0, 1)
        layout.addWidget(portLabel, 1, 0)
        layout.addWidget(self.portEdit, 1, 1)
        layout.addWidget(buttonBox, 2, 0, 1, 2)
        self.setLayout(layout)

        buttonBox.accepted.connect(self.my_accept)
        buttonBox.rejected.connect(self.reject)

    def my_accept(self):
        try:
            self.address = self.addressEdit.text()
            self.port = int(self.portEdit.text())
            self.accept()
        except Exception as e:
            print(e)
            QMessageBox.warning(self, 'Value error', 'Wrong value!')
            self.portEdit.selectAll()
            self.portEdit.setFocus()

    def get_connection_info(self):
        return self.address, self.port



app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()