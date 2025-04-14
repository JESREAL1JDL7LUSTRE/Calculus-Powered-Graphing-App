import numpy as np
import sympy as sp
from components.logic.funcinput import FuncInput
from components.logic.derivative import Derivative
from components.logic.integral import integral

class HomeController:
    def __init__(self, view):
        self.view = view

    def process_function(self, input_str, lower_bound, upper_bound):
        try:
            x = sp.symbols('x')
            x_val = np.linspace(-10, 10, 1000)
            x_val_for_integral = np.linspace(lower_bound, upper_bound, 1000)
            
            # Get function from input
            funcinput_instance = FuncInput()
            function = funcinput_instance.set_function(input_str)

            # Evaluate original function
            function_numeric = sp.lambdify(x, function, 'numpy')
            y_orig = function_numeric(x_val)

            # Derivative
            derivative_instance = Derivative(function)
            derivative_result = derivative_instance.calculate_derivative()
            y_derivative = sp.lambdify(x, derivative_result, 'numpy')(x_val)

            # Symbolic integral (indefinite)
            symbolic_integral = sp.integrate(function, x)

            # Convert symbolic integral to a numerical function for graphing
            symbolic_integral_func = sp.lambdify(x, symbolic_integral, 'numpy')
            y_symbolic = symbolic_integral_func(x_val)
            
            # Definite numeric integral (numerical result from scipy)
            integral_instance = integral(function, lower_bound, upper_bound)
            numeric_integral_result, _ = integral_instance.calculate()

            # For graphing: ∫₀ˣ f(t) dt for each x (definite integral)
            y_integral = [sp.integrate(function, (x, 0, val)).evalf() for val in x_val_for_integral]

            # Output to view
            self.view.update_result(function)
            self.view.derivative_result(str(derivative_result))
            
            # Show both integrals separately
            self.view.update_integral_symbolic(f" {symbolic_integral}")
            self.view.update_integral_numeric(f" {numeric_integral_result}")

            # Graphs
            self.view.update_function_graph(x_val, y_orig)
            self.view.update_derivative_graph(x_val, y_derivative)
            self.view.update_integral_graph(x_val, y_integral)
            self.view.update_symbolic_integral_graph(x_val, y_symbolic)

        except Exception as e:
            self.view.update_result(f"Error: {e}")
            self.view.derivative_result("Error")
            self.view.update_integral_symbolic("Error")
            self.view.update_integral_numeric("Error")
