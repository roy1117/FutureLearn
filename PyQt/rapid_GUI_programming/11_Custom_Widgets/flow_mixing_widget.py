from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.Qt import *
import sys

class YPipWidget(QWidget):
    valueChanged = pyqtSignal(float, float)

    def __init__(self, leftFlow=0, rightFlow=0, MaxFlow=100, parent=None):
        super().__init__(parent)
        self.leftSpinBox = QSpinBox(self)
        self.leftSpinBox.setRange(0, MaxFlow)
        self.leftSpinBox.setValue(leftFlow)
        self.leftSpinBox.setSuffix("l/s")
        self.leftSpinBox.setAlignment(Qt.AlignRight|Qt.AlignVCenter)
        self.leftSpinBox.valueChanged.connect(self.updateValue)

        self.rightSpinBox = QSpinBox(self)
        self.rightSpinBox.setRange(0, MaxFlow)
        self.rightSpinBox.setValue(rightFlow)
        self.rightSpinBox.setSuffix("l/s")
        self.rightSpinBox.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.rightSpinBox.valueChanged.connect(self.updateValue)

        self.label = QLabel(self)
        self.label.setFrameStyle(QFrame.StyledPanel | QFrame.Sunken)
        self.label.setAlignment(Qt.AlignCenter)
        fm = QFontMetricsF(self.font())
        self.label.setMinimumWidth(fm.width(" 999 l/s "))
        self.setSizePolicy(QSizePolicy(QSizePolicy.Expanding,
                                       QSizePolicy.Expanding))
        self.setMinimumSize(self.minimumSizeHint())
        self.updateValue()

    def updateValue(self):
        a = self.leftSpinBox.value()
        b = self.rightSpinBox.value()
        self.label.setText("%d l/s" % (a + b))
        self.valueChanged.emit(a, b)
        self.update()


    def values(self):
        return self.leftSpinBox.value(), self.rightSpinBox.value()

    def minimumSizeHint(self):
        return QSize(self.leftSpinBox.width() * 3,
                     self.leftSpinBox.height() * 5)

app = QApplication(sys.argv)
myWidget = YPipWidget()
myWidget.show()
app.exec_()