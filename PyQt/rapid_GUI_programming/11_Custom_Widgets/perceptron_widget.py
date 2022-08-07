import sys
import numpy as np
import PyQt5.QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

MAX_RAW_VALUE = 3
MIN_RAW_VALUE = -3

def get_color(raw_value):
    blue_thickness, red_thickness = 0, 0
    half_value = (MAX_RAW_VALUE + MIN_RAW_VALUE)/2
    if raw_value > half_value:
        blue_thickness = int(((raw_value - half_value) / (MAX_RAW_VALUE - half_value)) * 255)
    else:
        red_thickness = 255 - int(((raw_value - MIN_RAW_VALUE) / (half_value - MIN_RAW_VALUE)) * 255)
    return QColor(red_thickness, 0, blue_thickness, 255)

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
        # for test only, need to be moved to arguments
        self.biases = [np.random.randn(y, 1) for y in sizes[1:]]
        self.weights = [np.random.randn(y, x)
                        for x, y in zip(sizes[:-1], sizes[1:])]
        print(self.weights[1])
        layout = QGridLayout()
        # Setting first layer
        self.network = []
        for layer, number_of_perceptrons in enumerate(self.sizes):
            self.network.append([])
            for i in range(number_of_perceptrons):
                if layer == 0:
                    bias = 0
                else:
                    bias = self.biases[layer-1][i][0]
                perceptron = Perceptron(bias)
                self.network[layer].append(perceptron)
                layout.addWidget(perceptron, i, layer)

        self.setLayout(layout)

    def paintEvent(self, e):
        super().paintEvent(e)
        painter = QPainter()
        painter.begin(self)
        painter.setViewport(0, 0, self.width(), self.height())
        pen = QPen()
        pen.setWidth(3)

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

                    weight = self.weights[layer][index_of_next_perceptron][index_of_previous_perceptron]
                    weight_color = get_color(weight)
                    pen.setColor(weight_color)
                    painter.setPen(pen)

                    painter.drawLine(outPoint, inPoint)

        painter.end()


class Perceptron(QWidget):
    def __init__(self, bias, parent=None):
        super().__init__(parent)
        self.bias = bias
        self.setMinimumSize(100, 100)
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

    def paintEvent(self, e):
        bias = round(self.bias, 3)
        painter = QPainter()
        painter.begin(self)
        painter.setViewport(0, 0, self.width(), self.height())
        pen = QPen()
        pen.setWidth(3)
        pen.setColor(QColor('white'))
        brush = QBrush()
        bias_color = get_color(bias)
        brush.setColor(bias_color)
        brush.setStyle(Qt.SolidPattern)
        painter.setBrush(brush)
        painter.setPen(pen)
        painter.drawEllipse(0, 0, self.width(), self.height())

        font = QFont()
        font.setFamily('Times')
        font.setBold(True)
        font.setPointSize(10)
        painter.setFont(font)
        painter.drawText(0, 0, self.width(), self.height(), Qt.AlignCenter, str(bias))

        painter.end()


app = QApplication(sys.argv)
mainWindow = MainWindow()
mainWindow.show()
app.exec_()

