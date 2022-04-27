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
        self.address = 0
        self.quantity = 10
        self.prev_data = None
        self.connectionForm = ConnectionForm()
        self.slaveDefinitionForm = SlaveDefinitionForm()
        self.ipAddress = None
        self.port = None


        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(10)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.itemChanged.connect(self.edit_value)

        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)

        layout = QGridLayout()
        layout.addWidget(self.tableWidget, 0, 0)
        centralWidget.setLayout(layout)

        connectionAction = QAction("&Connection", self)
        helpText = "Connection Setting"
        connectionAction.setToolTip(helpText)
        connectionAction.setStatusTip(helpText)
        connectionAction.triggered.connect(self.open_server)

        setupAction = QAction("&Setup", self)
        helpText = "Slave Definition"
        setupAction.setToolTip(helpText)
        setupAction.setStatusTip(helpText)
        setupAction.triggered.connect(self.slave_definition_setup)

        fileMenu = QMenuBar()
        fileMenu.addAction(connectionAction)
        fileMenu.addAction(setupAction)
        self.setMenuBar(fileMenu)

        self.open_server()


    def start_thread(self):
        self.data_update_thread = Thread(target=self.check_data_bank_changed)
        self.data_update_thread.daemon = True
        self.data_update_thread.start()

    def close_thread(self):
        self.data_update_thread.stop()

    def open_server(self):
        if self.connectionForm.exec_():
            try:
                self.ipAddress, self.port = self.connectionForm.get_connection_info()
                self.server = ModbusServer(self.ipAddress, self.port, no_block=True)
                self.server.start()
                self.setWindowTitle('Modbus Slave, ip address : {0}, port : {1}'.format(self.ipAddress, self.port))
            except Exception as e:
                print(e)
                QMessageBox.warning(self, 'Connection error', 'cannot make a connection!')
                self.open_server()
            print('server opened successfully')
        self.set_default_value()

    def slave_definition_setup(self):
        if self.slaveDefinitionForm.exec_():
            try:
                self.address, self.quantity = self.connectionForm.get_connection_info()
                self.close_thread()
                self.set_default_value()
                self.start_thread()
            except Exception as e:
                print(e)
                QMessageBox.warning(self, 'Value error', 'cannot apply the setting!')


    def set_default_value(self):
        self.prev_data = DataBank.get_words(self.address, self.quantity)
        for i in range(self.quantity):
            row = i % 10
            col = int(i / 10)
            self.tableWidget.setItem(row, col, QTableWidgetItem(str(self.prev_data[i])))
            self.tableWidget.viewport().update()

    def edit_value(self, item):
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
        while True:
            new_data = DataBank.get_words(0, self.quantity)
            for i in range(self.quantity):
                if self.prev_data[i] != new_data[i]:
                    row = i % 10
                    col = int(i / 10)
                    self.tableWidget.setItem(row, col, QTableWidgetItem(str(new_data[i])))
                    self.tableWidget.viewport().update()
                    self.prev_data[i] = new_data[i]
            time.sleep(0.5)


class ConnectionForm(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('connection setting')
        self.ipAddress = '127.0.0.1'
        self.port = 502
        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok |
                                     QDialogButtonBox.Cancel)

        addressLabel = QLabel("&Ip address")
        self.addressEdit = QLineEdit(self.ipAddress)
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
            self.ipAddress = self.addressEdit.text()
            self.port = int(self.portEdit.text())
            self.accept()
        except Exception as e:
            print(e)
            QMessageBox.warning(self, 'Value error', 'Wrong value!')
            self.portEdit.selectAll()
            self.portEdit.setFocus()

    def get_connection_info(self):
        return self.ipAddress, self.port


class SlaveDefinitionForm(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('slave definition setup')
        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok |
                                     QDialogButtonBox.Cancel)
        self.address = 0
        self.quantity = 10
        addressLabel = QLabel("&Address")
        self.addressEdit = QLineEdit(str(self.address))
        addressLabel.setBuddy(self.addressEdit)

        quantityLabel = QLabel("&Quantity")
        self.quantityEdit = QLineEdit(str(self.quantity))
        quantityLabel.setBuddy(self.quantityEdit)

        layout = QGridLayout()
        layout.addWidget(addressLabel, 0, 0)
        layout.addWidget(self.addressEdit, 0, 1)
        layout.addWidget(quantityLabel, 1, 0)
        layout.addWidget(self.quantityEdit, 1, 1)
        layout.addWidget(buttonBox, 2, 0, 1, 2)
        self.setLayout(layout)

        buttonBox.accepted.connect(self.my_accept)
        buttonBox.rejected.connect(self.reject)

    def my_accept(self):
        try:
            self.address = int(self.addressEdit.text())
            self.quantity = int(self.quantityEdit.text())
            self.accept()
        except Exception as e:
            print(e)
            QMessageBox.warning(self, 'Value error', 'Wrong value!, only integer is acceptable')
            self.quantityEdit.selectAll()
            self.quantityEdit.setFocus()

    def get_slave_definition_info(self):
        return self.address, self.quantity


app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()