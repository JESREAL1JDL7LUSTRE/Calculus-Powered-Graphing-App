import sys
import matplotlib
matplotlib.use('Qt5Agg')  # Set the backend to Qt5Agg before importing pyplot
import matplotlib.pyplot as plt
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

class MatplotlibWidget(FigureCanvas):
    def __init__(self, parent=None):
        fig, self.ax = plt.subplots(figsize=(5, 4))
        super().__init__(fig)
        self.setParent(parent)
        self.plot_graph()

    def plot_graph(self):
        x = [0, 1, 2, 3, 4]
        y = [0, 1, 4, 9, 16]
        self.ax.plot(x, y, label="y = x^2", color='blue', marker='o')
        self.ax.grid(True)
        self.ax.set_title("Matplotlib in PySide6")
        self.ax.set_xlabel("X-axis")
        self.ax.set_ylabel("Y-axis")
        self.ax.legend()

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PySide6 + Matplotlib Example")
        self.setGeometry(100, 100, 600, 400)

        layout = QVBoxLayout()
        self.matplotlib_widget = MatplotlibWidget(self)
        layout.addWidget(self.matplotlib_widget)

        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
