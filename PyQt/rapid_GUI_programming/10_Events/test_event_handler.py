from PyQt5.QtWidgets import *
import sys

class Form(QDialog):
    def __init__(self):
        super().__init__()
        layout = QGridLayout()
        dial = CustomDial()
        layout.addWidget(dial, 0, 0)
        self.setLayout(layout)

    def mousePressEvent(self, event):
        print('parent mouse press event')

    def closeEvent(self, event):
        QMessageBox.warning(self, 'Warning', 'I want to know if you really meant to close')


class CustomDial(QDial):
    def __init__(self):
        super().__init__()

    def paintEvent(self, event):
        super().paintEvent(event)
        print('paint event')

    def mousePressEvent(self, event):
        print('child mouse press event')
        event.accept()


app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()