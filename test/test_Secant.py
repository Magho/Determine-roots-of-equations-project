from methods import Secant_method
from sympy import *
from sympy.functions import exp

x = Symbol('x')
function_formula = exp(-x) - x

call_func = Secant_method.Secant(function_formula, 1.0, 0.0, 0, 0)

# bool1 = call_func.verify_there_is_a_root()
# print(bool(bool1))

root = call_func.compute_root()
print(root)

call_func.plot_function()
