import sys
import time

from PyQt5 import QtWidgets
from PyQt5 import Qt
from PyQt5 import QtCore
# first argument is file path
# next arguments are string entered as parameter, separated by space
for i in sys.argv:
    print(i)

app = QtWidgets.QApplication