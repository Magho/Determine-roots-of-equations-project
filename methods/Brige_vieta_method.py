from sympy import *
import math
import matplotlib.pyplot as plt
import graphlab


# import pandas as pd


class BrigeVeta:

    num_of_iteration = 0

    # pass a function to me
    def __init__(self, function_formula, initial_x, ai, max_iterations, precision, x=Symbol('x')):
        self.function_formula = function_formula
        self.initial_x = initial_x
        self.ai = ai
        self.X = x
        self.max_iterations = max_iterations
        if max_iterations == 0:
            self.max_iterations = 50
        self.precision = precision
        if precision == 0:
            self.precision = 0.0001

    # def verify_there_is_a_root(self):
    #     function_value_at_upper_bound = self.function_formula.subs(self.X, self.upper_bound)
    #     function_value_at_lower_bound = self.function_formula.subs(self.X, self.lower_bound)
    #
    #     print(function_value_at_lower_bound)
    #     print(function_value_at_upper_bound)
    #
    #     if function_value_at_lower_bound * function_value_at_upper_bound < 0:
    #         return true

    def compute_root(self):

        # create the table1

        fxi = float(self.function_formula.subs(self.X, self.initial_x))
        table1 = graphlab.SFrame({'i': [0], 'Xi': [self.initial_x], 'F(Xi)': [fxi], 'relative_error': [None]})

        max_pow = len(self.ai) - 1
        j = 0

        while True:

            i = max_pow
            j = j + 1

            # create table2
            table = graphlab.SFrame({'i': [max_pow], 'ai': [self.ai[0]], 'bi': [self.ai[0]], 'ci': [self.ai[0]]})

            i = i - 1
            bi = ci = self.ai[0]
            k = 1
            while i >= 0:

                bi = bi * self.initial_x + self.ai[k]
                if i > 0:
                    ci = ci * self.initial_x + bi
                    temp = ci
                else:
                    temp = None

                # add Row2 to the table2
                row = graphlab.SFrame({'i': [i], 'ai': [self.ai[k]], 'bi': [bi], 'ci': [temp]})
                table = table.append(row)

                k = k + 1
                i = i - 1

            print(table)

            iterative_x = self.initial_x - (bi / ci)
            relative_error = (iterative_x - self.initial_x) / iterative_x

            # add Row1 to the table1

            fxi = float(self.function_formula.subs(self.X, iterative_x))
            row1 = graphlab.SFrame({'i': [j], 'Xi': [iterative_x], 'F(Xi)': [fxi],
                                    'relative_error': [math.fabs(relative_error)]})
            table1 = table1.append(row1)

            # break when reach max iteration or precision
            if (math.fabs(relative_error) <= self.precision) | (i >= self.max_iterations):
                break

            self.initial_x = iterative_x

        print (table1)
        return iterative_x

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
        axes.grid()
        plt.show()
