import Bisection_method
from sympy import *

x = Symbol('x')
function_formula = x ** 3 - 25

call_func = Bisection_method.BracketingMethod(function_formula, 3.0, 2.9, 0, 0)

bool1 = call_func.verify_there_is_a_root()
print(bool(bool1))

num_of_iterations = call_func.determine_number_of_iterations()
print(num_of_iterations)

root = call_func.compute_root()
print(root)
