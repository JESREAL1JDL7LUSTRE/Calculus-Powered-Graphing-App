from components.logic.derivative import derivative
from components.logic.funcinput import funcinput
from components.logic.integral import integral
from components.graph.graph import Graph
from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout
import numpy as np
import sympy as sp

class Magic(QWidget):
    def __init__(self):
        super().__init__()

    def magic_func(self):
        x = sp.symbols('x')
        x_val = np.linspace(-10, 10, 1000)
        # Get user input for function
        funcinput_instance = funcinput()
        function = funcinput_instance.set_function()
        
        function_numeric = sp.lambdify(x, function, 'numpy')
        y_orig = function_numeric(x_val)

        # Compute derivative
        derivative_instance = derivative(function)
        derivative_result = derivative_instance.calculate_derivative()
        function_numeric_derivative = sp.lambdify(x, derivative_result, 'numpy')
        y_derivative = function_numeric_derivative(x_val)

        # Compute integral
        integral_instance = integral(function, 0, 1)
        integral_result = integral_instance.calculate()
        y_integral = [sp.integrate(function, (x, 0, val)).evalf() for val in x_val]

        return derivative_result, integral_result, x_val, y_orig, y_derivative, y_integral
