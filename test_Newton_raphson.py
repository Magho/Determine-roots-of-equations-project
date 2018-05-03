import Newton_raphson_method
from sympy import *
#
# x = Symbol('x')
# function_formula = exp(-x) - x
#
# call_func = Newton_raphson_method.NewtonRaphson(function_formula, 0.0, 0, 0)
#
# # bool1 = call_func.verify_there_is_a_root()
# # print(bool(bool1))
#
# root = call_func.compute_root()
# print(root)
#
# call_func.plot_function()
# call_func.plot_derivative_function()


# ----------------------------------------------------- test 2 --------------------------------------------------

x = Symbol('x')
function_formula = x ** 3 - 0.165 * (x ** 2) + 3.993 * (10 ** (-4))

call_func = Newton_raphson_method.NewtonRaphson(function_formula, 0.05, 0, 0)

# bool1 = call_func.verify_there_is_a_root()
# print(bool(bool1))

root = call_func.compute_root()
print(root)

call_func.plot_function()
call_func.plot_derivative_function()
