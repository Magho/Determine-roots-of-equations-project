from sympy import *
import math
from numpy import arange


class BracketingMethod:

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
        function_value_at_upper_bound = self.function_formula.evalf(subs={self.X: self.upper_bound})
        function_value_at_lower_bound = self.function_formula.evalf(subs={self.X: self.lower_bound})

        if function_value_at_lower_bound * function_value_at_upper_bound < 0:
            return true

    def determine_number_of_iterations(self):
        BracketingMethod.num_of_iteration = math.ceil(((math.log10(self.upper_bound - self.lower_bound)
                                                        - math.log10(self.precision)) / math.log10(2)))
        return BracketingMethod.num_of_iteration

    def compute_root(self):

        xr = (self.upper_bound + self.lower_bound) / 2.0
        fxr = float(self.function_formula.evalf(subs={self.X: ((self.upper_bound + self.lower_bound) / 2.0)}))

        # create the table
        table = [['Xu', 'Xl', 'Xr', 'F(Xr)', 'relative_error']]
        row = [self.upper_bound, self.lower_bound, (self.upper_bound + self.lower_bound) / 2.0, fxr, None]
        table.append(row)

        i = 0
        while i < BracketingMethod.num_of_iteration:

            xr = (self.upper_bound + self.lower_bound) / 2.0
            function_value_at_xr = self.function_formula.evalf(subs={self.X: xr})

            if i > 0:

                eps = (xr - xr_old) / xr

                fxr = float(self.function_formula.evalf(self.X, xr))

                # add new row
                row = [self.upper_bound, self.lower_bound, xr, fxr, math.fabs(eps)]
                table.append(row)

                if math.fabs(eps) <= self.precision:
                    break

            if (function_value_at_xr * self.function_formula.evalf(subs={self.X: self.upper_bound})) < 0:
                self.lower_bound = xr
            else:
                self.upper_bound = xr

            xr_old = xr
            i = i + 1

            if i >= self.max_iterations:
                break

        print (table)
        return table, xr

    def get_x_y(self):

        x = arange(self.upper_bound, self.lower_bound, (self.upper_bound - self.lower_bound)/100)
        y = self.function_formula.evalf(subs={self.X: x})
        return x, y
