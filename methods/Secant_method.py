from sympy import *
import math
from numpy import arange


class Secant:

    num_of_iteration = 0
    root

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


    def compute_root(self):

        try:
            fxi = float(self.function_formula.evalf(subs={self.X: self.initial_xi}))
            fxi1 = float(self.function_formula.evalf(subs={self.X: self.initial_xi_1}))

            # create the table
            table = [['i', 'Xi', 'Xi-1', 'F(Xi)', 'F(Xi-1)', 'relative_error']]
            row = [0, self.initial_xi, self.initial_xi_1, fxi, fxi1, None]
            table.append(row)

            # if the initial guess is the root
            if int(self.function_formula.evalf(subs={self.X: self.initial_xi})) == 0:
                Secant.root = self.initial_x
                return [table], self.initial_xi, true
            elif int(self.function_formula.evalf(subs={self.X: self.initial_xi_1})) == 0:
                Secant.root = self.initial_xi_1
                return [table], self.initial_xi_1, true

            i = 0
            while True:

                i = i + 1

                numerator = float(self.function_formula.evalf(subs={self.X: self.initial_xi}) * (self.initial_xi - self.initial_xi_1))
                denominator = float(self.function_formula.evalf(subs={self.X: self.initial_xi}) - (self.initial_xi - self.initial_xi_1))

                if denominator == 0.0:
                    return [table], 0.0, false

                iterative_x = self.initial_xi - (numerator / denominator)

                # if the root is zero
                if iterative_x == 0.0:
                    relative_error = None
                else:
                    relative_error = (iterative_x - self.initial_xi) / iterative_x

                fxi = float(self.function_formula.evalf(subs={self.X: iterative_x}))
                fxi1 = float(self.function_formula.evalf(subs={self.X: self.initial_xi}))

                # add Row to the table
                row = [i, iterative_x, self.initial_xi, fxi, fxi1, math.fabs(relative_error)]
                table.append(row)

                # break when reach max iteration or precision
                if (math.fabs(relative_error) <= self.precision) | (i >= self.max_iterations):
                    break

                self.initial_xi_1 = self.initial_xi
                self.initial_xi = iterative_x

                if iterative_x < 1e-10 and iterative_x > -1e-10:
                    break

            final_table = [table]
            Secant.root = iterative_x
            print(final_table)
            return final_table, iterative_x, true
        except:
            return [[[]]], 0.0, false

    # to do call to check if root
    def is_root(self):
        try:
            if self.function_formula.evalf(subs={self.X: Secant.root}) < 1e-1 \
                    and self.function_formula.evalf(subs={self.X: Secant.root}) > -1e-1:
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
