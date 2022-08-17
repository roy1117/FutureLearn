from PyQt5.QtWidgets import QMainWindow, QLabel, QApplication
import sys


class Form(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        label = QLabel("Hello, World")
        self.setCentralWidget(label)

def main():
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    app.exec_()


if __name__ == "__main__":
    main()