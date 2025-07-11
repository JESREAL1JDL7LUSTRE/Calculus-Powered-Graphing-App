import sympy as sp
from sympy import symbols

class Derivative:
    def __init__(self, expression):
        self.expression = expression

    def calculate_derivative(self, n=1):
        return sp.diff(self.expression, symbols('x'), n)
