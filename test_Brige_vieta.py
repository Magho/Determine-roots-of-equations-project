import Brige_vieta_method
from sympy import *

x = Symbol('x')
function_formula = x ** 2 - 3 * x + 2

call_func = Brige_vieta_method.BrigeVeta(function_formula, 3.0, [1.0, -3.0, 2.0], 0, 0)

# bool1 = call_func.verify_there_is_a_root()
# print(bool(bool1))

root = call_func.compute_root()
print(root)

call_func.plot_function()
