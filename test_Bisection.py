import Bisection_method
from sympy import *


# ------------------------------------------------ test 1 -------------------------------------------------
x = Symbol('x')
function_formula = x ** 3 - 25

call_func = Bisection_method.BracketingMethod(function_formula, 3.0, 2.9, 0, 0)

bool1 = call_func.verify_there_is_a_root()
print(bool(bool1))

num_of_iterations = call_func.determine_number_of_iterations()
print(num_of_iterations)

root = call_func.compute_root()
print(root)

call_func.plot_function()

# ------------------------------------------------- test 2 ---------------------------------------------------

# x = Symbol('x')
# function_formula = x ** 3 - 0.165 * (x ** 2) + 3.993 * (10 ** (-4))
#
# call_func = Bisection_method.BracketingMethod(function_formula, 0.11, 0.0, 10, 0)
#
# bool1 = call_func.verify_there_is_a_root()
# print(bool(bool1))
#
# num_of_iterations = call_func.determine_number_of_iterations()
# print(num_of_iterations)
#
# root = call_func.compute_root()
# print(root)
#
# call_func.plot_function()
