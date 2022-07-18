import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.label = QtWidgets.QLabel()
        canvas = QtGui.QPixmap(400, 300)
        self.label.setPixmap(canvas)
        self.setCentralWidget(self.label)
        self.last_x, self.last_y = None, None

    def mouseMoveEvent(self, e):
        self.draw_lines(e)

    def draw_lines(self, e):
        if self.last_x is None:
            self.last_x = e.x()
            self.last_y = e.y()
            return
        pen = QtGui.QPen()
        pen.setColor(QtGui.QColor('red'))
        painter = QtGui.QPainter(self.label.pixmap())
        painter.setPen(pen)
        painter.drawLine(self.last_x, self.last_y, e.x(), e.y())
        painter.end()
        self.update()

        self.last_x = e.x()
        self.last_y = e.y()

    def mouseReleaseEvent(self, e):
        self.last_x = None
        self.last_y = None

    def draw_points(self, e):
        pen = QtGui.QPen()
        pen.setColor(QtGui.QColor('red'))
        painter = QtGui.QPainter(self.label.pixmap())
        painter.setPen(pen)
        painter.drawPoint(e.x(), e.y())
        painter.end()
        self.update()

    def mousePressEvent(self, e):
        print(e.x(), e.y())

app = QtWidgets.QApplication(sys.argv)
form = MainWindow()
form.show()
app.exec_()