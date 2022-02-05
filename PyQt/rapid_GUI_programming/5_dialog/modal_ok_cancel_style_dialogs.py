from PyQt5.QtWidgets import *
import sys

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("modal ok cancel type practice")
        self.format = dict(thousandsseparator=",",
        decimalmarker=".", decimalplaces=2,
        rednegatives=False)
        print(self.format)
        self.setNumberFormat1()

    def setNumberFormat1(self):
        dialog = NumberFormatDlg(self.format, self)
        dialog.show()
        # dialog has accept() and reject() method
        # accept() terminates event loop with return value true
        # reject() terminates event loop with return value false
        # both methods emit accepted rejected signal respectively for users to connect custom slots

        if dialog.exec_():
            print('finished')

class NumberFormatDlg(QDialog):
    def __init__(self, format, parent=None):
        super().__init__(parent)

        # define widgets with default value passed by parent
        thousandsLabel = QLabel("&Thousands separator")
        self.thousandsEdit = QLineEdit(format["thousandsseparator"])
        thousandsLabel.setBuddy(self.thousandsEdit)
        decimalMarkerLabel = QLabel("Decimal &marker")
        self.decimalMarkerEdit = QLineEdit(format["decimalmarker"])
        decimalMarkerLabel.setBuddy(self.decimalMarkerEdit)
        decimalPlacesLabel = QLabel("&Decimal places")
        self.decimalPlacesSpinBox = QSpinBox()
        decimalPlacesLabel.setBuddy(self.decimalPlacesSpinBox)
        self.decimalPlacesSpinBox.setRange(0, 6)
        self.decimalPlacesSpinBox.setValue(format["decimalplaces"])
        self.redNegativesCheckBox = QCheckBox("&Red negative numbers")
        self.redNegativesCheckBox.setChecked(format["rednegatives"])
        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok |
                                     QDialogButtonBox.Cancel)
        # copy original data to modify
        self.format = format.copy()

        # set layout
        gridlayout = QGridLayout()
        gridlayout.addWidget(thousandsLabel, 0, 0)
        gridlayout.addWidget(self.thousandsEdit, 0, 1)
        gridlayout.addWidget(decimalMarkerLabel, 1, 0)
        gridlayout.addWidget(self.decimalMarkerEdit, 1, 1)
        gridlayout.addWidget(decimalPlacesLabel, 2, 0)
        gridlayout.addWidget(self.decimalPlacesSpinBox, 2, 1)
        gridlayout.addWidget(self.redNegativesCheckBox, 3, 0, 1, 2)
        gridlayout.addWidget(buttonBox, 4, 0, 1, 2)
        self.setLayout(gridlayout)

        # make connections
        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)
        self.accepted.connect(self.print_hi)
        self.rejected.connect(self.print_hello)

    def print_hi(self):
        print('hi')

    def print_hello(self):
        print('hello')

app = QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
app.exec_()