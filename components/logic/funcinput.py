import sympy as sp
from sympy import symbols

class FuncInput:
    def __init__(self):
        self.x = symbols('x')
        self.function = None

    def set_function(self, func_str):
        self.function = sp.sympify(func_str)
        return self.function

    def evaluate_function(self, x_values):
        f_lambdified = sp.lambdify(self.x, self.function, 'numpy')
        return f_lambdified(x_values)
