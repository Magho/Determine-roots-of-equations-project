import False_position_method
from sympy import *

x = Symbol('x')
function_formula = 3 * (x ** 4) + 6.1 * (x ** 3) - 2 * (x ** 2) + 3 * x + 2

call_func = False_position_method.FalsePosition(function_formula, 0.0, -1.0, 0, 0)

bool1 = call_func.verify_there_is_a_root()
print(bool(bool1))

root = call_func.compute_root()
print(root)

call_func.plot_function()
