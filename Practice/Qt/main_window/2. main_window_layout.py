from PyQt5.QtWidgets import QWidget, QMainWindow, QLabel, QVBoxLayout, QApplication
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setGeometry(1000, 500, 300, 500)
        self.setWindowTitle('layout practice')
        # central widget is needed to use layout in main window
        self.centralwidget = QWidget(self)
        self.centralwidget.setGeometry(100, 100, 100, 100)
        self.setCentralWidget(self.centralwidget)

        self.vlayout = QVBoxLayout()
        self.widget1 = QLabel()
        self.widget1.setGeometry(0, 0, 50, 50)
        self.widget1.setStyleSheet('background-color:green;')

        self.widget2 = QLabel()
        self.widget2.setGeometry(0, 0, 50, 50)
        self.widget2.setStyleSheet('background-color:black;')

        self.vlayout.addWidget(self.widget1)
        self.vlayout.addWidget(self.widget2)
        self.centralwidget.setLayout(self.vlayout)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    sys.exit(app.exec_())
