from sympy import *
import math
# import pandas as pd


class FalsePosition:

    num_of_iteration = 0

    # pass a function to me
    def __init__(self, function_formula, upper_bound, lower_bound, max_iterations, precision, x=Symbol('x')):
        self.function_formula = function_formula
        self.upper_bound = upper_bound
        self.lower_bound = lower_bound
        self.X = x
        self.max_iterations = max_iterations
        if max_iterations == 0:
            self.max_iterations = 50
        self.precision = precision
        if precision == 0:
            self.precision = 0.0001

    def verify_there_is_a_root(self):
        function_value_at_upper_bound = self.function_formula.subs(self.X, self.upper_bound)
        function_value_at_lower_bound = self.function_formula.subs(self.X, self.lower_bound)

        print(function_value_at_lower_bound)
        print(function_value_at_upper_bound)

        if function_value_at_lower_bound * function_value_at_upper_bound < 0:
            return true

    def compute_root(self):

        i = 0
        while True:

            xr_new = ((self.lower_bound * self.function_formula.subs(self.X, self.upper_bound)) -
                      (self.upper_bound * self.function_formula.subs(self.X, self.lower_bound))) / (
                    self.function_formula.subs(self.X, self.upper_bound) -
                    self.function_formula.subs(self.X, self.lower_bound))

            function_value_at_xr_1_new = self.function_formula.subs(self.X, xr_new)

            if i == 0:
                print()
                # create the table
                # table = {'Xu': [self.upper_bound], 'Xl': [self.lower_bound], 'Xr': [xr_new],
                #          'F(Xr)': [function_value_at_xr_1_new], 'relative_error': [None]}
                # df = pd.DataFrame.from_dict(table)

            # break when reach max iteration or precision
            elif (math.fabs(xr_new - xr_1_old) <= self.precision) | (i > self.max_iterations):
                break

            else:
                eps = (xr_new - xr_1_old) / xr_new

                # row = {'Xu': [self.upper_bound], 'Xl': [self.lower_bound], 'Xr': [xr_new],
                #        'F(Xr)': [self.function_formula.subs(self.X, xr_new)], 'relative_error': [eps]}
                # df2 = pd.DataFrame.from_dict(row)
                # df.append(df2)

            if function_value_at_xr_1_new < 0:
                self.lower_bound = xr_new

            elif function_value_at_xr_1_new > 0:
                self.upper_bound = xr_new

            i = i + 1
            xr_1_old = xr_new

        return xr_new
