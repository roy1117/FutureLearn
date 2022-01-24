import sys
import urllib.request
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Form(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.data = {}
        message = self.set_data()
        print(self.data)
        self.fromComboBox = QComboBox()
        self.fromComboBox.addItems(["hello", "hi"])
        self.fromSpinBox = QDoubleSpinBox()
        self.fromSpinBox.setRange(0.1, 1000000)
        self.toComboBox = QComboBox()
        self.toComboBox.addItems(["hello", "hi"])
        self.toLabel = QLabel("1.00")

        grid = QGridLayout()
        grid.addWidget(self.fromComboBox, 1, 0)
        grid.addWidget(self.toComboBox, 2, 0)
        grid.addWidget(self.fromSpinBox, 1, 1)
        grid.addWidget(self.toLabel, 2, 1)
        self.setLayout(grid)

    def set_data(self): # Idea taken from the Python Cookbook
        try:
            date = "Unknown"
            self.fh = urllib.request.urlopen(
                "https://www.bankofcanada.ca/valet/observations/group/FX_RATES_DAILY/csv?start_date=2021-01-14")
            for i in self.fh:
                print(i)
            meta_data = self.get_text(whole_text=self.fh, start_text="id", end_text="OBSERVATIONS")
            meta_data = meta_data.replace('"', "")
            meta_data = meta_data.split("\n")
            for line in meta_data:
                if line == "\n":
                    continue
                else:
                    line = line.split(",")
                    if line[0].startswith("FX"):
                        self.data[line[0]] = {"id": line[1], "description": line[2]}

            rate_data = self.get_text(whole_text=self.fh, start_text="date", end_text="\n\n")
            print(rate_data)

                    # try:
                    #
                    # except ValueError:
                    #     pass
            return "Exchange Rates Date: " + date
        except Exception as e:
            return "Failed to download:\n%s" % e

    def get_text(self, whole_text, start_text, end_text):
        text = ""
        found_flag = False
        for line in whole_text:
            string = line.decode()
            if string == "\n":
                continue
            if found_flag:
                text = text + string
            if string.find(start_text) != -1:
                found_flag = True
            if string.find(end_text) != -1:
                break
        return text

app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()