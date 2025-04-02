from components.logic.derivative import derivative
from components.logic.funcinput import funcinput
from components.logic.integral import integral

class Magic:
    def __init__(self):
        pass

    def magic_func(self):
        # Get user input for function
        funcinput_instance = funcinput()
        function = funcinput_instance.set_function()

        # Compute derivative
        derivative_instance = derivative(function)
        derivative_result = derivative_instance.calculate_derivative()

        # Compute integral
        integral_instance = integral(function, 0, 1)
        integral_result = integral_instance.calculate()

        return derivative_result, integral_result
