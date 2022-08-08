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
        self.saveButton.clicked.connect(self.save_iamge)
        self.readButton = QPushButton("read")
        self.readButton.clicked.connect(self.read_binary)

        gridLayout = QGridLayout()
        gridLayout.addWidget(self.label1, 0, 0)
        gridLayout.addWidget(self.saveButton, 1, 0)
        gridLayout.addWidget(self.readButton, 2, 0)
        centralWidget.setLayout(gridLayout)


    def save_iamge(self):
        pixmap = QPixmap(self.label1.size())
        pixmap.scroll(50, 50, pixmap.rect())
        self.render(pixmap)
        pixmap.save("Test.bmp", "BMP", -1)

    def read_binary(self):
        with open("Test.bmp", 'rb') as file:
            self.bytes_data = file.read()
            print(self.bytes_data)





class Label(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMinimumSize(500, 500)
        self.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        self.last_x, self.last_y = None, None
        pixmap = QPixmap(self.width(), self.height())
        self.setPixmap(pixmap)

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


app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()