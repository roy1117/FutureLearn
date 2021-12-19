import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLabel


class Basic_window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.setGeometry(1000, 300, 340, 190)
        self.setStyleSheet('background-color:rgb(175,175,175);')
        self.setWindowTitle('good try')

        self.centralwidget = QWidget(self)
        self.setCentralWidget(self.centralwidget)

        self.widget1 = QLabel(self.centralwidget)
        self.widget1.setGeometry(10, 10, 100, 50)
        self.widget1.setStyleSheet('background-color:green;')

        self.widget2 = QLabel(self.centralwidget)
        self.widget2.setGeometry(120, 10, 100, 50)
        self.widget2.setStyleSheet('background-color:red;')

        self.widget3 = QLabel(self.centralwidget)
        self.widget3.setGeometry(230, 10, 100, 50)
        self.widget3.setStyleSheet('background-color:black;')

        self.widget4 = QLabel(self.centralwidget)
        self.widget4.setGeometry(10, 70, 100, 50)
        self.widget4.setStyleSheet('background-color:blue;')

        self.widget5 = QLabel(self.centralwidget)
        self.widget5.setGeometry(120, 70, 100, 50)
        self.widget5.setStyleSheet('background-color:yellow;')

        self.widget6 = QLabel(self.centralwidget)
        self.widget6.setGeometry(230, 70, 100, 50)
        self.widget6.setStyleSheet('background-color:purple;')

        self.widget6 = QLabel(self.centralwidget)
        self.widget6.setGeometry(10, 130, 100, 50)
        self.widget6.setStyleSheet('background-color:orange;')

        self.widget7 = QLabel(self.centralwidget)
        self.widget7.setGeometry(120, 130, 100, 50)
        self.widget7.setStyleSheet('background-color:brown;')

        self.widget8 = QLabel(self.centralwidget)
        self.widget8.setGeometry(230, 130, 100, 50)
        self.widget8.setStyleSheet('background-color:white;')

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Basic_window()
    sys.exit(app.exec_())
