import perceptron_widget
import network
from PyQt5.QtWidgets import *
import sys
import mnist_loader
"""
class Student1():
    def __init__(self, name):
        print("Student1")
        self.name = name

class Student2():
    def __init__(self, number):
        print("Student2")
        self.number = number

class Student3(Student1, Student2):
    def __init__(self, name, number):
        Student1.__init__(self, name)
        Student2.__init__(self, number)

roy = Student3("Roy", 1234)

"""


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.resize(1500, 800)
        self.neuronNetwork = Test(sizes=[784, 30, 10])
        centralWidget = QWidget()
        self.loadDataButton = QPushButton("Load data")
        self.loadDataButton.clicked.connect(self.load_data)
        self.uploadOneSampleButton = QPushButton("Upload one sample")
        self.uploadOneSampleButton.clicked.connect(self.neuronNetwork.upload_one_sample)
        self.feedOneSampleButton = QPushButton("Feed one sample")
        self.feedOneSampleButton.clicked.connect(self.feed_one_sample)


        scrollArea = QScrollArea()
        scrollArea.setWidget(self.neuronNetwork)

        gridLayout = QGridLayout()
        gridLayout.addWidget(scrollArea, 0, 1, 3, 1)
        gridLayout.addWidget(self.loadDataButton, 0, 0)
        gridLayout.addWidget(self.uploadOneSampleButton, 1, 0)
        gridLayout.addWidget(self.feedOneSampleButton, 2, 0)
        centralWidget.setLayout(gridLayout)

        self.setCentralWidget(centralWidget)
        scrollArea.setWidgetResizable(True)

    def load_data(self):
        training_data, validation_data, test_data = mnist_loader.load_data_wrapper()
        training_data = list(training_data)
        self.neuronNetwork.SGD(training_data)

    def feed_one_sample(self):
        """temporary implementation"""
        eta = 0.3
        self.neuronNetwork.feed_one_sample(eta)


class Test(network.CustomNetwork, perceptron_widget.NeuronNetowrk):
    def __init__(self, sizes, parent=None):
        network.CustomNetwork.__init__(self, sizes)
        perceptron_widget.NeuronNetowrk.__init__(self, parent)
        """book mark"""
        network.CustomNetwork.update_gui.connect(self.print_hi)

    def print_hi(self):
        print('hi')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    app.exec_()
