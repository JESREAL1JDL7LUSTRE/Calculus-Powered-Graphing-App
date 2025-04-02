import sympy as sp
from sympy import symbols, diff, simplify

class derivative:
    def __init__(self, expression):
        self.expression = expression

    def calculate_derivative(self):
        return sp.diff(self.expression, symbols('x'))