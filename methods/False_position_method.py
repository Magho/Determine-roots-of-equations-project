from sympy import *
import math


class FalsePosition:

    num_of_iteration = 0
    root

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
        try:
            function_value_at_upper_bound = self.function_formula.evalf(subs={self.X: self.upper_bound})
            function_value_at_lower_bound = self.function_formula.evalf(subs={self.X: self.lower_bound})

            print(function_value_at_lower_bound)
            print(function_value_at_upper_bound)

            if int(function_value_at_lower_bound) * int(function_value_at_upper_bound) > 0:
                return false
            else:
                return true
        except:
            return false

    def compute_root(self):

        try:
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

                    if int(self.function_formula.evalf(subs={self.X: self.upper_bound})) == 0:
                        FalsePosition.root = self.upper_bound
                        row = [self.upper_bound, self.lower_bound, self.upper_bound, 0.0, None]
                        table.append(row)
                        return [table], self.upper_bound, true
                    elif int(self.function_formula.evalf(subs={self.X: self.lower_bound})) == 0:
                        FalsePosition.root = self.lower_bound
                        row = [self.upper_bound, self.lower_bound, self.lower_bound, 0.0, None]
                        table.append(row)
                        return [table], self.lower_bound, true

                    table.append(row)

                else:

                    # if the root is zero
                    if xr_new == 0.0:
                        eps = None
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

                if function_value_at_xr_1_new < 1e-10 and function_value_at_xr_1_new > -1e-10:
                    break

                i = i + 1
                xr_1_old = xr_new

                # break when reach max iteration or precision
                if (math.fabs(xr_new - xr_1_old) >= self.precision) | (i >= self.max_iterations):
                    break

            final_table = [table]
            FalsePosition.root = xr_new

            print(final_table)
            return final_table, xr_new, true
        except:
            return [[[]]], 0.0, false

    # to do call to check if root
    def is_root(self):
        try:
            if self.function_formula.evalf(subs={self.X: FalsePosition.root}) < 1e-1 \
                    and self.function_formula.evalf(subs={self.X: FalsePosition.root}) > -1e-1:
                return true
            else:
                return false
        except:
            return false

    def get_x_y(self):

        a = []
        b = []

        for x in range(-50, 50, 1):
            y = self.function_formula.evalf(subs={self.X: x})
            a.append(x)
            b.append(y)
        return a, b

