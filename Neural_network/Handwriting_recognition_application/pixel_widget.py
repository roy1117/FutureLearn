from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

def get_input_color(thickness):
    rgb = int(thickness * 255)
    return QColor(rgb, rgb, rgb)

class PixelScreen(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMinimumSize(145, 145)
        self.setMaximumSize(145, 145)
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.pixels = []
        layout = QGridLayout()
        layout.setSpacing(0)
        for row in range(28):
            self.pixels.append([])
            for col in range(28):
                pixel = Pixel(1)
                self.pixels[row].append(pixel)
                layout.addWidget(pixel, row, col)
        self.setLayout(layout)

    def set_inputs(self, inputs):
        for row in range(28):
            for col in range(28):
                self.pixels[row][col].set_input(inputs[row*28+col][0])

class Pixel(QLabel):
    def __init__(self, input, parent=None):
        super().__init__(parent)
        self.input = input
        self.setMinimumSize(5, 5)
        self.setMaximumSize(5, 5)
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

    def set_input(self, input):
        self.input = input
        self.update()

    def paintEvent(self, event):
        super().paintEvent(event)
        painter = QPainter()
        painter.begin(self)
        painter.setViewport(0, 0, self.width(), self.height())

        brush = QBrush()
        color = get_input_color(self.input)
        brush.setColor(color)
        brush.setStyle(Qt.SolidPattern)
        painter.setBrush(brush)
        painter.drawRect(0, 0, self.width(), self.height())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    pixel = PixelScreen()
    pixel.show()
    app.exec_()