import perceptron_widget
import network
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
import mnist_loader


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
        network.Wrapper.__init__(self, sizes)
        perceptron_widget.NeuronNetowrk.__init__(self, parent)
        """book mark"""

    def print_hi(self):
        print('hi')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    app.exec_()
