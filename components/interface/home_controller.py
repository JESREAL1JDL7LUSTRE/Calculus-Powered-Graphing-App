import re
import numpy as np
import sympy as sp
from components.logic.funcinput import FuncInput
from components.logic.derivative import Derivative
from components.logic.integral import integral

class HomeController:
    def __init__(self, view):
        self.view = view

    def process_function(self, input_str, lower_bound = 0, upper_bound = 1, derivative_order = 1):
        try:
            s = self._preprocess_input(input_str)

            x = sp.symbols('x')
            xs = np.linspace(-25, 25, 1000)
            xi = np.linspace(lower_bound, upper_bound, 1000)

            # 2) Parse and lambdify
            f_expr = FuncInput().set_function(s)
            f_num = sp.lambdify(x, f_expr, 'numpy')
            y = self._broadcast_if_scalar(f_num(xs), xs.shape)

            # 3) Derivative
            d_expr = Derivative(f_expr).calculate_derivative(derivative_order)
            y_d = self._broadcast_if_scalar(sp.lambdify(x, d_expr, 'numpy')(xs), xs.shape)
            
            # 4) Symbolic (indefinite) integral
            sym_int = sp.integrate(f_expr, x)
            # **Reorder** terms so highest exponent first:
            sym_int = self._reorder_by_degree(sym_int)
            y_sym = self._broadcast_if_scalar(sp.lambdify(x, sym_int, 'numpy')(xs), xs.shape)

            # 5) Definite numeric integral
            num_int = sp.integrate(f_expr, (x, lower_bound, upper_bound))
            # For plotting cumulative integral:
            y_i = [sp.integrate(f_expr, (x, lower_bound, t)).evalf() for t in xi]

            # 6) Display (with nice formatting)
            self.view.update_result(self._postprocess_output(f_expr))
            self.view.derivative_result(self._postprocess_output(d_expr))
            self.view.update_integral_symbolic(self._postprocess_output(sym_int))
            self.view.update_integral_numeric(str(num_int))

            # 7) Graphs
            self.view.update_function_graph(xs, y)
            self.view.update_derivative_graph(xs, y_d)
            self.view.update_integral_graph(xi, y_i)
            self.view.update_symbolic_integral_graph(xs, y_sym)

        except Exception as e:
            err = f"Error: {e}"
            self.view.update_result(err)
            self.view.derivative_result(err)
            self.view.update_integral_symbolic(err)
            self.view.update_integral_numeric(err)

    def _preprocess_input(self, s):
        # only insert * where truly implicit
        s = re.sub(r'(\d)([a-zA-Z])', r'\1*\2', s)    # 3x → 3*x
        s = re.sub(r'(\))([a-zA-Z])', r'\1*\2', s)    # )x → )*x
        s = re.sub(r'(\d)(\()',       r'\1*\2', s)    # 3(x → 3*(x
        return s

    def _postprocess_output(self, expr):
        out = str(expr)
        out = out.replace('**', '^')
        out = re.sub(r'(\d+)\*([a-zA-Z])', r'\1\2', out)
        out = re.sub(r'([a-zA-Z])\*([a-zA-Z])', r'\1\2', out)
        out = re.sub(r'(\d+)(x\^\d+)/(\d+)', r'\1/\3\2', out)
        return out


    def _reorder_by_degree(self, expr):
        """
        For a Sympy Add-expression in x, reorder terms by descending exponent of x.
        Keeps non-Add exprs untouched.
        """
        if not isinstance(expr, sp.Add):
            return expr

        x = sp.Symbol('x')
        terms = expr.as_ordered_terms()  # Sympy’s default order

        def degree(term):
            # extract the exponent of x in this term (0 if none)
            pd = term.as_powers_dict()
            return float(pd.get(x, 0))

        # sort by exponent descending
        sorted_terms = sorted(terms, key=degree, reverse=True)
        return sp.Add(*sorted_terms)

    def _broadcast_if_scalar(self, val, ref_shape):
        return np.full(ref_shape, val) if np.isscalar(val) or np.ndim(val) == 0 else val
