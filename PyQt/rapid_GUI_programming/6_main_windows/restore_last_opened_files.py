from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from time import sleep
import sys

class Form(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.settings = QSettings("Nasa", "Space-x")
        self.lastFilenames = self.settings.value("previous")
        if self.lastFilenames is None:
            self.lastFilenames = []
        print(self.lastFilenames)

        self.lineEdit = QLineEdit()

        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)
        gridLayout = QGridLayout()
        gridLayout.addWidget(self.lineEdit, 0, 0)
        centralWidget.setLayout(gridLayout)


        menubar = QMenuBar()
        self.setMenuBar(menubar)

        filemenu = QMenu("file", self)
        menubar.addMenu(filemenu)

        for i in self.lastFilenames:
            self.append_action(filemenu, i, self.print_hi)

    def append_action(self, menu, action_text, slot):
        action = QAction(action_text, self)
        action.triggered.connect(slot)
        menu.addAction(action)

    def print_hi(self):
        print('hi')

    def closeEvent(self, event):
        super().closeEvent(event)
        currentFilename = self.lineEdit.text()
        if currentFilename == '':
            return
        self.lastFilenames.insert(0, currentFilename)
        if len(self.lastFilenames) > 5:
            self.lastFilenames = self.lastFilenames[:5]
        self.settings.setValue("previous", self.lastFilenames)


app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()