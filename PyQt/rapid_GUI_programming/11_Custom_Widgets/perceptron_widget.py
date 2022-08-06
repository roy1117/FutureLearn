import sys

import PyQt5.QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.resize(1500, 800)

        neuronNetwork = NeuronNetowrk(sizes=[30, 16, 10])
        scrollArea = QScrollArea()
        scrollArea.setWidget(neuronNetwork)
        self.setCentralWidget(scrollArea)
        scrollArea.setWidgetResizable(True)


class NeuronNetowrk(QWidget):
    def __init__(self, sizes, parent=None):
        super().__init__(parent)
        self.sizes = sizes
        layout = QGridLayout()
        # Setting first layer
        self.network = []
        for layer, number_of_perceptrons in enumerate(self.sizes):
            self.network.append([])
            for i in range(number_of_perceptrons):
                perceptron = Perceptron(i+1)
                self.network[layer].append(perceptron)
                layout.addWidget(perceptron, i, layer)

        self.setLayout(layout)

    def paintEvent(self, e):
        super().paintEvent(e)
        painter = QPainter()
        painter.begin(self)
        painter.setViewport(0, 0, self.width(), self.height())
        pen = QPen()
        pen.setColor(QColor('black'))
        pen.setWidth(3)
        painter.setPen(pen)

        for layer in range(len(self.sizes)-1):
            for index_of_previous_perceptron in range(self.sizes[layer]):
                for index_of_next_perceptron in range(self.sizes[layer+1]):
                    rect = self.network[layer][index_of_previous_perceptron].geometry()
                    x = rect.x()
                    y = rect.y()
                    width = rect.width()
                    height = rect.height()
                    outPoint = QPoint(x+width, y+int(height/2))

                    rect = self.network[layer+1][index_of_next_perceptron].geometry()
                    x = rect.x()
                    y = rect.y()
                    width = rect.width()
                    height = rect.height()
                    inPoint = QPoint(x, y + int(height / 2))

                    painter.drawLine(outPoint, inPoint)

        painter.end()


class Perceptron(QWidget):
    def __init__(self, bias, parent=None):
        super().__init__(parent)
        self.bias = bias
        self.setMinimumSize(100, 100)
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

    def paintEvent(self, e):
        painter = QPainter()
        painter.begin(self)
        painter.setViewport(0, 0, self.width(), self.height())
        pen = QPen()
        pen.setWidth(3)
        pen.setColor(QColor('black'))
        brush = QBrush()
        brush.setColor(QColor('red'))
        brush.setStyle(Qt.Dense1Pattern)
        painter.setBrush(brush)
        painter.setPen(pen)
        painter.drawEllipse(0, 0, self.width(), self.height())

        font = QFont()
        font.setFamily('Times')
        font.setBold(True)
        font.setPointSize(15)
        painter.setFont(font)
        painter.drawText(0, 0, self.width(), self.height(), Qt.AlignCenter, str(self.bias))

        painter.end()


app = QApplication(sys.argv)
mainWindow = MainWindow()
mainWindow.show()
app.exec_()

