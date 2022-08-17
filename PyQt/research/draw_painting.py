from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys


class Form(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.bytes_data = None
        self.label1 = Label()
        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)
        self.resize(500, 500)
        self.saveButton = QPushButton("save")
        self.saveButton.clicked.connect(self.label1.save_iamge)
        self.readButton = QPushButton("read")
        self.readButton.clicked.connect(self.label1.read_binary)
        self.clean = QPushButton("clean")
        self.clean.clicked.connect(self.label1.clean)

        gridLayout = QGridLayout()
        gridLayout.addWidget(self.label1, 0, 0)
        gridLayout.addWidget(self.saveButton, 1, 0)
        gridLayout.addWidget(self.readButton, 2, 0)
        gridLayout.addWidget(self.clean, 3, 0)
        centralWidget.setLayout(gridLayout)




class Label(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMinimumSize(28, 28)
        self.setMaximumSize(28, 28)
        self.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        self.last_x, self.last_y = None, None
        pixmap = QPixmap(self.width(), self.height())
        self.setPixmap(pixmap)

    def save_iamge(self):
        pixmap = QPixmap(self.size())
        self.render(pixmap)
        image = QImage()
        image = pixmap.toImage()
        image.save("Test.bmp", "BMP", -1)

    def read_binary(self):
        pixmap = QPixmap(self.size())
        self.render(pixmap)
        image = QImage()
        image = pixmap.toImage()
        for i in range(0, 28):
            for j in range(0, 28):
                rawColor = image.pixel(i, j)
                rgb = QColor(rawColor).getRgb()
                print(rgb)


    def paintEvent(self, e):
        super().paintEvent(e)

    def mousePressEvent(self, e):
        super().mousePressEvent(e)

    def mouseMoveEvent(self, e):
        super().mouseMoveEvent(e)
        if self.last_x is None:  # First event.
            self.last_x = e.x()
            self.last_y = e.y()
            return  # Ignore the first time.
        painter = QPainter(self.pixmap())

        pen = painter.pen()
        pen.setWidth(4)
        pen.setColor(QColor('blue'))
        painter.setPen(pen)
        painter.drawLine(self.last_x, self.last_y, e.x(), e.y())

        painter.end()
        self.update()

        # Update the origin for next time.
        self.last_x = e.x()
        self.last_y = e.y()

    def clean(self):
        painter = QPainter(self.pixmap())
        painter.begin(self)
        brush = QBrush()
        brush.setStyle(Qt.SolidPattern)
        brush.setColor(QColor('black'))
        painter.setBrush(brush)
        painter.drawRect(self.rect())
        painter.end()
        self.update()

app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()