import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from random import randint, choice



class MainWindow(QtWidgets.QMainWindow):
    colors = ['#FFD141', '#376F9F', '#0D1F2D', '#E9EBEF', '#EB5160']

    def __init__(self):
        super().__init__()

        self.label = QtWidgets.QLabel()
        canvas = QtGui.QPixmap(400, 300)
        self.label.setPixmap(canvas)
        self.setCentralWidget(self.label)
        self.draw_line()
        self.draw_point()
        self.draw_rects()
        self.draw_round_rects()
        self.draw_ellipse()
        self.draw_text()

    def draw_line(self):
        painter = QtGui.QPainter(self.label.pixmap())
        pen = QtGui.QPen()
        pen.setWidth(10)
        pen.setColor(QtGui.QColor('red'))
        painter.setPen(pen)
        painter.drawLine(400, 300, 300, 200)
        pen.setWidth(5)
        pen.setColor(QtGui.QColor('blue'))
        painter.setPen(pen)
        painter.drawLine(QtCore.QPoint(50, 100), QtCore.QPoint(100, 200))
        painter.end()

    def draw_point(self):
        pen = QtGui.QPen()
        pen.setWidth(3)
        painter = QtGui.QPainter(self.label.pixmap())
        for i in range(10000):
            pen = painter.pen()
            pen.setColor(QtGui.QColor(choice(self.colors)))
            painter.setPen(pen)
            painter.drawPoint(200 + randint(-100, 100), 150 + randint(-100, 100))
        painter.end()

    def draw_rects(self):
        painter = QtGui.QPainter(self.label.pixmap())
        pen = QtGui.QPen()
        brush = QtGui.QBrush()

        pen.setWidth(3)
        for i in range(4):
            brush.setColor(QtGui.QColor(choice(self.colors)))
            brush.setStyle(Qt.Dense1Pattern)
            pen.setColor(QtGui.QColor(choice(self.colors)))
            painter.setPen(pen)
            painter.setBrush(brush)
            painter.drawRect(randint(0, 400), randint(0, 300), randint(0, 400), randint(0, 300))
        # rects = []
        # for i in range(4):
        #     rects.append(QtCore.QRectF(randint(0, 400), randint(0, 300), randint(0, 400), randint(0, 300)))
        # painter.drawRects(rects)
        painter.end()

    def draw_round_rects(self):
        pen = QtGui.QPen()
        pen.setWidth(3)
        pen.setColor(QtGui.QColor(choice(self.colors)))
        painter = QtGui.QPainter(self.label.pixmap())
        painter.setPen(pen)
        painter.drawRoundedRect(0, 0, 100, 100, 20, 30)
        painter.end()

    def draw_ellipse(self):
        pen = QtGui.QPen()
        pen = QtGui.QPen()
        pen.setWidth(3)
        pen.setColor(QtGui.QColor(choice(self.colors)))
        painter = QtGui.QPainter(self.label.pixmap())
        painter.setPen(pen)
        painter.drawEllipse(0, 0, 100, 200)
        painter.end()

    def draw_text(self):
        painter = QtGui.QPainter(self.label.pixmap())
        pen = QtGui.QPen()
        pen.setWidth(1)
        pen.setColor(QtGui.QColor('green'))
        painter.setPen(pen)

        font = QtGui.QFont()
        font.setFamily('Times')
        font.setBold(True)
        font.setPointSize(40)
        painter.setFont(font)

        painter.drawText(100, 100, "Hello, World!")
        painter.end()

app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()