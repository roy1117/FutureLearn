import sys
import numpy as np
import PyQt5.QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

MAX_RAW_VALUE = 3
MIN_RAW_VALUE = -3


# Miscellaneous functions
def sigmoid(z):
    """The sigmoid function."""
    return 1.0/(1.0+np.exp(-z))


def sigmoid_prime(z):
    """Derivative of the sigmoid function."""
    return sigmoid(z)*(1-sigmoid(z))


def get_color(raw_value):
    blue_thickness, red_thickness = 0, 0
    half_value = (MAX_RAW_VALUE + MIN_RAW_VALUE)/2
    if raw_value > half_value:
        blue_thickness = int(((raw_value - half_value) / (MAX_RAW_VALUE - half_value)) * 255)
    else:
        red_thickness = 255 - int(((raw_value - MIN_RAW_VALUE) / (half_value - MIN_RAW_VALUE)) * 255)
    return QColor(red_thickness, 0, blue_thickness, 255)


class NeuronNetowrk(QWidget):

    update_input_signal = pyqtSignal(np.ndarray)

    def __init__(self, sizes, parent=None):
        super().__init__(parent)
        """The list ``sizes`` contains the number of neurons in the
        respective layers of the network.  For example, if the list
        was [2, 3, 1] then it would be a three-layer network, with the
        first layer containing 2 neurons, the second layer 3 neurons,
        and the third layer 1 neuron.  The biases and weights for the
        network are initialized randomly, using a Gaussian
        distribution with mean 0, and variance 1.  Note that the first
        layer is assumed to be an input layer, and by convention we
        won't set any biases for those neurons, since biases are only
        ever used in computing the outputs from later layers."""
        self.training_data = None
        self.training_data_len = None
        self.mini_batch = None
        self.num_layers = len(sizes)
        self.sizes = sizes
        self.biases = [np.random.randn(y, 1) for y in sizes[1:]]
        self.weights = [np.random.randn(y, x)
                        for x, y in zip(sizes[:-1], sizes[1:])]

        """PyQt Layout initialization"""
        layout = QGridLayout()
        # Setting first layer
        self.network = []
        for layer, number_of_perceptrons in enumerate(self.sizes):
            self.network.append([])
            for i in range(number_of_perceptrons):
                if layer == 0:
                    bias = 0
                else:
                    bias = self.biases[layer-1][i][0]
                perceptron = Perceptron(bias)
                self.network[layer].append(perceptron)
                layout.addWidget(perceptron, i, layer)

        self.setLayout(layout)

    def feedforward(self, a):
        """Return the output of the network if ``a`` is input."""
        for b, w in zip(self.biases, self.weights):
            a = sigmoid(np.dot(w, a)+b)
        return a

    def SGD(self, training_data):
        """Train the neural network using mini-batch stochastic
        gradient descent.  The ``training_data`` is a list of tuples
        ``(x, y)`` representing the training inputs and the desired
        outputs.  The other non-optional parameters are
        self-explanatory.  If ``test_data`` is provided then the
        network will be evaluated against the test data after each
        epoch, and partial progress printed out.  This is useful for
        tracking progress, but slows things down substantially."""
        self.training_data = training_data
        self.training_data = list(self.training_data)
        self.training_data_len = len(training_data)

    def upload_one_sample(self):
        self.mini_batch = self.training_data[0:1]
        self.update_input_perceptrons(self.mini_batch[0][0])
        self.update_input_signal.emit(self.mini_batch[0][0])

    def feed_one_sample(self, eta):
        self.update_mini_batch(self.mini_batch, eta)

    def update_mini_batch(self, mini_batch, eta):
        """Update the network's weights and biases by applying
        gradient descent using backpropagation to a single mini batch.
        The ``mini_batch`` is a list of tuples ``(x, y)``, and ``eta``
        is the learning rate."""
        nabla_b = [np.zeros(b.shape) for b in self.biases]
        nabla_w = [np.zeros(w.shape) for w in self.weights]
        for x, y in mini_batch:
            delta_nabla_b, delta_nabla_w = self.backprop(x, y)
            nabla_b = [nb+dnb for nb, dnb in zip(nabla_b, delta_nabla_b)]
            nabla_w = [nw+dnw for nw, dnw in zip(nabla_w, delta_nabla_w)]
        self.weights = [w-(eta/len(mini_batch))*nw
                        for w, nw in zip(self.weights, nabla_w)]
        self.biases = [b-(eta/len(mini_batch))*nb
                       for b, nb in zip(self.biases, nabla_b)]
        self.update_perceptrons_bias()

    def backprop(self, x, y):
        """Return a tuple ``(nabla_b, nabla_w)`` representing the
        gradient for the cost function C_x.  ``nabla_b`` and
        ``nabla_w`` are layer-by-layer lists of numpy arrays, similar
        to ``self.biases`` and ``self.weights``."""
        nabla_b = [np.zeros(b.shape) for b in self.biases]
        nabla_w = [np.zeros(w.shape) for w in self.weights]
        # feedforward
        activation = x
        activations = [x] # list to store all the activations, layer by layer
        zs = [] # list to store all the z vectors, layer by layer
        for b, w in zip(self.biases, self.weights):
            z = np.dot(w, activation)+b
            zs.append(z)
            activation = sigmoid(z)
            activations.append(activation)
        # backward pass
        delta = self.cost_derivative(activations[-1], y) * \
            sigmoid_prime(zs[-1])
        nabla_b[-1] = delta
        nabla_w[-1] = np.dot(delta, activations[-2].transpose())
        # Note that the variable l in the loop below is used a little
        # differently to the notation in Chapter 2 of the book.  Here,
        # l = 1 means the last layer of neurons, l = 2 is the
        # second-last layer, and so on.  It's a renumbering of the
        # scheme in the book, used here to take advantage of the fact
        # that Python can use negative indices in lists.
        for l in range(2, self.num_layers):
            z = zs[-l]
            sp = sigmoid_prime(z)
            delta = np.dot(self.weights[-l+1].transpose(), delta) * sp
            nabla_b[-l] = delta
            nabla_w[-l] = np.dot(delta, activations[-l-1].transpose())
        return (nabla_b, nabla_w)

    def evaluate(self, test_data):
        """Return the number of test inputs for which the neural
        network outputs the correct result. Note that the neural
        network's output is assumed to be the index of whichever
        neuron in the final layer has the highest activation."""
        test_results = [(np.argmax(self.feedforward(x)), y)
                        for (x, y) in test_data]
        return sum(int(x == y) for (x, y) in test_results)

    def cost_derivative(self, output_activations, y):
        """Return the vector of partial derivatives \partial C_x /
        \partial a for the output activations."""
        return (output_activations-y)

    def paintEvent(self, e):
        super().paintEvent(e)
        painter = QPainter()
        painter.begin(self)
        painter.setViewport(0, 0, self.width(), self.height())
        pen = QPen()
        pen.setWidth(3)

        for layer in range(len(self.sizes)-1):
            for index_of_previous_perceptron in range(self.sizes[layer]):
                for index_of_next_perceptron in range(self.sizes[layer+1]):
                    rect = self.network[layer][index_of_previous_perceptron].geometry()
                    x = rect.x()
                    y = rect.y()
                    width = rect.width()
                    height = rect.height()
                    outPoint = QPoint(x+width, y+int(height/2))

                    rect = self.network[layer+1][index_of_next_perceptron].geometry()
                    x = rect.x()
                    y = rect.y()
                    width = rect.width()
                    height = rect.height()
                    inPoint = QPoint(x, y + int(height / 2))

                    weight = self.weights[layer][index_of_next_perceptron][index_of_previous_perceptron]
                    weight_color = get_color(weight)
                    pen.setColor(weight_color)
                    painter.setPen(pen)

                    painter.drawLine(outPoint, inPoint)

        painter.end()

    def update_perceptrons_bias(self):
        "Implementation required"
        pass

    def update_input_perceptrons(self, input):
        try:
            for index, value in enumerate(input):
                self.network[0][index].setBias(value[0])
                print(value[0])
        except Exception as e:
            print(e)


class Perceptron(QWidget):
    def __init__(self, bias, parent=None):
        super().__init__(parent)
        self.bias = bias
        self.setMinimumSize(100, 100)
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

    def paintEvent(self, e):
        bias = round(self.bias, 3)
        painter = QPainter()
        painter.begin(self)
        painter.setViewport(0, 0, self.width(), self.height())
        pen = QPen()
        pen.setWidth(3)
        pen.setColor(QColor('white'))
        brush = QBrush()
        bias_color = get_color(bias)
        brush.setColor(bias_color)
        brush.setStyle(Qt.SolidPattern)
        painter.setBrush(brush)
        painter.setPen(pen)
        painter.drawEllipse(0, 0, self.width(), self.height())

        font = QFont()
        font.setFamily('Times')
        font.setBold(True)
        font.setPointSize(10)
        painter.setFont(font)
        painter.drawText(0, 0, self.width(), self.height(), Qt.AlignCenter, str(bias))

        painter.end()

    def setBias(self, bias):
        self.bias = bias
        self.update()



