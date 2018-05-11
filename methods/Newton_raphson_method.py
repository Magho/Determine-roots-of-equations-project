from sympy import *
import math
from numpy import arange


class NewtonRaphson:

    num_of_iteration = 0

    # pass a function to me
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

    def function_div(self, num, x=Symbol('x')):
        func1_div_x = self.function_formula.diff(x)
        return func1_div_x.evalf(subs={self.X: num})

    # def verify_there_is_a_root(self):
    #     function_value_at_upper_bound = self.function_formula.evalf(self.X, self.initial_x)
    #     function_value_at_lower_bound = self.function_formula.evalf(self.X, self.lower_bound)
    #
    #     print(function_value_at_lower_bound)
    #     print(function_value_at_upper_bound)
    #
    #     if function_value_at_lower_bound * function_value_at_upper_bound < 0:
    #         return true

    def compute_root(self):
        try:
            fxi = float(self.function_formula.evalf(subs={self.X: self.initial_x}))
            fxi_div = float(self.function_div(self.initial_x))
        except ZeroDivisionError:
            return "r0"
        except:
            return "err"
        # create the table
        table = [['i', 'Xi', 'F(Xi)', "F'(Xi)", 'relative_error']]
        row = [0, self.initial_x, fxi, fxi_div, None]
        table.append(row)

        i = 0

        while True:

            i = i + 1

            #if self.function_div(self.initial_x) == 0:
                # TODO determine what to do ?
                #print("division by zero")
            try:
                iterative_x = self.initial_x - (float(self.function_formula.evalf(subs={self.X: self.initial_x})) /
                                            float(self.function_div(self.initial_x)))
            except ZeroDivisionError:
                return "db0"
            except:
                return "err"

            try:
                relative_error = (iterative_x - self.initial_x) / iterative_x
            except ZeroDivisionError:
                return "r0"
            except:
                return "err"

            try:
                fxi = float(self.function_formula.evalf(subs={self.X: self.initial_x}))
                fxi_div = float(self.function_div(iterative_x))
            except ZeroDivisionError:
                return "r0"
            except:
                return "err"
            # add Row to the table
            row = [i, iterative_x, fxi, fxi_div, math.fabs(relative_error)]
            table.append(row)

            # break when reach max iteration or precision
            if (math.fabs(relative_error) <= self.precision) | (i >= self.max_iterations):
                break

            self.initial_x = iterative_x

        final_table = [table]
        return final_table, iterative_x

    def get_x_y(self):

        a = []
        b = []

        for x in range(-50, 50, 1):
            y = self.function_formula.evalf(subs={self.X: x})
            a.append(x)
            b.append(y)
        return a, b
