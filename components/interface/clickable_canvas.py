from PySide6.QtCore import Signal
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

class ClickableFigureCanvas(FigureCanvas):
    clicked = Signal(object, str)  # emits (figure, title)

    def __init__(self, figure, title):
        super().__init__(figure)
        self.title = title

    def mouseDoubleClickEvent(self, event):
        self.clicked.emit(self.figure, self.title)
