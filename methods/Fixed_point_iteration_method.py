from sympy import *
import math
from numpy import arange


class FixedPointIteration:

    num_of_iteration = 0
    root

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

    def compute_root(self):

        try:
            # create the table
            table = [['i', 'Xi', 'relative_error']]
            row = [0, self.initial_x, None]
            table.append(row)

            i = 0
            # if the initial guess is the root
            if int(self.function_formula.evalf(subs={self.X: self.initial_x})) == 0:
                return [table], self.initial_x

            while True:

                i = i + 1

                iterative_x = float(self.function_formula.evalf(subs={self.X: self.initial_x}))

                # if the root is zero
                if iterative_x == 0.0:
                    relative_error = None
                else:
                    relative_error = (iterative_x - self.initial_x) / iterative_x

                # add Row to the table
                row = [i, iterative_x, math.fabs(relative_error)]
                table.append(row)

                # break when reach max iteration or precision
                if (math.fabs(relative_error) <= self.precision) | (i >= self.max_iterations):
                    break

                self.initial_x = iterative_x

                if iterative_x < 1e-10 and iterative_x > -1e-10:
                    break

            final_table = [table]
            print (final_table)
            FixedPointIteration.root = iterative_x
            return final_table, iterative_x, true
        except:
            return [[[]]], 0.0, false


    # to do call to check if root
    def is_root(self):
        if FixedPointIteration.root < 1e-1 and FixedPointIteration.root > -1e-1:
            return true
        else:
            return false

    def get_x_y(self):

        a = []
        b = []

        for x in range(-50, 50, 1):
            y = self.function_formula.evalf(subs={self.X: x})
            a.append(x)
            b.append(y)
        return a, b

