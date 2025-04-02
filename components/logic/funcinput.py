
import sympy as sp

class funcinput:
    def __init__(self):
        self.function = None

    def set_function(self):
        function_str = input("Input Function: ")
        self.function = sp.sympify(function_str)
        return self.function
        
        