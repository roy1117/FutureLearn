from PyQt5.QtWidgets import QWidget, QMainWindow, QLabel, QVBoxLayout, QApplication, QPushButton, QGridLayout, QScrollArea
from PyQt5 import QtCore
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 1500, 700)
        self.setWindowTitle('scroll area')

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        self.v_layout = QVBoxLayout()
        self.central_widget.setLayout(self.v_layout)
        # create a scroll area and set its size and position
        self.scroll_area = QScrollArea(self.central_widget)
        self.scroll_area.setGeometry(10, 10, 500, 500)

        self.v_layout.addWidget(self.scroll_area)

        # ScrollBarAsNeeded is selected by default
        # self.scroll_area.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        # self.scroll_area.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)

        # scroll area can be set with only one widget
        # Therefore if you want to put multiple widgets, you need to create a container widget and add others
        self.scroll_contents = QWidget()
        # the most important part is that we should set the size the container widget which scroll area takes inside
        # this container widget should be bigger than scroll area so that scroll area shows bars
        self.scroll_contents.setGeometry(0, 0, 1800, 1000)

        self.pushbutton1 = QPushButton(self.scroll_contents)
        self.pushbutton1.setGeometry(0, 0, 100, 50)
        self.pushbutton1.setText('pushbutton1')

        # push button2's position cannot be seen if there is no scroll
        # its x position is bigger than scroll area but less than container widget size
        self.pushbutton2 = QPushButton(self.scroll_contents)
        self.pushbutton2.setGeometry(1300, 0, 100, 50)
        self.pushbutton2.setText('pushbutton2')

        # push button3's position cannot be seen even if there is scroll
        # its y position is bigger than scroll area and container widget so it appears only partly
        self.pushbutton3 = QPushButton(self.scroll_contents)
        self.pushbutton3.setGeometry(500, 980, 100, 50)
        self.pushbutton3.setText('pushbutton3')

        self.scroll_area.setWidget(self.scroll_contents)
        self.show()

if __name__ =='__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    sys.exit(app.exec_())