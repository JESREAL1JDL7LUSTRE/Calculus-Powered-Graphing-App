import numpy as np
import sympy as sp
from components.logic.funcinput import FuncInput
from components.logic.derivative import Derivative
from components.logic.integral import integral

class HomeController:
    def __init__(self, view):
        self.view = view

    def process_function(self, input_str):
        try:
            x = sp.symbols('x')
            x_val = np.linspace(-10, 10, 1000)
            
            # Get the function from the input string
            funcinput_instance = FuncInput()
            function = funcinput_instance.set_function(input_str)  # Get the user input function
            
            # Lambdify the function for evaluation over x_val
            function_numeric = sp.lambdify(x, function, 'numpy')
            y_orig = function_numeric(x_val)

            # Compute derivative
            derivative_instance = Derivative(function)
            derivative_result = derivative_instance.calculate_derivative()
            function_numeric_derivative = sp.lambdify(x, derivative_result, 'numpy')
            y_derivative = function_numeric_derivative(x_val)

            # Compute integral (numerical integration)
            integral_instance = integral(function, 0, 1)
            integral_result = integral_instance.calculate()
            y_integral = [sp.integrate(function, (x, 0, val)).evalf() for val in x_val]

            # Pass results to view
            self.view.update_result(function)
            self.view.derivative_result(f"{derivative_result}")
            self.view.integral_result(f"{integral_result}")

            # Update graphs
            self.view.update_function_graph(x_val, y_orig)
            self.view.update_derivative_graph(x_val, y_derivative)
            self.view.update_integral_graph(x_val, y_integral)

        except Exception as e:
            self.view.update_result(f"Error: {e}")
            self.view.derivative_result("Error")
            self.view.integral_result("Error")
