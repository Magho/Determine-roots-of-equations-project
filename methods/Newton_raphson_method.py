from sympy import *
import math
from numpy import arange


class NewtonRaphson:

    num_of_iteration = 0

    # pass a function to me
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

    def function_div(self, num, x=Symbol('x')):
        func1_div_x = self.function_formula.diff(x)
        return func1_div_x.evalf(subs={self.X: num})

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

        fxi = float(self.function_formula.evalf(subs={self.X: self.initial_x}))
        fxi_div = float(self.function_div(self.initial_x))

        # create the table
        table = [['i', 'Xi', 'F(Xi)', "F'(Xi)", 'relative_error']]
        row = [0, self.initial_x, fxi, fxi_div, None]
        table.append(row)

        i = 0

        while True:

            i = i + 1

            if self.function_div(self.initial_x) == 0:
                # TODO determine what to do ?
                print("division by zero")

            iterative_x = self.initial_x - (float(self.function_formula.evalf(subs={self.X: self.initial_x})) /
                                            float(self.function_div(self.initial_x)))
            relative_error = (iterative_x - self.initial_x) / iterative_x

            fxi = float(self.function_formula.evalf(subs={self.X: self.initial_x}))
            fxi_div = float(self.function_div(iterative_x))

            # add Row to the table
            row = [i, iterative_x, fxi, fxi_div, math.fabs(relative_error)]
            table.append(row)

            # break when reach max iteration or precision
            if (math.fabs(relative_error) <= self.precision) | (i >= self.max_iterations):
                break

            self.initial_x = iterative_x

        print(table)
        return table, iterative_x

    def get_x_y(self):

        x = arange(-50.0, 50.0, 1.0)
        y = self.function_formula.evalf(subs={self.X: x})
        return x, y
