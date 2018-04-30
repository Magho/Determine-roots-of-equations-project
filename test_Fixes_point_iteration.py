import Fixed_point_iteration_method
from sympy import *

x = Symbol('x')
function_formula = exp(-x)

call_func = Fixed_point_iteration_method.FixedPointIteration(function_formula, 0.1, 0, 0)

# bool1 = call_func.verify_there_is_a_root()
# print(bool(bool1))

root = call_func.compute_root()
print(root)

call_func.plot_function()