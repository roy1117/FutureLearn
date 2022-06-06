from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from time import sleep
import sys

class Form(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.fname = None
        self.settings = QSettings("Nasa", "Space-x")
        self.lastFilenames = self.settings.value("previous")
        self.lineEdit = QLineEdit()
        self.imageLabel = QLabel()
        if self.lastFilenames is None:
            self.lastFilenames = []
        else:
            self.set_pixmap(self.lastFilenames[0])





        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)
        gridLayout = QGridLayout()
        gridLayout.addWidget(self.lineEdit, 0, 0)
        gridLayout.addWidget(self.imageLabel, 1, 0)
        centralWidget.setLayout(gridLayout)

        openAction = QAction("Open", self)
        openAction.triggered.connect(self.open_file_dialog)

        recentMenu = QMenu("Recent", self)

        fileMenu = QMenu("file", self)
        fileMenu.addAction(openAction)
        fileMenu.addMenu(recentMenu)

        mirrorHorizontally = QAction("mirror horizontally", self)
        mirrorHorizontally.triggered.connect(self.mirror_horizontally)

        mirrorVetically = QAction("mirror vertically", self)
        mirrorVetically.triggered.connect(self.mirror_vertically)

        zoomImage = QAction("zoom image", self)
        zoomImage.triggered.connect(self.zoom_image)

        self.zoomSpinBox = QSpinBox()
        self.zoomSpinBox.setValue(100)
        self.zoomSpinBox.setMinimum(1)
        self.zoomSpinBox.setMaximum(400)
        self.zoomLabel = QLabel("Zoom")
        self.zoomSpinBox.valueChanged.connect(self.scale_image)

        editMenu = QMenu("Edit", self)
        editMenu.addAction(mirrorHorizontally)
        editMenu.addAction(mirrorVetically)
        editMenu.addAction(zoomImage)

        menubar = QMenuBar()
        self.setMenuBar(menubar)
        menubar.addMenu(fileMenu)
        menubar.addMenu(editMenu)

        toobar = QToolBar(self)
        toobar.addWidget(self.zoomLabel)
        toobar.addWidget(self.zoomSpinBox)
        self.addToolBar(toobar)

        for i in self.lastFilenames:
            self.append_action(recentMenu, i, self.recent_action_triggered)

    def scale_image(self, percent):
        factor = percent/100.0
        image = self.pixmap.toImage()
        width = int(image.width() * factor)
        height = int(image.height() * factor)
        size = QSize(width, height)
        image = image.scaled(size)
        pixmap = QPixmap()
        pixmap.convertFromImage(image)
        self.imageLabel.setPixmap(pixmap)

    def zoom_image(self):
        percent, ok = QInputDialog.getInt(self, "Zoom Image", "Enter the integer", 100, 1, 400)
        self.zoomSpinBox.setValue(percent)

    def mirror_horizontally(self):
        self.pixmap = self.imageLabel.pixmap()
        image = self.pixmap.toImage()
        image = image.mirrored(True, False)
        self.pixmap.convertFromImage(image)
        self.imageLabel.setPixmap(self.pixmap)

    def mirror_vertically(self):
        self.pixmap = self.imageLabel.pixmap()
        image = self.pixmap.toImage()
        image = image.mirrored(False, True)
        self.pixmap.convertFromImage(image)
        self.imageLabel.setPixmap(self.pixmap)

    def open_file_dialog(self):
        fname = QFileDialog.getOpenFileNames(self, 'Open File', './images', 'All File(*);; My Image File(*.png *.jpg)')[0][0]
        self.set_pixmap(fname)

    def set_pixmap(self, filename):
        self.fname = filename
        self.pixmap = QPixmap(filename)
        self.imageLabel.setPixmap(self.pixmap)
        self.imageLabel.resize(self.pixmap.width(), self.pixmap.height())

    def append_action(self, menu, action_text, slot):
        action = QAction(action_text, self)
        action.triggered.connect(slot)
        menu.addAction(action)

    def recent_action_triggered(self):
        self.set_pixmap(self.sender().text())

    def closeEvent(self, event):
        super().closeEvent(event)
        if self.fname is None:
            return
        if self.fname in self.lastFilenames:
            self.lastFilenames.remove(self.fname)
        self.lastFilenames.insert(0, self.fname)
        if len(self.lastFilenames) > 5:
            self.lastFilenames = self.lastFilenames[:5]
        self.settings.setValue("previous", self.lastFilenames)


app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()