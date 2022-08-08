from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class Form(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.resize(500, 500)
        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)
        label1 = QCustomLabel(label='Label1')
        label2 = QCustomLabel(label='Label2')
        label3 = QCustomLabel(label='Label3')
        label4 = QCustomLabel(label='Label4')

        gridLayout = QGridLayout()
        gridLayout.addWidget(label1, 0, 0)
        gridLayout.addWidget(label2, 0, 1)
        gridLayout.addWidget(label3, 1, 0)
        gridLayout.addWidget(label4, 1, 1)
        centralWidget.setLayout(gridLayout)


    def mousePressEvent(self, e):
        super().mousePressEvent(e)
        print('Main window size : {0}'.format(self.rect()))
        print('Main window mouse position : {0}'.format(e.pos()))

class QCustomLabel(QLabel):
    def __init__(self, parent=None, label=None):
        super().__init__(parent)
        self.label = label
        self.setMinimumSize(100, 100)
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)


    def mousePressEvent(self, e):
        super().mousePressEvent(e)
        print('label size : {0}'.format(self.rect()))
        print('label mouse position : {0}'.format(e.pos()))
        print('size hint : ', end="")
        print(self.sizeHint())
        print('minimum size hint : ', end="")
        print(self.minimumSizeHint())


    def paintEvent(self, e):
        super().paintEvent(e)
        painter = QPainter(self)
        brush = QBrush()
        color = QColor('red')
        brush.setStyle(Qt.Dense1Pattern)
        brush.setColor(color)
        painter.setBrush(brush)
        painter.drawRect(self.rect())

        pen = QPen()
        color = QColor('Black')
        pen.setColor(color)
        font = QFont()
        font.setBold(True)
        font.setPointSize(10)
        painter.setPen(pen)
        painter.setFont(font)
        painter.drawText(self.rect(), Qt.AlignmentFlag.AlignCenter, self.label)

    def sizeHint(self):
        return QSize(200, 200)





app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()