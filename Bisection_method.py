from sympy import *
import math
import matplotlib.pyplot as plt


# import pandas as pd


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
        function_value_at_upper_bound = self.function_formula.subs(self.X, self.upper_bound)
        function_value_at_lower_bound = self.function_formula.subs(self.X, self.lower_bound)

        print(function_value_at_lower_bound)
        print(function_value_at_upper_bound)

        if function_value_at_lower_bound * function_value_at_upper_bound < 0:
            return true

    def determine_number_of_iterations(self):
        BracketingMethod.num_of_iteration = math.ceil(((math.log10(self.upper_bound - self.lower_bound)
                                                        - math.log10(self.precision)) / math.log10(2)))
        return BracketingMethod.num_of_iteration

    def compute_root(self):
        xr = (self.upper_bound + self.lower_bound) / 2.0

        # create the table

        # table = {'Xu': [self.upper_bound], 'Xl': [self.lower_bound], 'Xr': [xr],
        #          'F(Xr)': [self.function_formula.subs(self.X, ((self.upper_bound + self.lower_bound) / 2.0))],
        #          'relative_error': [None]}
        #
        # df = pd.DataFrame.from_dict(table)

        i = 0
        while i < BracketingMethod.num_of_iteration:

            xr = (self.upper_bound + self.lower_bound) / 2.0

            # stop if max_iterations reached
            if i > self.max_iterations:
                break

            function_value_at_xr = self.function_formula.subs(self.X, xr)

            if i > 0:

                eps = (xr - xr_old) / xr

                # add Row to the table
                # row = {'Xu': [self.upper_bound], 'Xl': [self.lower_bound], 'Xr': [xr],
                #          'F(Xr)': [self.function_formula.subs(self.X, xr)], 'relative_error': [eps]}
                # df2 = pd.DataFrame.from_dict(row)
                # df.append(df2)

            if (function_value_at_xr * self.function_formula.subs(self.X, self.upper_bound)) < 0:
                self.lower_bound = xr
            else:
                self.upper_bound = xr
            xr_old = xr

            # TODO print table

            # stop if precision reached presented by max iteration
            i = i + 1
        return xr

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
