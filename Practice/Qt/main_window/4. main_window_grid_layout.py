from PyQt5.QtWidgets import QWidget, QMainWindow, QLabel, QVBoxLayout, QApplication, QPushButton, QGridLayout
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
        self.setWindowTitle('grid layout')

        self.centralwiget = QWidget()
        self.setCentralWidget(self.centralwiget)

        self.grid_layout = QGridLayout()
        self.centralwiget.setLayout(self.grid_layout)

        self.button1 = QPushButton(self.centralwiget)
        self.button1.setText('Button1')
        # move and resize doesn't work
        self.button1.resize(100, 100)
        self.button1.move(200, 300)
        self.grid_layout.addWidget(self.button1, 0, 0)

        self.button2 = QPushButton(self.centralwiget)
        # with fixed size the widget never shrinks or expands
        self.button2.setFixedSize(100, 100)
        self.button2.setText('Button2')
        self.grid_layout.addWidget(self.button2, 0, 1)

        self.button3 = QPushButton(self.centralwiget)
        self.button3.setText('Button3')
        self.grid_layout.addWidget(self.button3, 1, 0)

        self.button4 = QPushButton(self.centralwiget)
        self.button4.setText('Button4')
        self.grid_layout.addWidget(self.button4, 1, 1)

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    sys.exit(app.exec_())


