from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys


class Form(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        label1 = Label()
        label1.setStyleSheet("background-color:red;padding :3px;")

        spinbox = QSpinBox()
        spinbox.setRange(-1000, 1000)
        spinbox.setSingleStep(10)
        spinbox.valueChanged.connect(label1.increase_size)

        label1.setText("label1label1label1")
        layout = QVBoxLayout()
        layout.addWidget(label1)
        layout.addWidget(spinbox)

        self.setLayout(layout)


class Label(QLabel):
    resized = pyqtSignal(int, int)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.resized.connect(self.resize_text)
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.original_width = 300
        self.original_height = 20
        self.setFixedSize(self.original_width, self.original_height)

    def resize_text(self, box_width, box_height):
        print(box_width, box_height)
        font_size = box_height
        while True:
            font = QFont('Helvetica', font_size)
            metrics = QFontMetrics(font)
            text_width = metrics.width(self.text())
            text_height = metrics.height()
            if text_width < box_width and text_height < box_height:
                break
            else:
                font_size -= 1
        self.setFont(font)

    def resizeEvent(self, *args, **kwargs):
        super().resizeEvent(*args, **kwargs)
        self.resized.emit(self.width(), self.height())

    def increase_size(self, increment):
        self.setFixedSize(self.original_width+increment, self.original_height+increment)

app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()