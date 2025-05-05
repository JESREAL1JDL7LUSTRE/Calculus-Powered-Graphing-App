from PySide6.QtWidgets import QWidget, QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar

class GraphWindow(QWidget):
    def __init__(self, figure, title="Graph"):
        super().__init__()
        self.setWindowTitle(title)

        # Setup layout
        layout = QVBoxLayout(self)

        # Canvas and toolbar
        self.canvas = FigureCanvas(figure)
        self.toolbar = NavigationToolbar(self.canvas, self)

        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)

        self.setLayout(layout)
        self.resize(800, 600)
