from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys


class Form(QMainWindow):
    def __init__(self, parent=None):
        super().__init__()
        self.settings = QSettings("Mysoft", "Cheonan")

        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)

        self.sizeLabel = QLabel()
        self.lineEdit = QLineEdit()
        self.lineEdit.textChanged.connect(self.update_text)
        self.custLabel = QLabel()

        layout = QGridLayout()
        layout.addWidget(self.sizeLabel, 0, 0)
        layout.addWidget(self.lineEdit, 1, 0)

        layout.addWidget(self.custLabel, 2, 0)
        centralWidget.setLayout(layout)
        geometry = self.settings.value('geometry')
        text = self.settings.value('text')
        testTuple = self.settings.value('tuple')
        print(testTuple)
        self.custLabel.setText(text)
        print('saved geometry is {0}'.format(geometry))
        self.resize(geometry)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        message = 'height : {0}, width : {1}'.format(self.height(), self.width())
        self.sizeLabel.setText(message)

    def closeEvent(self, event):
        super().closeEvent(event)
        geometry = self.size()
        text = self.lineEdit.text()
        self.settings.setValue('geometry', geometry)
        self.settings.setValue('text', text)
        testTuple = (self.width(), self.height())
        self.settings.setValue('tuple', testTuple)
        print('last geometry is {0}'.format(geometry))
        print(type(geometry))

    def update_text(self, text):
        self.custLabel.setText(text)



app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()
