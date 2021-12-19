from PyQt5.QtWidgets import QWidget, QMainWindow, QLabel, QVBoxLayout, QApplication, QPushButton
import sys

# resize and move method has advantage
# 1. it doesn't require layout.(intuitive and simple)
# 2. can adjust size and position without any limitation.(duplication can also be possible)

# it has disadvantage
# 1. it doesn't adjust widget size according as screen size changes(fixed)
# 2. manual size and position calculation might entail duplication

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 1000, 500)
        self.setWindowTitle('resize and move')

        self.button1 = QPushButton(self)
        self.button1.setText('Button1')
        self.button1.resize(100, 100)
        self.button1.move(200, 20)
        self.button1.setStyleSheet('background-color:green;')

        self.button2 = QPushButton(self)
        self.button2.setText('Button2')
        self.button2.resize(100, 300)
        self.button2.move(200, 70)
        self.button2.setStyleSheet('background-color:red;')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    sys.exit(app.exec_())