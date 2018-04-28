from sympy import *
import math
import matplotlib.pyplot as plt

# import pandas as pd


class Secant:

    num_of_iteration = 0

    # pass a function to me
    def __init__(self, function_formula, initial_xi, initial_xi_1, max_iterations, precision, x=Symbol('x')):
        self.function_formula = function_formula
        self.initial_xi = initial_xi
        self.initial_xi_1 = initial_xi_1
        self.X = x
        self.max_iterations = max_iterations
        if max_iterations == 0:
            self.max_iterations = 50
        self.precision = precision
        if precision == 0:
            self.precision = 0.0001

    # def verify_there_is_a_root(self):
    #     function_value_at_upper_bound = self.function_formula.subs(self.X, self.initial_xi)
    #     function_value_at_lower_bound = self.function_formula.subs(self.X, self.initial_xi_1)
    #
    #     print(function_value_at_lower_bound)
    #     print(function_value_at_upper_bound)
    #
    #     if function_value_at_lower_bound * function_value_at_upper_bound < 0:
    #         return true

    def compute_root(self):

        # create the table

        # table = {'i': [0], 'Xi': [self.initial_xi], 'Xi-1': [self.initial_xi_1],
        #          'F(Xi)': [self.function_formula.subs(self.X, self.initial_xi)],
        #          'F(Xi-1)': [self.function_formula.subs(self.X, self.initial_xi_1)], 'relative_error': [None]}
        # df = pd.DataFrame.from_dict(table)

        i = 0
        while True:

            i = i + 1

            numerator = self.function_formula.subs(self.X, self.initial_xi) * (self.initial_xi - self.initial_xi_1)
            denominator = self.function_formula.subs(self.X, self.initial_xi) - (self.initial_xi - self.initial_xi_1)

            iterative_x = self.initial_xi - (numerator / denominator)
            relative_error = (iterative_x - self.initial_xi) / iterative_x

            # add Row to the table

            # row = {'i': [i], 'Xi': [iterative_x], 'Xi-1': [self.initial_xi],
            #                        'F(Xi)': [self.function_formula.subs(self.X, iterative_x)],
            #                        "F(Xi-1)": [self.function_formula.subs(self.X, self.initial_xi)],
            #                        'relative_error': [math.fabs(relative_error)]}
            # df2 = pd.DataFrame.from_dict(row)
            # df.append(df2)

            # break when reach max iteration or precision
            if (math.fabs(relative_error) <= self.precision) | (i > self.max_iterations):
                break

            self.initial_xi_1 = self.initial_xi
            self.initial_xi = iterative_x

        return iterative_x

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
