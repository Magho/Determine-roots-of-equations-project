from sympy import *
import math
import matplotlib.pyplot as plt
import graphlab

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

            xr_new = ((self.lower_bound * float(self.function_formula.subs(self.X, self.upper_bound))) -
                      (self.upper_bound * float(self.function_formula.subs(self.X, self.lower_bound)))) / (
                    float(self.function_formula.subs(self.X, self.upper_bound)) -
                    float(self.function_formula.subs(self.X, self.lower_bound)))

            function_value_at_xr_1_new = float(self.function_formula.subs(self.X, float(xr_new)))

            if i == 0:

                # create the table
                table = graphlab.SFrame({'Xu': [self.upper_bound], 'Xl': [self.lower_bound], 'Xr': [xr_new],
                                         'F(Xr)': [function_value_at_xr_1_new], 'relative_error': [None]})
            else:

                eps = (xr_new - xr_1_old) / xr_new

                # add row to the table
                fxr = float(self.function_formula.subs(self.X, xr_new))
                row = graphlab.SFrame({'Xu': [self.upper_bound], 'Xl': [self.lower_bound], 'Xr': [xr_new],
                                       'F(Xr)': [fxr], 'relative_error': [eps]})
                table = table.append(row)

            if function_value_at_xr_1_new < 0:
                self.lower_bound = xr_new

            elif function_value_at_xr_1_new > 0:
                self.upper_bound = xr_new

            i = i + 1
            xr_1_old = xr_new

            # break when reach max iteration or precision
            if (math.fabs(xr_new - xr_1_old) <= self.precision) | (i >= self.max_iterations):
                break

        print(table)
        return xr_new

    # TODO specify bounders
    def plot_function(self):

        a = []
        b = []

        for x in range(-50, 50, 1):
            y = self.function_formula.subs(self.X, x)
            a.append(x)
            b.append(y)

        fig = plt.figure()
        axes = fig.add_subplot(111)
        axes.plot(a, b)
        plt.show()
