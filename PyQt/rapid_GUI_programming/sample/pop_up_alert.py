import sys
import time
from PyQt5 import QtWidgets
from PyQt5 import Qt
from PyQt5 import QtCore

def print_hi():
    print('hi')

# first argument is file path
# next arguments are string entered as parameter, separated by space
for i in sys.argv:
    print(i)

app = QtWidgets.QApplication(sys.argv)

try:
    # setting default value
    message = "Alert!"
    due = QtCore.QTime.currentTime()
    # printed string "PyQt5.QtCore.QTime(19, 45, 9, 918)"
    print(due)

    # if there is no argument, it will generate an error
    # otherwise error will occur in split() or int() stopping the programme
    # if code goes to raise function, it will jump to except part without stopping the programme
    # it handles error (shows message), but it doesn't stop programme
    if len(sys.argv) < 2:
        raise ValueError
    hours, mins = sys.argv[1].split(":")
    due = QtCore.QTime(int(hours), int(mins))
    if not due.isValid():
        raise ZeroDivisionError
    if len(sys.argv) > 2:
        # join function example, takes one list argument and concatenate with given string
        # a = ["hi", "hello"]
        # print("-".join(a))
        # hi-hello
        message = " ".join(sys.argv[2:])
except ValueError:
    message = "No parameter has been given"

except ZeroDivisionError:
    message = "Wrong parameter has been given"


while QtCore.QTime.currentTime() < due:
    time.sleep(2)
    print("sleeping")

# The supported HTML tags are listed at http://doc.trolltech.com/richtext-html-subset.html
label = QtWidgets.QLabel("<font color=red size=72><b>" + message + "</b></font>")
label.setWindowFlags(QtCore.Qt.SplashScreen|QtCore.Qt.WindowStaysOnTopHint)
label.show()
QtCore.QTimer.singleShot(5000, print_hi)
QtCore.QTimer.singleShot(10000, app.quit) # 1 minute
app.exec_()