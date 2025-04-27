import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PySide6.QtWidgets import QWidget, QMainWindow, QVBoxLayout
from components.interface.ui_home import Ui_MainWindow  # <== THIS

class Home(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Load all the UI elements from QtDesigner
        
        # Create Matplotlib figures and attach them to the placeholder widgets
        # First create the Matplotlib figures
        self.figure_function = plt.figure()
        self.canvas_function = FigureCanvas(self.figure_function)

        self.figure_derivative = plt.figure()
        self.canvas_derivative = FigureCanvas(self.figure_derivative)

        self.figure_integral_numeric = plt.figure()
        self.canvas_integral_numeric = FigureCanvas(self.figure_integral_numeric)

        self.figure_integral_symbolic = plt.figure()
        self.canvas_integral_symbolic = FigureCanvas(self.figure_integral_symbolic)

        # Now attach the canvas inside the placeholders
        self.layout_function = QVBoxLayout(self.widget)
        self.layout_function.addWidget(self.canvas_function)

        self.layout_derivative = QVBoxLayout(self.widget_2)
        self.layout_derivative.addWidget(self.canvas_derivative)

        self.layout_integral_numeric = QVBoxLayout(self.widget_3)
        self.layout_integral_numeric.addWidget(self.canvas_integral_numeric)

        self.layout_integral_symbolic = QVBoxLayout(self.widget_4)
        self.layout_integral_symbolic.addWidget(self.canvas_integral_symbolic)


        # Connect buttons
        self.pushButton.clicked.connect(self.handle_input)

        self.pushButton_2.clicked.connect(lambda: self.insert_text("^2"))
        self.pushButton_3.clicked.connect(lambda: self.insert_text("^"))
        self.pushButton_4.clicked.connect(lambda: self.insert_text("sqrt()"))
        self.pushButton_5.clicked.connect(lambda: self.insert_text("("))
        self.pushButton_6.clicked.connect(lambda: self.insert_text(")"))
        self.pushButton_7.clicked.connect(lambda: self.insert_text("+"))
        self.pushButton_8.clicked.connect(lambda: self.insert_text("-"))
        self.pushButton_9.clicked.connect(lambda: self.insert_text("/"))
        self.pushButton_10.clicked.connect(lambda: self.insert_text("x"))

        self.controller = None  # Will be set later

    def set_controller(self, controller):
        self.controller = controller

    def handle_input(self):
        if self.controller:
            function_str = self.lineEdit.text()
            try:
                lower_bound = float(self.lineEdit_6.text())
                upper_bound = float(self.lineEdit_5.text())
            except ValueError:
                lower_bound = -10
                upper_bound = 10
            self.controller.process_function(function_str, lower_bound, upper_bound)

    def insert_text(self, text):
        """Insert text at the cursor position."""
        current_text = self.lineEdit.text()
        cursor_pos = self.lineEdit.cursorPosition()
        new_text = current_text[:cursor_pos] + text + current_text[cursor_pos:]
        self.lineEdit.setText(new_text)
        self.lineEdit.setCursorPosition(cursor_pos + len(text))

    def update_result(self, result):
        self.lineEdit.setText(str(result))

    def derivative_result(self, result):
        self.lineEdit_2.setText(str(result))

    def update_integral_symbolic(self, result):
        self.lineEdit_3.setText(str(result))

    def update_integral_numeric(self, result):
        self.lineEdit_4.setText(str(result))

    def update_function_graph(self, x, y):
        self.figure_function.clear()
        ax = self.figure_function.add_subplot(111)
        ax.plot(x, y, label="Function", color='blue')
        ax.set_title("Original Function")
        ax.grid(True)
        ax.axhline(0, color='black', lw=0.5, ls='--')
        ax.legend()
        self.canvas_function.draw()

    def update_derivative_graph(self, x, y):
        self.figure_derivative.clear()
        ax = self.figure_derivative.add_subplot(111)
        ax.plot(x, y, label="Derivative", color='red')
        ax.set_title("Derivative")
        ax.grid(True)
        ax.axhline(0, color='black', lw=0.5, ls='--')
        ax.legend()
        self.canvas_derivative.draw()

    def update_integral_graph(self, x, y):
        self.figure_integral_numeric.clear()
        ax = self.figure_integral_numeric.add_subplot(111)
        ax.plot(x, y, label="Numeric Integral", color='green')
        ax.set_title("Numeric Integral")
        ax.grid(True)
        ax.axhline(0, color='black', lw=0.5, ls='--')
        ax.legend()
        self.canvas_integral_numeric.draw()

    def update_symbolic_integral_graph(self, x, y):
        self.figure_integral_symbolic.clear()
        ax = self.figure_integral_symbolic.add_subplot(111)
        ax.plot(x, y, label="Symbolic Integral", color='purple')
        ax.set_title("Symbolic Integral")
        ax.grid(True)
        ax.axhline(0, color='black', lw=0.5, ls='--')
        ax.legend()
        self.canvas_integral_symbolic.draw()
