from PySide6.QtWidgets import QWidget
from components.graph.graph import Graph
from components.logic.magic import Magic

class Home(QWidget):
    def __init__(self):
        super().__init__()
        self.launch_home()

    def launch_home(self):
        magic_instance = Magic()
        derivative_result, integral_result, x_val, y_orig, y_derivative, y_integral = magic_instance.magic_func()
        print(f"Derivative: {derivative_result}")
        print(f"Integral: {integral_result}")
        
        Graph.plot_graph(x_val, y_orig, title="Original Function")
        Graph.plot_graph(x_val, y_derivative, title="Derivative")
        Graph.plot_graph(x_val, y_integral, title="Integral")