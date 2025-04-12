import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit

class Home(QWidget):
    def __init__(self):
        super().__init__()

        # UI Elements
        self.input_field = QLineEdit()
        self.result_label = QLabel("Result will appear here")
        self.result_label_derivative = QLabel("Derivative will appear here")
        self.result_label_integral = QLabel("Integral will appear here")
        self.btn = QPushButton("Submit")

        # Layout setup
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Enter a function:"))
        layout.addWidget(self.input_field)
        layout.addWidget(self.btn)
        layout.addWidget(self.result_label)
        layout.addWidget(self.result_label_derivative)
        layout.addWidget(self.result_label_integral)

        # Matplotlib canvases for graphs
        self.canvas_function = FigureCanvas(plt.figure())
        self.canvas_derivative = FigureCanvas(plt.figure())
        self.canvas_integral = FigureCanvas(plt.figure())

        # Add canvases to layout
        layout.addWidget(self.canvas_function)
        layout.addWidget(self.canvas_derivative)
        layout.addWidget(self.canvas_integral)

        self.setLayout(layout)

        # Initialize controller, will be set externally
        self.controller = None

        # Connect signals
        self.btn.clicked.connect(self.handle_input)

    def set_controller(self, controller):
        self.controller = controller

    def handle_input(self):
        if self.controller:
            function_str = self.input_field.text()
            self.controller.process_function(function_str)

    def update_result(self, result):
        self.result_label.setText(f"Result: {result}")

    def derivative_result(self, result):
        self.result_label_derivative.setText(f"Derivative: {result}")

    def integral_result(self, result):
        self.result_label_integral.setText(f"Integral: {result}")

    def update_function_graph(self, x, y):
        ax = self.canvas_function.figure.subplots()
        ax.plot(x, y, label='Function')
        ax.set_title("Function Plot")
        ax.set_xlabel("x")
        ax.set_ylabel("f(x)")
        ax.grid(True)
        ax.axhline(0, color='black', lw=0.5, ls='--')
        ax.legend()
        self.canvas_function.draw()

    def update_derivative_graph(self, x, y_derivative):
        ax = self.canvas_derivative.figure.subplots()
        ax.plot(x, y_derivative, label='Derivative', color='r')
        ax.set_title("Derivative Plot")
        ax.set_xlabel("x")
        ax.set_ylabel("f'(x)")
        ax.grid(True)
        ax.axhline(0, color='black', lw=0.5, ls='--')
        ax.legend()
        self.canvas_derivative.draw()

    def update_integral_graph(self, x, y_integral):
        ax = self.canvas_integral.figure.subplots()
        ax.plot(x, y_integral, label='Integral', color='g')
        ax.set_title("Integral Plot")
        ax.set_xlabel("x")
        ax.set_ylabel("∫f(x) dx")
        ax.grid(True)
        ax.axhline(0, color='black', lw=0.5, ls='--')
        ax.legend()
        self.canvas_integral.draw()
