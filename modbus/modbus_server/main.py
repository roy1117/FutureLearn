from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
from threading import Thread, Timer
from pyModbusTCP.server import ModbusServer, DataBank
import time

class Form(QMainWindow):
    def __init__(self):
        super().__init__()
        # Define variables in advance
        # Some of them have default value
        self.address = 0
        self.quantity = 10
        self.prevData = None
        self.connectionForm = ConnectionForm()
        self.slaveDefinitionForm = SlaveDefinitionForm()
        self.ipAddress = '127.0.0.1'
        self.port = 502
        self.updateModbusDataThread = None
        self.isThreadRunning = False
        self.columnOffset = None
        self.rowOffset = None

        # Define a table widget
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(10)
        self.tableWidget.setColumnCount(1)

        # Do layout work
        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)

        layout = QGridLayout()
        layout.addWidget(self.tableWidget, 0, 0)
        centralWidget.setLayout(layout)

        # Define menu and connect proper methods
        connectionAction = QAction("&Connection", self)
        helpText = "Connection Setting"
        connectionAction.setToolTip(helpText)
        connectionAction.setStatusTip(helpText)
        connectionAction.triggered.connect(self.ask_server_definition)

        setupAction = QAction("&Setup", self)
        helpText = "Slave Definition"
        setupAction.setToolTip(helpText)
        setupAction.setStatusTip(helpText)
        setupAction.triggered.connect(self.ask_slave_definition)

        fileMenu = QMenuBar()
        fileMenu.addAction(connectionAction)
        fileMenu.addAction(setupAction)
        self.setMenuBar(fileMenu)

        self.tableWidget.itemChanged.connect(self._handler_cell_value_changed)
        self.ask_server_definition()
        self.ask_slave_definition()



    def ask_server_definition(self):
        if self.connectionForm.exec_():
            try:
                self.ipAddress, self.port = self.connectionForm.get_connection_info()
            except Exception as e:
                print(e)
        self._open_server()

    def ask_slave_definition(self):
        if self.slaveDefinitionForm.exec_():
            try:
                self.address, self.quantity = self.slaveDefinitionForm.get_slave_definition_info()
                self.close_thread()
                self.set_default_value()
                self.start_thread()
            except Exception as e:
                print(e)
                QMessageBox.warning(self, 'Value error', 'cannot apply the setting!')

    def _open_server(self):
        try:
            self.server = ModbusServer(self.ipAddress, self.port, no_block=True)
            self.server.start()
            self.setWindowTitle('Modbus Slave, ip address : {0}, port : {1}'.format(self.ipAddress, self.port))
        except Exception as e:
            print(e)
            QMessageBox.warning(self, 'Connection error', 'cannot make a connection!')
            self.ask_server_definition()
        print('server opened successfully')
        # self.set_default_value()

    def thread_main(self):
        if self.isThreadRunning:
            self._handler_data_bank_changed()
            self.updateModbusDataThread = Timer(0.5, self.thread_main).start()

    def start_thread(self):
        self.isThreadRunning = True
        self.thread_main()

    def close_thread(self):
        self.isThreadRunning = False
        if self.updateModbusDataThread is not None:
            self.updateModbusDataThread.cancel()

    def set_default_value(self):
        self.tableWidget.itemChanged.disconnect(self._handler_cell_value_changed)
        self.prevData = DataBank.get_words(self.address, self.quantity)
        columnCount = int(len(self.prevData)/10+1)
        self.columnOffset = int(self.address/10)
        self.rowOffset = self.address - self.columnOffset * 10
        self.tableWidget.setColumnCount(columnCount)
        for i in range(columnCount):
            self.tableWidget.setHorizontalHeaderItem(i, QTableWidgetItem(str(i+self.columnOffset)))
        for i in range(10):
            self.tableWidget.setVerticalHeaderItem(i, QTableWidgetItem(str(i)))
        for i in range(columnCount * 10):
            row = i % 10
            col = int(i / 10)
            if i >= len(self.prevData) + self.rowOffset or i < self.rowOffset:
                item = QTableWidgetItem()
                item.setFlags(Qt.ItemFlag.NoItemFlags)
                self.tableWidget.setItem(row, col, item)
            else:
                self.tableWidget.setItem(row, col, QTableWidgetItem(str(self.prevData[i-self.rowOffset])))
        self.tableWidget.viewport().update()
        self.tableWidget.itemChanged.connect(self._handler_cell_value_changed)

    def _handler_cell_value_changed(self, item):
        row = item.row()
        col = item.column()
        index = col * 10 + row
        if index >= self.quantity + self.rowOffset:
            return
        pre_val = DataBank.get_words(index)[0]
        if item.text() == str(pre_val):
            return
        else:
            try:
                val = int(item.text())
                DataBank.set_words(self.columnOffset*10 + index, [val])
            except Exception as e:
                QMessageBox.warning(self, 'Warning', 'Only integer is acceptable')
                self.tableWidget.setItem(row, col, QTableWidgetItem(str(pre_val)))
                print(e)

    def _handler_data_bank_changed(self):
        newData = DataBank.get_words(self.address, self.quantity)
        for i in range(self.quantity):
            if self.prevData[i] != newData[i]:
                index = i + self.address - self.columnOffset * 10
                row = index % 10
                col = int(index / 10)
                self.tableWidget.setItem(row, col, QTableWidgetItem(str(newData[i])))
                self.prevData[i] = newData[i]
        self.tableWidget.viewport().update()


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