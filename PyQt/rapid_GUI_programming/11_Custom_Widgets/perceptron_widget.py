import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)
        layout = QGridLayout()
        centralWidget.setLayout(layout)

        perceptron1 = Perceptron(1)
        perceptron2 = Perceptron(2)
        perceptron3 = Perceptron(3)
        perceptron4 = Perceptron(4)

        layout.addWidget(perceptron1, 0, 0)
        layout.addWidget(perceptron2, 1, 0)
        layout.addWidget(perceptron3, 0, 1)
        layout.addWidget(perceptron4, 1, 1)


class Perceptron(QWidget):
    def __init__(self, bias, parent=None):
        super().__init__(parent)
        self.bias = bias
        self.setGeometry(0, 0, 300, 300)

    def paintEvent(self, e):
        painter = QPainter()
        painter.begin(self)
        painter.setViewport(0, 0, 300, 300)
        painter.setWindow(0, 0, 300, 300)
        pen = QPen()
        pen.setWidth(3)
        pen.setColor(QColor('black'))
        brush = QBrush()
        brush.setColor(QColor('red'))
        brush.setStyle(Qt.Dense1Pattern)
        painter.setBrush(brush)
        painter.setPen(pen)
        painter.drawRect(0, 0, self.width(), self.height())

        pen.setColor(QColor('black'))
        painter.setPen(pen)
        font = QFont()
        font.setFamily('Times')
        font.setBold(True)
        font.setPointSize(5)
        painter.setFont(font)
        painter.drawText(self.width()-10, self.height()-10, str(self.bias))

        painter.end()


app = QApplication(sys.argv)
mainWindow = MainWindow()
mainWindow.show()
app.exec_()

