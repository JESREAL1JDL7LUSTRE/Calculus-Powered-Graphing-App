import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui

class Home(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

def launch_home():
    app = QtWidgets.QApplication([])
    widget = Home()
    widget.resize(600, 800)
    widget.show()
    sys.exit(app.exec())
