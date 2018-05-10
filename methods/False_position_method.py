from sympy import *
import math
from numpy import arange


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
        function_value_at_upper_bound = self.function_formula.evalf(subs={self.X: self.upper_bound})
        function_value_at_lower_bound = self.function_formula.evalf(subs={self.X: self.lower_bound})

        print(function_value_at_lower_bound)
        print(function_value_at_upper_bound)

        if function_value_at_lower_bound * function_value_at_upper_bound < 0:
            return true

    def compute_root(self):

        i = 0
        while True:

            xr_new = ((self.lower_bound * float(self.function_formula.evalf(subs={self.X: self.upper_bound}))) -
                      (self.upper_bound * float(self.function_formula.evalf(subs={self.X: self.lower_bound})))) / (
                    float(self.function_formula.evalf(subs={self.X: self.upper_bound})) -
                    float(self.function_formula.evalf(subs={self.X: self.lower_bound})))

            function_value_at_xr_1_new = float(self.function_formula.evalf(subs={self.X: float(xr_new)}))

            if i == 0:

                # create the table
                table = [['Xu', 'Xl', 'Xr', 'F(Xr)', 'relative_error']]
                row = [self.upper_bound, self.lower_bound, xr_new, function_value_at_xr_1_new, None]
                table.append(row)

            else:

                eps = (xr_new - xr_1_old) / xr_new

                # add row to the table
                fxr = float(self.function_formula.evalf(subs={self.X: xr_new}))
                # add new row
                row = [self.upper_bound, self.lower_bound, xr_new, fxr, math.fabs(eps)]
                table.append(row)

            if function_value_at_xr_1_new < 0:
                self.lower_bound = xr_new

            elif function_value_at_xr_1_new > 0:
                self.upper_bound = xr_new

            i = i + 1
            xr_1_old = xr_new

            # break when reach max iteration or precision
            if (math.fabs(xr_new - xr_1_old) >= self.precision) | (i >= self.max_iterations):
                break

        print(table)
        return table, xr_new

    def get_x_y(self):

        x = arange(self.upper_bound, self.lower_bound, (self.upper_bound - self.lower_bound)/100)
        y = self.function_formula.evalf(subs={self.X: x})
        return x, y

