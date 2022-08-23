import perceptron_widget
import pixel_widget
import network
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
import mnist_loader
ETA = 0.3


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.resize(1500, 800)
        self.neuronNetwork = perceptron_widget.NeuronNetowrk(sizes=[784, 30, 10])
        centralWidget = QWidget()
        self.loadDataButton = QPushButton("Load data")
        self.loadDataButton.clicked.connect(self.load_data)
        self.uploadOneSampleButton = QPushButton("Upload one sample")
        self.uploadOneSampleButton.clicked.connect(self.neuronNetwork.upload_one_sample)
        self.feedOneSampleButton = QPushButton("Feed one sample")
        self.feedOneSampleButton.clicked.connect(self.feed_one_sample)
        self.trainingDataLabel = QLabel("loaded training data : 0")
        self.pixelScreen = pixel_widget.PixelScreen()

        self.neuronNetwork.update_input_signal.connect(self.pixelScreen.set_inputs)

        scrollArea = QScrollArea()
        scrollArea.setWidget(self.neuronNetwork)

        gridLayout = QGridLayout()
        gridLayout.addWidget(self.pixelScreen, 0, 0)
        gridLayout.addWidget(scrollArea, 0, 1, 1, 3)
        gridLayout.addWidget(self.trainingDataLabel, 1, 1)
        gridLayout.addWidget(self.loadDataButton, 2, 1)
        gridLayout.addWidget(self.uploadOneSampleButton, 2, 2)
        gridLayout.addWidget(self.feedOneSampleButton, 2, 3)
        centralWidget.setLayout(gridLayout)

        self.setCentralWidget(centralWidget)
        scrollArea.setWidgetResizable(True)

    def load_data(self):
        try:
            training_data, validation_data, test_data = mnist_loader.load_data_wrapper()
            training_data = list(training_data)
            self.neuronNetwork.SGD(training_data)
        except Exception as e:
            print(e)
        else:
            print('loading was successful')
            self.update_training_data_label()

    def feed_one_sample(self):
        """temporary implementation"""
        self.neuronNetwork.feed_one_sample(ETA)

    def update_training_data_label(self):
        text = "loaded training data : "
        data_length = str(len(self.neuronNetwork.training_data))
        self.trainingDataLabel.setText(text + data_length)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    app.exec_()
