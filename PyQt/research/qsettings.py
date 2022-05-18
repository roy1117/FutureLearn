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

        layout = QGridLayout()
        layout.addWidget(self.sizeLabel, 0, 0)
        centralWidget.setLayout(layout)
        geometry = self.settings.value('geometry')
        print('saved geometry is {0}'.format(geometry))
        self.resize(geometry)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        message = 'height : {0}, width : {1}'.format(self.height(), self.width())
        self.sizeLabel.setText(message)

    def closeEvent(self, event):
        super().closeEvent(event)
        geometry = self.size()
        self.settings.setValue('geometry', geometry)
        print('last geometry is {0}'.format(geometry))
        print(type(geometry))


app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()
