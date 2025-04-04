import scipy.integrate as spi
import sympy as sp

class integral:
    def __init__(self, function, lower_bound, upper_bound, num_points=1000):
        self.function = function
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
        self.num_points = num_points

    def calculate(self):
        x = sp.symbols('x')
        # Convert symbolic function to numeric Python function
        numeric_func = sp.lambdify(x, self.function, 'numpy')
        result, _ = spi.quad(numeric_func, self.lower_bound, self.upper_bound)
        return result
