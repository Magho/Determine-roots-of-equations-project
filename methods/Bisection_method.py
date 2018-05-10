from sympy import *
import math
import matplotlib.pyplot as plt
import graphlab
import numpy as np
import matplotlib.animation as animation


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

        if function_value_at_lower_bound * function_value_at_upper_bound < 0:
            return true

    def determine_number_of_iterations(self):
        BracketingMethod.num_of_iteration = math.ceil(((math.log10(self.upper_bound - self.lower_bound)
                                                        - math.log10(self.precision)) / math.log10(2)))
        return BracketingMethod.num_of_iteration

    def compute_root(self):

        xr = (self.upper_bound + self.lower_bound) / 2.0
        fxr = float(self.function_formula.subs(self.X, (self.upper_bound + self.lower_bound) / 2.0))

        # create the table
        table = graphlab.SFrame({'Xu': [self.upper_bound], 'Xl': [self.lower_bound],
                                 'Xr': [(self.upper_bound + self.lower_bound) / 2.0],
                                 'F(Xr)': [fxr], 'relative_error': [None]})

        # a = []
        # b = []
        #
        # x = 2 * self.lower_bound - self.upper_bound
        # for i in range(0, 150, 1):
        #     x = (3 * self.upper_bound - 3 * self.lower_bound)/150 + x
        #     y = self.function_formula.subs(self.X, x)
        #     a.append(x)
        #     b.append(y)
        #
        # fig = plt.figure()
        # axes = fig.add_subplot(111)
        # axes.plot(a, b)
        # plt.axhline(y=0, color='b')
        # plt.axvline(x=self.upper_bound, color='r')
        # plt.axvline(x=self.lower_bound, color='g')
        #
        # plt.show()

        i = 0
        while i < BracketingMethod.num_of_iteration:

            xr = (self.upper_bound + self.lower_bound) / 2.0
            function_value_at_xr = self.function_formula.subs(self.X, xr)

            if i > 0:

                eps = (xr - xr_old) / xr

                fxr = float(self.function_formula.subs(self.X, xr))
                row = graphlab.SFrame({'Xu': [self.upper_bound], 'Xl': [self.lower_bound], 'Xr': [xr],
                                       'F(Xr)': [fxr], 'relative_error': [math.fabs(eps)]})
                table = table.append(row)
                if math.fabs(eps) <= self.precision:
                    break

            if (function_value_at_xr * self.function_formula.subs(self.X, self.upper_bound)) < 0:
                self.lower_bound = xr
            else:
                self.upper_bound = xr
            xr_old = xr
            i = i + 1

            if i >= self.max_iterations:
                break

        print (table)
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
        axes.grid()
        axes.plot(a, b)
        plt.show()