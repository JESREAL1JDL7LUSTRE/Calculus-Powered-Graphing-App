import sympy as sp

x = sp.symbols('x')
I = sp.integrate(sp.log(x, 10), (x, 1, 5))
print(I.evalf())
