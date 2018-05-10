from sympy import *
import math
from numpy import arange


class FixedPointIteration:

    num_of_iteration = 0

    def __init__(self, function_formula, initial_x, max_iterations, precision, x=Symbol('x')):
        self.function_formula = function_formula
        self.initial_x = initial_x
        self.X = x
        self.max_iterations = max_iterations
        if max_iterations == 0:
            self.max_iterations = 50
        self.precision = precision
        if precision == 0:
            self.precision = 0.0001

    # def verify_there_is_a_root(self):
    #     function_value_at_upper_bound = self.function_formula.evalf(self.X, self.initial_x)
    #     function_value_at_lower_bound = self.function_formula.evalf(self.X, self.lower_bound)
    #
    #     print(function_value_at_lower_bound)
    #     print(function_value_at_upper_bound)
    #
    #     if function_value_at_lower_bound * function_value_at_upper_bound < 0:
    #         return true

    def compute_root(self):

        # create the table
        table = [['i', 'Xi', 'relative_error']]
        row = [0, self.initial_x, None]
        table.append(row)

        i = 0

        while True:

            i = i + 1

            iterative_x = float(self.function_formula.evalf(subs={self.X: self.initial_x}))
            relative_error = (iterative_x - self.initial_x) / iterative_x

            # add Row to the table
            row = [i, iterative_x, math.fabs(relative_error)]
            table.append(row)

            # break when reach max iteration or precision
            if (math.fabs(relative_error) <= self.precision) | (i >= self.max_iterations):
                break

            self.initial_x = iterative_x

        final_table = [table]
        print (final_table)
        return final_table, iterative_x

    def get_x_y(self):

        x = arange(-50.0, 50.0, 1.0)
        y = self.function_formula.evalf(subs={self.X: x})
        return x, y

